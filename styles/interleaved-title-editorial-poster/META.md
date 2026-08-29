# 超大标题图文穿插

```yaml
id: interleaved-title-editorial-poster
name: 超大标题图文穿插
input_modes: [text]
subjects: [person, sculpture, product, object, architecture, animal, abstract, concept]
outputs: [cover, poster]
default_ratio: "5:2"
required_fields: [主题词或原文, 画幅比例, 语言, 用途]
optional_fields: [副标题, 补充背景, 情绪倾向, 不想出现的元素]
source: styles/interleaved-title-editorial-poster/STYLE.md
style_anchors:
  - one central high-recognition subject with a clean sculptural silhouette
  - one enormous short title integrated into the composition
  - explicit back-title, subject, and front-title layers with controlled mutual occlusion
  - bold geometric sans-serif typography with clean edges and preserved readability
  - restrained editorial details, generous negative space, and a theme-derived 2-4 color palette
cover_shape_adaptation:
  - derive a 2-8 character Chinese title or 1-4 word English title when the source is long-form
  - recompose title lines, subject placement, layering, and whitespace for each requested aspect ratio
  - keep no more than three information levels: main title, central subject, and minimal support text
  - place occlusion away from a person's eyes, nose, mouth, and other critical identifying features
must_preserve:
  - exactly one core subject and one clear focal point
  - readable accurate main title despite partial cropping and occlusion
  - visible typography-subject interleaving in both directions, not text pasted over an image
  - modern magazine, exhibition, or brand-campaign editorial finish
avoid_when_applying_to_cover:
  - multiple unrelated subjects or noun-by-noun illustration
  - opaque or translucent text clutter, random overlap, or unreadable letterforms
  - blocked facial features, malformed typography, misspelled Chinese, or decorative gibberish
  - PPT, e-commerce, feed-ad, cheap template, or complex technology-dashboard aesthetics
```

## Style Intent

以一个中央主体和一个超大短标题共同建立构图，通过后景字、主体和前景字的双向遮挡形成明确空间层次。适合需要强编辑感、杂志封面感、展览海报感和品牌主视觉冲击力的内容。该 style 负责单一主体、标题尺度、图文穿插、比例适配和克制编辑细节；平台适配、文章摘要和通用输出规则由 `punk-cover` 负责。

## Use For

- 中文或英文短标题主导的社交封面、横幅和竖版海报
- 人物、雕塑、产品、物件、建筑或抽象装置作为单一主视觉的内容
- 需要标题本身参与构图，而不是简单“图片上加字”的主题
- 适合 X、微信公众号、小红书、展览视觉和品牌 campaign

## Avoid

- 多主体叙事、信息密集型图表或需要展示大量正文的内容
- 标题无法缩短且必须逐字完整占据主视觉的场景
- 低对比、弱层级、随机遮挡或普通模板式图文叠加
