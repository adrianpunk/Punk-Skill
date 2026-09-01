---
name: punk-avatar
description: Generate avatar images, surreal paper-art portraits, and reusable image prompts from the shared Punk style library for people, pets, objects, profile pictures, pet portraits, and keepsake cards. Use this skill to identify the subject from image or text, choose one avatar-capable style and any required style mode, compile the selected style atom into the avatar blueprint, save the final prompt, and generate the image when an image-generation tool is available.
---

# Punk Avatar

## Core Rule

`punk-avatar` is an avatar-shape workflow, not a style owner. Select exactly one reusable style from the repository-level `styles/` library, then compile that style atom into the avatar shape.

The final image prompt is not a loose concatenation of "avatar instructions + style instructions". It must be one integrated, avatar-specific prompt that applies the selected style to a profile image, portrait avatar, object avatar, pet avatar, or avatar-derived keepsake card.

Use three inputs:

1. `punk-avatar` task fields: subject type, source image or text description, intended use, likeness policy, avatar composition, aspect ratio, background simplification, crop safety, and universal output constraints.
2. The selected style's `META.md` metadata and `STYLE.md` reusable visual style atom.
3. `references/avatar-prompt-blueprint.md`, which defines the full avatar prompt shape.

The style file defines the reusable visual language. The avatar blueprint defines the output form. The final prompt must fuse them into one complete avatar-generation prompt.

## Resources

- Read `references/style-catalog.md` to list or choose avatar styles.
- Read `references/avatar-prompt-blueprint.md` before composing the final prompt.
- For the selected style, read both:
  - `../../styles/{style-id}/META.md`
  - `../../styles/{style-id}/STYLE.md`
- Expose only these seven styles in the `punk-avatar` menu:
  - `pixel-avatar`
  - `grotesque-soul-sketch`
  - `messy-crayon-pet-portrait`
  - `fashion-sketch-observation`
  - `polaroid-keepsake`
  - `minimal-paper-acrylic-block-illustration`
  - `surreal-pop-up-paper-landscape`
- `surreal-pop-up-paper-landscape` has two output modes. After reading its `META.md` and `STYLE.md`, read exactly one mode reference selected by the user:
  - `../../styles/surreal-pop-up-paper-landscape/references/before-after.md`
  - `../../styles/surreal-pop-up-paper-landscape/references/final-artwork.md`
- Do not expose cover/poster styles in the `punk-avatar` menu.
- Do not read `punk-cover` references or templates for avatar runs.

## Workflow

1. Analyze the source material:
   - If the user provides one or more images, treat image input as primary.
   - Identify the main subject type: `person`, `pet`, `object`, or `unclear`.
   - Extract only concise visual traits needed for an avatar: face/head shape, hair or fur, eyes, expression, posture, signature colors, clothing, accessories, object silhouette, and any must-preserve marks.
   - Use text as supplemental context: name, temperament, intended use, preferred background color, elements to preserve, and elements to avoid.
   - If there is no image and the user describes a fictional avatar, handle it as description-based generation. Do not promise likeness to a real photo.

2. Resolve aspect ratio:
   - Default ratio is always `1:1` inside `punk-avatar`.
   - If the user specifies `3:4`, `4:5`, `16:9`, or any custom ratio, keep the user's ratio exactly.
   - Do not use the selected style metadata's `default_ratio` as the avatar default.
   - For `polaroid-keepsake`, default to `1:1` in `punk-avatar`; only generate a vertical polaroid card when the user explicitly asks for a vertical ratio.
   - For `surreal-pop-up-paper-landscape`, use `3:2` for `before-after` mode and `3:4` for `final-artwork` mode when the user omits the ratio. Keep any user-specified ratio exactly.
   - Do not ask a ratio question when the user omits ratio.

