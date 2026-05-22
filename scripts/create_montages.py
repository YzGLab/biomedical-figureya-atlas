#!/usr/bin/env python3
"""Build a visual catalog, per-tool previews, and plot-type montages."""
from __future__ import annotations

import json
import math
import os
import re
import shutil
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont, ImageOps

try:
    import pypdfium2 as pdfium
except Exception:  # pragma: no cover - optional dependency
    pdfium = None

RASTER_EXTENSIONS = {".png", ".jpg", ".jpeg"}
VECTOR_EXTENSIONS = {".svg", ".pdf"}
VISUAL_EXTENSIONS = RASTER_EXTENSIONS | VECTOR_EXTENSIONS
FIGUREYA_REPO_URL = "https://github.com/ying-ge/FigureYa"

PREVIEW_SIZE = (900, 640)
MONTAGE_THUMB_SIZE = (400, 300)
MARGIN = 12
LABEL_HEIGHT = 38
MONTAGE_COLS = 4
MONTAGE_PAGE_SIZE = 16

PRIMARY_LABELS = {
    "biostatistics_general": "常规生物学/医学统计图",
    "bioinformatics_omics": "生信/组学分析图",
}

SECONDARY_LABELS = {
    "group_comparison": "分组比较：箱线图/小提琴/柱状图",
    "correlation_regression": "相关/回归/散点",
    "survival_prognosis": "生存/预后/Cox",
    "diagnostic_model": "ROC/AUC/校准/诊断模型",
    "distribution_summary": "分布/比例/Venn/组成",
    "general_visualization": "通用可视化",
    "single_cell": "单细胞/空间转录组",
    "enrichment_pathway": "富集/通路/GSEA/GSVA",
    "expression_deg": "表达矩阵/差异表达/RNA-seq",
    "mutation_cnv": "突变/CNV/TMB/MAF",
    "methylation_epigenomics": "甲基化/ATAC/ChIP/表观组",
    "genome_circos": "基因组/染色体/Circos",
    "multiomics_network": "多组学/网络/免疫浸润",
}

PREFERRED_NAME_KEYWORDS = (
    "example",
    "figureya",
    "output",
    "plot",
    "heatmap",
    "roc",
    "pca",
    "umap",
    "tsne",
    "box",
    "violin",
    "volcano",
    "bubble",
    "survival",
    "gsea",
    "forest",
    "circos",
    "cnv",
    "mutation",
    "bar",
    "scatter",
)

LOW_VALUE_NAME_KEYWORDS = (
    "method",
    "workflow",
    "pipeline",
    "download",
    "install",
    "input",
    "readme",
    "explain",
    "content",
    "preprocessing",
    "hoptop",
    "screenshot",
    "manual",
    "tutorial",
    "github",
    "browser",
    "files",
    "folder",
    "directory",
)

RESULT_DIR_NAMES = {
    "result",
    "results",
    "output",
    "outputs",
    "figure",
    "figures",
    "plot",
    "plots",
    "image",
    "images",
    "img",
}

SKIP_DIR_NAMES = {
    ".git",
    "__macosx",
    "packages",
    "package",
    "data",
    "script",
    "scripts",
    "node_modules",
}

OUTPUT_FUNCTION_PATTERN = re.compile(
    r"\b(?:pdf|png|jpeg|jpg|tiff|bmp|svg|cairo_pdf|ggsave)\s*\(",
    flags=re.IGNORECASE,
)


def relpath(path: Path, base: Path) -> str:
    """Return a stable slash-separated relative path."""
    return path.resolve().relative_to(base.resolve()).as_posix()


def figure_number(tool_id: str) -> str | None:
    match = re.match(r"FigureYa(\d+)", tool_id, flags=re.IGNORECASE)
    return match.group(1) if match else None


