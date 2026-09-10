# Third-Party Notices and Provenance Register

The Punk Skill licenses grant only rights controlled by the Licensor. A name,
reference, screenshot, prompt source, contributed image, font reference,
software name, or visual direction appearing in this repository does not imply
ownership, endorsement, affiliation, or permission from the referenced party.

Before the `v2.0.0` release, the maintainer must complete this register for
every externally sourced or contributed item.

| Path or component | Source and author | Source URL or record | Applicable license or written permission | Commercial use permitted | Evidence location | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `screenshots/` (all 38 example images) | Created by Licensor 庞静雯 using OpenAI ChatGPT Image 2.0 | [OpenAI Terms of Use](https://openai.com/policies/terms-of-use/) | Licensor-created outputs, subject to the provider terms applicable on the generation date and any rights in the inputs | Yes, subject to provider terms and input or third-party rights | Licensor's private ChatGPT generation/account records and declaration dated 2026-09-09 | Declared; generation evidence must be archived before `v2.0.0` |
| `styles/block-world/`, `styles/fashion-sketch-observation/`, `styles/grotesque-soul-sketch/`, `styles/messy-crayon-pet-portrait/`, `styles/pixel-avatar/`, and `styles/polaroid-keepsake/` | Licensor-authored prompts adapted from the Licensor's private exports dated 2026-06-16 | Source records named in each `META.md` | Licensor-authored material; no third-party permission asserted | Yes, subject to verification of the retained source records | Licensor's private export archive | Declared; source archive must be retained before `v2.0.0` |
| `styles/surreal-pop-up-paper-landscape/` | Licensor-authored prompt and Licensor-provided reference image | Source declaration in `META.md` | Licensor-provided material, subject to any privacy, publicity, or third-party rights in the reference image | Yes, only if the Licensor controls the required rights in the reference image | Licensor's private source and generation records | Declared; input-rights evidence must be retained before `v2.0.0` |
| `styles/anthropic-research-style/`, `styles/kimi-stlye/`, and `styles/godot-2d-pixel-metaphor-poster/` | Original repository text using third-party names only to identify a visual direction or software context | Repository files and Git history | No third-party logo, product interface, or official artwork is licensed; the names may be third-party trademarks | No trademark license is granted; commercial use of the repository text remains subject to contributor clearance below | Repository files and commit history | Reviewed for name/reference use; retain the existing no-logo and no-interface restrictions |

## Contributor and relicensing register

The repository history includes material authored by people other than the
Licensor. Historical copies already released under the MIT License keep those
rights. Before publishing `v2.0.0` under the dual-license terms, the maintainer
must either retain the affected material under its historical MIT terms or
store a signed CLA or other written permission that expressly permits the new
personal-use and paid-commercial licensing model.

| Contributor | Affected material | Existing basis | Required record for `v2.0.0` | Status |
| --- | --- | --- | --- | --- |
| [`jinchenma94`](https://github.com/jinchenma94) (`jinchenma`) | Foundational skill files, scripts, styles, documentation, and example images across 32 commits | Historical MIT release and Git history | Written CLA confirmation received by email on 2026-09-10 | Confirmed; retain the original email and signed CLA attachment in the private records archive |
| [`ozrwayne`](https://github.com/ozrwayne) (`Roland`) | Anthropic Research and Kimi styles and images; license-upgrade PR text | Historical MIT terms for merged contributions; current PR is unmerged | Written CLA confirmation and electronic signature received by email on 2026-09-10 | Confirmed; retain the original email in the private records archive |
| [`cq060806-sudo`](https://github.com/cq060806-sudo) (`Shengtaispa`) | Validation-script fixes merged in PR #1 | PR #1 was reverted by PR #10; no affected contribution remains in the current v2 work | No v2 relicensing record required while the reverted material stays excluded | Reverted and excluded from `v2.0.0` |

## Required review items

- prompts whose `META.md` files refer to external exports;
- user-contributed prompts and reference images;
- every screenshot under `screenshots/`;
- named visual directions that reference Anthropic, Kimi, Godot, or another
  third-party name;
- fonts, logos, interface elements, product names, and trademarks; and
- material copied or adapted from another repository, website, article,
  dataset, or generated-image service.

Items with unknown ownership or commercial permission must be removed from a
commercially licensed release until their status is documented.
