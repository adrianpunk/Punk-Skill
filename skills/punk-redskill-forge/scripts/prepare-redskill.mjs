#!/usr/bin/env node

import { cpSync, existsSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, rmSync, statSync, writeFileSync } from "node:fs";
import { basename, dirname, extname, join, relative, resolve, sep } from "node:path";
import { tmpdir } from "node:os";
import { spawnSync } from "node:child_process";

const args = process.argv.slice(2);
const value = (flag) => { const index = args.indexOf(flag); return index === -1 ? undefined : args[index + 1]; };
const fail = (message) => { console.error(`ERROR: ${message}`); process.exit(2); };
if (args.includes("--help") || args.includes("-h")) {
  console.log("用法：node prepare-redskill.mjs --source <本地文件夹|ZIP|链接> --output <输出目录> [--skill <相对路径>] [--title <标题>] [--version <版本>]\n\n创建独立 REDSkill 候选副本，绝不修改源文件；仅在没有阻断项时生成上传 ZIP。");
  process.exit(0);
}

const sourceArg = value("--source");
const outputArg = value("--output");
if (!sourceArg || !outputArg) fail("必须提供 --source 和 --output。");
const outputDir = resolve(outputArg);
if (existsSync(outputDir)) fail(`输出目录已存在：${outputDir}。请使用新的目录。`);

const workDir = mkdtempSync(join(tmpdir(), "punk-redskill-forge-"));
const sourceRoot = join(workDir, "source");
const blockers = [];
const warnings = [];
const notes = [];
const ignoredNames = new Set([".git", "node_modules", ".DS_Store", "__MACOSX", ".pytest_cache", ".next", "dist", "build", "coverage"]);
const ignoredExtensions = new Set([".pyc", ".pyo", ".class", ".o", ".so", ".dylib"]);
const textExtensions = new Set([".md", ".txt", ".yaml", ".yml", ".json", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".py", ".sh", ".bash", ".zsh", ".toml", ".ini", ".cfg", ".xml", ".html", ".css", ".csv"]);

