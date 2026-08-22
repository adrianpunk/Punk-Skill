# Punk REDSkill Forge

把任意可用的 Agent Skill 整理为适合提交小红书 REDSkill 的独立副本。

## 怎么用

在支持 Skills 的 Agent 中直接说：

```text
帮我把这个 Skill 整理成可上传 REDSkill 的版本：
<粘贴链接、文件夹路径或 ZIP 路径>
```

若一个来源中含有多个 Skill，系统会请你选择其中一个，而不会把它们混在一起。

## 它会做什么

- 原始 Skill 保持不变，另建可审查的上传副本。
- 检查疑似密钥、Cookie、隐藏指令、小红书账号自动化及第三方品牌/素材风险。
- 将常见的跨目录风格资源复制进副本，并修正其在 ZIP 中的相对路径。
- 生成 `REDSKILL-AUDIT.md`、`REDSKILL-SUBMISSION-FIELDS.md` 和根目录包含 `SKILL.md` 的上传 ZIP。
- 发现高风险阻断项时，不生成上传 ZIP，而是输出可定位的问题清单。

## 边界

它不代替小红书审核，也不保证审核通过。它不会替你提交或发布，也不会把自动发笔记、自动评论/回复/点赞/关注、凭证收集、Cookie 读取、隐藏行为等能力包装成合规 Skill。

发布前仍需核对小红书最新 REDSkill 规范、上传页字段和第三方素材/代码的授权情况。

## 技术预检（可选）

```sh
node scripts/prepare-redskill.mjs \
  --source "<链接、本地文件夹或 ZIP>" \
  --output "<输出目录>"
```

若来源中有多个 Skill，加上 `--skill "<相对目录或 SKILL.md>"` 指定目标。
