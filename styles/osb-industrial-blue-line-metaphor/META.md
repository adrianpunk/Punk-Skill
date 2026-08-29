# OSB 工业蓝线条隐喻

```yaml
id: osb-industrial-blue-line-metaphor
name: OSB 工业蓝线条隐喻
input_modes: [text]
subjects: [concept, relationship, action, object, typography, line_art]
outputs: [cover, poster]
default_ratio: "5:2"
required_fields: [主题, 主标题, 画幅比例, 用途]
optional_fields: [副标题, 禁止元素]
source: styles/osb-industrial-blue-line-metaphor/STYLE.md
style_anchors:
  - full-bleed front-facing authentic warm honey OSB board with irregular compressed wood strands and optional tiny black corner screws
  - one exact industrial blue selected from #087FBE, #007FC4, or #006FC0 and reused consistently for all text, lines, and graphics
  - heavy geometric sans-serif title fixed in the upper-left as matte acrylic or thin metal signage with minimal contact shadow
  - one simplified continuous-line metaphor in the lower or lower-right area using no more than three core graphic elements
  - at least 55 percent visible board negative space and no more than 30 percent line-art area
cover_shape_adaptation:
  - preserve the upper-left title and lower-right metaphor balance across every ratio while recomposing scale, line path, and whitespace
  - landscape formats should use a long horizontal or diagonal visual path across generous board space
  - square formats should shorten the path while keeping clear corner-to-corner balance and one focal relationship
  - vertical formats should redirect the line downward toward the lower-right without crowding the title or reducing negative space
must_preserve:
  - authentic OSB strand-board material rather than generic wood, plywood, cork, paperboard, or smooth furniture
  - one unified industrial blue and one coherent line language across title and metaphor
  - exact readable user-provided text only, with no fabricated labels, numbers, English, dates, brands, logos, or watermarks
  - one core concept, no more than three core graphic elements, line-art area at or below 30 percent, and negative space at or above 55 percent
avoid_when_applying_to_cover:
  - room, wall, desk, people, environmental context, realistic scene, cartoon stickers, photos, screenshots, UI, flowcharts, or infographics
  - real or colored logos, traced trademarks, stock icons, multiple icon sets, dense small symbols, or several competing metaphors
  - neon, glow, gradient, liquid text, mirrored metal, strong 3D extrusion, colored lighting, hard shadows, or decorative clutter
  - inconsistent blue shades, extra text, random English, fabricated metadata, mechanical cropping, stretching, or padding
```

## Style Intent

以真实 OSB 刨花板的天然粗粝纹理承载一组高度理性的工业蓝标识字与连续线隐喻，通过左上标题、右下图形和大面积木板留白表达一个核心关系、动作或结果。该 style 负责固定材质、颜色、字体物性、线稿语言、构图锚点和留白比例；平台确认、文章摘要、文件保存和生成工具调用由 `punk-cover` 负责。

## Use For

- 职场、组织、效率、关系、工具、方法、连接、阻力、流程变化和抽象观点
- 文章封面、X 或社交媒体封面、视频封面、建筑或创意工作室风海报
- 能压缩成一条路径、一个连接关系或一个结构变化的主题
- 需要粗粝真实材质与现代工业导视秩序形成反差的内容

## Avoid

- 依赖人物故事、产品摄影、复杂场景、数据图表或大量正文才能成立的主题
- 需要真实品牌 Logo、软件截图、彩色图标或多步骤流程图的内容
- 无法保留大面积留白、左上标题或单一蓝色线稿隐喻的密集排版任务
