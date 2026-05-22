#!/usr/bin/env python3
"""
Scan FigureYa directories and extract metadata from Rmd files.
Generates a JSON catalog of all plotting tools.
"""
import os
import re
import json
import glob

VISUAL_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.pdf', '.svg')
FIGUREYA_REPO_URL = 'https://github.com/ying-ge/FigureYa'

RESULT_DIR_NAMES = {
    'result', 'results', 'output', 'outputs', 'figure', 'figures',
    'plot', 'plots', 'image', 'images', 'img',
}

SKIP_DIR_NAMES = {
    '.git', '__macosx', 'packages', 'package', 'data', 'script',
    'scripts', 'node_modules',
}

BIOINFORMATICS_KEYWORDS = {
    'single_cell': ['single-cell', 'single cell', 'scrna', 'scRNA', 'Seurat', '单细胞', 'cellchat', 'monocle', 'slingshot', 'RNA velocity', 'spatial', '空间转录组'],
    'enrichment_pathway': ['GSEA', 'GO enrichment', 'GO term', 'GOplot', 'GO注释', 'KEGG', 'enrichment', '富集', '通路', 'pathway', 'GSVA', 'ssGSEA', 'clusterProfiler', 'fgsea'],
    'expression_deg': ['RNA-seq', 'RNAseq', 'DEG', 'differential expression', '差异表达', '表达矩阵', 'limma', 'DESeq2', 'edgeR', 'TPM', 'FPKM'],
    'mutation_cnv': ['mutation', 'CNV', 'copy number', 'GISTIC', 'MAF', 'TMB', 'SNV', '突变', '拷贝数'],
    'methylation_epigenomics': ['methylation', '甲基化', 'ATAC', 'ChIP', 'epigen', '表观'],
    'genome_circos': ['circos', 'chromosome', 'genome', 'genomic', '染色体', '基因组', 'Manhattan'],
    'multiomics_network': ['multi-omics', 'multiomics', 'WGCNA', 'network', '网络', 'immune infiltration', '免疫浸润', 'regulon'],
}

BIOSTATISTICS_KEYWORDS = {
    'group_comparison': ['boxplot', 'violin', 'barplot', '柱状图', '箱线图', '小提琴', 'group comparison', '差异比较'],
    'correlation_regression': ['correlation', '相关', 'regression', 'linear', 'logistic', 'scatter', '散点'],
    'survival_prognosis': ['survival', 'Kaplan', 'KM', 'cox', 'hazard', '生存', '预后'],
    'diagnostic_model': ['ROC', 'AUC', 'calibration', 'nomogram', 'DCA', '诊断', '校准'],
    'distribution_summary': ['density', 'histogram', 'pie', 'mosaic', 'venn', '分布', '比例'],
}

BIOINFO_PRIORITY = [
    'single_cell',
    'enrichment_pathway',
    'expression_deg',
    'mutation_cnv',
    'methylation_epigenomics',
    'genome_circos',
    'multiomics_network',
]

BIOSTAT_PRIORITY = [
    'diagnostic_model',
    'survival_prognosis',
    'group_comparison',
    'correlation_regression',
    'distribution_summary',
]

def extract_section(text, section_names, max_lines=50):
    """Extract content from a markdown section by heading name."""
    for name in section_names:
        # Match ## or # heading
        pattern = rf'(?:^|\n)#+\s*{re.escape(name)}\s*\n(.*?)(?=\n#+\s|\Z)'
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            content = match.group(1).strip()
            # Limit to max_lines
            lines = content.split('\n')
            content = '\n'.join(lines[:max_lines])
            # Remove markdown images and code blocks for cleaner text
            content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
            content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
            content = re.sub(r'`r[^`]+`', '', content)
            return ' '.join(content.split())[:500]
    return ""

def extract_libraries(rmd_text):
    """Extract library() and require() calls."""
    libs = set()
    for match in re.finditer(r'(?:library|require)\s*\(\s*["\']?([^\)"\']+)["\']?\s*\)', rmd_text):
        libs.add(match.group(1).strip())
    return sorted(libs)

def extract_dependencies(dep_text):
    """Extract package names from install_dependencies.R."""
    pkgs = set()
    # Match quoted package names
    for match in re.finditer(r'["\']([a-zA-Z][a-zA-Z0-9\.]*)["\']', dep_text):
        pkg = match.group(1)
        if pkg not in ('CRAN', 'en', 'TRUE', 'FALSE', 'NULL'):
            pkgs.add(pkg)
    return sorted(pkgs)

def find_rmd_files(tool_dir):
    """Find R Markdown files with case-insensitive extension handling."""
    files = []
    for path in glob.glob(os.path.join(tool_dir, '*')):
        if os.path.isfile(path) and os.path.splitext(path)[1].lower() == '.rmd':
            files.append(path)
    return sorted(files)

