# R Code Adaptation

Use this after selecting one or more FigureYa modules. Adapt the pattern into clean, runnable R code for the user's data.

## Adaptation Rules

- Read the selected `.Rmd`, `.rmd`, and helper `.R` files under `references/code/FigureYaXXX/`.
- Identify the core plotting code, not the demo data setup.
- Remove hardcoded local paths, downloads, working-directory changes, and unrelated analyses.
- Do not execute `install_dependencies.R` automatically.
- Preserve statistical meaning: tests, cutoffs, grouping, `n`, confidence intervals, and multiple-comparison logic.
- Prefer a smaller dependency set when several packages do the same job.
- Write code in a form the user can paste into an R script.

## Standard Script Shape

```r
# 1. Packages
# install.packages("...")
library(ggplot2)

# 2. Input schema
# Expected columns:
# - ...
input_file <- "your_data.csv"
df <- read.csv(input_file, check.names = FALSE)

# 3. Data preparation
# ...

# 4. Plot
p <- ggplot(df, aes(...)) +
  ...

# 5. Export
ggsave("figure.pdf", p, width = 183, height = 120, units = "mm", device = cairo_pdf)
ggsave("figure.png", p, width = 183, height = 120, units = "mm", dpi = 600)
```

## Publication Export Helper

Use vector output for editable manuscripts and raster output for preview/submission systems.

```r
save_pub_r <- function(plot, filename, width_mm = 183, height_mm = 120, dpi = 600) {
  w <- width_mm / 25.4
  h <- height_mm / 25.4

  if (requireNamespace("svglite", quietly = TRUE)) {
    svglite::svglite(paste0(filename, ".svg"), width = w, height = h)
    print(plot)
    grDevices::dev.off()
  }

  grDevices::cairo_pdf(paste0(filename, ".pdf"), width = w, height = h, family = "Arial")
  print(plot)
  grDevices::dev.off()

  if (requireNamespace("ragg", quietly = TRUE)) {
    ragg::agg_png(paste0(filename, ".png"), width = w, height = h, units = "in", res = dpi)
    print(plot)
    grDevices::dev.off()
  } else {
    ggsave(paste0(filename, ".png"), plot, width = w, height = h, dpi = dpi)
  }
}
```

## Package Map

| Need | Preferred packages |
|---|---|
| General ggplot figures | `ggplot2`, `dplyr`, `tidyr`, `ggrepel` |
| Statistical annotations | `ggpubr`, `rstatix`, or explicit test code |
| Multi-panel layout | `patchwork`, `cowplot` only when alignment requires it |
| Heatmaps | `ComplexHeatmap`, `circlize`, `pheatmap` for simpler cases |
| Survival | `survival`, `survminer`, `forestplot` |
| ROC / calibration | `pROC`, `timeROC`, `rms`, `ggplot2` |
| Enrichment | `clusterProfiler`, `enrichplot`, `fgsea`, `GOplot` |
| Mutation | `maftools`, `ComplexHeatmap`, `circlize` |
| Single-cell | `Seurat`, `SingleCellExperiment`, `ggplot2` |
| Genome/circular | `circlize`, `karyoploteR`, `ggtree` |

## FigureYa Attribution

If the final code substantially follows a FigureYa module, include a short note:

```text
Pattern adapted from the public FigureYa project: https://github.com/ying-ge/FigureYa
```

Do not claim the generated script is the original FigureYa code. It is an adapted plotting solution.
