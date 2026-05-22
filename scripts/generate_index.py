#!/usr/bin/env python3
"""Generate searchable Markdown indexes from the FigureYa JSON catalog."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

FIGUREYA_REPO_URL = "https://github.com/ying-ge/FigureYa"

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


def label_primary(value: str) -> str:
    return PRIMARY_LABELS.get(value, value or "未分类")


def label_secondary(value: str) -> str:
    return SECONDARY_LABELS.get(value, value or "未分类")


def short_text(text: str, limit: int = 150) -> str:
    text = " ".join((text or "").split())
    return text[:limit] + "..." if len(text) > limit else text


def tool_line(entry: dict) -> str:
    plot_types = ", ".join(entry.get("plot_types", [])[:4]) or "-"
    libs = ", ".join(entry.get("libraries", [])[:5]) or "-"
    visual = entry.get("visual_count", 0)
    desc = short_text(entry.get("description", ""))
    github = entry.get("github_url") or f"{FIGUREYA_REPO_URL}/tree/main/{entry['id']}"
    return f"- **{entry['id']}** — {entry.get('title', entry['id'])} | 图型: {plot_types} | 视觉文件: {visual} | 依赖: {libs} | GitHub: {github} | {desc}"


def build_group_maps(catalog: list[dict]) -> tuple[dict, dict, dict]:
    category_map = defaultdict(lambda: defaultdict(list))
    type_map = defaultdict(list)
    lib_map = defaultdict(list)
    for entry in catalog:
        primary = entry.get("primary_category", "biostatistics_general")
        secondary = entry.get("secondary_category", "general_visualization")
        category_map[primary][secondary].append(entry)
        for plot_type in entry.get("plot_types", []):
            type_map[plot_type].append(entry)
        for lib in entry.get("libraries", []):
            lib_map[lib].append(entry)
    return category_map, type_map, lib_map


def category_section(primary: str, secondary_map: dict[str, list[dict]]) -> list[str]:
    lines = [f"## {label_primary(primary)}", ""]
    for secondary, entries in sorted(secondary_map.items(), key=lambda item: (-len(item[1]), label_secondary(item[0]))):
        lines.append(f"### {label_secondary(secondary)} ({len(entries)}个)")
        lines.append("")
        for entry in sorted(entries, key=lambda item: item["id"].lower()):
            lines.append(tool_line(entry))
        lines.append("")
    return lines


def quick_lookup_table(catalog: list[dict]) -> list[str]:
    lines = [
        "## 快速查找表",
        "",
        "| 工具ID | 大类 | 二级类 | 图类型 | 关键R包 | 视觉文件 | 输入格式 | GitHub |",
        "|---|---|---|---|---|---:|---|---|",
    ]
    for entry in sorted(catalog, key=lambda item: item["id"].lower()):
        pts = ", ".join(entry.get("plot_types", [])[:3])
        libs = ", ".join(entry.get("libraries", [])[:3])
        fmts = ", ".join(entry.get("input_formats", [])[:3])
        github = entry.get("github_url") or f"{FIGUREYA_REPO_URL}/tree/main/{entry['id']}"
        lines.append(
            f"| {entry['id']} | {label_primary(entry.get('primary_category', ''))} | "
            f"{label_secondary(entry.get('secondary_category', ''))} | {pts} | {libs} | "
            f"{entry.get('visual_count', 0)} | {fmts} | {github} |"
        )
    lines.append("")
    return lines


def plot_type_section(type_map: dict[str, list[dict]]) -> list[str]:
    lines = ["## 按图类型分类", ""]
    for plot_type, entries in sorted(type_map.items(), key=lambda item: (-len(item[1]), item[0].lower())):
        ids = ", ".join(entry["id"] for entry in sorted(entries, key=lambda item: item["id"].lower())[:15])
        if len(entries) > 15:
            ids += f" 等({len(entries)}个)"
        lines.append(f"- **{plot_type}** ({len(entries)}个): {ids}")
    lines.append("")
    return lines


def library_section(lib_map: dict[str, list[dict]]) -> list[str]:
    lines = ["## 按R包分类 Top 40", ""]
    for lib, entries in sorted(lib_map.items(), key=lambda item: (-len(item[1]), item[0].lower()))[:40]:
        ids = ", ".join(entry["id"] for entry in sorted(entries, key=lambda item: item["id"].lower())[:8])
        if len(entries) > 8:
            ids += f" 等({len(entries)}个)"
        lines.append(f"- **{lib}**: {ids}")
    lines.append("")
    return lines


def generate_index(catalog_path: str, output_path: str) -> None:
    catalog_file = Path(catalog_path)
    output_file = Path(output_path)
    catalog = json.loads(catalog_file.read_text(encoding="utf-8"))
    category_map, type_map, lib_map = build_group_maps(catalog)

    lines = [
        "# FigureYa R绘图图库索引",
        "",
        f"总计 **{len(catalog)}** 个绘图工具。",
        "",
        "优先按大类检索：常规生物学/医学统计图用于分组比较、相关、ROC、生存、森林图等；生信/组学分析图用于表达矩阵、差异分析、富集、单细胞、突变/CNV、甲基化、基因组和多组学图。",
        "",
        "视觉预览见 `visual_index.md`；机器可读视觉信息见 `visual_catalog.json`。",
        f"来源仓库：{FIGUREYA_REPO_URL}。若本地 `references/code` 中没有对应模块或辅助脚本，优先访问该工具的 GitHub 目录。",
        "",
    ]

    for primary in ("biostatistics_general", "bioinformatics_omics"):
        if primary in category_map:
            lines.extend(category_section(primary, category_map[primary]))

    remaining = [primary for primary in category_map.keys() if primary not in {"biostatistics_general", "bioinformatics_omics"}]
    for primary in sorted(remaining):
        lines.extend(category_section(primary, category_map[primary]))

    lines.extend(plot_type_section(type_map))
    lines.extend(quick_lookup_table(catalog))
    lines.extend(library_section(lib_map))

    output_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"Index written to {output_file}")

    for primary, filename in [
        ("biostatistics_general", "index_biostatistics.md"),
        ("bioinformatics_omics", "index_bioinformatics.md"),
    ]:
        subset = []
        if primary in category_map:
            subset.extend([f"# {label_primary(primary)}", ""])
            subset.append("只在用户需求属于本大类时加载此文件；需要看图时再打开 `visual_index.md` 或对应 `assets/previews/*.jpg`。")
            subset.append("")
            subset.extend(category_section(primary, category_map[primary]))
            subset.extend(quick_lookup_table([entry for sec in category_map[primary].values() for entry in sec]))
        sidecar = output_file.parent / filename
        sidecar.write_text("\n".join(subset), encoding="utf-8")
        print(f"Sidecar index written to {sidecar}")


if __name__ == "__main__":
    import sys

    cat = sys.argv[1] if len(sys.argv) > 1 else "figureya_catalog.json"
    out = sys.argv[2] if len(sys.argv) > 2 else "figureya_index.md"
    generate_index(cat, out)
