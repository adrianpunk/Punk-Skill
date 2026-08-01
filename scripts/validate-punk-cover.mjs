import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(scriptDir, "..");
const skillPath = path.join(root, "skills", "punk-cover", "SKILL.md");
const blueprintPath = path.join(root, "skills", "punk-cover", "references", "cover-prompt-blueprint.md");
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

const skill = read(skillPath);
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
];

for (const check of skillChecks) {
  if (!check.test(skill)) {
    fail(`SKILL.md missing required compile rule phrase: ${check.label}`);
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
