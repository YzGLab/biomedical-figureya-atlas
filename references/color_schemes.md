# FigureYa 科研配色参考

## 核心原则
- 优先使用 **Nature/Cell/Science** 等顶刊常见配色
- 色盲友好：避免红绿对比，推荐蓝橙、蓝黄、紫黄等组合
- 数据映射清晰：连续数据用渐变，分类数据用离散色

## 常用R包配色

### ggplot2 默认
- `scale_color_discrete()` / `scale_fill_discrete()` — 分类数据默认配色
- `scale_color_brewer(palette = "Set1")` — 高对比度分类色
- `scale_color_brewer(palette = "Dark2")` — 色盲友好分类色
- `scale_color_viridis_c()` / `scale_fill_viridis_c()` — 连续数据，色盲友好
- `scale_color_distiller(palette = "RdBu")` — 双极连续数据（红蓝）

### RColorBrewer 推荐
- **分类 (Qualitative)**: Set1, Set2, Set3, Dark2, Paired
- **顺序 (Sequential)**: Blues, Greens, YlOrRd, PuBuGn
- **发散 (Diverging)**: RdBu, RdYlBu, PuOr, BrBG

### 自定义学术配色
```r
# Nature风格柔和配色
nature_palette <- c("#2874A6", "#E74C3C", "#27AE60", "#F39C12", "#8E44AD", "#16A085")

# Cell风格高饱和度配色
cell_palette <- c("#0072B2", "#D55E00", "#009E73", "#CC79A7", "#F0E442", "#56B4E9")

# 色盲友好配色 (Okabe-Ito)
okabe_ito <- c("#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000")
```

## 按图类型推荐

| 图类型 | 推荐配色方案 |
|--------|-------------|
| 热图 (Heatmap) | pheatmap默认, viridis, RdBu/RdYlBu发散色 |
| 箱线图/小提琴图 | 分组用Set1/Dark2, 对照vs实验用蓝/红或蓝/橙 |
| 散点图 (Scatter) | 按分组着色用Set2, 连续变量用viridis |
| 火山图 (Volcano) | 经典红(上调)/蓝(下调)/灰(不显著) |
| ROC曲线 | 多条曲线用rainbow或Dark2 |
| 生存曲线 (KM) | 不同组用对比鲜明的颜色 |
| GSEA富集图 | NES正值红/负值蓝 |
| 气泡图 (Bubble) | 大小映射p值, 颜色映射通路类型 |
| 饼图/马赛克图 | 避免过多颜色, 不超过6-8种 |
| 森林图 (Forest) | 整体效应深色, 亚组浅色 |

## 复杂热图配色 (ComplexHeatmap)
```r
# 表达矩阵标准化后的热图
colorRamp2(c(-2, 0, 2), c("#2166AC", "white", "#B2182B"))

# CNV热图
colorRamp2(c(-2, -1, 0, 1, 2), c("#2166AC", "#92C5DE", "white", "#F4A582", "#B2182B"))

# 相关性热图
colorRamp2(c(-1, 0, 1), c("#2166AC", "white", "#B2182B"))
```

## 单细胞配色
```r
# Seurat默认配色丰富但可能过于鲜艳
# 推荐自定义
colors <- c("#E64B35", "#4DBBD5", "#00A087", "#3C5488", "#F39B7F", "#8491B4",
            "#91D1C2", "#DC0000", "#7E6148", "#B09C85", "#3B4992", "#EE0000")
```
