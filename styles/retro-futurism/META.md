# 复古未来主义

```yaml
id: retro-futurism
name: 复古未来主义
input_modes: [text]
subjects: [technology, infrastructure, systems, future, science, city, work, media, editorial_topic]
outputs: [cover, poster, editorial_page]
default_ratio: "21:9"
required_fields: [主题或主标题, 画幅比例]
optional_fields: [副标题, 视觉叙事, 时代设定, 系统隐喻, 人物角色, 语言, 用途, 色彩偏好, 补充背景, 不想出现的元素]
source: styles/retro-futurism/STYLE.md
style_anchors:
  - mid-century imagined future expressed through monumental analog infrastructure, world-fair modernism, industrial architecture, transit systems, tubes, conveyors, and orbital or civic megastructures
  - one coherent flow, sorting system, machine process, or public infrastructure used as the visual metaphor rather than a collection of futuristic objects
  - small but legible human figures acting as workers, editors, engineers, clerks, travelers, or witnesses inside the system, providing scale and narrative tension
  - physical paper, folders, tickets, diagrams, punched cards, labels, and printed forms integrated into the machinery as material evidence of information flow
  - aged editorial print treatment with parchment, rust red, ochre, charcoal, petrol teal, faded blue, halftone, paper fibers, ink wear, and restrained registration drift
  - cinematic wide perspective with a strong central axis, radial or converging structural lines, and layered foreground, middle ground, and background depth
cover_shape_adaptation:
  - wide landscape covers favor a monumental central or slightly off-center system with clear title breathing room in the upper band, side band, or negative-space corridor
  - 16:9 covers retain the central-axis infrastructure while reserving a readable title zone and a human-scale figure or action as the narrative anchor
  - portrait covers turn the system into a vertical shaft, tower, archive, launch column, or stacked transit section; preserve the same analog future language without simply cropping the panorama
  - square covers use a strong radial hub or central machine chamber with asymmetrical paper and architectural layers around it
  - title typography behaves like period signage, printed editorial type, architectural lettering, or a physical label attached to the system, never like a floating modern interface
must_preserve:
  - one imagined future system, one primary flow or process, one central metaphor, and one readable human-scale action
  - physical cause-and-effect between tubes, belts, rails, chambers, documents, vehicles, or other system components
  - a believable mid-century material world: painted metal, concrete, glass, paper, enamel, rivets, dust, and imperfect print surfaces
  - a restrained period palette with the visual hierarchy led by the title and the system's central movement
  - complete, accurate, readable title text with only a small amount of supporting copy
  - visible scale contrast between monumental infrastructure and small human figures
avoid_when_applying_to_cover:
  - modern cyberpunk, neon glow, blue-purple sci-fi gradients, holographic HUDs, floating UI panels, code rain, glowing circuit boards, or generic AI imagery
  - clean contemporary 3D renders, photorealistic concept art, glossy product visualization, anime, game key art, or a sterile sci-fi spaceship interior
  - a random collage of rockets, robots, planets, screens, and gadgets without one coherent system or physical flow
  - oversized heroic character portraits, centered headshots, empty futuristic city skylines, or humans posed without an action
  - excessive microtext, fake labels, unreadable pseudo-writing, logos, watermarks, modern brand UI, or promotional feature lists
  - flat single-layer composition, equal-weight visual centers, arbitrary decorative machinery, or a hard rectangular poster frame
```

## Style Intent

把一个今天或未来才会发生的主题，交给一位 1930s–1960s 的工业设计师、世界博览会建筑师和科幻杂志美术编辑来想象。未来不是霓虹灯和悬浮 UI，而是一套宏大、可见、可触摸、略显过载的模拟基础设施：输送管道、分拣轨道、纸质档案、机械舱室、环形大厅、轨道交通、公共服务机器或太空时代的市民建筑。人物很小，但动作必须让人理解系统正在如何工作。

该 style 只负责复古未来主义的模拟基础设施、系统隐喻、人物尺度、复古印刷质感和编辑构图；平台适配、长文提炼、语言模式、文件保存与生图工具调用由 `punk-cover` 负责。

## Use For

- AI、自动化、信息过载、知识流动、组织系统、媒体、档案、工作方式和技术改变社会的主题
- 需要把抽象议题转化为“一个巨型系统正在处理某种东西”的文章、X 头图、微信公众号封面、视频封面和海报
- 未来城市、公共基础设施、科学传播、太空时代想象、工业流程和档案叙事

## Avoid

- 只需要极简文字、纯几何、纯摄影、现代 SaaS 产品界面或直接赛博朋克气质的任务
- 必须依赖多个互不相关的图标、功能卡片、人物肖像或产品截图才能成立的主题
- 无法收束为一个系统、一个流动过程、一个人类动作和一个核心隐喻的内容
