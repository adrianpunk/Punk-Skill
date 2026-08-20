# 复古时代错位编辑封面

```yaml
id: midcentury-surreal-editorial-cover
name: 复古时代错位编辑封面
input_modes: [text]
subjects: [concept, person, object, technology, scene, editorial_topic]
outputs: [cover, poster, editorial_page]
default_ratio: "auto"
required_fields: [主题或主标题, 画幅比例]
optional_fields: [副标题, 人物设定, 情感倾向, 语言, 用途, 补充背景, 不想出现的元素]
source: styles/midcentury-surreal-editorial-cover/STYLE.md
style_anchors:
  - modern minimal editorial cover composition with large warm-white negative space
  - 1940s-1960s American commercial illustration characters with varied faces, ages, roles, and actions
  - one contemporary or future object used as a clear era-displacement visual metaphor
  - vintage magazine collage edges, halftone dots, faded ink, paper fibers, and screen-print grain
  - restrained 3-5 color palette with black editorial typography and no generic AI-tech tropes
cover_shape_adaptation:
  - landscape covers reserve roughly 65-75 percent on the left for title and breathing room and 25-35 percent on the right for the visual event
  - portrait covers place title in the upper or upper-left area and the visual event in the lower or lower-right area
  - square covers remain visibly asymmetric rather than splitting the canvas into equal panels
  - dissolve illustration edges into the paper with feathered ink, dry-brush fade, collage erosion, or halftone disappearance instead of regular frames
must_preserve:
  - one topic, one action, one core object, one main metaphor, and one era-displacement relationship
  - clear, accurate, readable title with minimal supporting text
  - recognizable mid-century commercial illustration character without repeating a fixed face or gender pairing
  - modern object must serve the topic rather than exist as decorative technology
  - warm-white paper field, editorial hierarchy, and deliberate asymmetry
avoid_when_applying_to_cover:
  - generic AI imagery such as neon blue-purple gradients, cyberpunk glow, robots, AI brains, chips, holographic HUDs, code rain, or floating UI walls
  - photorealism, smooth modern digital painting, 3D CG, anime, or a generic beautiful recurring face
  - centered hero portrait, static people facing camera, equal left-right split, full-bleed busy scene, or hard rectangular collage frame
  - unnecessary props, multiple competing metaphors, feature lists, icons, logos, watermarks, dense labels, or fake magazine mastheads
```

## Style Intent

把今天或未来才会发生的主题，交给一位 1958 年的美国商业插画师来描绘。用现代极简编辑设计承载 1940s–1960s 复古商业插画人物，让人物正在使用一个当代或未来物件，并通过一次克制的超现实时代错位表达主题。该 style 只负责复古人物、时代错位、视觉隐喻、纸张印刷质感和编辑留白；平台适配、长文提炼和通用封面流程由 `punk-cover` 负责。

## Use For

- AI、Coding、数字人、知识库、创作工具、未来工作和技术改变人的主题
- 需要像独立杂志封面一样有观点、有故事、有复古质感的文章、X 头图、公众号封面和海报
- 需要人物动作与现代物件共同承载抽象概念，而不是把主题画成科技图标的内容

## Avoid

- 只需要纯文字、纯几何、摄影或严格信息图的任务
- 必须依赖大量说明文字、多个功能模块或多步骤流程才能成立的主题
- 无法收束为一个动作、一个核心物体和一个时代错位关系的内容
