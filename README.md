# Biomedical FigureYa Atlas

Biomedical FigureYa Atlas is a Claude/Codex skill for biomedical scientific figure generation, visual reference matching, and R plotting workflow reuse.

It extends the public [FigureYa](https://github.com/ying-ge/FigureYa) project into a curated figure atlas for AI-assisted research plotting. The skill combines a searchable catalog, visual preview gallery, categorized biostatistics and bioinformatics indexes, and lightweight R/Rmd reference code.

## What This Skill Provides

- A biomedical scientific figure gallery and visual catalog
- 306 manually reviewed preview images and 45 montage pages
- 312 FigureYa-derived plotting tool records
- Separate indexes for general biostatistics and bioinformatics/omics figures
- Reference R Markdown and helper R scripts for adapting plot workflows
- GitHub fallback links for each FigureYa module
- Color palette guidance for publication-style figures

## Use Cases

Use this skill when you need to:

- Create R code for biomedical or scientific plots
- Match a manuscript figure style to a reference implementation
- Choose between similar plot types such as heatmaps, ROC curves, survival curves, volcano plots, enrichment plots, single-cell figures, mutation/CNV plots, and multi-omics figures
- Convert FigureYa-style examples into reusable plotting templates
- Find paper-quality color and layout patterns for biomedical visualization

## Structure

```text
biomedical-figureya-atlas/
├── SKILL.md
├── assets/
│   ├── previews/
│   └── montages/
├── references/
│   ├── figureya_catalog.json
│   ├── figureya_index.md
│   ├── index_biostatistics.md
│   ├── index_bioinformatics.md
│   ├── visual_catalog.json
│   ├── visual_index.md
│   ├── visual_exclusions.json
│   ├── color_schemes.md
│   └── code/
└── scripts/
```

## How AI Agents Should Use It

1. Read `SKILL.md` for the workflow.
2. Start with `references/index_biostatistics.md` for general biological or medical statistics figures.
3. Start with `references/index_bioinformatics.md` for omics, single-cell, mutation, CNV, enrichment, methylation, or genome figures.
4. Use `references/visual_index.md` and `assets/montages/` when visual style matters.
5. Use `references/visual_catalog.json` for machine filtering and GitHub fallback links.
6. Read the selected module under `references/code/FigureYaXXX/` before adapting R code.

## Maintenance

The `scripts/` directory contains utilities to rebuild the atlas from a local FigureYa checkout:

- `scan_figureya.py` rebuilds the machine-readable catalog.
- `generate_index.py` rebuilds Markdown indexes.
- `create_montages.py` syncs preview images from the FigureYa web gallery and rebuilds montage pages.
- `sync_reference_code.py` copies lightweight `.Rmd`, `.rmd`, and `.R` source files without copying large HTML reports or data files.

HTML reports are intentionally not bundled because they are large generated outputs. Use `web_reports` in `references/visual_catalog.json` or the upstream GitHub links when full reports are needed.

## Attribution

This skill is derived from the public FigureYa repository:

https://github.com/ying-ge/FigureYa

Please acknowledge FigureYa when using its plot patterns, code structure, gallery images, or examples. Follow the citation and license information from the upstream FigureYa project.

## License

This repository is released under [CC BY-NC-SA 4.0](LICENSE) to align with the upstream FigureYa licensing terms. This means attribution is required, commercial use is restricted, and derivative works should be shared under the same license.

Third-party packages, libraries, datasets, and external tools referenced by the bundled R/Rmd examples retain their own licenses and citation requirements.

## Safety

Treat bundled R/Rmd files as reference implementations. Review code before execution, especially install scripts, downloaded dependencies, network calls, and file-system operations. Do not upload private research data to external services. Check package licenses, data-source requirements, and upstream citation requirements before reusing code in a manuscript or public project.
