from __future__ import annotations

import base64
import json
import mimetypes
import os
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from ..errors import PunkError

KEYCHAIN_SERVICE = "punk-skill-apimart"


@dataclass(frozen=True)
class APIMartConfig:
    api_key: str
    base_url: str = "https://api.apimart.ai/v1"
    model: str = "gpt-image-2"
    resolution: str = "1k"
    timeout_seconds: int = 180
    poll_interval_seconds: float = 2.0

    @classmethod
    def from_environment(cls) -> "APIMartConfig":
        api_key = (
            os.environ.get("PUNK_APIMART_API_KEY", "").strip()
            or os.environ.get("APIMART_API_KEY", "").strip()
            or read_keychain_key()
        )
        if not api_key:
            raise PunkError(
                "APIMart API key is not configured; use `punk config set-key` or PUNK_APIMART_API_KEY"
            )
        return cls(
            api_key=api_key,
            base_url=os.environ.get("PUNK_APIMART_BASE_URL", "https://api.apimart.ai/v1").strip(),
            model=os.environ.get("PUNK_IMAGE_MODEL", "gpt-image-2").strip(),
            resolution=os.environ.get("PUNK_IMAGE_RESOLUTION", "1k").strip(),
        )


@dataclass(frozen=True)
class GeneratedImage:
    saved_path: Path
    source_url: str
    task_id: str = ""
    provider: str = "apimart"

    def to_mapping(self) -> dict[str, str]:
        return {
            "provider": self.provider,
            "saved_path": str(self.saved_path),
            "source_url": self.source_url,
            "task_id": self.task_id,
        }


