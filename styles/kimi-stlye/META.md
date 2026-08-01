# kimi风格

```yaml
id: kimi-stlye
name: kimi风格
input_modes: [text]
subjects: [concept, object, product, material, research, system, scene]
outputs: [cover, poster, editorial_page]
default_ratio: "5:2"
required_fields: [主题, 主标题, 画幅比例, 语言, 用途]
optional_fields: [副标题, 核心概念, 主视觉物件, 辅助物件, 补充背景, 不想出现的元素]
source: styles/kimi-stlye/STYLE.md
style_anchors:
  - top-down archival still-life photography on a large softly lit table
  - pale gray-green or light mint background with restrained low-saturation materials
  - one abstract topic translated into a small set of real, relevant objects
  - Swiss editorial layout with a clean title zone and generous negative space
  - realistic metal, glass, wood, ceramic, paper, textile, pigment, or prototype materials
cover_shape_adaptation:
  - choose or preserve the platform ratio and rebuild the object layout for each landscape, portrait, or square canvas
  - keep the title area clean and readable instead of filling the whole table
  - use a small number of objects with clear hierarchy, spacing, overlap, and natural shadows
  - change the object set and spatial relationship for each topic; do not reuse a fixed archive-desk template
must_preserve:
  - top-down still-life photography and soft diffused light
  - pale gray-green or light mint background with low-saturation supporting colors
  - one clear title, one core concept, and one coherent object system
  - every object has a visible relationship to the topic
  - real material texture and enough negative space for an editorial cover
avoid_when_applying_to_cover:
  - Kimi logos, wordmarks, interface elements, signatures, or copied official layouts
  - fixed object combinations, paper piles, file clutter, or meaningless decoration
  - neon technology style, cyberpunk, cheap futurism, complex UI, or excessive glow
  - unreadable title, garbled text, dense microtype, or a table filled edge to edge
```

## Style Intent

以 `kimi风格` 为识别名称，把主题转化为俯视角档案桌静物摄影。使用淡灰绿灯箱桌面、少量真实物件、编辑排版和大面积留白，形成项目档案或设计研究桌的封面。名称用于指代视觉方向，不复制 Kimi 的 Logo、字标、产品界面或固定官方版式。平台适配、长文提炼和通用封面约束由 `punk-cover` 负责。

## Use For

- AI、研究、知识、产品、材料、系统和创意项目主题
- X、公众号、文章、产品介绍、教程和项目档案封面
- 需要真实静物摄影、概念物件和低饱和编辑排版的内容

## Avoid

- 需要人物叙事、复杂信息图、界面展示或动态场景的内容
- 无法转化为少量相关物件、只能依赖大量文字说明的主题
- 需要复制真实品牌界面、Logo 或广告画面的任务
