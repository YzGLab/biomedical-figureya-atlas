# FigureYa Visual Index

- Tools: **312**
- Tools with raster previews: **306**
- Manually excluded from visual matching: **6**
- Source visual files recorded: **306**

Use `visual_catalog.json` for machine filtering, then open the listed preview or montage image before choosing a reference implementation.
Entries with `preview_status: manual-excluded` are retained for code lookup but omitted from montage pages because their gallery preview is text/table/directory-like rather than a reusable plot style.
Source repository: https://github.com/ying-ge/FigureYa. If a local code module is missing, use the tool's GitHub URL in `visual_catalog.json`.

## Montage Pages

| Plot type | Pages |
|---|---|
| barplot | `assets/montages/montage_barplot_page1.jpg`<br>`assets/montages/montage_barplot_page2.jpg` |
| boxplot | `assets/montages/montage_boxplot.jpg` |
| bubble | `assets/montages/montage_bubble.jpg` |
| calibration | `assets/montages/montage_calibration.jpg` |
| chromosome | `assets/montages/montage_chromosome.jpg` |
| circos | `assets/montages/montage_circos.jpg` |
| correlation | `assets/montages/montage_correlation_page1.jpg`<br>`assets/montages/montage_correlation_page2.jpg`<br>`assets/montages/montage_correlation_page3.jpg`<br>`assets/montages/montage_correlation_page4.jpg`<br>`assets/montages/montage_correlation_page5.jpg`<br>`assets/montages/montage_correlation_page6.jpg` |
| dendrogram | `assets/montages/montage_dendrogram.jpg` |
| density | `assets/montages/montage_density.jpg` |
| forest | `assets/montages/montage_forest.jpg` |
| GO | `assets/montages/montage_GO_page1.jpg`<br>`assets/montages/montage_GO_page2.jpg` |
| GSEA | `assets/montages/montage_GSEA_page1.jpg`<br>`assets/montages/montage_GSEA_page2.jpg` |
| heatmap | `assets/montages/montage_heatmap_page1.jpg`<br>`assets/montages/montage_heatmap_page2.jpg`<br>`assets/montages/montage_heatmap_page3.jpg`<br>`assets/montages/montage_heatmap_page4.jpg` |
| line | `assets/montages/montage_line.jpg` |
| mosaic | `assets/montages/montage_mosaic.jpg` |
| mutation | `assets/montages/montage_mutation_page1.jpg`<br>`assets/montages/montage_mutation_page2.jpg`<br>`assets/montages/montage_mutation_page3.jpg` |
| network | `assets/montages/montage_network.jpg` |
| PCA | `assets/montages/montage_PCA.jpg` |
| pie | `assets/montages/montage_pie.jpg` |
| ROC | `assets/montages/montage_ROC_page1.jpg`<br>`assets/montages/montage_ROC_page2.jpg` |
| scatter | `assets/montages/montage_scatter.jpg` |
| survival | `assets/montages/montage_survival_page1.jpg`<br>`assets/montages/montage_survival_page2.jpg` |
| uncategorized | `assets/montages/montage_uncategorized_page1.jpg`<br>`assets/montages/montage_uncategorized_page2.jpg`<br>`assets/montages/montage_uncategorized_page3.jpg`<br>`assets/montages/montage_uncategorized_page4.jpg`<br>`assets/montages/montage_uncategorized_page5.jpg` |
| venn | `assets/montages/montage_venn.jpg` |
| violin | `assets/montages/montage_violin.jpg` |
| volcano | `assets/montages/montage_volcano.jpg` |

## Category Navigation

### 常规生物学/医学统计图

- **生存/预后/Cox**: 37 tools, 36 previews
- **相关/回归/散点**: 26 tools, 25 previews
- **ROC/AUC/校准/诊断模型**: 25 tools, 25 previews
- **通用可视化**: 14 tools, 14 previews
- **分布/比例/Venn/组成**: 11 tools, 11 previews
- **分组比较：箱线图/小提琴/柱状图**: 9 tools, 9 previews

### 生信/组学分析图

- **富集/通路/GSEA/GSVA**: 74 tools, 73 previews
- **单细胞/空间转录组**: 42 tools, 42 previews
- **表达矩阵/差异表达/RNA-seq**: 27 tools, 25 previews
- **甲基化/ATAC/ChIP/表观组**: 18 tools, 17 previews
- **突变/CNV/TMB/MAF**: 16 tools, 16 previews
- **基因组/染色体/Circos**: 11 tools, 11 previews
- **多组学/网络/免疫浸润**: 2 tools, 2 previews


## Tool Previews

### 常规生物学/医学统计图

#### 生存/预后/Cox

