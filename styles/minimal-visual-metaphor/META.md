# 极简视觉隐喻风

```yaml
id: minimal-visual-metaphor
name: 极简视觉隐喻风
input_modes: [text]
subjects: [concept, business, technology, system, object, person, scene]
outputs: [cover, poster]
default_ratio: "5:2"
required_fields: [主题词, 画幅比例, 语言, 用途]
optional_fields: [核心动作, 抽象实体, 人物动作, 补充背景, 情绪倾向, 不想出现的元素]
source: styles/minimal-visual-metaphor/STYLE.md
style_anchors:
  - premium business and technology editorial cover with modern Swiss restraint
  - one readable but indirect abstract physical apparatus expressing a single action or change
  - warm white paper-textured background with generous negative space
  - graphite black, charcoal gray, and one low-saturation translucent ink-green accent
  - matte graphite metal, precise black modules, frosted green glass, and soft natural shadows
  - exact readable title in a clean Chinese sans-serif with at most one key word or number highlighted in ink green
cover_shape_adaptation:
  - for landscape ratios, place the exact title on the left in roughly 50-55 percent of the canvas and the metaphor apparatus on the right in roughly 40-45 percent
  - for portrait ratios, place the exact title above and the metaphor apparatus below while retaining one visual center and ample negative space
  - translate the topic into one core action such as connecting, converging, aligning, advancing, dismantling, penetrating, folding, balancing, transforming, growing, or crossing
  - use only a few precise objects; an optional small realistic person may perform the decisive action and provide scale
must_preserve:
  - one single visual story with a clear action, relationship, and result
  - quiet gallery-like composition, precise spacing, and substantial warm-white negative space
  - restrained palette limited to warm white, graphite black, charcoal gray, and low-saturation translucent ink green
  - exact, complete, clearly readable title with no other readable text
  - material realism, soft natural shadows, and premium editorial sculpture quality
avoid_when_applying_to_cover:
  - literal icons, explainer diagrams, instruction-manual illustration, dashboards, or multiple competing concepts
  - cyberpunk, neon, blue-purple gradients, robots, AI brains, chips, sci-fi cities, or screen-filled UI
  - cartoons, home-interior styling, cheap 3D, exaggerated lighting, logos, watermarks, subtitles, borders, or decorative microtext
  - unnecessary people, theatrical poses, visual clutter, or decorative lines without semantic purpose
```

## Style Intent

把商业、科技、组织和系统主题转译为一个“可读但不直白”的抽象实体装置。通过单一核心动作、少量精确物体和可选的小比例人物，表达连接、汇聚、推进、转化或跨越等关系变化。画面像一件置于画廊中的编辑雕塑，克制、高级、清楚，而不是图标化说明或科技概念堆砌。平台适配、长文提炼和通用封面约束由 `punk-cover` 负责。

## Use For

- AI、商业科技、产品、组织、工作流、系统变化和趋势分析
- 需要把抽象关系或变化做成实体隐喻的公众号、X、文章和报告封面
- 需要高级、极简、易读、留白充分的编辑视觉

## Avoid

- 主题只能依赖复杂数据、界面截图或多步骤流程才能说明
- 需要热闹、卡通、霓虹、强娱乐化或多人物叙事的内容
- 无法收束为一个核心动作和一组清楚物体关系的主题
