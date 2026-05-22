# Visual Matching

Use this when visual style is part of the task: paper-figure recreation, reference-image matching, "which FigureYa looks closest", layout imitation, or journal-style polishing.

## Visual Authority

The usable visual references are:

- `assets/previews/FigureYaXXX.jpg` for one normalized preview per FigureYa module.
- `assets/montages/montage_*.jpg` for broad browsing by plot family.
- `references/visual_catalog.json` for preview paths, exclusion status, source gallery image, and web report links.

Do not infer style from a file name or catalog entry alone. Open the preview or montage before using visual style as evidence.

## Exclusion Rule

Skip entries where:

- `visual_excluded` is `true`;
- `preview_status` is `manual-excluded`;
- preview is text/table/directory-like rather than a reusable plot style.

Those modules may still be used for code lookup, but not for visual matching.

## What To Compare

Compare concrete visual features:

- panel count and layout;
- dominant plot geometry;
- axis orientation and scale;
- legend placement;
- direct labels and annotations;
- statistical marks and p-value display;
- color mapping and palette saturation;
- use of facets, side annotations, or tracks;
- information density and whitespace;
- whether the plot is single-panel, composite, or atlas-like.

## Matching Procedure

1. Retrieve 5-10 visual candidates by plot type from `visual_catalog.json` or `visual_index.md`.
2. Open the relevant montage when the plot family has many candidates.
3. Open the top preview images directly if the user provided a reference style.
4. Reduce to 1-3 final FigureYa IDs.
5. Read the selected local R/Rmd code only after the visual shortlist is set.

## User-Facing Summary

When reporting a visual match, say:

- which FigureYa ID was selected;
- what visual features match;
- which features need adaptation;
- whether the match is analytical, visual, or both.

Avoid exposing private local absolute paths. Relative repository paths are acceptable in development answers.