def choose_main_rmd(tool_dir, rmd_files):
    """Prefer the Rmd whose stem matches the FigureYa directory name."""
    dirname = os.path.basename(tool_dir).lower()
    for path in rmd_files:
        stem = os.path.splitext(os.path.basename(path))[0].lower()
        if stem == dirname:
            return path
    for path in rmd_files:
        stem = os.path.splitext(os.path.basename(path))[0].lower()
        if dirname in stem or stem in dirname:
            return path
    return rmd_files[0]

def find_visual_files(tool_dir):
    """Collect local visual assets for the tool."""
    files = []
    for root, dirnames, filenames in os.walk(tool_dir):
        dirnames[:] = [name for name in dirnames if name.lower() not in SKIP_DIR_NAMES]
        rel_dir = os.path.relpath(root, tool_dir)
        rel_parts = [] if rel_dir == '.' else [part.lower() for part in rel_dir.split(os.sep)]
        is_top_level = rel_dir == '.'
        is_result_dir = any(part in RESULT_DIR_NAMES for part in rel_parts)
        if not is_top_level and not is_result_dir:
            continue
        for filename in filenames:
            if os.path.splitext(filename)[1].lower() in VISUAL_EXTENSIONS:
                files.append(os.path.join(root, filename))
    records = []
    for path in sorted(set(files)):
        name = os.path.basename(path)
        stem = os.path.splitext(name)[0].lower()
        kind = 'figure'
        if any(word in stem for word in ['method', 'workflow', 'pipeline', 'explain', 'install', 'download', 'input', 'readme', 'files', 'folder', 'directory']):
            kind = 'method'
        elif 'example' in stem:
            kind = 'example'
        records.append({
            'path': os.path.relpath(path, tool_dir),
            'name': name,
            'ext': os.path.splitext(name)[1].lower().lstrip('.'),
            'kind': kind,
            'size_bytes': os.path.getsize(path),
        })
    return records

def keyword_hits(text, keyword_map):
    hits = []
    text_lower = text.lower()
    for tag, keywords in keyword_map.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                hits.append(tag)
                break
    return hits

def classify_tool(entry_text, plot_types, libraries):
    """Classify a tool into a coarse retrieval bucket and a finer analysis class."""
    haystack = ' '.join([entry_text, ' '.join(plot_types), ' '.join(libraries)])
    bioinfo_hits = keyword_hits(haystack, BIOINFORMATICS_KEYWORDS)
    biostat_hits = keyword_hits(haystack, BIOSTATISTICS_KEYWORDS)
    bioinfo_hits = sorted(bioinfo_hits, key=lambda tag: BIOINFO_PRIORITY.index(tag) if tag in BIOINFO_PRIORITY else 99)
    biostat_hits = sorted(biostat_hits, key=lambda tag: BIOSTAT_PRIORITY.index(tag) if tag in BIOSTAT_PRIORITY else 99)

    strong_bioinfo = [tag for tag in bioinfo_hits if tag in {
        'single_cell',
        'enrichment_pathway',
        'expression_deg',
        'mutation_cnv',
        'methylation_epigenomics',
        'genome_circos',
    }]
    endpoint_stats = [tag for tag in biostat_hits if tag in {
        'survival_prognosis',
        'diagnostic_model',
        'correlation_regression',
        'group_comparison',
        'distribution_summary',
    }]

    # Common statistical endpoints should stay easy to find even when their
    # examples use omics-derived features. Omics workflows stay in bioinformatics.
    if endpoint_stats and not any(tag in strong_bioinfo for tag in {
        'single_cell',
        'enrichment_pathway',
        'methylation_epigenomics',
        'genome_circos',
    }):
        primary = 'biostatistics_general'
        secondary = endpoint_stats[0]
    elif strong_bioinfo:
        primary = 'bioinformatics_omics'
        secondary = strong_bioinfo[0]
    elif endpoint_stats:
        primary = 'biostatistics_general'
        secondary = endpoint_stats[0]
    elif 'multiomics_network' in bioinfo_hits:
        primary = 'bioinformatics_omics'
        secondary = 'multiomics_network'
    else:
        primary = 'biostatistics_general'
        secondary = 'general_visualization'

    tags = []
    for tag in bioinfo_hits + biostat_hits:
        if tag not in tags:
            tags.append(tag)

    return primary, secondary, tags

