import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(scriptDir, "..");
const skillPath = path.join(root, "skills", "punk-cover", "SKILL.md");
const blueprintPath = path.join(root, "skills", "punk-cover", "references", "cover-prompt-blueprint.md");
const platformCatalogPath = path.join(root, "skills", "punk-cover", "references", "platform-catalog.md");
const englishReadmePath = path.join(root, "README.en.md");
const stylesDir = path.join(root, "styles");

const requiredStyleFields = [
  "style_anchors:",
  "cover_shape_adaptation:",
  "must_preserve:",
  "avoid_when_applying_to_cover:",
];

function read(file) {
  return fs.readFileSync(file, "utf8");
}

function fail(message) {
  failures.push(message);
}

function fencedYaml(markdown) {
  const match = markdown.match(/```yaml\r?\n([\s\S]*?)\r?\n```/);
  return match ? match[1] : "";
}

const failures = [];

if (!fs.existsSync(blueprintPath)) {
  fail(`Missing cover prompt blueprint: ${path.relative(root, blueprintPath)}`);
}

if (!fs.existsSync(platformCatalogPath)) {
  fail(`Missing platform catalog: ${path.relative(root, platformCatalogPath)}`);
}

if (!fs.existsSync(englishReadmePath)) {
  fail(`Missing English README: ${path.relative(root, englishReadmePath)}`);
}

const skill = read(skillPath);
const platformCatalog = fs.existsSync(platformCatalogPath) ? read(platformCatalogPath) : "";
const englishReadme = fs.existsSync(englishReadmePath) ? read(englishReadmePath) : "";
const skillChecks = [
  {
    label: "compile that style atom into the cover shape",
    test: (text) => text.includes("compile that style atom into the cover shape"),
  },
  {
    label: "references/cover-prompt-blueprint.md",
    test: (text) => text.includes("references/cover-prompt-blueprint.md"),
  },
  {
    label: "do not append raw style content as a standalone second section",
    test: (text) =>
      /Do not append (the )?raw [`\w.-]+ content as a standalone second section/.test(text),
  },
  {
    label: "localized language mode",
    test: (text) =>
      text.includes("host system language/locale") &&
      text.includes("中文") &&
      text.includes("English"),
  },
  {
    label: "automatic nearest-ratio resolution",
    test: (text) =>
      text.includes("automatically resolve to the numerically closest") &&
      text.includes("do not ask the user to choose another ratio"),
  },
  {
    label: "platform catalog reference",
    test: (text) => text.includes("references/platform-catalog.md"),
  },
];

for (const check of skillChecks) {
  if (!check.test(skill)) {
    fail(`SKILL.md missing required compile rule phrase: ${check.label}`);
  }
}

const platformChecks = [
  ["supported generation ratios", "Supported generation ratios"],
  ["X requested ratio", "5:2"],
  ["WeChat requested ratio", "2.35:1"],
  ["closest-ratio disclosure", "Only the closest supported ratio can be generated"],
  ["X resolved ratio", "| X | `5:2` | `21:9` |"],
  ["WeChat resolved ratio", "| 微信公众号 | WeChat public account | `2.35:1` | `21:9` |"],
  ["global platform option", "Instagram"],
];

for (const [label, phrase] of platformChecks) {
  if (!platformCatalog.includes(phrase)) {
    fail(`Platform catalog missing ${label}: ${phrase}`);
  }
}

const readmeChecks = [
  ["language switch link", "[中文](./README.md)"],
  ["global platform coverage", "Instagram, Facebook, LinkedIn, YouTube, TikTok"],
  ["ratio limitation guidance", "does not claim compliance with any platform's cover-size standard"],
];

for (const [label, phrase] of readmeChecks) {
  if (!englishReadme.includes(phrase)) {
    fail(`README.en.md missing ${label}: ${phrase}`);
  }
}

const styleDirs = fs
  .readdirSync(stylesDir)
  .map((name) => path.join(stylesDir, name))
  .filter((dir) => fs.statSync(dir).isDirectory());

let eligibleCount = 0;
for (const dir of styleDirs) {
  const metaFile = path.join(dir, "META.md");
  const styleFile = path.join(dir, "STYLE.md");
  if (!fs.existsSync(metaFile)) {
    fail(`${path.relative(root, dir)} missing META.md`);
    continue;
  }

  const markdown = read(metaFile);
  const yaml = fencedYaml(markdown);
  if (!yaml) {
    fail(`${path.relative(root, metaFile)} has no fenced yaml metadata`);
    continue;
  }

  const isCoverStyle = /outputs:\s*\[[^\]]*\b(cover|poster)\b[^\]]*\]/.test(yaml);
  if (!isCoverStyle) continue;

  eligibleCount += 1;
  if (!fs.existsSync(styleFile)) {
    fail(`${path.relative(root, dir)} missing STYLE.md`);
  }

  for (const field of requiredStyleFields) {
    if (!yaml.includes(field)) {
      fail(`${path.relative(root, metaFile)} missing ${field}`);
    }
  }
}

if (eligibleCount === 0) {
  fail("No cover/poster styles found");
}

if (failures.length) {
  console.error("punk-cover validation failed:");
  for (const item of failures) console.error(`- ${item}`);
  process.exit(1);
}

console.log(`punk-cover validation passed for ${eligibleCount} cover/poster styles.`);
