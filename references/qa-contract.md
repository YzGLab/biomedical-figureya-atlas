# QA Contract

Use this before final delivery of code, candidate recommendations, or a publication-style figure workflow.

## Retrieval QA

| Check | Pass Condition |
|---|---|
| Domain | Candidate is routed to `biostatistics_general` or `bioinformatics_omics` correctly |
| Plot family | Selected FigureYa ID matches the requested chart type |
| Input shape | Expected columns, matrix, or object type is explicit |
| Local source | Local code path or GitHub fallback is identified |
| Visual evidence | Preview/montage was opened when style matching mattered |
| Candidate count | Final recommendation is narrowed to 1-3 tools |

## Code QA

| Check | Pass Condition |
|---|---|
| Dependencies | Required packages are listed with install hints |
| Data preparation | User data schema and transformation steps are clear |
| Demo cleanup | Demo paths, downloads, unrelated analysis, and private paths are removed |
| Statistics | Test, cutoff, `n`, grouping, and adjustment assumptions are stated |
| Colors | Palette matches data type and avoids misleading mappings |
| Export | Vector and preview/submission outputs are included when publication quality is requested |
| Reproducibility | Random seeds are set when stochastic steps appear |

## Safety QA

- Do not execute unreviewed install scripts or network/download code from FigureYa examples.
- Do not upload private data to external services.
- Do not disclose private absolute paths in final answers.
- Check upstream package/data licenses and citations before manuscript or public reuse.
- Acknowledge FigureYa when patterns, code structure, or images are used.

## Minimal Final Answer Contents

For a candidate-selection answer:

```text
Selected FigureYa ID(s):
Why:
Expected input:
Main packages:
Preview/code source:
Next adaptation step:
```

For a code-generation answer:

```text
What the script expects:
What it produces:
How to run:
Packages:
Attribution:
```
