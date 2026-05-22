# FigureYa Figure Contract

Use this before selecting a FigureYa module or writing R code. The purpose is to make the atlas retrieval decision explicit and defensible.

## Required Contract

Create a compact working contract:

```text
Task mode:
Data domain:
Plot family:
Scientific purpose:
Input shape:
Expected columns/objects:
Style constraint:
Candidate FigureYa IDs:
Final output:
Reviewer/statistics risk:
```

## Task Modes

| Mode | Use When | Output |
|---|---|---|
| `search` | User asks what FigureYa tool fits a requirement | 1-3 candidate IDs with reasons |
| `visual match` | User wants to imitate a paper/reference/preview style | Preview comparison and selected ID(s) |
| `code adaptation` | User wants runnable plotting code | Clean R script/snippet adapted from selected pattern |
| `figure audit` | User asks to improve or review an existing plot | Issues, risks, and concrete edits |
| `color advice` | User asks for palette or journal style | Palette rationale plus R scale code |

## Domain Routing

Choose `biostatistics_general` for group comparisons, ROC/AUC, calibration, survival/KM, Cox, forest plots, clinical tables, correlation/regression, Venn, distribution summaries, and diagnostic models.

Choose `bioinformatics_omics` for RNA-seq, expression matrices, DEGs, volcano plots, GSEA/GO/KEGG/GSVA, single-cell, spatial transcriptomics, mutation, CNV, TMB, methylation, ATAC/ChIP, genome tracks, circos, immune infiltration, and multi-omics workflows.

If the user request spans both domains, retrieve from both indexes but still rank a final set of 1-3 tools.

## Input Shape Defaults

State the expected input explicitly. If the user has not provided data, assume one of these common shapes:

| Plot family | Default input |
|---|---|
| Expression heatmap | gene x sample matrix plus optional sample annotation table |
| Volcano | data frame with gene, logFC/log2FC, pvalue, padj/FDR |
| Box/violin/bar | long data frame with value, group, optional facet/sample columns |
| Survival/KM/Cox | sample x clinical table with time, event, group/risk score/covariates |
| ROC/calibration | sample x table with outcome, predicted score/probability, model label |
| GSEA/enrichment | ranked gene list or enrichment result table |
| Mutation/onco plot | MAF-like mutation table or maftools-compatible object |
| Single-cell | Seurat/SCE object or embedding coordinates plus metadata |

## Selection Rules

- Prefer a FigureYa module whose domain, plot family, and input shape all match.
- Prefer local bundled code under `references/code/FigureYaXXX/` over GitHub fallback.
- Prefer visual previews only after the analytical match is plausible.
- If two modules are equivalent, choose the simpler one with fewer dependencies.
- If no module matches well, use the closest FigureYa pattern only as visual inspiration and write a clean R implementation.

## Response Contract

When answering the user, report:

- selected FigureYa ID(s);
- why they match;
- expected input format;
- required R packages;
- any important assumptions;
- FigureYa attribution when its patterns or code structure influenced the result.