- **FigureYa116supervisedCluster** — preview: `assets/previews/FigureYa116supervisedCluster.jpg`; selected source: `gallery/FigureYa116.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa116supervisedCluster
- **FigureYa143survCor** — preview: `assets/previews/FigureYa143survCor.jpg`; selected source: `gallery/FigureYa143.png`; types: correlation, scatter; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa143survCor
- **FigureYa156enrichSimulation** — preview: `assets/previews/FigureYa156enrichSimulation.jpg`; selected source: `gallery/FigureYa156.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa156enrichSimulation
- **FigureYa171subgroupSurv** — preview: `assets/previews/FigureYa171subgroupSurv.jpg`; selected source: `gallery/FigureYa171.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa171subgroupSurv
- **FigureYa183condSurv** — preview: `assets/previews/FigureYa183condSurv.jpg`; selected source: `gallery/FigureYa183.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa183condSurv
- **FigureYa184ranger** — preview: `assets/previews/FigureYa184ranger.jpg`; selected source: `gallery/FigureYa184.png`; types: forest, survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa184ranger
- **FigureYa186swimmerplot** — preview: `assets/previews/FigureYa186swimmerplot.jpg`; selected source: `gallery/FigureYa186.png`; types: barplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa186swimmerplot
- **FigureYa187RMS** — preview: `assets/previews/FigureYa187RMS.jpg`; selected source: `gallery/FigureYa187.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa187RMS
- **FigureYa190batchLogistic** — preview: `assets/previews/FigureYa190batchLogistic.jpg`; selected source: `gallery/FigureYa190.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa190batchLogistic
- **FigureYa192breakpoint** — preview: `assets/previews/FigureYa192breakpoint.jpg`; selected source: `gallery/FigureYa192.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa192breakpoint
- **FigureYa193RiskTable** — preview: `assets/previews/FigureYa193RiskTable.jpg`; selected source: `gallery/FigureYa193.png`; types: forest; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa193RiskTable
- **FigureYa196PanPie** — preview: `assets/previews/FigureYa196PanPie.jpg`; selected source: `gallery/FigureYa196.png`; types: pie; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa196PanPie
- **FigureYa197SmoothHaz** — preview: `assets/previews/FigureYa197SmoothHaz.jpg`; selected source: `gallery/FigureYa197.png`; types: density, survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa197SmoothHaz
- **FigureYa1survivalCurve_update** — preview: `assets/previews/FigureYa1survivalCurve_update.jpg`; selected source: `gallery/FigureYa1.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa1survivalCurve_update
- **FigureYa204PCAscore** — preview: `assets/previews/FigureYa204PCAscore.jpg`; selected source: `gallery/FigureYa204.png`; types: correlation, PCA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa204PCAscore
- **FigureYa20mortality** — preview: `assets/previews/FigureYa20mortality.jpg`; selected source: `gallery/FigureYa20.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa20mortality
- **FigureYa216MetaREM** — preview: `assets/previews/FigureYa216MetaREM.jpg`; selected source: `gallery/FigureYa216.png`; types: forest; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa216MetaREM
- **FigureYa21TCGA2table** — preview: `assets/previews/FigureYa21TCGA2table.jpg`; selected source: `gallery/FigureYa21.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa21TCGA2table
- **FigureYa220repeatedLasso** — preview: `assets/previews/FigureYa220repeatedLasso.jpg`; selected source: `gallery/FigureYa220.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa220repeatedLasso
- **FigureYa221tenFoldRF** — preview: `assets/previews/FigureYa221tenFoldRF.jpg`; selected source: `gallery/FigureYa221.png`; types: forest; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa221tenFoldRF
- **FigureYa22FPKM2TPM** — preview: `no raster preview`; selected source: `none`; types: -; visuals: 0 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa22FPKM2TPM
- **FigureYa233genepair** — preview: `assets/previews/FigureYa233genepair.jpg`; selected source: `gallery/FigureYa233.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa233genepair
- **FigureYa250ImmGenePair** — preview: `assets/previews/FigureYa250ImmGenePair.jpg`; selected source: `gallery/FigureYa250.png`; types: density; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa250ImmGenePair
- **FigureYa251NPHSurv** — preview: `assets/previews/FigureYa251NPHSurv.jpg`; selected source: `gallery/FigureYa251.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa251NPHSurv
- **FigureYa284pairwiseLogrank** — preview: `assets/previews/FigureYa284pairwiseLogrank.jpg`; selected source: `gallery/FigureYa284.png`; types: correlation, survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa284pairwiseLogrank
- **FigureYa298ecdfPvalue** — preview: `assets/previews/FigureYa298ecdfPvalue.jpg`; selected source: `gallery/FigureYa298.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa298ecdfPvalue
- **FigureYa299pancanSurv** — preview: `assets/previews/FigureYa299pancanSurv.jpg`; selected source: `gallery/FigureYa299.png`; types: correlation, heatmap, survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa299pancanSurv
- **FigureYa316RF_XGBoost_Boruta** — preview: `assets/previews/FigureYa316RF_XGBoost_Boruta.jpg`; selected source: `gallery/FigureYa316.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa316RF_XGBoost_Boruta
- **FigureYa35batch_bestSeparationV3_update** — preview: `assets/previews/FigureYa35batch_bestSeparationV3_update.jpg`; selected source: `gallery/FigureYa35.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa35batch_bestSeparationV3_update
- **FigureYa36nSurvV3** — preview: `assets/previews/FigureYa36nSurvV3.jpg`; selected source: `gallery/FigureYa36.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa36nSurvV3
- **FigureYa47HRtable** — preview: `assets/previews/FigureYa47HRtable.jpg`; selected source: `gallery/FigureYa47.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa47HRtable
- **FigureYa4bestSeparation** — preview: `assets/previews/FigureYa4bestSeparation.jpg`; selected source: `gallery/FigureYa4.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa4bestSeparation
- **FigureYa51TMB_update** — preview: `assets/previews/FigureYa51TMB_update.jpg`; selected source: `gallery/FigureYa51.png`; types: boxplot, scatter, mutation, survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa51TMB_update
- **FigureYa81immune_network** — preview: `assets/previews/FigureYa81immune_network.jpg`; selected source: `gallery/FigureYa81.png`; types: correlation, network; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa81immune_network
- **FigureYa90subgroup** — preview: `assets/previews/FigureYa90subgroup.jpg`; selected source: `gallery/FigureYa90.png`; types: forest; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa90subgroup
- **FigureYa91cluster_heatmap** — preview: `assets/previews/FigureYa91cluster_heatmap.jpg`; selected source: `gallery/FigureYa91.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa91cluster_heatmap
- **FigureYa99smoothHRv2** — preview: `assets/previews/FigureYa99smoothHRv2.jpg`; selected source: `gallery/FigureYa99.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa99smoothHRv2

#### 相关/回归/散点

- **FigureYa103coAbundant** — preview: `assets/previews/FigureYa103coAbundant.jpg`; selected source: `gallery/FigureYa103.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa103coAbundant
- **FigureYa117multilinearDE** — preview: `assets/previews/FigureYa117multilinearDE.jpg`; selected source: `gallery/FigureYa117.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa117multilinearDE
- **FigureYa125FishertestV2** — preview: `assets/previews/FigureYa125FishertestV2.jpg`; selected source: `gallery/FigureYa125.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa125FishertestV2
- **FigureYa131CMap_update** — preview: `assets/previews/FigureYa131CMap_update.jpg`; selected source: `gallery/FigureYa131.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa131CMap_update
- **FigureYa141risk** — preview: `assets/previews/FigureYa141risk.jpg`; selected source: `gallery/FigureYa141.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa141risk
- **FigureYa149rankHeatmap** — preview: `assets/previews/FigureYa149rankHeatmap.jpg`; selected source: `gallery/FigureYa149.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa149rankHeatmap
- **FigureYa152DouleCorPlot** — preview: `assets/previews/FigureYa152DouleCorPlot.jpg`; selected source: `gallery/FigureYa152.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa152DouleCorPlot
- **FigureYa154immuneSubtypes** — preview: `assets/previews/FigureYa154immuneSubtypes.jpg`; selected source: `gallery/FigureYa154.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa154immuneSubtypes
- **FigureYa163twoVarCor_update** — preview: `assets/previews/FigureYa163twoVarCor_update.jpg`; selected source: `gallery/FigureYa163.png`; types: correlation, scatter; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa163twoVarCor_update
- **FigureYa179AMDAplot** — preview: `assets/previews/FigureYa179AMDAplot.jpg`; selected source: `gallery/FigureYa179.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa179AMDAplot
- **FigureYa181multiCorrelation** — preview: `assets/previews/FigureYa181multiCorrelation.jpg`; selected source: `gallery/FigureYa181.png`; types: correlation, scatter, network; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa181multiCorrelation
- **FigureYa201ClusterCorrelation** — preview: `assets/previews/FigureYa201ClusterCorrelation.jpg`; selected source: `gallery/FigureYa201.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa201ClusterCorrelation
- **FigureYa229PCOA** — preview: `assets/previews/FigureYa229PCOA.jpg`; selected source: `gallery/FigureYa229.png`; types: scatter, PCA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa229PCOA
- **FigureYa234panImmune** — preview: `assets/previews/FigureYa234panImmune.jpg`; selected source: `gallery/FigureYa234.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa234panImmune
- **FigureYa288MutualExclusivity** — preview: `assets/previews/FigureYa288MutualExclusivity.jpg`; selected source: `gallery/FigureYa288.png`; types: correlation, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa288MutualExclusivity
- **FigureYa321volcanoSE** — preview: `assets/previews/FigureYa321volcanoSE.jpg`; selected source: `gallery/FigureYa321.png`; types: correlation, volcano; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa321volcanoSE
- **FigureYa37correlationV2_update** — preview: `assets/previews/FigureYa37correlationV2_update.jpg`; selected source: `gallery/FigureYa37.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa37correlationV2_update
- **FigureYa41GEO2lncRNA_update** — preview: `no raster preview`; selected source: `none`; types: correlation; visuals: 0 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa41GEO2lncRNA_update
- **FigureYa64triangle** — preview: `assets/previews/FigureYa64triangle.jpg`; selected source: `gallery/FigureYa64.png`; types: correlation, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa64triangle
- **FigureYa65SVM** — preview: `assets/previews/FigureYa65SVM.jpg`; selected source: `gallery/FigureYa65.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa65SVM
- **FigureYa70mutationEvents** — preview: `assets/previews/FigureYa70mutationEvents.jpg`; selected source: `gallery/FigureYa70.png`; types: correlation, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa70mutationEvents
- **FigureYa76corrgram** — preview: `assets/previews/FigureYa76corrgram.jpg`; selected source: `gallery/FigureYa76.png`; types: correlation, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa76corrgram
- **FigureYa7PSM** — preview: `assets/previews/FigureYa7PSM.jpg`; selected source: `gallery/FigureYa7.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa7PSM
- **FigureYa92immune_gene_update** — preview: `assets/previews/FigureYa92immune_gene_update.jpg`; selected source: `gallery/FigureYa92.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa92immune_gene_update
- **FigureYa97correlationV3** — preview: `assets/previews/FigureYa97correlationV3.jpg`; selected source: `gallery/FigureYa97.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa97correlationV3
- **FigureYa9heatmap** — preview: `assets/previews/FigureYa9heatmap.jpg`; selected source: `gallery/FigureYa9.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa9heatmap

