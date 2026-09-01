# 立体人物扁平景色纸艺

```yaml
id: surreal-pop-up-paper-landscape
name: 立体人物扁平景色纸艺
input_modes: [image]
subjects: [person, scene]
outputs: [before_after, portrait, editorial_artwork]
default_ratio: mode-specific
required_fields: [上传人物照片, 输出模式]
optional_fields: [画幅比例]
source: user-contributed prompt and reference image
modes:
  before-after:
    name: 前后对比图
    default_ratio: "3:2"
    reference: references/before-after.md
  final-artwork:
    name: 单张效果图
    default_ratio: "3:4"
    reference: references/final-artwork.md
style_anchors:
  - one photorealistic upright person rising from the original scene flattened onto paper
  - environment folded backward around the subject contact point by 75 to 85 degrees
  - non-person vertical height compressed to 10 to 20 percent
  - warm off-white fibrous art paper, broad negative space, and a short soft contact shadow
  - wide shallow oval or fan-shaped landscape with photographic detail and restrained paper-fiber edges
must_preserve:
  - recognizable identity, face, hair, expression, clothing, accessories, pose, gesture, body proportions, camera angle, lighting, and color
  - major scene elements and their original color relationships
  - a clear 90-degree spatial contrast between upright person and paper-parallel environment
avoid_when_applying_to_avatar:
  - redesigning, beautifying, cartoonizing, duplicating, or deforming the person
  - any upright car, building, tree, mountain, furniture, or other non-person element
  - ordinary background replacement, background blur, full-scene watercolor treatment, or a flat photo collage
  - long hard shadows, narrow pointed projections, cutout halos, text, borders, logos, or watermarks
```

## Style Intent

把一张人物环境照转化为超现实纸艺装置：人物保持真实、清晰、三维并垂直于纸面；照片中的其余世界从人物脚下或身体接触点向后翻倒，压缩成贴在纸面上的宽浅二维景色。作品具有摄影真实感、立体书结构和高级编辑插图气质。

## Use For

- 人物与汽车、建筑、道路、海面、山川、餐厅、树木、桌椅等环境同时出现的照片
- 希望保留真人身份与动作，同时制造“人物从扁平现实中站起”效果的图像
- 需要原图与效果并排展示，或只需要一张最终艺术效果图的任务

## Avoid

- 没有人物主体、人物被严重遮挡或无法确认主要人物的输入
- 需要重设计人物、改变服装动作、卡通化或插画化人物的任务
- 需要保留正常直立背景、复杂文字排版或多人物合成的任务
