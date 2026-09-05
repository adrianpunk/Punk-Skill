# 纸面击凸压凹封面

```yaml
id: paper-emboss-deboss-cover
name: 纸面击凸压凹封面
input_modes: [text]
subjects: [concept, typography, object, scene]
outputs: [cover, poster]
default_ratio: "5:2"
required_fields: [主题或主标题]
optional_fields: [副标题, 画幅比例, 输出尺寸, 输出模式, 用途, 语言, 文字模式, 情感倾向, 色彩倾向, 补充语境, 必须出现, 禁止出现]
source: styles/paper-emboss-deboss-cover/STYLE.md
style_anchors:
  - authentic cotton or art-paper surface with visible fiber, tooth, and studio side-lighting
  - letterpress-like emboss and deboss as the only physical relief, not cut-paper layers or plastic 3D type
  - one restrained visual metaphor expressed as a single paper-relief graphic
  - editorial typography that participates in composition through split lines, offset, edge placement, mixed orientation, or embedding into the graphic
  - 1-2 main colors plus optional micro accent, with large negative space as a compositional actor
cover_shape_adaptation:
  - derive one high-impact visual title when the source title is long, while preserving the complete title as secondary microtype
  - randomly recombine typeface family, type hierarchy, title placement, composition logic, metaphor, palette, and emboss/deboss assignment for each new cover
  - recompose title scale, graphic placement, whitespace, reading path, and relief direction for every target ratio
  - for a requested multi-size suite, keep metaphor, paper material, and palette identity consistent, but invent a new editorial layout for each ratio instead of cropping
must_preserve:
  - real paper relief with crisp impression edges, natural paper thickness, and soft side-light shadows
  - exactly one main graphic metaphor and a clear three-level type hierarchy
  - text-image inseparability: title, graphic, and whitespace must form one editorial sentence
  - quiet independent-magazine / art-book-cover temperament rather than a generic poster template
avoid_when_applying_to_cover:
  - plastic 3D modeling, metal engraving, foil stamping as the main look, neon, glossy CGI, or exaggerated extrusion
  - layered paper-cut diorama, collage, illustration clutter, or multiple competing subjects
  - always-left or always-centered title templates, PPT covers, e-commerce ads, and fabricated editorial filler
  - misspellings, unreadable titles, dense gradients, or more than two dominant colors plus one accent
```

## Style Intent

把主题提炼成一个克制的纸面隐喻，再用真实纸张质感、击凸与压凹工艺、灵活编辑排版和大量留白做成艺术画册封面或独立杂志封面。该 style 负责纸张工艺、文字构图、隐喻图形、随机版式实验和视觉气质；平台确认、文章摘要、文件保存和生成工具调用由 `punk-cover` 负责。

## Use For

- 设计、艺术、方法论、品牌、写作、哲学、关系和抽象概念主题
- 需要安静、现代、克制、聪明、高级气质的封面或海报
- 小红书、微信公众号、X、书封、展览海报和设计画册视觉
- 标题本身可以成为构图，而不是贴在画面上的说明文字

## Avoid

- 必须同时展示多个同权重主体、复杂数据或大量正文的信息图任务
- 依赖写实人物、产品摄影、金属机械或高饱和霓虹才能成立的主题
- 需要儿童插画、剪纸层叠、拼贴、赛博朋克或夸张立体字的任务
