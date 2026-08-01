# Anthropic Research 风格

```yaml
id: anthropic-research-style
name: Anthropic Research 风格
input_modes: [text]
subjects: [concept, essay, research, technology, knowledge, system]
outputs: [cover, poster, editorial_page]
default_ratio: "5:2"
required_fields: [主题, 主标题, 核心表达, 画幅比例, 用途]
optional_fields: [副标题, 背景方案, 强调色, 不想出现的元素]
source: styles/anthropic-research-style/STYLE.md
style_anchors:
  - restrained AI research-lab editorial cover with a large flat color field
  - one readable serif main title as the primary visual center
  - one abstract hand-drawn line metaphor derived from the topic's core value
  - substantial negative space with 2-4 small organic balancing shapes
  - fixed low-saturation palette using terracotta, black, warm gray, sage green, or haze blue
cover_shape_adaptation:
  - landscape ratios place the title and abstract metaphor in an asymmetric editorial composition with large open space
  - portrait ratios keep the title dominant and the metaphor compact, with decoration occupying no more than 5% of the canvas
  - show only the main title by default; when the user supplies a subtitle, keep it to one short supporting line
  - convert the topic into a conceptual structure, path, node system, outline, or spatial relation instead of drawing the topic object literally
must_preserve:
  - one main title, one core metaphor, and one visual center
  - flat background selected from the fixed color system without gradients
  - serif-led editorial typography with restrained sans-serif or monospace support text
  - sparse hand-drawn linework and stable negative space
avoid_when_applying_to_cover:
  - Anthropic logos, wordmarks, signatures, or copied official layouts
  - marketing-poster hierarchy, product-launch visuals, or commercial template feel
  - robots for AI, ordinary computers for web topics, or book piles for knowledge topics
  - cyberpunk, neon, blue glow, 3D rendering, gradients, dense infographics, or large text blocks
```

## Style Intent

以 Anthropic Research 风格为识别名称，使用纯色背景、衬线主标题、手绘线稿、抽象隐喻和大面积留白形成研究报告式封面。名称用于指代视觉方向，不复制 Anthropic 的 Logo、品牌署名、字标或固定版式。平台适配、长文提炼和通用封面约束由 `punk-cover` 负责。

## Use For

- AI、研究、知识、系统、网页和设计方法主题
- X 封面、文章封面、产品介绍和教程海报
- 需要少量文字、抽象隐喻和纯色背景的编辑封面

## Avoid

- 营销海报、科技发布会和商业模板
- 需要复杂数据图表、产品界面或多场景叙事的内容
- 需要复制真实品牌视觉识别的任务
