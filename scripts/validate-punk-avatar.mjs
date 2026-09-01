import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(scriptDir, "..");
const skillPath = path.join(root, "skills", "punk-avatar", "SKILL.md");
const catalogPath = path.join(root, "skills", "punk-avatar", "references", "style-catalog.md");
const blueprintPath = path.join(root, "skills", "punk-avatar", "references", "avatar-prompt-blueprint.md");

const allowedStyleIds = [
  "pixel-avatar",
  "grotesque-soul-sketch",
  "messy-crayon-pet-portrait",
  "fashion-sketch-observation",
  "polaroid-keepsake",
  "minimal-paper-acrylic-block-illustration",
  "surreal-pop-up-paper-landscape",
];

function read(file) {
  return fs.readFileSync(file, "utf8");
}

function fail(message) {
  failures.push(message);
}

const failures = [];

for (const file of [skillPath, catalogPath, blueprintPath]) {
  if (!fs.existsSync(file)) {
    fail(`Missing required file: ${path.relative(root, file)}`);
  }
}

if (!failures.length) {
  const skill = read(skillPath);
  for (const phrase of [
    "compile that style atom into the avatar shape",
    "references/avatar-prompt-blueprint.md",
    "Do not append the raw `STYLE.md` content as a standalone second section",
    "Default ratio is always `1:1` inside `punk-avatar`",
  ]) {
    if (!skill.includes(phrase)) {
      fail(`SKILL.md missing required compile rule phrase: ${phrase}`);
    }
  }

  const catalog = read(catalogPath);
  const catalogStyleIds = [...catalog.matchAll(/\|\s*[^|\n]+\|\s*`([a-z0-9-]+)`\s*\|/g)].map(
    (match) => match[1],
  );
  const uniqueCatalogStyleIds = [...new Set(catalogStyleIds)];
  const disallowed = uniqueCatalogStyleIds.filter((id) => !allowedStyleIds.includes(id));
  const missing = allowedStyleIds.filter((id) => !uniqueCatalogStyleIds.includes(id));

  if (disallowed.length) {
    fail(`Avatar catalog contains disallowed style IDs: ${disallowed.join(", ")}`);
  }

  if (missing.length) {
    fail(`Avatar catalog missing allowed style IDs: ${missing.join(", ")}`);
  }

  for (const styleId of allowedStyleIds) {
    const stylePath = path.join(root, "styles", styleId, "STYLE.md");
    const promptPath = path.join(root, "styles", styleId, "STYLE.md");

    if (!fs.existsSync(stylePath)) {
      fail(`Missing style metadata: ${path.relative(root, stylePath)}`);
    }

    if (!fs.existsSync(promptPath)) {
      fail(`Missing style file: ${path.relative(root, promptPath)}`);
    }
  }

  for (const modeFile of ["before-after.md", "final-artwork.md"]) {
    const modePath = path.join(
      root,
      "styles",
      "surreal-pop-up-paper-landscape",
      "references",
      modeFile,
    );
    if (!fs.existsSync(modePath)) {
      fail(`Missing surreal paper-art mode: ${path.relative(root, modePath)}`);
    }
  }

  const surrealStylePath = path.join(
    root,
    "styles",
    "surreal-pop-up-paper-landscape",
    "STYLE.md",
  );
  if (fs.existsSync(surrealStylePath)) {
    const surrealStyle = read(surrealStylePath);
    for (const phrase of ["before-after", "final-artwork", "75°–85°", "10%–20%"]) {
      if (!surrealStyle.includes(phrase)) {
        fail(`surreal-pop-up-paper-landscape STYLE.md missing mode anchor: ${phrase}`);
      }
    }
  }

  const blueprint = read(blueprintPath);
  for (const phrase of [
    "Likeness Policy",
    "Crop",
    "profile-picture size",
    "For `polaroid-keepsake`, keep the polaroid frame recognizable even at `1:1`",
  ]) {
    if (!blueprint.includes(phrase)) {
      fail(`avatar-prompt-blueprint.md missing required avatar rule phrase: ${phrase}`);
    }
  }
}

if (failures.length) {
  console.error("punk-avatar validation failed:");
  for (const item of failures) console.error(`- ${item}`);
  process.exit(1);
}

console.log(`punk-avatar validation passed for ${allowedStyleIds.length} avatar styles.`);
