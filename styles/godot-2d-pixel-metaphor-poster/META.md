# Godot 2D 像素隐喻海报

```yaml
id: godot-2d-pixel-metaphor-poster
name: Godot 2D 像素隐喻海报
input_modes: [text]
subjects: [concept, character, environment, scene, system, world]
outputs: [cover, poster]
default_ratio: "5:2"
required_fields: [主题原文, 图片比例, 用途]
optional_fields: [补充语境, 情绪倾向, 禁止元素]
source: styles/godot-2d-pixel-metaphor-poster/STYLE.md
style_anchors:
  - one abstract idea translated into one concrete level, one game mechanic, and one immediately legible visual metaphor
  - one main pixel character performing one clear action toward or against one symbolic goal or obstacle
  - handcrafted 16-bit or 32-bit pixel art with crisp edges, consistent sprite scale, coherent pixel grid, and tilemap world logic
  - indie-game promotional-poster finish with environmental storytelling, cinematic pixel lighting, strong focus, and deliberate negative space
  - complete original theme text integrated into the game world through pixel typography, architecture, terrain, light, or character interaction
cover_shape_adaptation:
  - wide formats should emphasize horizontal movement, complete world depth, and distance between character and target
  - vertical formats should emphasize ascent, descent, growth path, or a distant target along the vertical axis
  - square formats should compress the metaphor into one central symbol, loop, or compact level with strong thumbnail recognition
  - recompose title position, character scale, level space, movement path, and negative space for custom ratios instead of cropping
must_preserve:
  - exactly one core viewpoint, one main metaphor, one main character, one action, and one goal or obstacle
  - accurate and fully readable original theme text, with one to three keywords optionally emphasized
  - shared pixel resolution and grid logic across character, environment, text, lighting, particles, and shadows
  - game-world depth and level-design logic without looking like a screenshot or gameplay interface
avoid_when_applying_to_cover:
  - photorealism, 3D render, ordinary anime, vector illustration, pixel-filtered photography, or mixed-resolution assets
  - multiple protagonists, multiple stories, multiple metaphors, four-panel layouts, crowded text, or complex game UI
  - inventory bars, status panels, menus, random English, watermark, logo, fabricated game metadata, or misspelled Chinese
  - copied characters, maps, sprites, tiles, icons, logos, trademarks, or recognizable levels from existing games
  - blurry pixels, smoothing filters, inconsistent pixel scales, weak title hierarchy, or generic screenshot composition
```

## Style Intent

把一句主题提炼成一个可以被玩家体验的 Godot 2D 像素关卡，通过角色动作、环境关系、游戏机制和目标/阻碍表达单一核心观点。该 style 负责像素网格、关卡世界、机制隐喻、标题入景、色彩气质和比例重构；平台确认、文章摘要、文件保存和生成工具调用由 `punk-cover` 负责。

## Use For

- 成长、长期主义、方向选择、内耗、希望、专注力、信息洪流和人与系统关系
- AI、工具、知识、时代变化、规则冲突和抽象观点类内容
- 公众号、X、小红书、视频封面、独立游戏风宣传海报和文章题图
- 能被转译为一个角色动作、一套关卡机制和一个清楚目标或阻碍的主题

## Avoid

- 需要多个同权重人物、复杂剧情分镜、完整游戏 UI 或大量数据说明的信息图任务
- 纯头像、照片转像素、写实肖像或需要复刻具体游戏资产的请求
- 无法容纳主题原文、单一隐喻或清楚视觉焦点的密集排版任务
