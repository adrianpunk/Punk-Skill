# Preflight interpretation

`prepare-redskill.mjs` is deliberately conservative. It performs a mechanical inspection; it does not understand intent, licences, or every implementation language.

| Finding | Meaning | Required action |
| --- | --- | --- |
| `BLOCKER_SECRET_PATTERN` | Content resembles a credential or private key. | Remove/revoke it in the source, then rerun. Never package it. |
| `BLOCKER_XHS_AUTOMATION_PATTERN` | Content resembles Xiaohongshu account automation. | Redesign or remove the capability; do not ship a cosmetic copy. |
| `BLOCKER_HIDDEN_BEHAVIOR_PATTERN` | An instruction resembles hidden or scope-changing behavior. | Rewrite transparently or remove, then get author confirmation. |
| `WARN_BINARY_OR_EXECUTABLE` | A file needs manual inspection. | Confirm it is needed, safe, licensed, and disclosed. |
| `WARN_EXTERNAL_REFERENCE` | A referenced path may not exist after packaging. | Copy and relink the dependency or document why it is not needed. |
| `WARN_THIRD_PARTY_BRANDING` | Names or assets may need rights/attribution review. | Verify permission and attribution, or exclude it. |

The generated package documentation only describes what the source declares. Edit it when the actual capability, data use, or dependency story differs. Do not add a permission statement that the code cannot uphold.
