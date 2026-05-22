---
name: biomedical-figureya-atlas
description: >-
  R-first biomedical scientific figure atlas built from the public FigureYa repository. Use when the user needs to find, classify, imitate, adapt, or generate R code for biomedical publication figures, including biostatistics/medical statistics plots, bioinformatics and omics visualizations, paper-figure recreation, visual style matching from preview images, FigureYa template selection, color palette recommendations, and journal-ready SVG/PDF/PNG export advice. Prefer local catalog search, preview images, and bundled R/Rmd reference code before web fallbacks. Do not use for interactive dashboards or non-biomedical illustration-first graphics.
---

# Biomedical FigureYa Atlas

Use this skill as a fast retrieval-and-adaptation layer over the local FigureYa atlas. The goal is not to copy FigureYa code verbatim; the goal is to identify the closest local visual and analytical pattern, then adapt it into clean, runnable R code for the user's data and publication context.

This skill follows progressive disclosure: keep `SKILL.md` as the routing layer, then load only the relevant files in `references/` for contract, retrieval, visual matching, R adaptation, QA, indexes, code, or color decisions.

This is an **R-first** skill. FigureYa reference implementations are R/Rmd modules. If the user asks for Python, use this atlas only for visual/style reference and say clearly that the reusable implementations here are R-based.

## Operating Contract

Start by turning the user request into a compact figure contract. Open `references/figure-contract.md` when the task requires candidate selection, code adaptation, visual matching, or figure review.

1. **Task mode**: `search`, `visual match`, `code adaptation`, `figure audit`, or `color advice`.
2. **Data domain**: `biostatistics_general` or `bioinformatics_omics`.
3. **Plot family**: heatmap, boxplot, violin, volcano, GSEA, survival, ROC, forest, mutation, single-cell, spatial, circos, correlation, etc.
4. **Input shape**: expected columns or matrix/object type.
5. **Output target**: R snippet, complete R script, candidate FigureYa IDs, preview comparison, or publication export package.

Ask at most one clarifying question only when the missing information changes the tool family or data shape. Otherwise, proceed with explicit assumptions and placeholders.

## Fast Retrieval Workflow

Use the smallest useful source first. Avoid loading giant catalogs or many Rmd files into context. Open `references/retrieval-workflow.md` for command patterns, bilingual keyword routing, and candidate-ranking rules.

1. **Route by domain**
   - General medical/biostatistics: open `references/index_biostatistics.md`.
   - Bioinformatics/omics: open `references/index_bioinformatics.md`.
   - Unclear or cross-domain: search `references/figureya_catalog.json` with `jq` or `rg`; open `references/figureya_index.md` only if a human-readable overview is needed.

2. **Search candidates**
   - Prefer `rg` for keyword search across indexes and code.
   - Prefer `jq` for structured filtering by `plot_types`, `primary_category`, `secondary_category`, `analysis_tags`, `libraries`, `input_formats`, and `id`.
   - Match Chinese and English terms. Examples: `火山图|volcano`, `生存|survival|KM`, `富集|GSEA|GO|KEGG`, `突变|mutation|oncoplot`, `相关|correlation`.

3. **Rank only 1-3 tools**
   - Choose by data-domain match first, then plot family, then input format, then package similarity, then visual similarity.
   - Prefer modules with bundled code under `references/code/FigureYaXXX/`.
   - Use the `github_url` from the catalog only when local code is missing or incomplete.

4. **Open reference code sparingly**
   - Read only the selected module's `.Rmd`, `.rmd`, and helper `.R` files.
   - Inspect dependency loading, input examples, core plotting chunks, object names, color mapping, statistics, and export calls.
   - Do not execute `install_dependencies.R` or network/download code without reviewing it first.

5. **Adapt, do not paste**
   - Produce a minimal, coherent R script for the user's data.
   - Keep FigureYa's useful structure, package choices, and visual grammar, but remove demo-specific paths, downloads, and unrelated analysis.

## Visual Matching Workflow

Use visual assets when the user says they want to imitate a paper style, asks which FigureYa result to choose, supplies a reference image, or cares about layout/color/legend style. Open `references/visual-matching.md` for the full preview/montage workflow.

1. Search `references/visual_catalog.json` or `references/visual_index.md` for candidate IDs.
2. Ignore candidates with `preview_status: manual-excluded` or `visual_excluded: true` for style matching.
3. Open the preview image at `assets/previews/FigureYaXXX.jpg`, or the relevant montage in `assets/montages/`.
4. Compare panel layout, marks, color mapping, annotation style, legend placement, axes, statistical labels, and density of information.
5. Select 1-3 final candidates before reading code.

Do not infer visual details from a filename or JSON path alone. Open the actual preview or montage whenever visual similarity is part of the decision.

## Code Generation Rules

Generate R code that is ready to adapt to real user data. Open `references/r-code-adaptation.md` before producing a complete script or adapting a selected FigureYa module.