def read_keychain_key() -> str:
    if os.name != "posix" or not Path("/usr/bin/security").exists():
        return ""
    result = subprocess.run(
        ["/usr/bin/security", "find-generic-password", "-s", KEYCHAIN_SERVICE, "-w"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def save_keychain_key(api_key: str) -> None:
    value = api_key.strip()
    if not value:
        raise PunkError("API key is empty")
    if os.name != "posix" or not Path("/usr/bin/security").exists():
        raise PunkError("macOS Keychain is not available")
    result = subprocess.run(
        [
            "/usr/bin/security",
            "add-generic-password",
            "-U",
            "-s",
            KEYCHAIN_SERVICE,
            "-a",
            os.environ.get("USER", "punk-skill"),
            "-w",
            value,
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise PunkError(result.stderr.strip() or "failed to save API key in Keychain")


def normalize_ratio(ratio: str) -> str:
    return {
        "1:1": "1:1",
        "3:4": "3:4",
        "4:5": "4:5",
        "16:9": "16:9",
        "5:2": "21:9",
        "2.35:1": "21:9",
    }.get(ratio, ratio or "1:1")


def source_image_payload(source: str) -> str:
    if not source:
        return ""
    if source.startswith(("http://", "https://", "data:")):
        return source
    path = Path(source).expanduser().resolve()
    if not path.is_file():
        raise PunkError(f"source image does not exist: {path}")
    mime_type = mimetypes.guess_type(path.name)[0] or "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


class APIMartProvider:
    def __init__(self, config: APIMartConfig, sleep: Callable[[float], None] = time.sleep):
        self.config = config
        self.sleep = sleep

    def _generation_endpoint(self) -> str:
        base = self.config.base_url.rstrip("/")
        return base if base.endswith("/images/generations") else f"{base}/images/generations"

    def _task_endpoint(self, task_id: str) -> str:
        base = self.config.base_url.rstrip("/")
        if base.endswith("/images/generations"):
            base = base[: -len("/images/generations")]
        return f"{base}/tasks/{urllib.parse.quote(task_id)}?language=zh"

    def _request_json(self, url: str, method: str = "GET", payload: dict[str, Any] | None = None) -> dict[str, Any]:
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        request = urllib.request.Request(
            url,
            data=data,
            method=method,
            headers={
                "Authorization": f"Bearer {self.config.api_key}",
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                text = response.read().decode("utf-8")
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="replace")
            raise PunkError(f"APIMart request failed ({error.code}): {self._error_message(body)}") from error
        except urllib.error.URLError as error:
            raise PunkError(f"APIMart request failed: {error.reason}") from error
        try:
            parsed = json.loads(text)
        except json.JSONDecodeError as error:
            raise PunkError("APIMart returned an invalid JSON response") from error
        if not isinstance(parsed, dict):
            raise PunkError("APIMart returned an unexpected response")
        return parsed

    @staticmethod
    def _error_message(text: str) -> str:
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            return text[:300] or "unknown error"
        error = payload.get("error") if isinstance(payload, dict) else None
        if isinstance(error, str):
            return error
        if isinstance(error, dict) and isinstance(error.get("message"), str):
            return error["message"]
        if isinstance(payload, dict) and isinstance(payload.get("message"), str):
            return payload["message"]
        return "unknown error"

    def _download(self, source_url: str, output_stem: Path) -> Path:
        request = urllib.request.Request(source_url, headers={"User-Agent": "punk-skill/0.1"})
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                content = response.read()
                mime_type = response.headers.get_content_type()
        except urllib.error.URLError as error:
            raise PunkError(f"image was generated but download failed: {error.reason}") from error
        extension = {"image/jpeg": ".jpg", "image/webp": ".webp"}.get(mime_type, ".png")
        destination = output_stem.with_suffix(extension)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
        return destination

    @staticmethod
    def _immediate_url(payload: dict[str, Any]) -> str:
        data = payload.get("data")
        first = data[0] if isinstance(data, list) and data and isinstance(data[0], dict) else {}
        for value in (first.get("url"), payload.get("url")):
            if isinstance(value, str) and value:
                return value
        return ""

    @staticmethod
    def _task_id(payload: dict[str, Any]) -> str:
        data = payload.get("data")
        first = data[0] if isinstance(data, list) and data and isinstance(data[0], dict) else {}
        value = first.get("task_id") or payload.get("task_id")
        return value if isinstance(value, str) else ""

    @staticmethod
    def _completed_url(payload: dict[str, Any]) -> tuple[str, str]:
        data = payload.get("data") if isinstance(payload.get("data"), dict) else {}
        status = data.get("status") if isinstance(data.get("status"), str) else ""
        result = data.get("result") if isinstance(data.get("result"), dict) else {}
        images = result.get("images") if isinstance(result.get("images"), list) else []
        first = images[0] if images and isinstance(images[0], dict) else {}
        raw_url = first.get("url")
        if isinstance(raw_url, list):
            url = raw_url[0] if raw_url and isinstance(raw_url[0], str) else ""
        else:
            url = raw_url if isinstance(raw_url, str) else ""
        return status, url

    def generate(self, prompt: str, ratio: str, output_stem: Path, source_image: str = "") -> GeneratedImage:
        request_payload: dict[str, Any] = {
            "model": self.config.model,
            "prompt": prompt,
            "n": 1,
            "size": normalize_ratio(ratio),
            "resolution": self.config.resolution,
        }
        image = source_image_payload(source_image)
        if image:
            request_payload["image_urls"] = [image]
        submitted = self._request_json(self._generation_endpoint(), "POST", request_payload)
        immediate_url = self._immediate_url(submitted)
        task_id = self._task_id(submitted)
        if immediate_url:
            saved = self._download(immediate_url, output_stem)
            return GeneratedImage(saved_path=saved, source_url=immediate_url, task_id=task_id)
        if not task_id:
            raise PunkError("APIMart response did not include an image URL or task_id")

        deadline = time.monotonic() + self.config.timeout_seconds
        while time.monotonic() < deadline:
            self.sleep(self.config.poll_interval_seconds)
            payload = self._request_json(self._task_endpoint(task_id))
            status, result_url = self._completed_url(payload)
            if status == "failed":
                raise PunkError(f"APIMart generation failed: {self._error_message(json.dumps(payload))}")
            if status != "completed":
                continue
            if not result_url:
                raise PunkError("APIMart task completed without an image URL")
            saved = self._download(result_url, output_stem)
            return GeneratedImage(saved_path=saved, source_url=result_url, task_id=task_id)
        raise PunkError(f"APIMart generation timed out after {self.config.timeout_seconds} seconds")