def gallery_image_for_tool(tool_id: str, gallery_dir: Path | None) -> Path | None:
    if gallery_dir is None:
        return None
    number = figure_number(tool_id)
    if number is None:
        return None
    candidates = [
        gallery_dir / f"FigureYa{number}.png",
        gallery_dir / f"Figureya{number}.png",
        gallery_dir / f"figureya{number}.png",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def load_chapter_map(source_root: Path) -> dict[str, list[dict[str, object]]]:
    chapters_path = source_root / "chapters.json"
    if not chapters_path.exists():
        return {}
    try:
        chapters = json.loads(chapters_path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    by_folder: dict[str, list[dict[str, object]]] = {}
    for item in chapters:
        folder = str(item.get("folder", ""))
        if folder:
            by_folder.setdefault(folder, []).append(item)
    return by_folder


def clean_directory(path: Path) -> None:
    """Remove generated files under a known output directory."""
    path = path.resolve()
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def load_visual_exclusions(skill_root: Path) -> set[str]:
    """Load tool IDs whose previews should stay excluded from visual matching."""
    path = skill_root / "references" / "visual_exclusions.json"
    if not path.exists():
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return {str(item) for item in data}
    return {str(item) for item in data.get("excluded_preview_ids", [])}


def load_font(size: int) -> ImageFont.ImageFont:
    for font_name in ("arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(font_name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def label_primary(value: str) -> str:
    return PRIMARY_LABELS.get(value, value or "未分类")


def label_secondary(value: str) -> str:
    return SECONDARY_LABELS.get(value, value or "未分类")


def discover_visual_files(tool_dir: Path, output_names: set[str] | None = None) -> list[Path]:
    output_names = output_names or set()
    files: list[Path] = []
    if not tool_dir.exists():
        return []
    for child in tool_dir.rglob("*"):
        if not child.is_file() or child.suffix.lower() not in VISUAL_EXTENSIONS:
            continue
        rel_parts = [part.lower() for part in child.relative_to(tool_dir).parts[:-1]]
        if any(part in SKIP_DIR_NAMES for part in rel_parts):
            continue
        is_top_level = len(rel_parts) == 0
        is_result_dir = any(part in RESULT_DIR_NAMES for part in rel_parts)
        is_declared_output = child.name.lower() in output_names
        if is_top_level or is_result_dir or is_declared_output:
            files.append(child)
    return sorted(files, key=lambda p: (rank_visual_file(p), natural_key(p.name)))


def natural_key(text: str) -> list[object]:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def image_dimensions(path: Path) -> tuple[int | None, int | None]:
    if path.suffix.lower() not in RASTER_EXTENSIONS:
        return None, None
    try:
        with Image.open(path) as img:
            return img.size
    except Exception:
        return None, None


def classify_visual(path: Path) -> str:
    stem = path.stem.lower()
    if is_low_value_visual(path):
        return "method"
    if "example" in stem:
        return "example"
    if path.suffix.lower() == ".pdf":
        return "pdf-output"
    if path.suffix.lower() == ".svg":
        return "svg-output"
    return "raster-output"


def is_low_value_visual(path: Path) -> bool:
    stem = path.stem.lower()
    return any(keyword in stem for keyword in LOW_VALUE_NAME_KEYWORDS)


def normalized_name(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def is_same_name_overview(path: Path, tool_id: str) -> bool:
    """Treat folder-name screenshots as documentation previews, not plots."""
    return normalized_name(path.stem) == normalized_name(tool_id)


def extract_declared_outputs(tool_dir: Path) -> set[str]:
    """Find output image/PDF filenames explicitly written by the Rmd code."""
    outputs: set[str] = set()
    for rmd_path in sorted(tool_dir.glob("*.Rmd")):
        try:
            text = rmd_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        lines = text.splitlines()
        for index, line in enumerate(lines):
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "include_graphics" in stripped:
                continue
            if not OUTPUT_FUNCTION_PATTERN.search(stripped):
                continue
            window = "\n".join(lines[index : min(index + 5, len(lines))])
            for match in re.finditer(r"""["']([^"']+\.(?:pdf|png|jpe?g|svg))["']""", window, flags=re.IGNORECASE):
                outputs.add(Path(match.group(1)).name.lower())
    return outputs


def rank_visual_file(path: Path) -> tuple[int, int, str]:
    """Lower rank is better."""
    stem = path.stem.lower()
    score = 1000
    if path.suffix.lower() in RASTER_EXTENSIONS:
        score -= 120
    if path.suffix.lower() == ".pdf":
        score -= 40
    for idx, keyword in enumerate(PREFERRED_NAME_KEYWORDS):
        if keyword in stem:
            score -= 90 - min(idx, 40)
    for keyword in LOW_VALUE_NAME_KEYWORDS:
        if keyword in stem:
            score += 160
    if stem == "example":
        score -= 120
    try:
        size_score = min(int(math.log(max(path.stat().st_size, 1), 2)), 40)
    except OSError:
        size_score = 0
    return score, -size_score, path.name.lower()


def result_candidate_score(path: Path, tool_id: str, output_names: set[str], plot_types: Iterable[str]) -> tuple[int, int, str]:
    """Lower rank is better for final result previews."""
    name_lower = path.name.lower()
    stem = path.stem.lower()
    score = 1000

    if name_lower in output_names:
        score -= 500
    if path.suffix.lower() == ".pdf":
        score -= 110
    elif path.suffix.lower() in RASTER_EXTENSIONS:
        score -= 70

    for plot_type in plot_types:
        if str(plot_type).lower() in stem:
            score -= 120

    for keyword in PREFERRED_NAME_KEYWORDS:
        if keyword in stem:
            score -= 20

    if "example" in stem:
        score += 35
    if is_low_value_visual(path):
        score += 1000
    if is_same_name_overview(path, tool_id) and name_lower not in output_names:
        score += 1000

    try:
        size_score = min(int(math.log(max(path.stat().st_size, 1), 2)), 40)
    except OSError:
        size_score = 0
    return score, -size_score, name_lower


def visual_record(path: Path, source_root: Path) -> dict[str, object]:
    width, height = image_dimensions(path)
    return {
        "path": relpath(path, source_root),
        "name": path.name,
        "ext": path.suffix.lower().lstrip("."),
        "kind": classify_visual(path),
        "size_bytes": path.stat().st_size,
        "width": width,
        "height": height,
        "rank": rank_visual_file(path)[0],
    }


def gallery_visual_record(path: Path, source_root: Path) -> dict[str, object]:
    width, height = image_dimensions(path)
    return {
        "path": relpath(path, source_root),
        "name": path.name,
        "ext": path.suffix.lower().lstrip("."),
        "kind": "gallery-preview",
        "size_bytes": path.stat().st_size,
        "width": width,
        "height": height,
        "rank": 0,
    }


def select_preview_source(tool_id: str, paths: Iterable[Path], output_names: set[str], plot_types: Iterable[str]) -> Path | None:
    files = list(paths)
    renderable = [p for p in files if p.suffix.lower() in RASTER_EXTENSIONS or (p.suffix.lower() == ".pdf" and pdfium is not None)]

    declared = [
        p for p in renderable
        if p.name.lower() in output_names and not is_low_value_visual(p)
    ]
    if declared:
        return sorted(declared, key=lambda p: result_candidate_score(p, tool_id, output_names, plot_types))[0]

    fallback = [
        p for p in renderable
        if not is_low_value_visual(p)
        and not is_same_name_overview(p, tool_id)
        and not p.stem.lower().startswith(("nature", "science", "cell"))
    ]
    if fallback:
        return sorted(fallback, key=lambda p: result_candidate_score(p, tool_id, output_names, plot_types))[0]

    # Do not use method/workflow/readme/browser screenshots as a visual preview.
    # They remain searchable in visual_catalog.json but are excluded from montages.
    return None


def render_pdf_first_page(source: Path) -> Image.Image:
    if pdfium is None:
        raise RuntimeError("pypdfium2 is not available")
    pdf = pdfium.PdfDocument(str(source))
    try:
        page = pdf[0]
        try:
            bitmap = page.render(scale=2.0)
            image = bitmap.to_pil()
            return image.convert("RGB")
        finally:
            close = getattr(page, "close", None)
            if close:
                close()
    finally:
        close = getattr(pdf, "close", None)
        if close:
            close()


def make_letterboxed_image(source: Path, size: tuple[int, int], label: str | None = None) -> Image.Image:
    canvas = Image.new("RGB", size, "white")
    try:
        if source.suffix.lower() == ".pdf":
            img = render_pdf_first_page(source)
        else:
            img = Image.open(source)
        with img:
            img = ImageOps.exif_transpose(img)
            if img.mode in ("RGBA", "P", "LA"):
                img = img.convert("RGB")
            img = trim_whitespace(img)
            contained = ImageOps.contain(img, size, Image.LANCZOS)
            x = (size[0] - contained.width) // 2
            y = (size[1] - contained.height) // 2
            canvas.paste(contained, (x, y))
    except Exception:
        draw_placeholder(canvas, label or source.name, "image failed to open")
    return canvas


def trim_whitespace(img: Image.Image, threshold: int = 246, padding: int = 14) -> Image.Image:
    """Crop large near-white borders while preserving labels and legends."""
    rgb = img.convert("RGB")
    gray = rgb.convert("L")
    # Pixels darker than the threshold are treated as content. Most FigureYa
    # outputs use white backgrounds, so this removes exported page margins.
    mask = gray.point(lambda value: 255 if value < threshold else 0, mode="1")
    bbox = mask.getbbox()
    if not bbox:
        return rgb

    left, top, right, bottom = bbox
    left = max(left - padding, 0)
    top = max(top - padding, 0)
    right = min(right + padding, rgb.width)
    bottom = min(bottom + padding, rgb.height)

    cropped_area = (right - left) * (bottom - top)
    full_area = rgb.width * rgb.height
    if cropped_area < full_area * 0.01:
        return rgb
    return rgb.crop((left, top, right, bottom))


def draw_placeholder(canvas: Image.Image, title: str, subtitle: str) -> None:
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(24)
    subtitle_font = load_font(16)
    w, h = canvas.size
    draw.rectangle((0, 0, w - 1, h - 1), outline=(210, 210, 210), width=2)
    draw.text((24, h // 2 - 30), title[:54], fill=(30, 30, 30), font=title_font)
    draw.text((24, h // 2 + 8), subtitle[:76], fill=(90, 90, 90), font=subtitle_font)


def write_tool_preview(tool_id: str, source_path: Path | None, output_dir: Path) -> str | None:
    if source_path is None:
        return None
    preview = make_letterboxed_image(source_path, PREVIEW_SIZE, tool_id)
    out_path = output_dir / f"{tool_id}.jpg"
    preview.save(out_path, quality=88, optimize=True)
    return out_path.name


def build_visual_catalog(
    catalog: list[dict[str, object]],
    source_root: Path,
    preview_dir: Path,
    skill_root: Path,
    gallery_dir: Path | None = None,
    excluded_preview_ids: set[str] | None = None,
) -> list[dict[str, object]]:
    visual_catalog: list[dict[str, object]] = []
    chapter_map = load_chapter_map(source_root)
    excluded_preview_ids = excluded_preview_ids or set()
    for entry in catalog:
        tool_id = str(entry["id"])
        tool_dir = source_root / tool_id
        is_excluded = tool_id in excluded_preview_ids
        gallery_source = None if is_excluded else gallery_image_for_tool(tool_id, gallery_dir)
        output_names = extract_declared_outputs(tool_dir) if gallery_source is None and not is_excluded else set()
        visual_paths = discover_visual_files(tool_dir, output_names) if gallery_source is None and not is_excluded else []
        selected_source = None if is_excluded else gallery_source or select_preview_source(tool_id, visual_paths, output_names, entry.get("plot_types", []))
        preview_name = None if is_excluded else write_tool_preview(tool_id, selected_source, preview_dir)
        records = [] if is_excluded else ([gallery_visual_record(gallery_source, source_root)] if gallery_source else [visual_record(path, source_root) for path in visual_paths])
        selected_name = selected_source.name.lower() if selected_source else None
        chapter_records = chapter_map.get(tool_id, [])
        visual_catalog.append(
            {
                "id": tool_id,
                "title": entry.get("title", tool_id),
                "plot_types": entry.get("plot_types", []),
                "primary_category": entry.get("primary_category", "biostatistics_general"),
                "secondary_category": entry.get("secondary_category", "general_visualization"),
                "analysis_tags": entry.get("analysis_tags", []),
                "description": entry.get("description", ""),
                "source_dir": tool_id,
                "source_repository": entry.get("source_repository") or FIGUREYA_REPO_URL,
                "github_url": entry.get("github_url") or f"{FIGUREYA_REPO_URL}/tree/main/{tool_id}",
                "preview_image": f"assets/previews/{preview_name}" if preview_name else None,
                "preview_status": "manual-excluded" if is_excluded else ("gallery-preview" if gallery_source and preview_name else ("result-preview" if preview_name else "no-result-preview")),
                "visual_excluded": is_excluded,
                "selected_source_image": relpath(selected_source, source_root) if selected_source else None,
                "selected_source_is_declared_output": selected_name in output_names if selected_name else False,
                "selected_source_is_gallery": bool(gallery_source),
                "declared_output_files": sorted(output_names),
                "web_reports": [
                    {
                        "title": item.get("title"),
                        "html": item.get("html"),
                        "text": item.get("text"),
                        "thumb": item.get("thumb"),
                    }
                    for item in chapter_records
                ],
                "visual_count": len(records),
                "raster_count": sum(1 for item in records if item["ext"] in {"png", "jpg", "jpeg"}),
                "pdf_count": sum(1 for item in records if item["ext"] == "pdf"),
                "svg_count": sum(1 for item in records if item["ext"] == "svg"),
                "visual_files": records,
            }
        )
    return visual_catalog


def group_tools_by_type(catalog: list[dict[str, object]]) -> dict[str, list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = {}
    for entry in catalog:
        for plot_type in entry.get("plot_types", []) or ["uncategorized"]:
            grouped.setdefault(str(plot_type), []).append(entry)
    return grouped


def group_tools_by_category(catalog: list[dict[str, object]]) -> dict[str, dict[str, list[dict[str, object]]]]:
    grouped: dict[str, dict[str, list[dict[str, object]]]] = {}
    for entry in catalog:
        primary = str(entry.get("primary_category") or "biostatistics_general")
        secondary = str(entry.get("secondary_category") or "general_visualization")
        grouped.setdefault(primary, {}).setdefault(secondary, []).append(entry)
    return grouped


def create_montage_page(entries: list[dict[str, object]], preview_dir: Path, output_path: Path) -> None:
    columns = min(MONTAGE_COLS, max(1, len(entries)))
    rows = math.ceil(len(entries) / columns)
    cell_w = MONTAGE_THUMB_SIZE[0] + MARGIN * 2
    cell_h = MONTAGE_THUMB_SIZE[1] + LABEL_HEIGHT + MARGIN * 2
    canvas = Image.new("RGB", (columns * cell_w + MARGIN, rows * cell_h + MARGIN), "white")
    draw = ImageDraw.Draw(canvas)
    font = load_font(15)
    small_font = load_font(12)

    for index, entry in enumerate(entries):
        col = index % columns
        row = index // columns
        x = MARGIN + col * cell_w
        y = MARGIN + row * cell_h

        preview_rel = entry.get("preview_image")
        preview_path = preview_dir / f"{entry['id']}.jpg"
        if preview_rel and preview_path.exists():
            thumb = make_letterboxed_image(preview_path, MONTAGE_THUMB_SIZE, str(entry["id"]))
        else:
            thumb = Image.new("RGB", MONTAGE_THUMB_SIZE, "white")
            draw_placeholder(thumb, str(entry["id"]), "no raster preview")

        canvas.paste(thumb, (x, y))
        draw.rectangle((x, y, x + MONTAGE_THUMB_SIZE[0], y + MONTAGE_THUMB_SIZE[1]), outline=(220, 220, 220))
        label = str(entry["id"])
        draw.text((x, y + MONTAGE_THUMB_SIZE[1] + 5), label[:38], fill=(0, 0, 0), font=font)
        counts = f"{entry.get('raster_count', 0)} raster / {entry.get('pdf_count', 0)} pdf"
        draw.text((x, y + MONTAGE_THUMB_SIZE[1] + 23), counts, fill=(90, 90, 90), font=small_font)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, quality=88, optimize=True)


def build_montages(visual_catalog: list[dict[str, object]], preview_dir: Path, montage_dir: Path, skill_root: Path) -> dict[str, list[str]]:
    montage_index: dict[str, list[str]] = {}
    included_catalog = [
        entry for entry in visual_catalog
        if entry.get("preview_image") and not entry.get("visual_excluded")
    ]
    grouped = group_tools_by_type(included_catalog)
    for plot_type, entries in sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0].lower())):
        entries = sorted(entries, key=lambda item: (0 if item.get("preview_image") else 1, str(item["id"]).lower()))
        pages: list[str] = []
        for start in range(0, len(entries), MONTAGE_PAGE_SIZE):
            chunk = entries[start : start + MONTAGE_PAGE_SIZE]
            page = start // MONTAGE_PAGE_SIZE + 1
            suffix = f"_page{page}" if len(entries) > MONTAGE_PAGE_SIZE else ""
            filename = f"montage_{plot_type}{suffix}.jpg"
            output_path = montage_dir / filename
            create_montage_page(chunk, preview_dir, output_path)
            pages.append(relpath(output_path, skill_root))
        montage_index[plot_type] = pages
    return montage_index


def write_visual_index(
    visual_catalog: list[dict[str, object]],
    montage_index: dict[str, list[str]],
    output_path: Path,
) -> None:
    total = len(visual_catalog)
    with_preview = sum(1 for entry in visual_catalog if entry.get("preview_image"))
    excluded = sum(1 for entry in visual_catalog if entry.get("visual_excluded"))
    total_visuals = sum(int(entry.get("visual_count", 0)) for entry in visual_catalog)
    lines: list[str] = [
        "# FigureYa Visual Index",
        "",
        f"- Tools: **{total}**",
        f"- Tools with raster previews: **{with_preview}**",
        f"- Manually excluded from visual matching: **{excluded}**",
        f"- Source visual files recorded: **{total_visuals}**",
        "",
        "Use `visual_catalog.json` for machine filtering, then open the listed preview or montage image before choosing a reference implementation.",
        "Entries with `preview_status: manual-excluded` are retained for code lookup but omitted from montage pages because their gallery preview is text/table/directory-like rather than a reusable plot style.",
        f"Source repository: {FIGUREYA_REPO_URL}. If a local code module is missing, use the tool's GitHub URL in `visual_catalog.json`.",
        "",
        "## Montage Pages",
        "",
        "| Plot type | Pages |",
        "|---|---|",
    ]
    for plot_type, pages in sorted(montage_index.items(), key=lambda item: item[0].lower()):
        lines.append(f"| {plot_type} | " + "<br>".join(f"`{page}`" for page in pages) + " |")

    lines.extend(["", "## Category Navigation", ""])
    for primary, secondary_map in sorted(group_tools_by_category(visual_catalog).items(), key=lambda item: label_primary(item[0])):
        lines.append(f"### {label_primary(primary)}")
        lines.append("")
        for secondary, entries in sorted(secondary_map.items(), key=lambda item: (-len(item[1]), label_secondary(item[0]))):
            with_preview_count = sum(1 for entry in entries if entry.get("preview_image"))
            lines.append(f"- **{label_secondary(secondary)}**: {len(entries)} tools, {with_preview_count} previews")
        lines.append("")

    lines.extend(["", "## Tool Previews", ""])
    for primary, secondary_map in sorted(group_tools_by_category(visual_catalog).items(), key=lambda item: label_primary(item[0])):
        lines.append(f"### {label_primary(primary)}")
        lines.append("")
        for secondary, entries in sorted(secondary_map.items(), key=lambda item: (-len(item[1]), label_secondary(item[0]))):
            lines.append(f"#### {label_secondary(secondary)}")
            lines.append("")
            for entry in sorted(entries, key=lambda item: str(item["id"]).lower()):
                preview = entry.get("preview_image") or "no raster preview"
                selected = entry.get("selected_source_image") or "none"
                types = ", ".join(entry.get("plot_types", [])[:4]) or "-"
                github = entry.get("github_url") or f"{FIGUREYA_REPO_URL}/tree/main/{entry['id']}"
                lines.append(
                    f"- **{entry['id']}** — preview: `{preview}`; selected source: `{selected}`; "
                    f"types: {types}; visuals: {entry.get('raster_count', 0)} raster / {entry.get('pdf_count', 0)} pdf; GitHub: {github}"
                )
            lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Create FigureYa visual previews and montages.")
    parser.add_argument("catalog_path", nargs="?", default="references/figureya_catalog.json")
    parser.add_argument("source_root", nargs="?", default=".")
    parser.add_argument("assets_dir", nargs="?", default="assets")
    parser.add_argument("--skill-root", default=None, help="Skill root used for relative paths.")
    parser.add_argument("--gallery-dir", default=None, help="Authoritative FigureYa gallery image directory.")
    args = parser.parse_args()

    catalog_path = Path(args.catalog_path).resolve()
    source_root = Path(args.source_root).resolve()
    assets_dir = Path(args.assets_dir).resolve()
    skill_root = Path(args.skill_root).resolve() if args.skill_root else assets_dir.parent.resolve()
    gallery_dir = Path(args.gallery_dir).resolve() if args.gallery_dir else source_root / "gallery"
    if not gallery_dir.exists():
        gallery_dir = None

    preview_dir = assets_dir / "previews"
    montage_dir = assets_dir / "montages"
    clean_directory(preview_dir)
    clean_directory(montage_dir)

    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    excluded_preview_ids = load_visual_exclusions(skill_root)
    visual_catalog = build_visual_catalog(catalog, source_root, preview_dir, skill_root, gallery_dir, excluded_preview_ids)
    montage_index = build_montages(visual_catalog, preview_dir, montage_dir, skill_root)

    references_dir = skill_root / "references"
    references_dir.mkdir(parents=True, exist_ok=True)
    (references_dir / "visual_catalog.json").write_text(
        json.dumps(visual_catalog, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_visual_index(visual_catalog, montage_index, references_dir / "visual_index.md")

    print(f"Generated {sum(1 for entry in visual_catalog if entry.get('preview_image'))} previews.")
    print(f"Generated {sum(len(pages) for pages in montage_index.values())} montage pages.")
    if excluded_preview_ids:
        print(f"Excluded {len(excluded_preview_ids)} manually reviewed previews.")
    if gallery_dir:
        print(f"Used gallery source: {gallery_dir}")
    print(f"Visual catalog written to {references_dir / 'visual_catalog.json'}")
    print(f"Visual index written to {references_dir / 'visual_index.md'}")


if __name__ == "__main__":
    main()