#### ROC/AUC/校准/诊断模型

- **FigureYa102multipanelROC** — preview: `assets/previews/FigureYa102multipanelROC.jpg`; selected source: `gallery/FigureYa102.png`; types: ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa102multipanelROC
- **FigureYa123mutVSexpr** — preview: `assets/previews/FigureYa123mutVSexpr.jpg`; selected source: `gallery/FigureYa123.png`; types: correlation, survival, ROC, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa123mutVSexpr
- **FigureYa129TCGAbox** — preview: `assets/previews/FigureYa129TCGAbox.jpg`; selected source: `gallery/FigureYa129.png`; types: ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa129TCGAbox
- **FigureYa138NiceCalibration** — preview: `assets/previews/FigureYa138NiceCalibration.jpg`; selected source: `gallery/FigureYa138.png`; types: calibration; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa138NiceCalibration
- **FigureYa146TMEbox** — preview: `assets/previews/FigureYa146TMEbox.jpg`; selected source: `gallery/FigureYa146.png`; types: correlation, boxplot, ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa146TMEbox
- **FigureYa159LR_RF_V2** — preview: `assets/previews/FigureYa159LR_RF_V2.jpg`; selected source: `gallery/FigureYa159.png`; types: forest; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa159LR_RF_V2
- **FigureYa189timeCindex** — preview: `assets/previews/FigureYa189timeCindex.jpg`; selected source: `gallery/FigureYa189.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa189timeCindex
- **FigureYa191bestLogistic** — preview: `assets/previews/FigureYa191bestLogistic.jpg`; selected source: `gallery/FigureYa191.png`; types: ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa191bestLogistic
- **FigureYa200pairwiseAUC** — preview: `assets/previews/FigureYa200pairwiseAUC.jpg`; selected source: `gallery/FigureYa200.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa200pairwiseAUC
- **FigureYa203ComBat** — preview: `assets/previews/FigureYa203ComBat.jpg`; selected source: `gallery/FigureYa203.png`; types: correlation, ROC, PCA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa203ComBat
- **FigureYa212drugTargetV2** — preview: `assets/previews/FigureYa212drugTargetV2.jpg`; selected source: `gallery/FigureYa212.png`; types: venn; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa212drugTargetV2
- **FigureYa219GMM** — preview: `assets/previews/FigureYa219GMM.jpg`; selected source: `gallery/FigureYa219.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa219GMM
- **FigureYa225GiViTl** — preview: `assets/previews/FigureYa225GiViTl.jpg`; selected source: `gallery/FigureYa225.png`; types: calibration; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa225GiViTl
- **FigureYa238corRiskMut** — preview: `assets/previews/FigureYa238corRiskMut.jpg`; selected source: `gallery/FigureYa238.png`; types: forest, pie, correlation, ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa238corRiskMut
- **FigureYa246supervisedGDSC** — preview: `assets/previews/FigureYa246supervisedGDSC.jpg`; selected source: `gallery/FigureYa246.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa246supervisedGDSC
- **FigureYa247oncoPredict** — preview: `assets/previews/FigureYa247oncoPredict.jpg`; selected source: `gallery/FigureYa247.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa247oncoPredict
- **FigureYa24ROC** — preview: `assets/previews/FigureYa24ROC.jpg`; selected source: `gallery/FigureYa24.png`; types: ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa24ROC
- **FigureYa286ExprCorORR** — preview: `assets/previews/FigureYa286ExprCorORR.jpg`; selected source: `gallery/FigureYa286.png`; types: correlation, ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa286ExprCorORR
- **FigureYa291PancanProgSigatureV2** — preview: `assets/previews/FigureYa291PancanProgSigatureV2.jpg`; selected source: `gallery/FigureYa291.png`; types: correlation, ROC, scatter; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa291PancanProgSigatureV2
- **FigureYa294HCCdrug** — preview: `assets/previews/FigureYa294HCCdrug.jpg`; selected source: `gallery/FigureYa294.png`; types: scatter, calibration, heatmap, correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa294HCCdrug
- **FigureYa30nomogram_update** — preview: `assets/previews/FigureYa30nomogram_update.jpg`; selected source: `gallery/FigureYa30.png`; types: forest; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa30nomogram_update
- **FigureYa31lasso_update** — preview: `assets/previews/FigureYa31lasso_update.jpg`; selected source: `gallery/FigureYa31.png`; types: correlation, survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa31lasso_update
- **FigureYa33DCA_update** — preview: `assets/previews/FigureYa33DCA_update.jpg`; selected source: `gallery/FigureYa33.png`; types: survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa33DCA_update
- **FigureYa6rHRs** — preview: `assets/previews/FigureYa6rHRs.jpg`; selected source: `gallery/FigureYa6.png`; types: ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa6rHRs
- **FigureYa85timeROC** — preview: `assets/previews/FigureYa85timeROC.jpg`; selected source: `gallery/FigureYa85.png`; types: ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa85timeROC

#### 通用可视化

- **FigureYa106immunotherapy** — preview: `assets/previews/FigureYa106immunotherapy.jpg`; selected source: `gallery/FigureYa106.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa106immunotherapy
- **FigureYa124AssociationHeatmap** — preview: `assets/previews/FigureYa124AssociationHeatmap.jpg`; selected source: `gallery/FigureYa124.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa124AssociationHeatmap
- **FigureYa148SimpleDendrogram** — preview: `assets/previews/FigureYa148SimpleDendrogram.jpg`; selected source: `gallery/FigureYa148.png`; types: dendrogram; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa148SimpleDendrogram
- **FigureYa176BlandAltman** — preview: `assets/previews/FigureYa176BlandAltman.jpg`; selected source: `gallery/FigureYa176.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa176BlandAltman
- **FigureYa199crosslink** — preview: `assets/previews/FigureYa199crosslink.jpg`; selected source: `gallery/FigureYa199.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa199crosslink
- **FigureYa244PCAPlot** — preview: `assets/previews/FigureYa244PCAPlot.jpg`; selected source: `gallery/FigureYa244.png`; types: PCA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa244PCAPlot
- **FigureYa252mclust** — preview: `assets/previews/FigureYa252mclust.jpg`; selected source: `gallery/FigureYa252.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa252mclust
- **FigureYa273BAPC** — preview: `assets/previews/FigureYa273BAPC.jpg`; selected source: `gallery/FigureYa273.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa273BAPC
- **FigureYa302NTPPAM** — preview: `assets/previews/FigureYa302NTPPAM.jpg`; selected source: `gallery/FigureYa302.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa302NTPPAM
- **FigureYa38PCA** — preview: `assets/previews/FigureYa38PCA.jpg`; selected source: `gallery/FigureYa38.png`; types: PCA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa38PCA
- **FigureYa59volcanoV2** — preview: `assets/previews/FigureYa59volcanoV2.jpg`; selected source: `gallery/FigureYa59.png`; types: volcano; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa59volcanoV2
- **FigureYa63pubmedMiningV2** — preview: `assets/previews/FigureYa63pubmedMiningV2.jpg`; selected source: `gallery/FigureYa63.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa63pubmedMiningV2
- **FigureYa75bubble_volcano** — preview: `assets/previews/FigureYa75bubble_volcano.jpg`; selected source: `gallery/FigureYa75.png`; types: bubble, volcano; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa75bubble_volcano
- **FigureYa98STEMheatmapV2** — preview: `assets/previews/FigureYa98STEMheatmapV2.jpg`; selected source: `gallery/FigureYa98.png`; types: line, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa98STEMheatmapV2

#### 分布/比例/Venn/组成

- **FigureYa112Plus_venn** — preview: `assets/previews/FigureYa112Plus_venn.jpg`; selected source: `gallery/FigureYa112.png`; types: venn; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa112Plus_venn
- **FigureYa112venn** — preview: `assets/previews/FigureYa112venn.jpg`; selected source: `gallery/FigureYa112.png`; types: venn; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa112venn
- **FigureYa144DiagHeatmap** — preview: `assets/previews/FigureYa144DiagHeatmap.jpg`; selected source: `gallery/FigureYa144.png`; types: heatmap, pie; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa144DiagHeatmap
- **FigureYa237circVenn** — preview: `assets/previews/FigureYa237circVenn.jpg`; selected source: `gallery/FigureYa237.png`; types: venn; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa237circVenn
- **FigureYa248MutLandscape** — preview: `assets/previews/FigureYa248MutLandscape.jpg`; selected source: `gallery/FigureYa248.png`; types: heatmap, mutation, pie; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa248MutLandscape
- **FigureYa257armCNV** — preview: `assets/previews/FigureYa257armCNV.jpg`; selected source: `gallery/FigureYa257.png`; types: density; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa257armCNV
- **FigureYa320ClontypeHeatmap** — preview: `assets/previews/FigureYa320ClontypeHeatmap.jpg`; selected source: `gallery/FigureYa320.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa320ClontypeHeatmap
- **FigureYa77baseZoom** — preview: `assets/previews/FigureYa77baseZoom.jpg`; selected source: `gallery/FigureYa77.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa77baseZoom
- **FigureYa78gganatogram** — preview: `assets/previews/FigureYa78gganatogram.jpg`; selected source: `gallery/FigureYa78.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa78gganatogram
- **FigureYa87fish** — preview: `assets/previews/FigureYa87fish.jpg`; selected source: `gallery/FigureYa87.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa87fish
- **FigureYa8radar** — preview: `assets/previews/FigureYa8radar.jpg`; selected source: `gallery/FigureYa8.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa8radar

