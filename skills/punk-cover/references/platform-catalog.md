# Punk Cover Platform Catalog

This catalog defines the platform choices shown by `punk-cover` and separates a
platform's requested publishing ratio from the ratio that the current image
generation tool can actually produce.

## Supported generation ratios

The image-generation tool currently accepts only:

`1:1`, `2:3`, `3:2`, `4:3`, `3:4`, `9:16`, `16:9`, and `21:9`.

These are generation constraints, not claims about any platform's recommended
cover or thumbnail dimensions.

## Platform choices

| 中文模式平台 / 场景 | English mode platform / use case | Requested ratio | Generation ratio | 中文说明 | English note |
| --- | --- | ---: | ---: | --- | --- |
| 小红书 | Xiaohongshu | `3:4` | `3:4` | 当前生图工具支持此比例。 | Exact supported ratio. |
| 微信公众号 | WeChat public account | `2.35:1` | `21:9` | 只能生成最接近的比例。 | Only the closest supported ratio can be generated. |
| X | X | `5:2` | `21:9` | 只能生成最接近的比例。 | Only the closest supported ratio can be generated. |
| Instagram 方形贴文 | Instagram square post | `1:1` | `1:1` | 当前生图工具支持此比例。 | Exact supported ratio. |
| Instagram 竖版贴文 | Instagram portrait post | `4:5` | `3:4` | 只能生成最接近的比例。 | Only the closest supported ratio can be generated. |
| Instagram 横版贴文 | Instagram landscape post | `1.91:1` | `16:9` | 只能生成最接近的比例。 | Only the closest supported ratio can be generated. |
| Instagram 快拍 / Reels | Instagram Stories / Reels | `9:16` | `9:16` | 当前生图工具支持此比例。 | Exact supported ratio. |
| Facebook 贴文 / 链接预览 | Facebook post / link preview | `1.91:1` | `16:9` | 只能生成最接近的比例。 | Only the closest supported ratio can be generated. |
| LinkedIn 贴文 / 链接预览 | LinkedIn post / link preview | `1.91:1` | `16:9` | 只能生成最接近的比例。 | Only the closest supported ratio can be generated. |
| YouTube 缩略图 / 视频封面 | YouTube thumbnail / video cover | `16:9` | `16:9` | 当前生图工具支持此比例。 | Exact supported ratio. |
| TikTok 视频封面 | TikTok video cover | `9:16` | `9:16` | 当前生图工具支持此比例。 | Exact supported ratio. |
| Pinterest Pin | Pinterest Pin | `2:3` | `2:3` | 当前生图工具支持此比例。 | Exact supported ratio. |
| Snapchat Spotlight / 快拍 | Snapchat Spotlight / Story | `9:16` | `9:16` | 当前生图工具支持此比例。 | Exact supported ratio. |
| Reddit 贴文 | Reddit post | `1:1` | `1:1` | 当前生图工具支持此比例。 | Exact supported ratio. |
| Threads 贴文 | Threads post | `1:1` | `1:1` | 当前生图工具支持此比例。 | Exact supported ratio. |
| Bluesky 贴文 | Bluesky post | `1:1` | `1:1` | 当前生图工具支持此比例。 | Exact supported ratio. |
| Medium 文章封面 | Medium article cover | `16:9` | `16:9` | 当前生图工具支持此比例。 | Exact supported ratio. |

## Ratio resolution rules

1. Preserve the user's requested platform and requested ratio in the derived
   fields so the output remains transparent.
2. If the requested ratio is supported, use it directly.
3. If it is not supported, choose the numerically closest supported ratio
   automatically. Do not stop to ask the user to choose a second ratio.
4. Before the prompt or image is generated, explicitly state in the active
   language mode: “只能生成最接近的比例：{generation ratio}（请求比例：{requested
   ratio}）。” or “Only the closest supported ratio can be generated: {generation
   ratio} (requested: {requested ratio}).”
5. Use the resolved generation ratio everywhere the image tool needs an aspect
   ratio. Keep the requested ratio only as an explanatory field.
6. Do not describe the resolved ratio as meeting a platform's cover-size
   standard. It is simply the closest ratio available to the image tool.
7. For a custom unsupported ratio, apply the same nearest-ratio rule instead of
   silently substituting a ratio or presenting an unsupported tool value.
