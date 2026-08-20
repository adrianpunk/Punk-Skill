---
name: punk-cover
description: Generate cover images and reusable image prompts from the shared Punk style library for articles, Xiaohongshu notes, WeChat public account posts, X posts, topic drafts, and requests for covers, social cover images, poster prompts, style-template-based image prompts, or image generation from long-form text. Use this skill to analyze source content, confirm platform/aspect ratio and visual style, save the final prompt, and generate the image when an image-generation tool is available.
---

# Punk Cover

## Core Rule

`punk-cover` is a cover-generation workflow, not a style owner. Select exactly one reusable style from the repository-level `styles/` library, then compile that style atom into the cover shape.

The final image prompt is not a loose concatenation of "cover instructions + style instructions". It must be one integrated, cover-specific prompt that applies the selected style to the cover format.

Use three inputs:

1. `punk-cover` task fields: platform, aspect ratio, title clarity, article summarization, cover communication goals, and universal output constraints.
2. The selected style's `META.md` metadata and `STYLE.md` reusable visual style atom.
3. `references/cover-prompt-blueprint.md`, which defines the full cover prompt shape.

The style file defines the reusable visual language. The cover blueprint defines the output form. The final prompt must fuse them into one complete cover-generation prompt.

## Resources

- Read `references/style-catalog.md` to list or choose cover styles.
- Read `references/cover-prompt-blueprint.md` before composing the final prompt.
- For the selected style, read both:
  - `../../styles/{style-id}/META.md`
  - `../../styles/{style-id}/STYLE.md`
- Only expose styles whose `META.md` metadata has `outputs` containing `cover` or `poster`.
- Do not expose photo, avatar, portrait, pet-only, polaroid-only, or image-remix styles in the `punk-cover` menu unless their metadata explicitly includes `cover` or `poster`.
- Do not use legacy cover templates. Use only the selected style's `META.md`, `STYLE.md`, and `references/cover-prompt-blueprint.md`.

## Workflow

1. Analyze the source material:
   - Extract the core visual subject.
   - Preserve the complete user title or topic when one exists, but do not copy the full article body into any output field.
   - Draft an optional subtitle when the selected style has a subtitle field.
   - Summarize context, audience, mood, metaphor, and banned elements.
   - Convert long source material into concise derived fields: title/topic, 1-3 sentence context summary, visual subject, audience, mood, metaphor, and banned elements.

2. Confirm platform and aspect ratio before generating any prompt:
   - Xiaohongshu: `3:4`
   - WeChat public account: `2.35:1`
   - X: `5:2`
   - Custom: keep the user's ratio exactly.
   - If the user only provides source content, ask which platform they want to publish to. Do not generate the prompt yet.
   - If the user provides a custom ratio, use it and do not ask for platform unless the platform matters for wording.
   - Only skip this question when the user has already provided a platform, a ratio, or explicitly says to decide everything automatically.

3. Confirm style before generating any prompt:
   - If the user specifies one catalog style, use it.
   - If the user supplies a complete visual direction that matches a catalog style, including the `复古时代错位编辑封面` brief, treat that style as specified and use the matching `META.md` and `STYLE.md` without asking the user to repeat the style.
   - If no style is specified, recommend exactly three eligible catalog styles based on the content and give a one-sentence reason for each, then ask the user to choose one or provide a custom style direction.
   - Do not show all eligible styles by default unless the user asks for the full menu.
   - Only auto-select one style when the user explicitly says to decide everything automatically, not merely because they provided an article.

4. Use this confirmation gate:
   - When platform/ratio or style is missing, stop after asking the question. Do not fill a style file, save prompt files, or generate an image.
   - The first response for article-only input should contain the platform question and three recommended styles.
   - If both platform/ratio and style are known, continue without asking.

5. Compile the final image prompt:
   - Use `references/cover-prompt-blueprint.md` as the required structure for `prompts/cover.md`.
   - Read exactly one selected style visual atom from `../../styles/{style-id}/STYLE.md`.
   - Read the selected style metadata from `../../styles/{style-id}/META.md`, including `style_anchors`, `cover_shape_adaptation`, `must_preserve`, and `avoid_when_applying_to_cover` when present.
   - Extract the selected style's non-negotiable visual anchors: materials, spatial logic, title treatment, typography behavior, texture, color system, and style-specific negative constraints.
   - Fuse the cover task fields and style anchors into one full cover prompt. The final prompt should read like a complete cover-generation brief, similar to the legacy complete prompts in `exports/`, not like two unrelated prompt fragments pasted together.
   - Include cover-shape sections for role/task, input fields, content understanding, title hierarchy, cover composition, style application, image-text relationship, typography, color/material/texture, negative constraints, and final standard.
   - Every cover decision must be expressed through the selected style. For example, if the style is torn collage, the title, subject, support text, background, and metaphor must be implemented as torn paper, old newspaper, tape, grain, halftone, and paper layers; not as a generic cover with collage words appended.
   - Do not append the raw `STYLE.md` content as a standalone second section. Rewrite and adapt its style atoms into the cover blueprint.
   - Do not combine multiple styles or add a second custom style section.
   - Replace or resolve all explicit placeholders such as `{{主题词}}`, `{{副标题，可留空}}`, `{{画幅比例...}}`, `{{语言...}}`, `{{用途...}}`, `{{补充背景，可留空}}`, `{{情绪倾向...}}`, `{{不想出现的元素，可留空}}`, and any other `{{...}}` fields.
   - If a needed detail has no matching placeholder, merge it into the nearest cover section such as `补充语境`, `风格落地方式`, or `禁用元素`.
   - For long articles, fill title/topic fields with concise derived titles or title layers, not the article text.
   - Put only summarized context into the prompt; do not paste the original article body into the final prompt.
   - Leave optional fields blank only when the prompt says they can be blank.
   - Do not output analysis inside the final prompt.

