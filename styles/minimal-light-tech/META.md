# 极简轻科技

```yaml
id: minimal-light-tech
name: 极简轻科技
input_modes: [text, image]
subjects: [technology, product, tutorial, tool, brand, concept, essay]
outputs: [cover, poster]
default_ratio: "5:2"
required_fields: [内容主题, 画面文字, 画幅比例, 渐变色系选择, 是否提供 logo]
optional_fields: [配色补充说明, 主视觉偏好, logo 使用说明, 参考图说明]
source: styles/minimal-light-tech/STYLE.md
style_anchors:
  - clean white, warm-white, or light gray background with large negative space
  - one single visual anchor only: lightly dimensionalized brand logo OR one abstract soft 3D glass/gradient form
  - soft refined gradients concentrated on the anchor, not filling the canvas
  - modern ultra-bold Chinese sans-serif title in black or near-black
  - quiet premium light-tech product cover feel without cyberpunk or dense UI
cover_shape_adaptation:
  - landscape ratios prefer left-title and right-anchor, or quiet asymmetric balance with generous breathing room
  - portrait ratios keep title in the upper or middle zone and the single anchor compact below or beside it
  - never print the aspect-ratio numbers into the image; ratio only controls composition
  - when 画面文字 is「无文字」, rely on the single visual anchor and leave typography out
must_preserve:
  - one visual center and one anchor only
  - large clean negative space on a light background
  - exact on-screen text when the user did not choose「无文字」
  - soft gradient or light dimensional treatment limited to the anchor
avoid_when_applying_to_cover:
  - cyberpunk neon, dense UI panels, dashboards, collage, or filling the frame
  - multiple anchors, multiple logos, icon grids, or competing decorations
  - heavy textures, loud marketing posters, people, product photography clutter, or hard metallic chrome
  - printing ratio labels, watermarks, or unrelated small supporting text blocks
```

## Style Intent

极简轻科技是一种以大面积纯白 / 暖白 / 浅灰留白为底、只用一个主视觉锚点的轻科技产品封面风格。锚点可以是轻微立体化的品牌 Logo，或一枚抽象的柔和 3D 玻璃 / 渐变形体；渐变只集中在锚点上，标题使用现代超粗黑体、黑色或近黑。该 style 只负责轻科技极简视觉语言、单一锚点、渐变色系和排版气质；平台适配、长文提炼和通用封面约束由 `punk-cover` 负责。

## Use For

- 科技产品、工具教程、品牌概念、轻科技主题和干净现代的文章 / 视频封面
- X 封面、公众号封面、产品发布头图、教程海报和品牌概念海报
- 需要纯白留白、单一渐变锚点、现代黑体标题、克制高级感的视觉

## Avoid

- 赛博朋克、霓虹、密集界面、信息图、拼贴或把画面填满的内容
- 需要人物故事、复杂场景叙事、多 Logo 生态图或强营销冲击的封面
- 需要重金属质感、硬科幻装甲、大量标签说明或多主视觉的任务