#### 分组比较：箱线图/小提琴/柱状图

- **FigureYa105GDSC** — preview: `assets/previews/FigureYa105GDSC.jpg`; selected source: `gallery/FigureYa105.png`; types: boxplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa105GDSC
- **FigureYa12box** — preview: `assets/previews/FigureYa12box.jpg`; selected source: `gallery/FigureYa12.png`; types: boxplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa12box
- **FigureYa173fancybar** — preview: `assets/previews/FigureYa173fancybar.jpg`; selected source: `gallery/FigureYa173.png`; types: barplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa173fancybar
- **FigureYa227boxdensity** — preview: `assets/previews/FigureYa227boxdensity.jpg`; selected source: `gallery/FigureYa227.png`; types: density, boxplot, scatter; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa227boxdensity
- **FigureYa297Rbar** — preview: `assets/previews/FigureYa297Rbar.jpg`; selected source: `gallery/FigureYa297.png`; types: correlation, barplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa297Rbar
- **FigureYa48Adonis** — preview: `assets/previews/FigureYa48Adonis.jpg`; selected source: `gallery/FigureYa48.png`; types: correlation, barplot, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa48Adonis
- **FigureYa55panCancer_violinV2** — preview: `assets/previews/FigureYa55panCancer_violinV2.jpg`; selected source: `gallery/FigureYa55.png`; types: violin; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa55panCancer_violinV2
- **FigureYa55plus_pancancer_boxplot** — preview: `assets/previews/FigureYa55plus_pancancer_boxplot.jpg`; selected source: `gallery/FigureYa55.png`; types: boxplot, violin; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa55plus_pancancer_boxplot
- **FigureYa94STEMbox_update** — preview: `assets/previews/FigureYa94STEMbox_update.jpg`; selected source: `gallery/FigureYa94.png`; types: boxplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa94STEMbox_update

### 生信/组学分析图

#### 富集/通路/GSEA/GSVA

