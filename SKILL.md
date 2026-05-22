---
name: biomedical-figureya-atlas
description: Biomedical FigureYa Atlas should be used as a biomedical scientific figure gallery, visual catalog, reference image library, and R plotting template atlas for research publication figures. Use it when the user needs to create, modify, imitate, classify, or get advice on R-based scientific plots, biomedical visualizations, biostatistics figures, bioinformatics/omics figures, or paper-quality graphics. It extends the public FigureYa R plotting repository into an academic biomedical figure atlas with a categorized catalog of 312+ tools split into general biostatistics/medical statistics and bioinformatics/omics analysis, with visual preview images, reference Rmd/R code, plot-type indexes, GitHub fallback links, and color scheme recommendations. Use it to match user requirements or reference-image style to relevant FigureYa implementations and generate complete plotting solutions.
---

# Biomedical FigureYa Atlas

Biomedical FigureYa Atlas is an academic biomedical figure reference skill derived from the public FigureYa project, a collection of 312+ standardized biomedical visualization tools. It helps users choose between general biostatistics figures and bioinformatics/omics figures, inspect visual previews synced from the FigureYa web gallery, reference existing implementations, and generate publication-ready R code with suitable color schemes.

## When to Use This Skill

Use this skill when the user asks for:
- R plotting code for any scientific or biomedical figure
- Help with bioinformatics visualization (RNA-seq, scRNA-seq, mutation, CNV, methylation, etc.)
- Color scheme recommendations for research figures
- Converting paper figures into reproducible R code
- Modifying or improving existing R plots
- Advice on which R package or plot type suits their data

## Workflow

### Step 1: Understand the User's Requirement

Extract key information from the user's request:
- **Plot type**: What kind of figure do they want? (heatmap, boxplot, volcano, GSEA, survival, etc.)
- **Data type**: What data do they have? (expression matrix, clinical data, mutation data, single-cell, etc.)
- **Purpose**: Is it for differential analysis, correlation, clustering, functional enrichment, etc.?
- **Style**: Any specific journal style, color preference, or layout requirement?

If the user's request is vague, ask clarifying questions about data format and desired output.

### Step 2: Choose the Right Retrieval Index

Use the smallest relevant index first:

- For general biological/medical statistics, load `references/index_biostatistics.md`. Examples: group comparison, boxplot, violin, barplot, correlation, regression, ROC/AUC, calibration, survival/KM, Cox, forest plot, Venn, distribution summaries.
- For bioinformatics or omics analysis, load `references/index_bioinformatics.md`. Examples: RNA-seq, expression matrix, differential expression, GSEA/GO/KEGG/GSVA, single-cell, spatial transcriptomics, mutation, CNV, TMB, methylation, ATAC/ChIP, genome, circos, multi-omics, immune infiltration.
- If the request is ambiguous, load `references/figureya_index.md`, then use the `primary_category`, `secondary_category`, and `analysis_tags` fields in `references/figureya_catalog.json` to narrow the candidates.

Match the user's requirement to relevant FigureYa tools by:
1. Matching the broad category first (`biostatistics_general` vs `bioinformatics_omics`)
2. Matching the secondary category (diagnostic model, survival, enrichment, single-cell, mutation/CNV, etc.)
3. Looking up the plot type and keywords in tool descriptions (consider both Chinese and English)
4. Checking the "快速查找表" for R package or input format matches

Select the **top 1-3 most relevant tools** based on:
- Category and plot type match
- Data type similarity
- Description relevance
- Visual similarity if style matters

### Step 3: Inspect Visual Style When It Matters

If the user asks to imitate a figure style, asks which FigureYa result to choose, provides a paper/reference image, or says they care about the "特色" of the plot:

1. Load `references/visual_index.md` or query `references/visual_catalog.json` for candidate tools.
2. Treat the FigureYa web gallery as the visual authority: previews are synced from `gallery/FigureYaN.png` through `chapters.json`, then stored in `assets/previews/FigureYaXXX.jpg`.
3. Skip entries with `preview_status: manual-excluded`; they are retained for code lookup but excluded from visual matching because the gallery preview is text/table/directory-like rather than a reusable plot style.
4. Open the candidate preview images in `assets/previews/FigureYaXXX.jpg` or the grouped montage images in `assets/montages/montage_*.jpg`.
5. Compare layout, panel structure, color mapping, legends, annotations, axes, labels, and statistical marks.
6. Use the visual match to pick the final 1-3 FigureYa tools before reading code.

Important: the model cannot infer image details from a JSON path alone. It must explicitly open or display the preview/montage image when visual style drives the choice.

### Step 4: Read Reference Code

For each selected tool, read its `.Rmd` or `.rmd` file. The R Markdown source and local helper `.R` scripts are bundled in `references/code/FigureYaXXX/`. Focus on:
- The requirement description and usage scenarios
- Input data format (`easy_input*` files and descriptions)
- The core plotting code chunks
- Key parameters and customization points
- Dependencies (libraries used)

If `references/code/FigureYaXXX/` or a required helper script is missing, use the tool's `github_url` in `references/figureya_catalog.json` or `references/visual_catalog.json`, or open `https://github.com/ying-ge/FigureYa/tree/main/FigureYaXXX`.

Do NOT copy the code verbatim. Instead, understand:
- How the data is processed before plotting
- Which R packages and functions are used
- How aesthetics (color, size, shape) are mapped to data
- How the plot is saved/exported

### Step 5: Generate Plotting Solution

