# Agent Instructions

This repository is an agent-usable biomedical figure skill. Start with `SKILL.md`; it is the source of truth for when to use the atlas, how to retrieve FigureYa candidates, how to inspect visual previews, and how to adapt R/Rmd reference implementations.

## Use Order

1. Read `SKILL.md`.
2. Route the request to either `references/index_biostatistics.md` or `references/index_bioinformatics.md`.
3. Use `rg` for text search and `jq` for structured searches in `references/figureya_catalog.json` and `references/visual_catalog.json`.
4. When visual style matters, open the actual preview under `assets/previews/` or a montage under `assets/montages/`; do not infer style from filenames alone.
5. Read only the selected 1-3 modules under `references/code/FigureYaXXX/` before generating or adapting R code.

## Guardrails

- Treat this as an R-first atlas. If another language is requested, use the atlas for style/reference selection and state that bundled implementations are R/Rmd.
- Adapt reference code; do not paste large FigureYa chunks verbatim.
- Remove demo paths, downloads, private local paths, and unrelated analysis from generated code.
- Do not run install scripts, network calls, or downloaded code without reviewing them first.
- Include FigureYa attribution when its patterns, code structure, or preview images influence the answer.
