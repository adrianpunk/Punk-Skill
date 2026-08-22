---
name: punk-redskill-forge
description: 将一个 Skill 整理为适合上传小红书 REDSkill 的独立副本，生成安全审计、提交字段和上传 ZIP。适用于用户提供链接、文件夹或 ZIP；不可用于自动运营小红书账号。
---

# Punk REDSkill Forge

把用户提供的 Skill 整理为一个独立、可审查的 REDSkill 上传包，且绝不修改原始 Skill。产物是诚实可安装的副本、审计报告和提交字段草案，而不是“保证审核通过”的承诺。

## 对用户的说法

默认用中文沟通与输出。用户可以直接这样说：

```text
帮我把这个 Skill 整理成可上传 REDSkill 的版本：
<粘贴链接、文件夹路径或 ZIP 路径>
```

不要要求用户使用英文命令，也不要把来源标签化为“GitHub Skill”。当来源确实是 GitHub 链接时，可在审计报告的“来源”字段中如实记录链接。

## 安全边界

绝不打包或协助隐藏以下内容：

- 自动发布笔记、评论、回复、点赞、关注或刷互动等账号运营能力；
- 凭证、Cookie、私钥、Token、API Key、浏览器数据，或无法说明用途的数据收集；
- 违法服务、夸大功能、暗中改变 Agent 行为的提示词，或隐藏功能。

发现上述内容时，停止打包并在审计中列为“阻断项”。不要为了让检查通过而暗中删除功能；应说明问题并要求作者明确移除或重新设计。不得代替用户发布到小红书。

## 工作流程

1. 接收链接、本地文件夹或 ZIP。若找到多个 `SKILL.md`，请用户选择要整理的 Skill；不要自动合并无关 Skill。用户提供路径或链接仅授权检查和复制，不授权修改原件或发布。
2. 阅读 [REDSkill 上传规范](references/redskill-upload-policy.md)，并使用小红书 CLI 核对当前官方通知后再作合规判断。平台最新规范与上传页提示优先。
3. 运行预检工具。它会创建独立副本、扫描阻断项，并写出审计：

```sh
node scripts/prepare-redskill.mjs \
  --source "<github-url | local-directory | zip>" \
  --output "<output-directory>" \
  [--skill "<relative-folder-or-SKILL.md>"]
```

如存在阻断项，命令会以非零状态结束且不生成上传 ZIP；原始 Skill 始终不会被修改。

4. 阅读 `REDSKILL-AUDIT.md`。所有阻断项必须通过明确的源文件改动或作者确认的移除/重构来解决。警告项也需要有记录在案的判断；“未命中规则”不等于绝对安全。
5. 将副本与原件对照审查。保留真实功能及必需的代码/资源，只改写必要的说明、权限、数据使用、来源归属与用户可见声明。若所选 Skill 依赖文件夹外的资源，确保资源被复制且路径能从 ZIP 根目录解析。
6. 将生成的 `REDSKILL-SUBMISSION-FIELDS.md` 作为真实的表单草案。标题、说明、标签和封面必须描述同一项实际能力；发布后保持 Skill ID 稳定。

## 无法直接完成时

- 多个 Skill：请用户选定源子目录，不自动合并。
- 凭证、账号自动化、隐藏行为或违规服务：停止并报告阻断项。
- 外部依赖缺失或路径断裂：不得猜测；仅在许可证/权利和功能清楚时打包依赖，否则请作者决定。
- 第三方风格、名称或素材：仅在权利和署名明确时保留；复用权不清楚的品牌预设优先移除。

## 交付内容

对于无阻断项的候选包，交付：

- `<slug>-redskill.zip`：`SKILL.md` 位于压缩包根目录；
- `REDSKILL-AUDIT.md`：检查结果、警告、来源与剩余人工审核项；
- `REDSKILL-SUBMISSION-FIELDS.md`：不夸大的提交字段草案；
- 解压后的完整副本，供透明检查。

根据 [预检结果说明](references/preflight-interpretation.md) 处理发现项。`references/redskill-upload.rule.yml` 是用于独立定性复核的可选 x-cmd 规则集，使用前先执行 `x rule lint`。
