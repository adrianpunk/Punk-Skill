# 黑色复古现代主义封面

```yaml
id: black-midcentury-modernist-cover
name: 黑色复古现代主义封面
input_modes: [text]
subjects: [concept, person, product, architecture, animal, technology, service_scene, object]
outputs: [cover, poster]
default_ratio: "5:2"
required_fields: [主题词, 画幅比例, 语言, 用途]
optional_fields: [副标题, 辅助短句, 核心主体, 点缀色, 补充背景, 情绪倾向, 不想出现的元素]
source: styles/black-midcentury-modernist-cover/STYLE.md
style_anchors:
  - black-dominant mid-century modern editorial illustration
  - retro book cover, vintage magazine, noir, and geometric graphic design language
  - strict three-color system with black, warm white, and one vivid accent color
  - one simplified core subject, one visual center, and one main title group
  - flat geometric shapes, silhouette-like light and shadow, restrained screen-print grain
cover_shape_adaptation:
  - adapt layout to the selected aspect ratio, including image-left text-right, text-left image-right, centered subject, upper-lower split, or single-subject poster composition
  - keep one core subject and one accent-color focus, with generous black negative space where useful
  - horizontal covers may use strong side-by-side subject and typography balance
  - vertical covers should prioritize a compact poster-like hierarchy with the title and subject clearly separated
must_preserve:
  - black as the dominant color across background or subject
  - "no more than three colors: black, white or warm ivory, and one vivid accent"
  - mid-century modern retro editorial illustration character
  - strong, readable title and concise supporting text
  - full-bleed edges with no card frame, border, rounded white margin, or outer pale band
avoid_when_applying_to_cover:
  - neon cyberpunk, modern blue-purple technology gradients, glass effects, metallic 3D, or complex lighting
  - multicolor palettes, multiple bright accents, complex gradients, or high-saturation colorful poster treatment
  - photorealism, anime style, 3D rendering, dense mechanical detail, busy icon systems, or internet-ad clutter
  - information overload, many labels, parameter panels, serial numbers, or explanatory text
```

## Style Intent

黑色复古现代主义封面是一种黑色主导、三色克制、图形化强的复古编辑插画风格。它融合 20 世纪中期现代主义书封、复古杂志封面、黑色电影气质和几何平面设计语言，把主题提炼成一个清晰主体、一个色彩重点和一组醒目标题。该 style 只负责视觉语言、配色、主体概括、图文秩序和边缘约束；平台适配、长文提炼和通用封面结构由 `punk-cover` 负责。

## Use For

- 观点文章、服务介绍、产品主题、人物专题、城市建筑、科技设备和抽象概念封面
- 需要复古高级、理性克制、黑色主导、标题醒目和强封面感的公众号、X、视频封面和海报
- 适合希望主题清楚但不落入普通互联网宣传海报的内容

## Avoid

- 需要照片写实、3D 产品渲染、赛博科技感、复杂信息图或多主体叙事的封面
- 需要大面积彩色渐变、华丽光效、玻璃质感、金属质感或高饱和多彩视觉的任务
- 依赖大量小字、标签、编号和说明文字才能成立的内容
