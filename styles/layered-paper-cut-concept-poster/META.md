# 立体纸雕概念海报

```yaml
id: layered-paper-cut-concept-poster
name: 立体纸雕概念海报
input_modes: [text]
subjects: [concept, object, scene, typography]
outputs: [cover, poster]
default_ratio: "5:2"
required_fields: [主题或主标题]
optional_fields: [副标题, 画幅比例, 输出尺寸, 输出模式, 用途, 语言, 文字模式, 情感倾向, 色彩倾向, 补充语境, 必须出现, 禁止出现]
source: styles/layered-paper-cut-concept-poster/STYLE.md
style_anchors:
  - physically believable layered cut paper with visible thickness, apertures, fibers, folds, curled edges, and soft contact shadows
  - one precise conceptual metaphor expressed through a single spatial relationship or transformation
  - generous negative space, one focal composition, and restrained editorial hierarchy
  - title integrated into the paper construction as a cutout, layer, window, path, enclosure, or interleaved structure
  - limited coherent palette and one unified studio light shared by image, typography, and paper layers
cover_shape_adaptation:
  - derive one high-impact core word for the first visual when the source title is long, while preserving the complete title as secondary information
  - recompose subject scale, title placement, whitespace, reading direction, paper-layer direction, and information density for every target ratio
  - for a requested multi-size suite, compile and generate one independently composed image per ratio while preserving the same metaphor, material, palette, and identity
  - reduce information in ultra-wide or ultra-tall formats and emphasize one simple visual relationship
must_preserve:
  - real paper-cut construction rather than a flat illustration with a paper texture filter
  - exactly one main visual metaphor and one clear focal point
  - shared lighting, perspective, materiality, and depth across text, image, and paper layers
  - accurate user text, premium negative space, controlled color, and natural paper shadows
avoid_when_applying_to_cover:
  - flat illustration, childish craft, simple cut-paper border, decorative clutter, multiple competing subjects, or dense information
  - plastic, foam, metal, neon technology, cheap CGI, hard black shadows, or overcomplicated backgrounds
  - fabricated editorial text, misspellings, gibberish, detached typography, or generic PPT and e-commerce layouts
  - crop, stretch, padding, mockup, contact sheet, grid, or one-size-fits-all adaptation for multiple ratios
```

## Style Intent

把主题中最重要的关系、矛盾或变化提炼为一个真实立体纸雕隐喻，以精确纸层、克制留白、柔和光影和图文一体的编辑排版完成高级概念海报。该 style 负责纸张材质、隐喻转译、空间关系、比例重构和视觉气质；平台确认、文章摘要、文件保存和生成工具调用由 `punk-cover` 负责。

## Use For

- 概念、方法论、知识、成长、连接、阻力、变化和关系主题
- 需要温暖、安静、克制、理性、治愈、神秘或高级气质的封面
- 小红书、微信公众号、X、展览海报、品牌视觉和多尺寸传播套图
- 能被提炼成一个清楚空间动作或视觉关系的长文章与短标题

## Avoid

- 必须同时展示多个同权重主体、复杂数据或大量正文的信息图任务
- 依赖写实人物相似度、金属机械结构或高饱和霓虹才能成立的主题
- 无法允许任何标题提炼、留白或视觉隐喻的纯信息排版任务