- Include dependency loading and installation hints, but do not run installs automatically.
- Define a clear expected input schema near the top of the script.
- Use placeholders like `input_file <- "your_data.csv"` instead of hardcoded local paths.
- Use `ggplot2` for common statistical plots; use `ComplexHeatmap`, `circlize`, `survminer`, `clusterProfiler`, `enrichplot`, `maftools`, `Seurat`, or other specialized packages when the selected FigureYa pattern needs them.
- Preserve statistical meaning: state test choice, grouping variable, `n`, confidence interval, p-value adjustment, or cutoff logic where relevant.
- Export publication files with explicit size and resolution, usually PDF/SVG for editable/vector output plus PNG/TIFF for preview or submission.
- Use comments in the user's language. If the user writes Chinese, bilingual comments are acceptable but keep them concise.

When user data is absent, provide a small synthetic example only if it helps demonstrate column names or object structure. Label synthetic data clearly.

## Color And Style Rules

Load `references/color_schemes.md` when the user asks about colors, journal style, heatmaps, multi-group categories, or final polishing.

- Continuous data: prefer `viridis`, `Blues`, or controlled `colorRamp2`.
- Diverging data: use blue-white-red or blue-white-orange with explicit midpoint.
- Categorical data with 2-8 groups: use Okabe-Ito, `Dark2`, `Set2`, or a restrained journal-style palette.
- More than 8 groups: prefer faceting, grouping, or annotation bars instead of adding many saturated colors.
- Heatmaps: use `ComplexHeatmap::Heatmap()` plus `circlize::colorRamp2()` when precise mapping matters.
- Avoid `rainbow()` for scientific figures unless reproducing an existing FigureYa pattern and explain the replacement when improving it.

## Quality Gate Before Final Answer

Open `references/qa-contract.md` before final delivery of code, candidate recommendations, or publication-style figure workflows. At minimum, check:

- The selected FigureYa ID(s) match the user's domain and plot family.
- The expected input format is explicit.
- Required packages are listed.
- Demo paths, downloads, and private local paths are removed from generated code.
- Figure export dimensions and formats are included when the user asks for publication-quality output.
- If visual style was important, at least one preview or montage was actually opened.
- Attribution is included when FigureYa patterns, code structure, or preview images influenced the result.

## Source, Privacy, And Safety

Biomedical FigureYa Atlas is derived from the public FigureYa repository: `https://github.com/ying-ge/FigureYa`.

Acknowledge FigureYa when using its plot patterns, code structure, gallery images, or examples. Treat bundled R/Rmd files as reference implementations, not as blindly executable scripts. Do not upload private user data to external services. Do not disclose private local paths or internal file names in user-facing output unless the user asks for an audit trail.

## Resource Map

| Resource | Use When |
|---|---|
| `references/figure-contract.md` | Need to convert a user request into task mode, data domain, plot family, input shape, output target, and selection rules |
| `references/retrieval-workflow.md` | Need command patterns, bilingual keyword routing, structured `jq` filters, and candidate-ranking rubric |
| `references/visual-matching.md` | User wants to imitate a paper/reference style or compare FigureYa previews/montages |
| `references/r-code-adaptation.md` | Need to adapt selected `.Rmd`/`.R` modules into clean runnable R code |
| `references/qa-contract.md` | Before final delivery, candidate recommendations, code generation, or publication workflow packaging |
| `references/index_biostatistics.md` | Fast lookup for survival, ROC, forest, Cox, calibration, correlation, box/violin/bar, Venn, and other general biomedical statistics plots |
| `references/index_bioinformatics.md` | Fast lookup for RNA-seq, DEGs, enrichment, single-cell, spatial, mutation, CNV, methylation, ATAC/ChIP, genome, immune, and multi-omics plots |
| `references/figureya_catalog.json` | Structured filtering by ID, category, plot type, libraries, dependencies, tags, input format, and GitHub URL |
| `references/figureya_index.md` | Human-readable full catalog overview when the smaller indexes are insufficient |
| `references/visual_catalog.json` | Structured visual matching and preview path lookup |
| `references/visual_index.md` | Human-readable visual index grouped by plot family |
| `references/color_schemes.md` | Palette recommendations and R color code |
| `references/code/FigureYaXXX/` | Bundled `.Rmd`, `.rmd`, and helper `.R` reference implementations for selected tools |
| `assets/previews/FigureYaXXX.jpg` | One normalized preview image per usable FigureYa module |
| `assets/montages/montage_*.jpg` | Thumbnail grids for broad visual browsing by plot family |
| `scripts/*.py` | Maintenance scripts for rescanning FigureYa, regenerating indexes, syncing code, and creating montages |

## Useful Local Commands

Use these patterns to keep retrieval fast:

```bash
# Keyword search in compact indexes
rg -n "volcano|火山|差异表达|DEG" references/index_bioinformatics.md

# Structured search by plot type
jq -r '.[] | select((.plot_types // []) | index("volcano")) | [.id, .secondary_category, .github_url] | @tsv' references/figureya_catalog.json

# Visual candidates with preview paths
jq -r '.[] | select((.plot_types // []) | index("survival")) | select(.visual_excluded == false) | [.id, .preview_image] | @tsv' references/visual_catalog.json

# List bundled code for a selected module
find references/code/FigureYa59volcanoV2 -maxdepth 1 -type f | sort
```