def scan_figureya(base_dir, output_file):
    """Scan all FigureYa directories and build catalog."""
    catalog = []

    # Find all FigureYa directories
    dirs = sorted(glob.glob(os.path.join(base_dir, 'FigureYa*')))

    for d in dirs:
        if not os.path.isdir(d):
            continue

        dirname = os.path.basename(d)

        # Find the main Rmd file. Some FigureYa folders use lower-case .rmd.
        rmd_files = find_rmd_files(d)
        if not rmd_files:
            continue
        rmd_file = choose_main_rmd(d, rmd_files)

        # Read Rmd
        try:
            with open(rmd_file, 'r', encoding='utf-8', errors='ignore') as f:
                rmd_text = f.read()
        except Exception:
            continue

        # Read install_dependencies.R if exists
        dep_file = os.path.join(d, 'install_dependencies.R')
        deps = []
        if os.path.exists(dep_file):
            try:
                with open(dep_file, 'r', encoding='utf-8', errors='ignore') as f:
                    dep_text = f.read()
                deps = extract_dependencies(dep_text)
            except Exception:
                pass

        # Extract metadata
        title_match = re.search(r'^---\s*\n.*?title:\s*"([^"]+)".*?\n---', rmd_text, re.DOTALL)
        title = title_match.group(1) if title_match else dirname

        # Extract requirement/description
        req_cn = extract_section(rmd_text, ['需求描述', 'Requirement description', '需求'])
        scenario_cn = extract_section(rmd_text, ['应用场景', '使用场景', 'Application scenarios', 'Usage scenario', '场景'])
        input_cn = extract_section(rmd_text, ['输入数据', 'Input data', '数据格式'])

        # Combine description
        description = req_cn or ""
        if scenario_cn:
            description += " | 场景: " + scenario_cn

        # Extract plot types from description
        plot_types = []
        type_keywords = {
            'PCA': ['PCA'],
            'ROC': ['ROC'],
            'heatmap': ['热图', 'heatmap', 'heat map'],
            'boxplot': ['boxplot', '箱线图', 'box plot'],
            'volcano': ['volcano', '火山图'],
            'bubble': ['bubble', '泡泡图', '气泡图'],
            'venn': ['venn', '韦恩图'],
            'GSEA': ['GSEA'],
            'survival': ['survival', '生存曲线', 'KM曲线', 'Kaplan'],
            'scatter': ['scatter', '散点图'],
            'barplot': ['barplot', '柱状图', '条形图'],
            'line': ['line plot', '折线图'],
            'pie': ['pie', '饼图'],
            'dendrogram': ['dendrogram', '树状图'],
            'network': ['network', '网络图'],
            'correlation': ['correlation', '相关'],
            'mutation': ['mutation', '突变'],
            'chromosome': ['chromosome', '染色体'],
            'forest': ['forest', '森林图'],
            'calibration': ['calibration', '校准曲线'],
            'violin': ['violin', '小提琴图'],
            'density': ['density', '密度图'],
            'mosaic': ['mosaic', '马赛克图'],
            'circos': ['circos', '圈图'],
            'GO': ['GO enrichment', '功能富集', '富集分析'],
        }
        text_lower = (description + " " + title + " " + dirname).lower()
        for ptype, keywords in type_keywords.items():
            for kw in keywords:
                if kw.lower() in text_lower:
                    plot_types.append(ptype)
                    break

        # Extract input format hints
        input_formats = []
        format_keywords = {
            'CSV': ['.csv', 'csv'],
            'TXT': ['.txt', 'txt'],
            'Excel': ['.xls', 'xlsx', 'excel'],
            'matrix': ['matrix', '表达矩阵', 'expr'],
            'gene list': ['gene list', '基因列表'],
        }
        all_text = (rmd_text + " " + input_cn).lower()
        for fmt, keywords in format_keywords.items():
            for kw in keywords:
                if kw.lower() in all_text:
                    input_formats.append(fmt)
                    break
        input_formats = list(set(input_formats))

        # Check for example image
        has_example = os.path.exists(os.path.join(d, 'example.png')) or \
                      any(glob.glob(os.path.join(d, 'example*')))

        libraries = extract_libraries(rmd_text)
        visual_files = find_visual_files(d)
        entry_text = " ".join([dirname, title, description])
        primary_category, secondary_category, analysis_tags = classify_tool(entry_text, list(set(plot_types)), libraries)

        entry = {
            'id': dirname,
            'title': title,
            'description': description[:600] if description else f"R绘图工具: {title}",
            'plot_types': list(set(plot_types)),
            'primary_category': primary_category,
            'secondary_category': secondary_category,
            'analysis_tags': analysis_tags,
            'libraries': libraries,
            'dependencies': deps,
            'input_formats': input_formats,
            'has_example': has_example,
            'has_visual_assets': bool(visual_files),
            'visual_count': len(visual_files),
            'visual_files': visual_files,
            'code_path': os.path.join('references', 'code', dirname),
            'source_repository': FIGUREYA_REPO_URL,
            'github_url': f'{FIGUREYA_REPO_URL}/tree/main/{dirname}',
            'path': d,
        }
        catalog.append(entry)

    # Write catalog
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)

    print(f"Scanned {len(catalog)} FigureYa tools.")
    print(f"Catalog written to {output_file}")

    # Print summary
    all_types = {}
    for entry in catalog:
        for pt in entry['plot_types']:
            all_types[pt] = all_types.get(pt, 0) + 1
    print("\nPlot type distribution:")
    for pt, count in sorted(all_types.items(), key=lambda x: -x[1]):
        print(f"  {pt}: {count}")

if __name__ == '__main__':
    import sys
    base = sys.argv[1] if len(sys.argv) > 1 else '.'
    out = sys.argv[2] if len(sys.argv) > 2 else 'figureya_catalog.json'
    scan_figureya(base, out)
