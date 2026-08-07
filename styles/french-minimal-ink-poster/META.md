# 法式极简墨线海报

```yaml
id: french-minimal-ink-poster
name: 法式极简墨线海报
input_modes: [text]
subjects: [concept, essay, technology, relationship, emotion, system, choice]
outputs: [cover, poster]
default_ratio: "5:2"
required_fields: [主题词, 主标题, 画幅比例, 语言, 用途]
optional_fields: [副标题, 补充背景, 情绪倾向, 核心隐喻, 主体类型, 强调色, 不想出现的元素]
source: styles/french-minimal-ink-poster/STYLE.md
style_anchors:
  - warm ivory or old-paper background with 70%-85% negative space
  - sparse black hand-drawn ink lines, brush marks, broken edges, and slight bleeding
  - one precise visual metaphor derived from the topic's core judgment
  - French editorial poster typography with clear title hierarchy
  - at most one tiny restrained accent color on a word, line, node, or small detail
cover_shape_adaptation:
  - landscape ratios use asymmetric title and visual-subject placement with large open space between them
  - portrait ratios keep the main visual center small or partially cropped, leaving a calm editorial field for title and subtitle
  - title must remain one of the first visual anchors and may break into 2-3 lines when long
  - visual subject can be a person, object, abstract structure, distance, break, shadow, or digital trace depending on topic meaning
must_preserve:
  - one core metaphor, one main visual center, one readable main title
  - quiet French minimal editorial mood
  - hand-drawn ink texture, incomplete contours, and restrained paper warmth
  - "sparse text: one title and at most 1-2 short subtitle lines"
  - technology themes must include a subtle but clear digital trace without becoming tech UI
avoid_when_applying_to_cover:
  - using the topic noun directly as a generic icon
  - defaulting every topic to a face, hand, back view, heart, bird, cage, rope, road, moon, bulb, clock, or seedling
  - chips, robots, mechanical brains, glowing networks, dashboards, or data panels for AI and technology topics
  - photo realism, 3D rendering, commercial technology landing-page style, infographic layout, or icon stacks
  - multiple metaphors, crowded scenes, large blocks of text, watermarks, signatures, dates, URLs, or unrelated brand marks
```

## Style Intent

用法式编辑海报的克制排版、大片留白和手绘墨线，把文章主题压缩成一个准确的视觉隐喻。重点不是画全主题，而是先理解核心观点、矛盾、情绪和因果，再选择人物、物体、结构、距离、遮挡或轻微数字痕迹作为唯一视觉中心。该 style 只负责墨线极简海报的视觉语言；平台适配、长文提炼和通用封面结构由 `punk-cover` 负责。

## Use For

- AI、互联网、算法、数字世界等需要克制科技联想的观点封面
- 爱情、关系、孤独、信任、选择、成长和告别等情绪或人生主题
- 制度、规则、效率、循环、信息差、边界、秩序和风险等抽象议题
- 需要安静、高级、少文字、大留白、强隐喻的公众号、X 头图和艺术海报

## Avoid

- 需要强营销感、复杂叙事、产品功能展示或信息图说明的内容
- 需要鲜艳多色、照片质感、3D 质感、赛博科技光效或大面积装饰背景的封面
- 主题必须展示多个概念、多个角色、完整场景或详细流程时