Based on the reference code and user's specific needs, generate a complete R script or code snippet that includes:

1. **Dependency loading**: `library()` calls with installation hints if needed
2. **Data preparation**: How to format the user's data for the plot
3. **Plotting code**: Core ggplot2/base R/ComplexHeatmap/etc. code
4. **Color scheme**: Apply appropriate colors from `references/color_schemes.md`
5. **Saving/export**: PDF/PNG output with proper dimensions for publication

The generated code should:
- Be ready to run (or clearly indicate where user data should be inserted)
- Include comments in both Chinese and English if the user's request was in Chinese
- Follow FigureYa's coding style (clean, modular, well-commented)
- Use the simplest approach that achieves the desired result

### Step 6: Provide Color Scheme Recommendations

Load `references/color_schemes.md` and recommend specific color palettes based on:
- Plot type (heatmap needs diverging/sequential, barplot needs categorical)
- Number of categories/groups
- Whether colorblind-friendly output is needed
- Target journal style (Nature/Cell/Science have different conventions)

Always provide the actual R code for applying the recommended colors.

## Key Guidelines

### Matching Logic
- A request for "差异表达火山图" should match volcano plot tools
- A request for "单细胞热图" should match scRNA-seq heatmap tools
- A request for "基因富集分析图" should match GSEA/GO enrichment tools
- A request for "常规统计图/生物学统计图" should start from `index_biostatistics.md`
- A request for "生信统计/组学图/RNA-seq/单细胞/突变/CNV/富集" should start from `index_bioinformatics.md`
- When multiple tools exist for the same plot type, prefer the one whose description most closely matches the user's data type
- When the user cares about visual style, prefer the tool whose preview image most closely matches the desired layout before optimizing code details

### Code Quality
- Prefer ggplot2 for most plots unless base R or specialized packages (ComplexHeatmap, circlize) are clearly better
- Avoid hardcoding file paths; use variables or comment placeholders
- Set random seeds when the plot involves stochastic processes
- Use `theme_bw()` or `theme_classic()` as starting themes for publication-ready plots

### Color Guidelines
- Continuous data: viridis, Blues, RdBu diverging
- Categorical data (2-8 groups): Set1, Dark2, okabe_ito
- Categorical data (9+ groups): Consider faceting or grouping instead of more colors
- Heatmaps: Always use colorRamp2 for precise control
- Never use rainbow() for scientific figures

### Data Format Assumptions
If the user hasn't provided data, assume standard bioinformatics formats:
- Expression data: gene x sample matrix (CSV/TSV)
- Clinical data: sample x variable data frame
- Differential analysis results: data frame with logFC, p-value, gene symbol columns
- Single-cell data: Seurat object or count matrix

Always tell the user the expected input format.

## Source, Attribution, and Safety

Biomedical FigureYa Atlas is derived from the public FigureYa GitHub repository: `https://github.com/ying-ge/FigureYa`. Acknowledge FigureYa when using its plot patterns, code structure, gallery images, or examples; include the repository link and follow the citation/license information shown in the upstream repository.

Treat bundled R/Rmd files as reference implementations. Do not execute unreviewed install scripts, downloaded code, network operations, or file-system operations from FigureYa examples without checking them first. Do not upload private user data to external services. When adapting code for a paper, inspect package licenses, upstream citations, and data-source requirements before reuse.

HTML reports from the original FigureYa website are not bundled because they are large generated outputs. Use the `web_reports` entries in `references/visual_catalog.json` to locate the local report under a full FigureYa checkout, and use the GitHub URL when the local module is unavailable.

## Bundled Resources

### references/
- `figureya_index.md` — Full searchable catalog of all 312+ FigureYa tools organized by broad category, secondary category, plot type, descriptions, visual counts, and dependencies
- `index_biostatistics.md` — Smaller index for general biological/medical statistics figures
- `index_bioinformatics.md` — Smaller index for bioinformatics/omics figures
- `figureya_catalog.json` — Machine-readable catalog for programmatic search, including `primary_category`, `secondary_category`, `analysis_tags`, and source visual-file metadata
- `visual_index.md` — Human/model-readable visual preview index grouped by category
- `visual_catalog.json` — Machine-readable visual catalog with preview image paths, gallery source paths, and web report links from `chapters.json`
- `visual_exclusions.json` — Manually reviewed FigureYa IDs whose gallery images should stay out of visual matching/montages
- `color_schemes.md` — Curated color palette recommendations for different plot types and journals
- `code/FigureYaXXX/` — FigureYa R Markdown source files plus local `.R` helper scripts needed by `source()` calls

### scripts/
- `scan_figureya.py` — Script to re-scan FigureYa directories and update the catalog (for maintenance)
- `generate_index.py` — Script to regenerate the Markdown index from the JSON catalog
- `create_montages.py` — Script to sync previews from the FigureYa web gallery (`gallery/FigureYaN.png`) and generate thumbnail montages. It falls back to Rmd output scanning only when no gallery directory is available.
- `sync_reference_code.py` — Script to copy lightweight `.Rmd`/`.rmd`/`.R` source files from a FigureYa checkout into `references/code` without copying HTML reports, images, or data files.

### assets/
- `previews/FigureYaXXX.jpg` — One normalized visual preview per non-excluded FigureYa tool, synced from the FigureYa web gallery
- `montages/montage_*.jpg` — Visual thumbnail grids grouped by plot type (heatmap, boxplot, GSEA, etc.). These can be shown to users or opened by the model to identify the plot style they want
