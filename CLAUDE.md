# Claude Instructions

Use this repository through `SKILL.md`. The folder follows the standard skill layout with `SKILL.md`, `references/`, `assets/`, `scripts/`, and `agents/openai.yaml`.

Use the procedural references the same way as the Nature-style skill pattern:

- `references/figure-contract.md` for task classification and selection constraints.
- `references/retrieval-workflow.md` for fast local search and candidate ranking.
- `references/visual-matching.md` when preview/montage comparison matters.
- `references/r-code-adaptation.md` before writing complete R code.
- `references/qa-contract.md` before final delivery.

For biomedical R figure tasks, retrieve candidates from the local indexes before using the web:

- `references/index_biostatistics.md` for survival, ROC, forest, Cox, calibration, correlation, box/violin/bar, and other medical statistics plots.
- `references/index_bioinformatics.md` for RNA-seq, DEG, enrichment, single-cell, spatial, mutation, CNV, methylation, ATAC/ChIP, genome, immune, and multi-omics plots.
- `references/figureya_catalog.json` and `references/visual_catalog.json` for structured filtering.
- `assets/previews/` and `assets/montages/` for visual style matching.

Keep context small: select 1-3 FigureYa modules, then read only those `.Rmd`, `.rmd`, or helper `.R` files under `references/code/`. Generate clean R code for the user's data rather than copying the original examples wholesale.
