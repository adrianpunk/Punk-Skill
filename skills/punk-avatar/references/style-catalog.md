# Punk Avatar Style Catalog

Use these user-visible style names. This catalog references reusable style atoms in the repository-level `styles/` directory. `punk-avatar` may list only the seven styles below.

Do not copy prompt bodies into this catalog. Read the selected style's `META.md` and `STYLE.md` after the user chooses a style.

Styles default to `1:1` inside `punk-avatar`, regardless of the `default_ratio` in style metadata, except `surreal-pop-up-paper-landscape`: its `before-after` mode defaults to `3:2` and its `final-artwork` mode defaults to `3:4`. Always keep the user's custom ratio when explicitly provided.

| Style | Style ID | Subject | Metadata | Style | Best For |
| --- | --- | --- | --- | --- | --- |
| 像素头像 | `pixel-avatar` | person, pet, object | `styles/pixel-avatar/META.md` | `styles/pixel-avatar/STYLE.md` | Standard profile avatars, icon-like portraits, symbolic avatars, objects, and unclear subjects. |
| 怪诞灵魂手绘 | `grotesque-soul-sketch` | person, pet | `styles/grotesque-soul-sketch/META.md` | `styles/grotesque-soul-sketch/STYLE.md` | Funny, expressive, sketchy, personality-driven people or pet avatars. |
| 凌乱蜡笔宠物肖像 | `messy-crayon-pet-portrait` | pet | `styles/messy-crayon-pet-portrait/META.md` | `styles/messy-crayon-pet-portrait/STYLE.md` | Pet avatars, named pet portraits, light crayon and colored-pencil pet drawings. |
| 时尚速写观察页 | `fashion-sketch-observation` | person | `styles/fashion-sketch-observation/META.md` | `styles/fashion-sketch-observation/STYLE.md` | Human profile portraits with fashion sketch, travel observation, street-photo, or film-still energy. |
| 拍立得纪念卡 | `polaroid-keepsake` | pet | `styles/polaroid-keepsake/META.md` | `styles/polaroid-keepsake/STYLE.md` | Pet avatar-derived keepsake cards, named pet watercolor polaroid portraits, collectible pet images. |
| 极简纸感丙烯色块插画 | `minimal-paper-acrylic-block-illustration` | person, pet, object, scene, concept | `styles/minimal-paper-acrylic-block-illustration/META.md` | `styles/minimal-paper-acrylic-block-illustration/STYLE.md` | Small symbolic subjects on rough white paper with thin hand-drawn lines, vivid acrylic blocks, and large negative space. |
| 立体人物扁平景色纸艺 | `surreal-pop-up-paper-landscape` | person, scene | `styles/surreal-pop-up-paper-landscape/META.md` | `styles/surreal-pop-up-paper-landscape/STYLE.md` | Photorealistic people rising from a flattened paper-plane version of the original environment, as either a before/after comparison or one final artwork. |

## Style-Specific Modes

`立体人物扁平景色纸艺` requires one output mode:

- `before-after` / `前后对比图`: preserve the source photo as the left panel and place the transformed paper artwork on the right. Read `styles/surreal-pop-up-paper-landscape/references/before-after.md`.
- `final-artwork` / `单张效果图`: output only the transformed paper artwork. Read `styles/surreal-pop-up-paper-landscape/references/final-artwork.md`.

If the style is selected but the mode is missing, ask the user to choose one. Never generate both by default.

## Recommendation Rules

- Pet subject: recommend `凌乱蜡笔宠物肖像`, `拍立得纪念卡`, `怪诞灵魂手绘`, and optionally `像素头像`.
- Person subject: recommend `怪诞灵魂手绘`, `时尚速写观察页`, and `像素头像`.
- Object subject or unclear subject: recommend `像素头像` first.
- For a photo or theme that needs small subject scale, paper texture, clear color blocks, and quiet whitespace, recommend `极简纸感丙烯色块插画`.
- For a person photo whose real subject should emerge from a flattened version of the original scene, recommend `立体人物扁平景色纸艺`.
- Do not recommend pet-only styles for people or objects.
- Do not recommend cover/poster styles here.
