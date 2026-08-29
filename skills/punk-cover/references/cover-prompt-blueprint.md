# Punk Cover Prompt Blueprint

This blueprint defines the complete cover-prompt shape used by `punk-cover`.

`styles/{style-id}/STYLE.md` is a reusable visual style atom. This blueprint is the cover shape. The final `prompts/01-cover.md` must compile the selected style atom into this cover shape and read like one complete image-generation prompt.

Do not paste this blueprint verbatim with empty placeholders. Fill it with derived article fields and selected style anchors.

## Required Final Prompt Structure

```text
# {style name} cover prompt

You are a top-tier cover art director, editorial visual designer, typography designer, and image-generation prompt director.

Create one single {platform} cover image with aspect ratio {ratio}.

The cover must use the selected visual style: {style name} / {style id}.
This style is not a decorative filter. Every major cover decision must be implemented through this style's visual language.

## Input

- Title/topic: {title_or_topic}
- Title hierarchy:
  - A-layer / main visual title: {short_high_impact_title}
  - B-layer / complete title: {complete_title}
  - C-layer / subtitle or small text: {subtitle}
- Platform: {platform}
- Aspect ratio: {ratio}
- Output dimensions: {output_dimensions_or_auto}
- Output mode: {single_image_or_one_member_of_multi_size_suite}
- Language: {language}
- Use case: {use_case}
- Short context summary: {summary}
- Visual subject: {visual_subject}
- Audience: {audience}
- Mood: {mood}
- Visual metaphor: {metaphor}
- Banned elements: {banned_elements}

## Content Understanding

Understand the source material before composing the image, but do not output analysis in the image.

Use only derived fields from the article. Do not paste the original article body into the image, prompt, metadata, or small text system.

The cover must communicate:

1. What the topic is at first glance.
2. What the core tension, insight, or metaphor is at second glance.
3. Why this cover belongs to the selected visual style, not a generic cover template.

## Cover Objective

Generate a deliberate editorial cover, not a generic illustration, PPT cover, course cover, advertisement, or information card.

The main title must be complete, accurate, and clearly readable. If the source title is long, use the title hierarchy above:

- A-layer: a short high-impact visual title.
- B-layer: the complete title or complete meaning.
- C-layer: subtitle, context line, label, or small editorial text.

## Style Application

Apply the selected style's non-negotiable anchors:

- Style anchors: {style_anchors}
- Cover-shape adaptation: {cover_shape_adaptation}
- Must preserve: {must_preserve}
- Style-specific avoid list: {avoid_when_applying_to_cover}

These anchors must visibly affect:

1. Main title treatment.
2. Visual subject construction.
3. Background or spatial system.
4. Supporting text and label system.
5. Texture, material, color, or rendering method.
6. The visual metaphor.

Do not mention a style trait unless it is actually visible in the final image.

## Composition

Design a cover-specific composition using the selected style.

Define:

- Primary visual center: {primary_visual_center}
- Secondary visual elements: {secondary_visual_elements}
- Background or space system: {background_space_system}
- Foreground/background layering: {layering_strategy}
- Reading path: {reading_path}
- Shareability constraint: the topic must be legible in a fast social feed.

## Image-Text Relationship

The title, subject, and style must be fused.

The title must not be a caption pasted on top of an unrelated image. The selected style must determine how the text exists in the scene:

- Where the main title lives.
- How the subtitle is carried.
- How labels, dates, tags, or small text behave.
- How images, objects, textures, or geometry interact with letterforms.

## Typography

Use typography appropriate to {style name}.

Rules:

- Preserve correct Chinese characters.
- Keep the main title readable.
- Do not crop, misspell, or over-distort key text.
- Use only a small amount of supporting text.
- Supporting text must deepen the cover concept, not become random filler.

## Color, Material, and Texture

Use the selected style's color, material, and texture logic:

{color_material_texture_rules}

The result must feel like a finished cover artwork in this style, not a style word applied superficially.

## Negative Constraints

Avoid:

- {banned_elements}
- Generic cover layout.
- PPT or course-cover feel.
- E-commerce advertisement feel.
- Unrelated decoration.
- Missing or unreadable main title.
- Long article text copied into the image.
- Style-specific failures: {avoid_when_applying_to_cover}

## Final Standard

Generate only one final image.

Do not output explanations, alternatives, grids, contact sheets, or multi-option compositions.

The final image must satisfy all of these:

1. It is clearly a {platform} cover at {ratio}.
2. It communicates the article topic quickly.
3. It uses the selected style as the visible organizing language.
4. The main title is readable and accurate.
5. The visual metaphor is present and style-native.
6. The result has the completeness and specificity of a legacy full cover prompt, while keeping the selected style reusable as an independent atom.
```

## Compilation Notes

- Rewrite the blueprint into a natural final prompt. Do not leave meta-instructions like `{primary_visual_center}` unresolved.
- For a multi-size suite, compile this blueprint once per target ratio or dimension. Each compiled prompt must request exactly one independently composed image and identify its target dimensions; do not ask one prompt to create a grid or contact sheet.
- Preserve the suite's content, metaphor, style identity, material, and palette across targets, while recomposing scale, typography, whitespace, reading direction, and spatial behavior for each ratio.
- Use the selected `META.md` metadata when it provides structured fields.
- Use `STYLE.md` to recover style language that is not yet structured in metadata.
- The final prompt may add style-specific sections when needed, but must not add another style.
- The final prompt should be longer and more complete than the raw style atom, because it includes cover shape, title hierarchy, and content adaptation.