- **FigureYa109SubtypeGSEA_update** — preview: `assets/previews/FigureYa109SubtypeGSEA_update.jpg`; selected source: `gallery/FigureYa109.png`; types: heatmap, GO, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa109SubtypeGSEA_update
- **FigureYa114ternaryCluster** — preview: `assets/previews/FigureYa114ternaryCluster.jpg`; selected source: `gallery/FigureYa114.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa114ternaryCluster
- **FigureYa118MulticlassDESeq2** — preview: `assets/previews/FigureYa118MulticlassDESeq2.jpg`; selected source: `gallery/FigureYa118.png`; types: correlation, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa118MulticlassDESeq2
- **FigureYa119Multiclasslimma** — preview: `assets/previews/FigureYa119Multiclasslimma.jpg`; selected source: `gallery/FigureYa119.png`; types: correlation, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa119Multiclasslimma
- **FigureYa11bubble** — preview: `assets/previews/FigureYa11bubble.jpg`; selected source: `gallery/FigureYa11.png`; types: heatmap, GO, bubble; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa11bubble
- **FigureYa120MulticlassedgeR** — preview: `assets/previews/FigureYa120MulticlassedgeR.jpg`; selected source: `gallery/FigureYa120.png`; types: GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa120MulticlassedgeR
- **FigureYa126CorrelationHeatmap** — preview: `assets/previews/FigureYa126CorrelationHeatmap.jpg`; selected source: `gallery/FigureYa126.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa126CorrelationHeatmap
- **FigureYa127HeatmapPie** — preview: `assets/previews/FigureYa127HeatmapPie.jpg`; selected source: `gallery/FigureYa127.png`; types: correlation, heatmap, pie; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa127HeatmapPie
- **FigureYa132alteration** — preview: `assets/previews/FigureYa132alteration.jpg`; selected source: `gallery/FigureYa132.png`; types: heatmap, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa132alteration
- **FigureYa136fgsea** — preview: `assets/previews/FigureYa136fgsea.jpg`; selected source: `gallery/FigureYa136.png`; types: GO, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa136fgsea
- **FigureYa13GSEA_Java_update** — preview: `assets/previews/FigureYa13GSEA_Java_update.jpg`; selected source: `gallery/FigureYa13.png`; types: GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa13GSEA_Java_update
- **FigureYa142circosBar** — preview: `assets/previews/FigureYa142circosBar.jpg`; selected source: `gallery/FigureYa142.png`; types: barplot, circos; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa142circosBar
- **FigureYa145target** — preview: `assets/previews/FigureYa145target.jpg`; selected source: `gallery/FigureYa145.png`; types: network; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa145target
- **FigureYa147interaction** — preview: `assets/previews/FigureYa147interaction.jpg`; selected source: `gallery/FigureYa147.png`; types: network; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa147interaction
- **FigureYa151pathifier** — preview: `assets/previews/FigureYa151pathifier.jpg`; selected source: `gallery/FigureYa151.png`; types: heatmap, GO, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa151pathifier
- **FigureYa153ccgraph** — preview: `assets/previews/FigureYa153ccgraph.jpg`; selected source: `gallery/FigureYa153.png`; types: mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa153ccgraph
- **FigureYa15WGCNA** — preview: `assets/previews/FigureYa15WGCNA.jpg`; selected source: `gallery/FigureYa15.png`; types: heatmap, GO; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa15WGCNA
- **FigureYa161stemness** — preview: `assets/previews/FigureYa161stemness.jpg`; selected source: `gallery/FigureYa161.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa161stemness
- **FigureYa168legoplot** — preview: `assets/previews/FigureYa168legoplot.jpg`; selected source: `gallery/FigureYa168.png`; types: pie, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa168legoplot
- **FigureYa170ImmuLncRNA** — preview: `assets/previews/FigureYa170ImmuLncRNA.jpg`; selected source: `gallery/FigureYa170.png`; types: line, scatter, correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa170ImmuLncRNA
- **FigureYa174squareCross** — preview: `assets/previews/FigureYa174squareCross.jpg`; selected source: `gallery/FigureYa174.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa174squareCross
- **FigureYa18oncoplot_update** — preview: `assets/previews/FigureYa18oncoplot_update.jpg`; selected source: `gallery/FigureYa18.png`; types: heatmap, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa18oncoplot_update
- **FigureYa195PanPaire** — preview: `assets/previews/FigureYa195PanPaire.jpg`; selected source: `gallery/FigureYa195.png`; types: GSEA, heatmap, boxplot, correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa195PanPaire
- **FigureYa202consensusGene** — preview: `assets/previews/FigureYa202consensusGene.jpg`; selected source: `gallery/FigureYa202.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa202consensusGene
- **FigureYa207Randomization** — preview: `assets/previews/FigureYa207Randomization.jpg`; selected source: `gallery/FigureYa207.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa207Randomization
- **FigureYa208FPI** — preview: `assets/previews/FigureYa208FPI.jpg`; selected source: `gallery/FigureYa208.png`; types: correlation, ROC, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa208FPI
- **FigureYa209batchEnrich** — preview: `assets/previews/FigureYa209batchEnrich.jpg`; selected source: `gallery/FigureYa209.png`; types: barplot, GO, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa209batchEnrich
- **FigureYa211multiCohortImmSubtype** — preview: `assets/previews/FigureYa211multiCohortImmSubtype.jpg`; selected source: `gallery/FigureYa211.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa211multiCohortImmSubtype
- **FigureYa214KEGG_hierarchyV2** — preview: `assets/previews/FigureYa214KEGG_hierarchyV2.jpg`; selected source: `gallery/FigureYa214.png`; types: GO, circos; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa214KEGG_hierarchyV2
- **FigureYa228linkCor** — preview: `assets/previews/FigureYa228linkCor.jpg`; selected source: `gallery/FigureYa228.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa228linkCor
- **FigureYa230immunelandscape** — preview: `assets/previews/FigureYa230immunelandscape.jpg`; selected source: `gallery/FigureYa230.png`; types: correlation, heatmap, GO, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa230immunelandscape
- **FigureYa253panGSEA** — preview: `assets/previews/FigureYa253panGSEA.jpg`; selected source: `gallery/FigureYa253.png`; types: correlation, GO, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa253panGSEA
- **FigureYa255TIME** — preview: `assets/previews/FigureYa255TIME.jpg`; selected source: `gallery/FigureYa255.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa255TIME
- **FigureYa259circLink** — preview: `assets/previews/FigureYa259circLink.jpg`; selected source: `gallery/FigureYa259.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa259circLink
- **FigureYa260CNV** — preview: `assets/previews/FigureYa260CNV.jpg`; selected source: `gallery/FigureYa260.png`; types: barplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa260CNV
- **FigureYa263panDiff** — preview: `assets/previews/FigureYa263panDiff.jpg`; selected source: `gallery/FigureYa263.png`; types: correlation, boxplot, GSEA, barplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa263panDiff
- **FigureYa264epiImmune** — preview: `assets/previews/FigureYa264epiImmune.jpg`; selected source: `gallery/FigureYa264.png`; types: correlation, barplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa264epiImmune
- **FigureYa265panCNV** — preview: `assets/previews/FigureYa265panCNV.jpg`; selected source: `gallery/FigureYa265.png`; types: correlation, boxplot, GSEA, barplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa265panCNV
- **FigureYa266panHeatmap** — preview: `assets/previews/FigureYa266panHeatmap.jpg`; selected source: `gallery/FigureYa266.png`; types: bubble, GSEA, heatmap, boxplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa266panHeatmap
- **FigureYa268panCNVexpr** — preview: `assets/previews/FigureYa268panCNVexpr.jpg`; selected source: `gallery/FigureYa268.png`; types: scatter, GSEA, boxplot, correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa268panCNVexpr
- **FigureYa270panMeth** — preview: `assets/previews/FigureYa270panMeth.jpg`; selected source: `gallery/FigureYa270.png`; types: correlation, boxplot, GSEA, barplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa270panMeth
- **FigureYa271panMethExpr** — preview: `assets/previews/FigureYa271panMethExpr.jpg`; selected source: `gallery/FigureYa271.png`; types: correlation, boxplot, GSEA, barplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa271panMethExpr
- **FigureYa276panSNV** — preview: `assets/previews/FigureYa276panSNV.jpg`; selected source: `gallery/FigureYa276.png`; types: heatmap, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa276panSNV
- **FigureYa279panGeneGSEA** — preview: `assets/previews/FigureYa279panGeneGSEA.jpg`; selected source: `gallery/FigureYa279.png`; types: GO, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa279panGeneGSEA
- **FigureYa280TMEofSTS** — preview: `assets/previews/FigureYa280TMEofSTS.jpg`; selected source: `gallery/FigureYa280.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa280TMEofSTS
- **FigureYa282CMAP_XSum** — preview: `assets/previews/FigureYa282CMAP_XSum.jpg`; selected source: `gallery/FigureYa282.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa282CMAP_XSum
- **FigureYa283vennyPvalue** — preview: `assets/previews/FigureYa283vennyPvalue.jpg`; selected source: `gallery/FigureYa283.png`; types: correlation, venn, barplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa283vennyPvalue
- **FigureYa287L2logV2** — preview: `assets/previews/FigureYa287L2logV2.jpg`; selected source: `gallery/FigureYa287.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa287L2logV2
- **FigureYa292HCCsubtype** — preview: `assets/previews/FigureYa292HCCsubtype.jpg`; selected source: `gallery/FigureYa292.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa292HCCsubtype
- **FigureYa293machineLearning** — preview: `assets/previews/FigureYa293machineLearning.jpg`; selected source: `gallery/FigureYa293.png`; types: violin, survival, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa293machineLearning
- **FigureYa296VIPER** — preview: `assets/previews/FigureYa296VIPER.jpg`; selected source: `gallery/FigureYa296.png`; types: correlation, heatmap, mutation, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa296VIPER
- **FigureYa300pancanCor** — preview: `assets/previews/FigureYa300pancanCor.jpg`; selected source: `gallery/FigureYa300.png`; types: correlation, ROC, scatter; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa300pancanCor
- **FigureYa303panCircos** — preview: `assets/previews/FigureYa303panCircos.jpg`; selected source: `gallery/FigureYa303.png`; types: GSEA, circos; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa303panCircos
- **FigureYa305PMAPscore** — preview: `assets/previews/FigureYa305PMAPscore.jpg`; selected source: `gallery/FigureYa305.png`; types: correlation, network, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa305PMAPscore
- **FigureYa307CNVHeatmap** — preview: `assets/previews/FigureYa307CNVHeatmap.jpg`; selected source: `gallery/FigureYa307.png`; types: forest, heatmap, pie, correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa307CNVHeatmap
- **FigureYa311PAM50Heatmap** — preview: `assets/previews/FigureYa311PAM50Heatmap.jpg`; selected source: `gallery/FigureYa311.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa311PAM50Heatmap
- **FigureYa312CellPreference** — preview: `assets/previews/FigureYa312CellPreference.jpg`; selected source: `gallery/FigureYa312.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa312CellPreference
- **FigureYa322SSEA** — preview: `assets/previews/FigureYa322SSEA.jpg`; selected source: `gallery/FigureYa322.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa322SSEA
- **FigureYa32ID_table** — preview: `no raster preview`; selected source: `none`; types: heatmap, boxplot, GO; visuals: 0 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa32ID_table
- **FigureYa39bar** — preview: `assets/previews/FigureYa39bar.jpg`; selected source: `gallery/FigureYa39.png`; types: GO; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa39bar
- **FigureYa42oncoprintV2_update** — preview: `assets/previews/FigureYa42oncoprintV2_update.jpg`; selected source: `gallery/FigureYa42.png`; types: correlation, heatmap, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa42oncoprintV2_update
- **FigureYa44profile** — preview: `assets/previews/FigureYa44profile.jpg`; selected source: `gallery/FigureYa44.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa44profile
- **FigureYa52GOplot** — preview: `assets/previews/FigureYa52GOplot.jpg`; selected source: `gallery/FigureYa52.png`; types: GO, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa52GOplot
- **FigureYa5bubbles** — preview: `assets/previews/FigureYa5bubbles.jpg`; selected source: `gallery/FigureYa5.png`; types: bubble, GO; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa5bubbles
- **FigureYa60GSEA_clusterProfilerV2** — preview: `assets/previews/FigureYa60GSEA_clusterProfilerV2.jpg`; selected source: `gallery/FigureYa60.png`; types: GO, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa60GSEA_clusterProfilerV2
- **FigureYa61GSVA** — preview: `assets/previews/FigureYa61GSVA.jpg`; selected source: `gallery/FigureYa61.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa61GSVA
- **FigureYa68friendsV2** — preview: `assets/previews/FigureYa68friendsV2.jpg`; selected source: `gallery/FigureYa68.png`; types: correlation, GO; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa68friendsV2
- **FigureYa71ssGSEA_update** — preview: `assets/previews/FigureYa71ssGSEA_update.jpg`; selected source: `gallery/FigureYa71.png`; types: GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa71ssGSEA_update
- **FigureYa80GOclustering** — preview: `assets/previews/FigureYa80GOclustering.jpg`; selected source: `gallery/FigureYa80.png`; types: GO; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa80GOclustering
- **FigureYa83enrichment** — preview: `assets/previews/FigureYa83enrichment.jpg`; selected source: `gallery/FigureYa83.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa83enrichment
- **FigureYa84roast** — preview: `assets/previews/FigureYa84roast.jpg`; selected source: `gallery/FigureYa84.png`; types: GO; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa84roast
- **FigureYa88DAVIDkappa** — preview: `assets/previews/FigureYa88DAVIDkappa.jpg`; selected source: `gallery/FigureYa88.png`; types: GO; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa88DAVIDkappa
- **FigureYa95pairwise** — preview: `assets/previews/FigureYa95pairwise.jpg`; selected source: `gallery/FigureYa95.png`; types: correlation, scatter, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa95pairwise
- **FigureYa96R2** — preview: `assets/previews/FigureYa96R2.jpg`; selected source: `gallery/FigureYa96.png`; types: heatmap, GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa96R2