3. Confirm style before generating any prompt:
   - If the user specifies one catalog style, use it.
   - If the user supplies a complete visual direction that matches a catalog style, including the `极简纸感丙烯色块插画` or `立体人物扁平景色纸艺` brief, treat that style as specified and use its style atom without asking the user to repeat the style.
   - If no style is specified, recommend 2-3 eligible styles based on the subject type and ask the user to choose one.
   - When style is missing, stop after asking. Do not fill a style file, save prompt files, or generate an image.
   - Only auto-select one style when the user explicitly says to decide everything automatically.
   - For `surreal-pop-up-paper-landscape`, also resolve the output mode. Map requests for `前后对比图`, `对比图`, `before/after`, or `comparison` to `before-after`; map `效果图`, `单张效果图`, `成品图`, `final artwork`, or `single image` to `final-artwork`.
   - If the user selects `surreal-pop-up-paper-landscape` but gives no mode, ask only which of the two modes to use and stop. Do not generate both unless the user explicitly requests both.

4. Recommendation rules:
   - Pet subject: recommend `凌乱蜡笔宠物肖像`, `拍立得纪念卡`, and `怪诞灵魂手绘`; include `像素头像` when a more icon-like avatar may fit.
   - Person subject: recommend `怪诞灵魂手绘`, `时尚速写观察页`, and `像素头像`.
   - Object subject or unclear subject: recommend `像素头像` first.
   - A photo or theme that needs a small symbolic subject, rough white paper, clear acrylic blocks, and large negative space: recommend `极简纸感丙烯色块插画`.
   - A person photo with a recognizable surrounding scene that should become a photorealistic upright figure emerging from a flattened paper landscape: recommend `立体人物扁平景色纸艺`.
   - Do not recommend `messy-crayon-pet-portrait` for people.
   - Do not recommend `fashion-sketch-observation` for pets or objects unless the user explicitly asks for that style.
   - Do not recommend `polaroid-keepsake` for people or objects.

5. Use this confirmation gate:
   - Missing style: ask for style choice and stop.
   - Missing ratio: silently use the default resolved in step 2.
   - Known style: continue without asking.
   - `surreal-pop-up-paper-landscape` with missing mode: ask for `前后对比图` or `单张效果图` and stop.
   - If both style and subject are known enough to proceed, compile the prompt.

6. Compile the final image prompt:
   - Use `references/avatar-prompt-blueprint.md` as the required structure for `prompts/avatar.md`.
   - Read exactly one selected style visual atom from `../../styles/{style-id}/STYLE.md`.
   - Read the selected style metadata from `../../styles/{style-id}/META.md`.
   - For `surreal-pop-up-paper-landscape`, read and compile exactly one selected mode reference. The mode reference controls whether the result is a side-by-side comparison or one standalone artwork; never blend the two output contracts.
   - Extract the selected style's non-negotiable visual anchors: subject treatment, composition, background behavior, line or texture system, color logic, typography or handwritten behavior, likeness constraints, and negative constraints.
   - Fuse the avatar task fields and style anchors into one full avatar prompt. The final prompt should read like a complete avatar-generation brief, not like two unrelated prompt fragments pasted together.
   - Include avatar-shape sections for role/task, input fields, source interpretation, subject identity, likeness policy, avatar composition, crop safety, background, style application, color/material/texture, optional text/name handling, negative constraints, and final standard.
   - Do not append the raw `STYLE.md` content as a standalone second section. Rewrite and adapt its style atoms into the avatar blueprint.
   - Do not combine multiple styles or add a second custom style section.
   - Replace or resolve all explicit placeholders from the selected style file.
   - For image-based inputs, preserve recognizable subject identity without creating a photorealistic copy unless the selected style requires realistic structure.
   - For text-only fictional avatars, say the image should follow the description and avoid claims such as "preserve photo likeness".
   - Do not bring cover-title hierarchy, article summaries, platform propagation rules, or social-cover composition into the avatar prompt.
   - Do not output analysis inside the final prompt.

