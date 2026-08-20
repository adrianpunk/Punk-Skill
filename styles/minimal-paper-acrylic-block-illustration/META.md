# 极简纸感丙烯色块插画

```yaml
id: minimal-paper-acrylic-block-illustration
name: 极简纸感丙烯色块插画
input_modes: [image, text]
subjects: [person, pet, object, scene, concept]
outputs: [avatar, portrait, editorial_page]
default_ratio: "1:1"
required_fields: [照片或主题]
optional_fields: [画幅比例, 名称或文字, 用途, 情绪倾向, 保留特征, 不想出现的元素]
source: styles/minimal-paper-acrylic-block-illustration/STYLE.md
style_anchors:
  - rough white paper with visible fibers and a quiet editorial field
  - highly simplified subject silhouette occupying roughly 10-20 percent of the canvas
  - thin, light, slightly unstable hand-drawn lines used only for structural hints
  - two to four clear acrylic paint color blocks with hand-painted uneven edges
  - large negative space, restrained childlike poetry, and symbolic scene extraction
subject_composition:
  - keep one primary subject or one symbolic scene and remove nonessential details
  - preserve the most recognizable pose, action, outline, structure, or visual mark
  - for profile-avatar use, keep the small subject readable at thumbnail size without turning it into a full-frame close-up
background_behavior:
  - use rough white paper as the default background
  - suggest the original environment with at most a few lines or one small color field when semantically necessary
color_material_texture_rules:
  - use no more than four main colors, selected from vivid red, yellow, blue, green, or a restrained subset
  - allow a small amount of black or dark gray for structural lines
  - visible paper grain, acrylic flat-paint coverage, slight pigment unevenness, and handmade edges
must_preserve:
  - one memorable visual moment rather than a miniature realistic copy
  - small subject, generous white space, clear color blocks, and strong recognition
  - paper texture and hand-made imperfection
avoid_when_applying_to_avatar:
  - colored-pencil, crayon, watercolor wash, pure line art, heavy oil paint, smooth digital illustration, 3D, or commercial cartoon gloss
  - crowded background, excessive perspective, more than four main colors, tiny faint color accents, or over-detailed realism
  - decorative elements that do not support the subject, repeated generic AI polish, or a fixed recurring composition
```

## Style Intent

把照片或主题提炼成一张极简纸感手绘封面插画。画面像画在略粗糙的白纸上：用细而轻的手绘线条提示结构，用少量但明确的丙烯色块让主体成立。默认主体只占画面约 10%–20%，大面积留白承担安静、克制、童趣、轻松和诗意。该 style 只负责主体提炼、纸张媒介、线条、丙烯色块和留白；头像流程、比例、裁切安全和输出规则由 `punk-avatar` 负责。

## Use For

- 人物、宠物、物品、建筑或具有明确视觉符号的主题照片
- 需要把一个场景提炼成小型编辑插画、头像衍生图或纸感视觉卡片的内容
- 需要少细节、强识别、明显色块和大量留白的轻量视觉表达

## Avoid

- 需要写实相似度、完整场景重建、复杂信息图或满版海报的任务
- 依赖大量文字、多个主体或丰富背景才能说明的主题
- 无法归纳为一个清晰轮廓、动作、结构或视觉记忆点的素材