#### 单细胞/空间转录组

- **FigureYa111markerGene** — preview: `assets/previews/FigureYa111markerGene.jpg`; selected source: `gallery/FigureYa111.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa111markerGene
- **FigureYa150diversityScore** — preview: `assets/previews/FigureYa150diversityScore.jpg`; selected source: `gallery/FigureYa150.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa150diversityScore
- **FigureYa160scGSVA** — preview: `assets/previews/FigureYa160scGSVA.jpg`; selected source: `gallery/FigureYa160.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa160scGSVA
- **FigureYa166scCNV** — preview: `assets/previews/FigureYa166scCNV.jpg`; selected source: `gallery/FigureYa166.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa166scCNV
- **FigureYa167TumorIndex** — preview: `assets/previews/FigureYa167TumorIndex.jpg`; selected source: `gallery/FigureYa167.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa167TumorIndex
- **FigureYa177RNAvelocity** — preview: `assets/previews/FigureYa177RNAvelocity.jpg`; selected source: `gallery/FigureYa177.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa177RNAvelocity
- **FigureYa178receptorLigand** — preview: `assets/previews/FigureYa178receptorLigand.jpg`; selected source: `gallery/FigureYa178.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa178receptorLigand
- **FigureYa185sciATAC** — preview: `assets/previews/FigureYa185sciATAC.jpg`; selected source: `gallery/FigureYa185.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa185sciATAC
- **FigureYa194pySCENIC** — preview: `assets/previews/FigureYa194pySCENIC.jpg`; selected source: `gallery/FigureYa194.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa194pySCENIC
- **FigureYa206scHeatmap** — preview: `assets/previews/FigureYa206scHeatmap.jpg`; selected source: `gallery/FigureYa206.png`; types: heatmap, GO, bubble; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa206scHeatmap
- **FigureYa222PCAgene** — preview: `assets/previews/FigureYa222PCAgene.jpg`; selected source: `gallery/FigureYa222.png`; types: PCA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa222PCAgene
- **FigureYa223scNMF** — preview: `assets/previews/FigureYa223scNMF.jpg`; selected source: `gallery/FigureYa223.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa223scNMF
- **FigureYa224scMarker** — preview: `assets/previews/FigureYa224scMarker.jpg`; selected source: `gallery/FigureYa224.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa224scMarker
- **FigureYa231scScore** — preview: `assets/previews/FigureYa231scScore.jpg`; selected source: `gallery/FigureYa231.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa231scScore
- **FigureYa232scRankHeatmap** — preview: `assets/previews/FigureYa232scRankHeatmap.jpg`; selected source: `gallery/FigureYa232.png`; types: heatmap, barplot, GO, PCA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa232scRankHeatmap
- **FigureYa235scDEG** — preview: `assets/previews/FigureYa235scDEG.jpg`; selected source: `gallery/FigureYa235.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa235scDEG
- **FigureYa239ST_PDAC** — preview: `assets/previews/FigureYa239ST_PDAC.jpg`; selected source: `gallery/FigureYa239.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa239ST_PDAC
- **FigureYa241scRNA_NMI** — preview: `assets/previews/FigureYa241scRNA_NMI.jpg`; selected source: `gallery/FigureYa241.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa241scRNA_NMI
- **FigureYa243scMarkerGroupHeatmap** — preview: `assets/previews/FigureYa243scMarkerGroupHeatmap.jpg`; selected source: `gallery/FigureYa243.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa243scMarkerGroupHeatmap
- **FigureYa254scViolin** — preview: `assets/previews/FigureYa254scViolin.jpg`; selected source: `gallery/FigureYa254.png`; types: bubble, heatmap, GO, violin; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa254scViolin
- **FigureYa267scCellChat** — preview: `assets/previews/FigureYa267scCellChat.jpg`; selected source: `gallery/FigureYa267.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa267scCellChat
- **FigureYa269scMetabolism** — preview: `assets/previews/FigureYa269scMetabolism.jpg`; selected source: `gallery/FigureYa269.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa269scMetabolism
- **FigureYa272scBulkCCCI** — preview: `assets/previews/FigureYa272scBulkCCCI.jpg`; selected source: `gallery/FigureYa272.png`; types: correlation, ROC, network, GO; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa272scBulkCCCI
- **FigureYa274MuSiCbulkProop** — preview: `assets/previews/FigureYa274MuSiCbulkProop.jpg`; selected source: `gallery/FigureYa274.png`; types: GSEA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa274MuSiCbulkProop
- **FigureYa275scAUCell** — preview: `assets/previews/FigureYa275scAUCell.jpg`; selected source: `gallery/FigureYa275.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa275scAUCell
- **FigureYa27tSNE_update** — preview: `assets/previews/FigureYa27tSNE_update.jpg`; selected source: `gallery/FigureYa27.png`; types: ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa27tSNE_update
- **FigureYa285scRNA_monocle** — preview: `assets/previews/FigureYa285scRNA_monocle.jpg`; selected source: `gallery/FigureYa285.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa285scRNA_monocle
- **FigureYa28color** — preview: `assets/previews/FigureYa28color.jpg`; selected source: `gallery/FigureYa28.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa28color
- **FigureYa290BarGraph** — preview: `assets/previews/FigureYa290BarGraph.jpg`; selected source: `gallery/FigureYa290.png`; types: barplot, ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa290BarGraph
- **FigureYa301scCoExpr** — preview: `assets/previews/FigureYa301scCoExpr.jpg`; selected source: `gallery/FigureYa301.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa301scCoExpr
- **FigureYa304MAGIC** — preview: `assets/previews/FigureYa304MAGIC.jpg`; selected source: `gallery/FigureYa304.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa304MAGIC
- **FigureYa306slingshot** — preview: `assets/previews/FigureYa306slingshot.jpg`; selected source: `gallery/FigureYa306.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa306slingshot
- **FigureYa308IHS** — preview: `assets/previews/FigureYa308IHS.jpg`; selected source: `gallery/FigureYa308.png`; types: correlation, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa308IHS
- **FigureYa310CPDBChordGramV2** — preview: `assets/previews/FigureYa310CPDBChordGramV2.jpg`; selected source: `gallery/FigureYa310.png`; types: bubble, circos; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa310CPDBChordGramV2
- **FigureYa314SingleRScore** — preview: `assets/previews/FigureYa314SingleRScore.jpg`; selected source: `gallery/FigureYa314.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa314SingleRScore
- **FigureYa315SingleRFraction** — preview: `assets/previews/FigureYa315SingleRFraction.jpg`; selected source: `gallery/FigureYa315.png`; types: correlation, boxplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa315SingleRFraction
- **FigureYa317RoeDot** — preview: `assets/previews/FigureYa317RoeDot.jpg`; selected source: `gallery/FigureYa317.png`; types: line, heatmap, GO; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa317RoeDot
- **FigureYa318GenesetDEDotplot** — preview: `assets/previews/FigureYa318GenesetDEDotplot.jpg`; selected source: `gallery/FigureYa318.png`; types: line, correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa318GenesetDEDotplot
- **FigureYa319ContribScore** — preview: `assets/previews/FigureYa319ContribScore.jpg`; selected source: `gallery/FigureYa319.png`; types: barplot; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa319ContribScore
- **FigureYa323STpathseq** — preview: `assets/previews/FigureYa323STpathseq.jpg`; selected source: `gallery/FigureYa323.png`; types: pie; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa323STpathseq
- **FigureYa40lineage** — preview: `assets/previews/FigureYa40lineage.jpg`; selected source: `gallery/FigureYa40.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa40lineage
- **FigureYa93UMAP** — preview: `assets/previews/FigureYa93UMAP.jpg`; selected source: `gallery/FigureYa93.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa93UMAP

#### 表达矩阵/差异表达/RNA-seq

- **FigureYa101PCA** — preview: `assets/previews/FigureYa101PCA.jpg`; selected source: `gallery/FigureYa101.png`; types: PCA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa101PCA
- **FigureYa10chromosomeV2_update** — preview: `assets/previews/FigureYa10chromosomeV2_update.jpg`; selected source: `gallery/FigureYa10.png`; types: chromosome, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa10chromosomeV2_update
- **FigureYa122mut2expr** — preview: `assets/previews/FigureYa122mut2expr.jpg`; selected source: `gallery/FigureYa122.png`; types: mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa122mut2expr
- **FigureYa135multiVolcano** — preview: `assets/previews/FigureYa135multiVolcano.jpg`; selected source: `gallery/FigureYa135.png`; types: volcano; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa135multiVolcano
- **FigureYa155ATAC** — preview: `assets/previews/FigureYa155ATAC.jpg`; selected source: `gallery/FigureYa155.png`; types: chromosome, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa155ATAC
- **FigureYa169sigHeatmap** — preview: `assets/previews/FigureYa169sigHeatmap.jpg`; selected source: `gallery/FigureYa169.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa169sigHeatmap
- **FigureYa172ggplot2Gviz** — preview: `assets/previews/FigureYa172ggplot2Gviz.jpg`; selected source: `gallery/FigureYa172.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa172ggplot2Gviz
- **FigureYa175quadrant** — preview: `assets/previews/FigureYa175quadrant.jpg`; selected source: `gallery/FigureYa175.png`; types: scatter; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa175quadrant
- **FigureYa210survivalScape** — preview: `assets/previews/FigureYa210survivalScape.jpg`; selected source: `gallery/FigureYa210.png`; types: correlation, survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa210survivalScape
- **FigureYa213customizeHeatmap** — preview: `assets/previews/FigureYa213customizeHeatmap.jpg`; selected source: `gallery/FigureYa213.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa213customizeHeatmap
- **FigureYa218Elasticnet** — preview: `assets/previews/FigureYa218Elasticnet.jpg`; selected source: `gallery/FigureYa218.png`; types: network; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa218Elasticnet
- **FigureYa23count2TPM** — preview: `no raster preview`; selected source: `none`; types: -; visuals: 0 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa23count2TPM
- **FigureYa240CRISPR** — preview: `assets/previews/FigureYa240CRISPR.jpg`; selected source: `gallery/FigureYa240.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa240CRISPR
- **FigureYa242corMethExpr** — preview: `assets/previews/FigureYa242corMethExpr.jpg`; selected source: `gallery/Figureya242.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa242corMethExpr
- **FigureYa245VarDecompose** — preview: `assets/previews/FigureYa245VarDecompose.jpg`; selected source: `gallery/FigureYa245.png`; types: mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa245VarDecompose
- **FigureYa281wheel** — preview: `assets/previews/FigureYa281wheel.jpg`; selected source: `gallery/FigureYa281.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa281wheel
- **FigureYa289TILSig** — preview: `assets/previews/FigureYa289TILSig.jpg`; selected source: `gallery/FigureYa289.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa289TILSig
- **FigureYa295ClassDiscovery** — preview: `assets/previews/FigureYa295ClassDiscovery.jpg`; selected source: `gallery/FigureYa295.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa295ClassDiscovery
- **FigureYa2ggtree+pheatmap+msa** — preview: `assets/previews/FigureYa2ggtree+pheatmap+msa.jpg`; selected source: `gallery/FigureYa2.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa2ggtree+pheatmap+msa
- **FigureYa34count2FPKMv2** — preview: `assets/previews/FigureYa34count2FPKMv2.jpg`; selected source: `gallery/FigureYa34.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa34count2FPKMv2
- **FigureYa3genomeView** — preview: `assets/previews/FigureYa3genomeView.jpg`; selected source: `gallery/FigureYa3.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa3genomeView
- **FigureYa53PPImodule** — preview: `assets/previews/FigureYa53PPImodule.jpg`; selected source: `gallery/FigureYa53.png`; types: network; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa53PPImodule
- **FigureYa56immune_inflitrationV3** — preview: `assets/previews/FigureYa56immune_inflitrationV3.jpg`; selected source: `gallery/FigureYa56.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa56immune_inflitrationV3
- **FigureYa58lncRNAreannotation** — preview: `no raster preview`; selected source: `none`; types: correlation; visuals: 0 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa58lncRNAreannotation
- **FigureYa59Plus_GEO2DEG** — preview: `assets/previews/FigureYa59Plus_GEO2DEG.jpg`; selected source: `gallery/FigureYa59.png`; types: volcano; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa59Plus_GEO2DEG
- **FigureYa73batchCorrelation** — preview: `assets/previews/FigureYa73batchCorrelation.jpg`; selected source: `gallery/FigureYa73.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa73batchCorrelation
- **FigureYa82IGVzoom** — preview: `assets/previews/FigureYa82IGVzoom.jpg`; selected source: `gallery/FigureYa82.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa82IGVzoom

#### 甲基化/ATAC/ChIP/表观组

- **FigureYa115cofactor** — preview: `assets/previews/FigureYa115cofactor.jpg`; selected source: `gallery/FigureYa115.png`; types: correlation, heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa115cofactor
- **FigureYa121MethCGIcluster** — preview: `assets/previews/FigureYa121MethCGIcluster.jpg`; selected source: `gallery/FigureYa121.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa121MethCGIcluster
- **FigureYa130coxSVM** — preview: `assets/previews/FigureYa130coxSVM.jpg`; selected source: `gallery/FigureYa130.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa130coxSVM
- **FigureYa140mosaicpie** — preview: `assets/previews/FigureYa140mosaicpie.jpg`; selected source: `gallery/FigureYa140.png`; types: pie, mosaic; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa140mosaicpie
- **FigureYa14circos** — preview: `assets/previews/FigureYa14circos.jpg`; selected source: `gallery/FigureYa14.png`; types: chromosome, density, circos; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa14circos
- **FigureYa157ChIPpvalue** — preview: `assets/previews/FigureYa157ChIPpvalue.jpg`; selected source: `gallery/FigureYa157.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa157ChIPpvalue
- **FigureYa162boxViolin** — preview: `assets/previews/FigureYa162boxViolin.jpg`; selected source: `gallery/FigureYa162.png`; types: density, boxplot, correlation, violin; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa162boxViolin
- **FigureYa165heatmapPvalue** — preview: `assets/previews/FigureYa165heatmapPvalue.jpg`; selected source: `gallery/FigureYa165.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa165heatmapPvalue
- **FigureYa215DNAage** — preview: `assets/previews/FigureYa215DNAage.jpg`; selected source: `gallery/FigureYa215.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa215DNAage
- **FigureYa249Regulon** — preview: `assets/previews/FigureYa249Regulon.jpg`; selected source: `gallery/FigureYa249.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa249Regulon
- **FigureYa258SNF** — preview: `assets/previews/FigureYa258SNF.jpg`; selected source: `gallery/FigureYa258.png`; types: network; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa258SNF
- **FigureYa278heatmapPoints** — preview: `assets/previews/FigureYa278heatmapPoints.jpg`; selected source: `gallery/FigureYa278.png`; types: heatmap, bubble; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa278heatmapPoints
- **FigureYa45V2** — preview: `no raster preview`; selected source: `none`; types: heatmap; visuals: 0 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa45V2
- **FigureYa57profile_1bw** — preview: `assets/previews/FigureYa57profile_1bw.jpg`; selected source: `gallery/FigureYa57.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa57profile_1bw
- **FigureYa62twoAxis** — preview: `assets/previews/FigureYa62twoAxis.jpg`; selected source: `gallery/FigureYa62.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa62twoAxis
- **FigureYa66单因素cox** — preview: `assets/previews/FigureYa66单因素cox.jpg`; selected source: `gallery/FigureYa66.png`; types: forest; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa66单因素cox
- **FigureYa67phastCons** — preview: `assets/previews/FigureYa67phastCons.jpg`; selected source: `gallery/FigureYa67.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa67phastCons
- **FigureYa72biomarker** — preview: `assets/previews/FigureYa72biomarker.jpg`; selected source: `gallery/FigureYa72.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa72biomarker

#### 突变/CNV/TMB/MAF

- **FigureYa110mutationSignature** — preview: `assets/previews/FigureYa110mutationSignature.jpg`; selected source: `gallery/FigureYa110.png`; types: heatmap, ROC, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa110mutationSignature
- **FigureYa113MutSigCV** — preview: `assets/previews/FigureYa113MutSigCV.jpg`; selected source: `gallery/FigureYa113.png`; types: mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa113MutSigCV
- **FigureYa139TMB_titv** — preview: `assets/previews/FigureYa139TMB_titv.jpg`; selected source: `gallery/FigureYa139.png`; types: mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa139TMB_titv
- **FigureYa158MutationPattern** — preview: `assets/previews/FigureYa158MutationPattern.jpg`; selected source: `gallery/FigureYa158.png`; types: ROC, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa158MutationPattern
- **FigureYa188CNVload** — preview: `assets/previews/FigureYa188CNVload.jpg`; selected source: `gallery/FigureYa188.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa188CNVload
- **FigureYa198SignatureCombinationV2** — preview: `assets/previews/FigureYa198SignatureCombinationV2.jpg`; selected source: `gallery/FigureYa198.png`; types: forest, survival, mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa198SignatureCombinationV2
- **FigureYa19Lollipop** — preview: `assets/previews/FigureYa19Lollipop.jpg`; selected source: `gallery/FigureYa19.png`; types: mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa19Lollipop
- **FigureYa205immunophenoscore_update** — preview: `assets/previews/FigureYa205immunophenoscore_update.jpg`; selected source: `gallery/FigureYa205.png`; types: correlation, scatter; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa205immunophenoscore_update
- **FigureYa256panelLink** — preview: `assets/previews/FigureYa256panelLink.jpg`; selected source: `gallery/FigureYa256.png`; types: mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa256panelLink
- **FigureYa25Sankey_update** — preview: `assets/previews/FigureYa25Sankey_update.jpg`; selected source: `gallery/FigureYa25.png`; types: mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa25Sankey_update
- **FigureYa261circGene** — preview: `assets/previews/FigureYa261circGene.jpg`; selected source: `gallery/FigureYa261.png`; types: chromosome, circos; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa261circGene
- **FigureYa262GDC** — preview: `assets/previews/FigureYa262GDC.jpg`; selected source: `gallery/FigureYa262.png`; types: mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa262GDC
- **FigureYa277Immunomodulator** — preview: `assets/previews/FigureYa277Immunomodulator.jpg`; selected source: `gallery/FigureYa277.png`; types: correlation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa277Immunomodulator
- **FigureYa74OmicCircos** — preview: `assets/previews/FigureYa74OmicCircos.jpg`; selected source: `gallery/FigureYa74.png`; types: mutation, circos; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa74OmicCircos
- **FigureYa79CNV** — preview: `assets/previews/FigureYa79CNV.jpg`; selected source: `gallery/FigureYa79.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa79CNV
- **FigureYa86SNPmotif** — preview: `assets/previews/FigureYa86SNPmotif.jpg`; selected source: `gallery/FigureYa86.png`; types: mutation; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa86SNPmotif

#### 基因组/染色体/Circos

- **FigureYa128Prognostic** — preview: `assets/previews/FigureYa128Prognostic.jpg`; selected source: `gallery/FigureYa128.png`; types: correlation, ROC; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa128Prognostic
- **FigureYa164PCA3D** — preview: `assets/previews/FigureYa164PCA3D.jpg`; selected source: `gallery/FigureYa164.png`; types: PCA; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa164PCA3D
- **FigureYa180FGAplotV2** — preview: `assets/previews/FigureYa180FGAplotV2.jpg`; selected source: `gallery/FigureYa180.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa180FGAplotV2
- **FigureYa182RFSurvV2** — preview: `assets/previews/FigureYa182RFSurvV2.jpg`; selected source: `gallery/FigureYa182.png`; types: forest, survival; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa182RFSurvV2
- **FigureYa217RMR** — preview: `assets/previews/FigureYa217RMR.jpg`; selected source: `gallery/FigureYa217.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa217RMR
- **FigureYa236circGroup** — preview: `assets/previews/FigureYa236circGroup.jpg`; selected source: `gallery/FigureYa236.png`; types: heatmap, circos; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa236circGroup
- **FigureYa26circos_R** — preview: `assets/previews/FigureYa26circos_R.jpg`; selected source: `gallery/FigureYa26.png`; types: correlation, circos; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa26circos_R
- **FigureYa313CircularPlot** — preview: `assets/previews/FigureYa313CircularPlot.jpg`; selected source: `gallery/FigureYa313.png`; types: scatter, circos; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa313CircularPlot
- **FigureYa43ManhattanV2** — preview: `assets/previews/FigureYa43ManhattanV2.jpg`; selected source: `gallery/FigureYa43.png`; types: chromosome; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa43ManhattanV2
- **FigureYa69cancerSubtype** — preview: `assets/previews/FigureYa69cancerSubtype.jpg`; selected source: `gallery/FigureYa69.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa69cancerSubtype
- **FigureYa89ggplotCirco** — preview: `assets/previews/FigureYa89ggplotCirco.jpg`; selected source: `gallery/FigureYa89.png`; types: heatmap, circos; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa89ggplotCirco

#### 多组学/网络/免疫浸润

- **FigureYa16fitting** — preview: `assets/previews/FigureYa16fitting.jpg`; selected source: `gallery/FigureYa16.png`; types: -; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa16fitting
- **FigureYa17WGCNA_heatmap** — preview: `assets/previews/FigureYa17WGCNA_heatmap.jpg`; selected source: `gallery/FigureYa17.png`; types: heatmap; visuals: 1 raster / 0 pdf; GitHub: https://github.com/ying-ge/FigureYa/tree/main/FigureYa17WGCNA_heatmap