7. Save files before image generation:
   - Create `punk-assets/punk-avatar/{slug}/prompts/avatar.md` with the complete filled prompt.
   - If image generation returns an explicit local file path, downloadable URL, or image bytes for the current run, save that artifact as `punk-assets/punk-avatar/{slug}/avatar.png`.
   - Do not infer the correct artifact by scanning broad generated-image directories, because those directories may contain unrelated images from other runs.
   - If the image-generation tool only returns an inline preview with no explicit retrievable artifact for the current run, do not create a fake `avatar.png`.

8. Generate an image by default after saving the prompt when a usable image-generation tool is available, such as `image_gen`. Treat inline preview generation as successful image generation, but treat local `avatar.png` saving as successful only when the tool explicitly exposes a current-run artifact. Skip image generation only when the user explicitly asks for prompt-only output or the current environment has no image-generation tool. If image generation is unavailable, return the prompt file path and the full prompt content.

## First Response Format

For input with no style, ask concisely:

```text
默认画幅：1:1。

请选择一个头像风格：
- `风格 A`：reason tied to the subject.
- `风格 B`：reason tied to the subject.
- `风格 C`：reason tied to the subject.

也可以回复 "auto" 让我自动选择。
```

Do not ask for ratio unless the user explicitly wants ratio options.

## Style Selection Heuristics

- Use `pixel-avatar` for people, pets, objects, symbolic avatars, icon-like profile pictures, and unclear subjects.
- Use `grotesque-soul-sketch` for people or pets that should feel expressive, funny, sketchy, and personality-driven.
- Use `messy-crayon-pet-portrait` only for pets and pet portrait avatars.
- Use `fashion-sketch-observation` only for people, especially fashion, travel, street-photo, film-still, or editorial personal portraits.
- Use `polaroid-keepsake` only for pets, especially memorial, collectible, named pet cards, and avatar-derived keepsake cards.
- Use `minimal-paper-acrylic-block-illustration` for people, pets, objects, scenes, or themes that need a simplified paper-texture illustration with vivid acrylic color blocks and a very small subject.
- Use `surreal-pop-up-paper-landscape` for image-based person portraits where the real figure must stay upright and photorealistic while the photographed environment folds down into a shallow paper-plane landscape.

## Avatar Prompt Blueprint

Use `references/avatar-prompt-blueprint.md` as the full prompt structure. The block below is retained only as the required task-field content that must be represented inside the integrated final prompt.

```text
# punk-avatar task instructions

Create one single avatar image. Aspect ratio: {ratio}.

Use the following derived subject fields only:
- Subject type: {subject_type}
- Generation mode: {image_based_or_description_based}
- Subject identity: {subject_identity}
- Recognizable traits: {recognizable_traits}
- Name or text to include: {name_or_text}
- Intended use: {use_case}
- Background preference: {background_preference}
- Mood: {mood}
- Preserve: {preserve}
- Avoid: {avoid}

For image-based inputs, preserve the subject's most recognizable traits while translating them into the selected style. Do not claim exact biometric identity or photorealistic duplication.

For description-based inputs, create a fictional avatar from the description. Do not write that it preserves photo likeness.

The avatar must work as a profile image: readable at small size, centered or deliberately framed, clear silhouette, no important facial features or subject marks cropped out, simplified background, and one final output.

Generate only one final image. Do not output explanations, alternatives, grids, contact sheets, or multi-option compositions.
```

## Output Discipline

- The final generated prompt must be one integrated avatar-specific prompt compiled from the avatar task fields, `references/avatar-prompt-blueprint.md`, and exactly one selected style atom.
- Do not paste the selected style `STYLE.md` as a standalone second section. Adapt its style atoms into the avatar blueprint.
- The final prompt must preserve the selected style's non-negotiable anchors from `META.md` and `STYLE.md`.
- Do not copy unrelated user text into the final prompt; use concise derived subject fields.
- Do not include style-selection rationale inside the prompt file.
- Do not combine multiple styles.
- Do not add cover/poster title hierarchy, article summary, or platform cover rules.