6. Save files before image generation:
   - Create `punk-assets/punk-cover/{slug}/prompts/cover.md` with the complete filled prompt.
   - If image generation returns an explicit local file path, downloadable URL, or image bytes for the current run, save that artifact as `punk-assets/punk-cover/{slug}/cover.png`.
   - Do not infer the correct artifact by scanning broad generated-image directories, because those directories may contain unrelated images from other runs.
   - If the image-generation tool only returns an inline preview with no explicit retrievable artifact for the current run, do not create a fake `cover.png`.

7. Generate an image by default after saving the prompt when a usable image-generation tool is available, such as `image_gen`. Treat inline preview generation as successful image generation, but treat local `cover.png` saving as successful only when the tool explicitly exposes a current-run artifact. Skip image generation only when the user explicitly asks for prompt-only output or the current environment has no image-generation tool. If image generation is unavailable, return the prompt file path and the full prompt content.

## First Response Format

For article-only input with no platform and no style, ask concisely:

1. Which platform/aspect ratio should this cover target?
   - Xiaohongshu: `3:4`
   - WeChat public account: `2.35:1`
   - X: `5:2`
   - Custom: provide the ratio
2. Recommended styles:
   - `Style A`: reason tied to the article.
   - `Style B`: reason tied to the article.
   - `Style C`: reason tied to the article.

End by asking the user to choose a platform and one style, or to say "auto" if they want the skill to decide everything.

## Style Selection Heuristics

- Use styles whose `outputs` metadata contains `cover` or `poster`.
- Use business/report styles for strategy, product, AI, startup, industry, consulting, or analysis content.
- Use `复古时代错位编辑封面` for AI, coding, digital work, future tools, or contemporary topics that benefit from a human-centered mid-century illustration and one restrained era-displacement metaphor.
- Use journal/concept styles for science, research, medicine, engineering, or mechanism-heavy content.
- Use collage, giant-title, block, brick, or diffuse styles for social posts that need stronger shareability.
- Use black-white minimal or avant-geometry styles for abstract, philosophical, critical, or high-contrast editorial themes.
- Do not recommend styles whose metadata is avatar-only, portrait-only, pet-only, polaroid-only, or image-only unless they also declare `cover` or `poster`.

## Cover Prompt Blueprint

Use `references/cover-prompt-blueprint.md` as the full prompt structure. The block below is retained only as the required task-field content that must be represented inside the integrated final prompt.

```text
# punk-cover cover task instructions

Create one single cover image for {platform}. Aspect ratio: {ratio}.

Use the following derived content only:
- Title/topic: {title_or_topic}
- Optional subtitle: {subtitle}
- Short context summary: {summary}
- Visual subject: {visual_subject}
- Audience: {audience}
- Mood: {mood}
- Visual metaphor: {metaphor}
- Banned elements: {banned_elements}

The main title must be complete, accurate, and clearly readable. If the source title is long, extract a short high-impact visual title while preserving the complete meaning through a smaller title, subtitle, or context line.

For long articles, use only derived fields such as title, summary, visual subject, metaphor, and supplemental context. Do not paste the original article body into the image, prompt, metadata, or small text system.

The cover must work for sharing: first glance identifies the topic, second glance reveals the visual metaphor. The image should feel like a deliberate editorial cover, not a generic illustration.

Avoid universal cover failures: PPT cover feel, course-cover feel, generic information-graphic template, e-commerce advertisement, unrelated decoration, misspelled title, missing title, title cropped beyond recognition, or title severely blocked by visual elements.

Generate only one final image. Do not output explanations, alternatives, grids, contact sheets, or multi-option compositions.
```

## Output Discipline

- The final generated prompt must be one integrated cover-specific prompt compiled from the cover task fields, `references/cover-prompt-blueprint.md`, and exactly one selected style atom.
- Do not paste the selected style `STYLE.md` as a standalone second section. Adapt its style atoms into the cover blueprint.
- The final prompt must preserve the selected style's non-negotiable anchors from `META.md` and `STYLE.md`.
- Do not copy long source text into the final prompt; use summaries and extracted fields.
- Do not include style-selection rationale inside the prompt file.
- Do not combine multiple styles.
- Do not add a second custom style section beyond the selected style visual layer.
- Do not expose non-cover styles in the style menu.