function run(command, commandArgs, cwd) {
  const result = spawnSync(command, commandArgs, { cwd, encoding: "utf8" });
  if (result.status !== 0) fail(`${command} failed: ${(result.stderr || result.stdout || "unknown error").trim()}`);
}
function materializeSource() {
  if (/^https:\/\/(www\.)?github\.com\//.test(sourceArg) || /^git@github\.com:/.test(sourceArg)) {
    run("git", ["clone", "--depth", "1", sourceArg, sourceRoot]);
    return;
  }
  const path = resolve(sourceArg);
  if (!existsSync(path)) fail(`源文件不存在：${path}`);
  if (statSync(path).isDirectory()) { cpSync(path, sourceRoot, { recursive: true, dereference: false }); return; }
  if (extname(path).toLowerCase() === ".zip") { mkdirSync(sourceRoot); run("unzip", ["-q", path, "-d", sourceRoot]); return; }
  fail("源文件必须是本地文件夹、ZIP 压缩包或 GitHub 链接。");
}
function walk(root, callback) {
  for (const entry of readdirSync(root, { withFileTypes: true })) {
    if (ignoredNames.has(entry.name)) continue;
    const absolute = join(root, entry.name);
    if (entry.isDirectory()) walk(absolute, callback);
    else if (entry.isFile()) callback(absolute);
  }
}
function findSkillFiles(root) {
  const found = [];
  walk(root, (file) => { if (basename(file) === "SKILL.md") found.push(file); });
  return found;
}
function selectSkill() {
  const wanted = value("--skill");
  const skillFiles = findSkillFiles(sourceRoot);
  if (wanted) {
    const candidate = resolve(sourceRoot, wanted);
    const target = basename(candidate) === "SKILL.md" ? candidate : join(candidate, "SKILL.md");
    if (!target.startsWith(sourceRoot + sep) || !existsSync(target)) fail(`找不到指定的 Skill：${wanted}`);
    return target;
  }
  if (skillFiles.length === 1) return skillFiles[0];
  if (skillFiles.length === 0) fail("源文件中没有找到 SKILL.md。");
  fail(`发现多个 Skill；请用 --skill 指定其中一个：\n${skillFiles.map((f) => `  - ${relative(sourceRoot, dirname(f))}`).join("\n")}`);
}
function copyCandidate(skillFile) {
  const skillDir = dirname(skillFile);
  mkdirSync(outputDir, { recursive: true });
  for (const entry of readdirSync(skillDir)) if (!ignoredNames.has(entry)) cpSync(join(skillDir, entry), join(outputDir, entry), { recursive: true, dereference: false });
  let ancestor = skillDir;
  while (ancestor.startsWith(sourceRoot)) {
    const licence = readdirSync(ancestor).find((entry) => /^(licen[cs]e|copying)(\.[a-z0-9-]+)?$/i.test(entry));
    if (licence) {
      const destination = join(outputDir, licence);
      if (!existsSync(destination)) {
        cpSync(join(ancestor, licence), destination, { recursive: false, dereference: false });
        notes.push(`已从源文件树复制 ${licence}，便于许可证追溯。`);
      }
      break;
    }
    if (ancestor === sourceRoot) break;
    ancestor = dirname(ancestor);
  }
  const skillCopy = join(outputDir, "SKILL.md");
  const content = readFileSync(skillCopy, "utf8");
  const styleRef = resolve(skillDir, "../../styles");
  if (content.includes("../../styles/") && existsSync(styleRef) && statSync(styleRef).isDirectory()) {
    cpSync(styleRef, join(outputDir, "styles"), { recursive: true, dereference: false });
    writeFileSync(skillCopy, content.replaceAll("../../styles/", "styles/"));
    notes.push("已复制仓库级 styles 资源，并将 ../../styles/ 引用改为从 ZIP 根目录解析。");
  }
}
function addFinding(kind, file, line, excerpt) {
  const entry = { kind, target: `${relative(outputDir, file)}:${line}`, excerpt };
  (kind.startsWith("BLOCKER") ? blockers : warnings).push(entry);
}
function scanFile(file) {
  const ext = extname(file).toLowerCase();
  const rel = relative(outputDir, file);
  if (ignoredExtensions.has(ext)) { warnings.push({ kind: "WARN_BINARY_OR_EXECUTABLE", target: rel, excerpt: "保留了编译产物或缓存文件；请确认它是否必需。" }); return; }
  if (!textExtensions.has(ext)) { warnings.push({ kind: "WARN_BINARY_OR_EXECUTABLE", target: rel, excerpt: "保留了非文本文件；请检查安全性、用途、授权与披露。" }); return; }
  const content = readFileSync(file, "utf8");
  const checks = [
    ["BLOCKER_SECRET_PATTERN", /-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|(?:api[_-]?key|password|secret|token)\s*[:=]\s*["'][^"'\s]{12,}/i],
    ["BLOCKER_XHS_AUTOMATION_PATTERN", /(?:xhs\s+(?:post|comment|reply|like|follow)|xiaohongshu.{0,45}(?:auto(?:matically)?\s*(?:post|publish|comment|reply|like|follow)|自动(?:发布|评论|回复|点赞|关注))|自动(?:发布笔记|回复评论|点赞|关注))/i],
    ["BLOCKER_HIDDEN_BEHAVIOR_PATTERN", /(?:ignore (?:all |any |the )?(?:previous|prior) instructions|hidden (?:behavior|action|function)|secretly (?:collect|send|upload|execute)|绕过(?:用户|安全|限制))/i],
  ];
  for (const [kind, pattern] of checks) {
    const match = content.match(pattern);
    if (match && match.index !== undefined) addFinding(kind, file, content.slice(0, match.index).split("\n").length, match[0].slice(0, 180));
  }
  if (/(?:anthropic|openai|google|apple|microsoft|xiaohongshu)\s+(?:style|风格|logo|商标)/i.test(content)) {
    const match = content.match(/(?:anthropic|openai|google|apple|microsoft|xiaohongshu).{0,80}/i);
    warnings.push({ kind: "WARN_THIRD_PARTY_BRANDING", target: rel, excerpt: (match?.[0] || "第三方品牌内容").slice(0, 180) });
  }
  for (const match of content.matchAll(/(?:\.\.\/)+[A-Za-z0-9_.-]+\/[A-Za-z0-9_./-]+/g)) {
    const potential = resolve(dirname(file), match[0]);
    if (!potential.startsWith(outputDir + sep) || !existsSync(potential)) warnings.push({ kind: "WARN_EXTERNAL_REFERENCE", target: rel, excerpt: `可能无法解析的相对引用：${match[0]}` });
  }
}
function scanCandidate() { walk(outputDir, scanFile); }
function description() {
  const text = readFileSync(join(outputDir, "SKILL.md"), "utf8");
  const frontmatter = text.match(/^---\s*\n([\s\S]*?)\n---/);
  return frontmatter?.[1].match(/^description:\s*["']?(.+?)["']?\s*$/m)?.[1] || "[请人工补充准确的用户可见功能说明]";
}
function slugify(input) { return input.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "redskill"; }
function writeDocs(skillFile) {
  const inferred = basename(dirname(skillFile));
  const title = value("--title") || inferred.replace(/[-_]+/g, " ");
  const version = value("--version") || "0.1.0";
  const capability = description();
  const report = (items) => items.length ? items.map((item) => `- **${item.kind}** — \`${item.target}\`: ${item.excerpt}`).join("\n") : "- 机械扫描未发现问题。";
  writeFileSync(join(outputDir, "REDSKILL-AUDIT.md"), `# REDSkill 上传前审计\n\n- 来源：\`${sourceArg}\`\n- 选定的源 Skill：\`${relative(sourceRoot, skillFile)}\`\n- 候选版本：\`${version}\`\n- 状态：**${blockers.length ? "已阻断：解决全部阻断项后方可上传" : "未发现机械扫描阻断项：仍须人工复核"}**\n\n## 阻断项\n\n${report(blockers)}\n\n## 警告项\n\n${report(warnings)}\n\n## 打包说明\n\n${notes.length ? notes.map((note) => `- ${note}`).join("\n") : "- 候选副本由选定 Skill 文件夹复制而来，原始 Skill 未被修改。"}\n\n## 必须人工复核\n\n- 确认包内实际代码和提示词，与声明的功能、权限、数据使用及输出一致。\n- 确认全部依赖、第三方内容、名称和素材拥有适当许可证或授权。\n- 确认不存在小红书账号自动化、凭证处理、隐藏行为或未声明的网络/本地数据访问。\n- 提交前查看小红书最新 REDSkill 官方规范与上传页。\n`);
  writeFileSync(join(outputDir, "REDSKILL-SUBMISSION-FIELDS.md"), `# REDSkill 提交字段草案\n\n- 建议标题：\`${title}\`\n- 建议版本：\`${version}\`\n- 功能说明：${capability}\n- 来源：\`${sourceArg}\`\n- 建议的数据/权限说明：\`仅使用用户在当前任务中提供的文字、图片和设置；不请求凭证、Cookie、API Key、浏览器数据或无关的本地文件。\`\n\n请复核并替换所有无法准确描述源 Skill 的字段。不要宣称官方背书、保证审核通过、保证结果，或声称包内并未实现的能力。\n`);
  writeFileSync(join(outputDir, "README-REDSKILL.md"), `# ${title}\n\n这是根据 \`${sourceArg}\` 单独整理的 REDSkill 候选副本，用于透明检查和 REDSkill 提交前审阅。\n\n## 声明功能\n\n${capability}\n\n## 边界\n\n本包不得自动操作小红书账号、收集凭证/Cookie/API Key、访问无关本地数据或执行隐藏行为。提交前请阅读 \`REDSKILL-AUDIT.md\`。\n`);
  return slugify(title);
}

try {
  materializeSource();
  const skillFile = selectSkill();
  copyCandidate(skillFile);
  scanCandidate();
  const slug = writeDocs(skillFile);
  if (blockers.length) {
    console.error(`预检已阻断。审计报告：${join(outputDir, "REDSKILL-AUDIT.md")}`);
    process.exitCode = 1;
  } else {
    const zipPath = resolve(dirname(outputDir), `${slug}-redskill.zip`);
    if (existsSync(zipPath)) fail(`ZIP 已存在：${zipPath}。请使用其他输出目录，或由用户明确决定如何处理旧文件。`);
    run("zip", ["-qr", zipPath, "."], outputDir);
    console.log(`候选副本已创建：${outputDir}\n上传压缩包已创建：${zipPath}\n提交前请阅读：${join(outputDir, "REDSKILL-AUDIT.md")}`);
  }
} finally {
  rmSync(workDir, { recursive: true, force: true });
}
