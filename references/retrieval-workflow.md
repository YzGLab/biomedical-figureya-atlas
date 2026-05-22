# Retrieval Workflow

Use this file when selecting FigureYa candidates. Keep retrieval narrow and evidence-based.

## Search Order

1. Use compact indexes first:
   - `references/index_biostatistics.md`
   - `references/index_bioinformatics.md`
2. Use `references/figureya_catalog.json` for structured filtering.
3. Use `references/visual_catalog.json` only when visual preview status or preview paths matter.
4. Use `references/figureya_index.md` only when compact indexes are insufficient.
5. Use the upstream GitHub URL only when local code for the selected module is missing or incomplete.

## Keyword Map

Search both Chinese and English terms.

| Need | Search terms |
|---|---|
| Volcano / differential expression | `volcano`, `火山`, `差异表达`, `DEG`, `logFC`, `FDR` |
| Heatmap | `heatmap`, `热图`, `ComplexHeatmap`, `pheatmap`, `表达矩阵` |
| Survival / Cox | `survival`, `生存`, `KM`, `Kaplan`, `Cox`, `HR`, `预后` |
| ROC / diagnostic model | `ROC`, `AUC`, `诊断`, `calibration`, `校准`, `nomogram` |
| Enrichment | `GSEA`, `GO`, `KEGG`, `GSVA`, `富集`, `通路` |
| Single-cell | `single-cell`, `scRNA`, `Seurat`, `UMAP`, `tSNE`, `marker` |
| Mutation / CNV | `mutation`, `突变`, `MAF`, `oncoplot`, `CNV`, `TMB` |
| Correlation / regression | `correlation`, `相关`, `scatter`, `regression`, `回归` |
| Forest / subgroup | `forest`, `森林图`, `subgroup`, `亚组`, `HR` |
| Circular / genome | `circos`, `circle`, `genome`, `chromosome`, `基因组`, `染色体` |

## Useful Commands

```bash
# Search compact indexes
rg -n "volcano|火山|差异表达|DEG" references/index_bioinformatics.md

# Structured search by plot type
jq -r '.[] | select((.plot_types // []) | index("volcano")) | [.id, .secondary_category, .input_formats, .github_url] | @tsv' references/figureya_catalog.json

# Search descriptions and tags together
jq -r '.[] | select(((.description // "") + " " + ((.analysis_tags // []) | join(" "))) | test("GSEA|GO|KEGG|富集"; "i")) | [.id, (.plot_types // [] | join(",")), .secondary_category] | @tsv' references/figureya_catalog.json

# Visual candidates with usable preview paths
jq -r '.[] | select((.plot_types // []) | index("survival")) | select(.visual_excluded == false) | [.id, .preview_image] | @tsv' references/visual_catalog.json

# Inspect bundled code for one module
find references/code/FigureYa59volcanoV2 -maxdepth 1 -type f | sort
```

## Ranking Rubric

Score candidates mentally in this order:

1. **Analytical match**: same statistical/biological task.
2. **Data-shape match**: user data fits the module's expected input with minimal conversion.
3. **Package match**: dependencies are appropriate and not unnecessarily heavy.
4. **Visual match**: preview has the requested layout, color logic, annotation, and density.
5. **Adaptation cost**: fewer demo-specific steps, downloads, or hardcoded paths.

Return only the top 1-3 candidates unless the user explicitly asks for a broad catalog.

## Candidate Report Format

```text
Candidate:
Why it matches:
Input expected:
Main packages:
Preview path:
Local code path:
Risk/adaptation note:
```
