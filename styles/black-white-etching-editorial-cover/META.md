# 黑白复古蚀刻版画封面

```yaml
id: black-white-etching-editorial-cover
name: 黑白复古蚀刻版画封面
input_modes: [text, image]
subjects: [concept, typography, object, scene, mechanism, surreal_editorial]
outputs: [cover, poster]
default_ratio: "5:2"
required_fields: [标题或主题, 核心意思]
optional_fields: [画幅比例, 视觉方向, 副标题, 输出尺寸, 输出模式, 用途, 语言, 文字模式, 情绪倾向, 必须出现, 禁止出现]
source: styles/black-white-etching-editorial-cover/STYLE.md
style_anchors:
  - strict black, white, and line-made gray values with strong tonal contrast
  - 19th-century copperplate engraving, etching, wood engraving, and antique scientific-illustration marks
  - fine parallel hatching, cross-hatching, stippling, engraved contours, and visible handmade print texture
  - one dominant conceptual or surreal editorial metaphor rather than a literal keyword collage
  - clear silhouette and visual center from a distance, with dense craft detail revealed up close
  - intentionally uneven information density: refined focal detail, simplified support areas, and controlled pure-black fields
cover_shape_adaptation:
  - let the ratio determine the scene, perspective, subject scale, and reading path; never crop or stretch a finished composition
  - use wide ratios for environmental narrative and horizontal motion, portrait ratios for vertical scale and descent/ascent, and square ratios for a concentrated emblematic encounter
  - if text is requested, render the complete title as restrained engraved editorial type integrated into the print; if the user explicitly requests a pure-image cover or `文字模式: 无文字`, use the title only to guide the metaphor and do not render text
  - preserve one strong visual memory point while allowing the metaphor, viewpoint, scale, material, quantity, and physical logic to change from cover to cover
must_preserve:
  - monochrome print language with no color accents, neon, glow, or smooth digital gradients
  - one legible core silhouette and one primary metaphor with a clear spatial relationship
  - authentic engraved marks: hatching, cross-hatching, stippling, etched contours, and tactile paper/ink irregularity
  - high contrast, deliberate negative space, and non-uniform detail density
  - a restrained, mysterious, rational, philosophical, and surreal editorial temperament
avoid_when_applying_to_cover:
  - obvious modern 3D rendering, plastic surfaces, glossy CGI, cheap cyberpunk, or generic AI concept-art polish
  - keyword-object piles, multiple unrelated symbols, stock illustration composition, or decorative filler
  - flat black-and-white vector art, comic-book inking, smooth airbrush shading, watercolor, or colored printmaking
  - unreadable title lettering, fabricated editorial filler, excessive small text, logos, watermarks, grids, contact sheets, or e-commerce layout
```

## Style Intent

把标题、主题和核心意思转译成一张具有强烈概念感的纯黑白封面。画面借用十九世纪铜版画、蚀刻版画、木口木刻、古典科学插图和超现实编辑插画的视觉语法：灰阶不依赖数字渐变，而由排线、交叉排线、点描和雕刻线条生成。该 style 负责版画媒介、概念隐喻、黑白层次、构图密度和气质；平台适配、标题提炼、文件保存与生成工具调用由 `punk-cover` 负责。

## Use For

- 哲学、批判性观点、未来议题、机制解释、社会观察和具有思考感的主题
- 需要一眼形成视觉悬念、细看发现叙事关系的编辑封面、书封和展览海报
- 用户已指定黑白、复古蚀刻、铜版画、木刻、古典科学插图或超现实版画方向的封面
- 需要把抽象矛盾转化成一个场景、动作、尺度关系、空间结构或物理隐喻的内容

## Avoid

- 依赖彩色品牌识别、摄影写实、产品界面或复杂信息图才能成立的任务
- 必须同时展示多个同等重要主体、步骤或数据关系的内容
- 需要霓虹、发光、光滑 3D、赛博朋克、卡通或鲜艳商业广告质感的内容

## Visual Translation

- 先理解主题真正要表达的观点、矛盾、关系或问题，再选择一个能承载它的画面，而不是把名词逐个画成物件。
- 优先使用一个强核心概念。人物、环境、建筑、机械、生物、自然、抽象结构或超现实空间都可以成为主体，但必须服务于同一条视觉叙事。
- 可以改变现实中的尺度、数量、空间、方向、功能、材质、位置和因果逻辑，让熟悉的事物产生陌生感；只要视觉关系仍然能回扣核心意思。
- 避免机械套用机器人、芯片、大脑、书本等惯用符号。是否使用某个元素由具体内容决定。

## Engraved Print Language

- 画面固定为纯黑、纯白和由黑白线条形成的灰阶。不要出现任何彩色、棕褐色、蓝色或局部染色。
- 使用细密平行排线表现平面和方向，用交叉排线建立深色体积，用点描处理雾、皮肤、石材、纸张和远景，用粗细变化的雕刻线勾勒结构与轮廓。
- 线条要有铜版雕刻和手工印刷留下的微小不均匀：局部断裂、墨量变化、纸面颗粒、轻微套印误差都可以存在，但不能变成脏乱噪点。
- 明暗应有清晰的黑白对照。允许大面积纯黑作为背景、洞口、阴影或未知区域，也允许主体附近出现极高密度的精细版画细节。
- 材质通过线条方向、密度、间距、断续和刻痕来区分，不使用塑料高光、平滑渐变或照片滤镜。

## Composition and Density

- 先建立远看可识别的整体轮廓、视觉中心和主次关系，再把近看细节集中到主体、动作、关键结构或隐喻发生的位置。
- 根据目标比例重新设计空间：横向画幅适合展开环境叙事、水平运动和左右关系；纵向画幅适合巨大主体、深井、上升、坠落和垂直尺度；方形画幅适合集中冲突、局部特写和象征性构图。
- 让不同区域拥有不同信息密度。主体和关键区域精细刻画，次要区域适当简化、淡出或留黑，不要把每个角落平均填满。
- 可以使用中心、偏心、对称、非对称、俯视、仰视、平视、强透视、近景或远景，但必须保持一个明确的视觉主轴。
- 不要为了“丰富”堆放第二套符号系统。辅助元素只有在帮助理解空间、动作或主题关系时才出现。

## Title and Pure-Image Mode

- 标题、主题和核心意思先作为创作输入，帮助确定画面叙事和视觉隐喻。
- 只有在用户要求文字封面、提供文字模式或 `punk-cover` 的平台任务需要标题时，才把文字纳入画面；文字应像版画中的编辑标题、图注或刻印标识，和主体共享同一套黑白纸墨质感。
- 当用户明确要求“纯图封面”或“无文字”，禁止加入标题、解释句、标签、品牌、页码或伪造的小字；画面只用视觉关系表达主题。
- 文字模式未明确时，遵循 `punk-cover` 的通用标题可读性要求，不让蚀刻纹理破坏标题识别，不用大段小字填充空白。

## Atmosphere and Final Standard

整体保持克制、神秘、深邃、理性、超现实和具有思考感，可根据主题进一步偏向宏大、孤独、压迫、未知、荒诞、诗意、冷静、庄严或探索感。最终画面应介于编辑插画、哲学书籍插图、复古科学版画和超现实艺术之间：远看轮廓清晰、黑白关系有力；近看排线、点描、刻痕和纸墨纹理丰富；画面干净有秩序，概念明确但不把答案全部说尽。

不要输出分析、解释、备选方案、网格、拼图、联系表或多张成图。每个目标比例只生成一张独立最终封面。
