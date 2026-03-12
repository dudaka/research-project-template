"""Organize marker-converted papers into Tier 3 reference structure.

Usage:
    1. Convert PDF: marker <paper.pdf>
    2. Place output directory in incoming_papers/
    3. Run: uv run organize_papers.py

Creates:
    docs/references/<paper_slug>/
        CLAUDE.md              Navigation map
        references/            Section files
        assets/                Figures
"""
import json
import re
import shutil
from pathlib import Path


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[-\s]+', '_', text)


def update_global_files(paper_name, target_path):
    """Update CLAUDE.md ingested papers list and LIT_REVIEW.md."""
    root_claude = Path("CLAUDE.md")
    if root_claude.exists():
        content = root_claude.read_text()
        entry = f"- {paper_name}: `{target_path}/CLAUDE.md`"
        if paper_name not in content:
            content = content.replace("(none yet)", entry)
            if entry not in content:
                marker = "### Ingested Papers\n"
                idx = content.find(marker)
                if idx != -1:
                    insert_at = idx + len(marker) + 1
                    content = content[:insert_at] + entry + "\n" + content[insert_at:]
            root_claude.write_text(content)

    lit_review = Path("docs/research_log/LIT_REVIEW.md")
    if lit_review.exists():
        content = lit_review.read_text()
        if paper_name in content:
            return
        new_row = f"| {paper_name} | TBD | TBD | TBD | TBD |"
        lines = content.split("\n")
        insert_idx = None
        for i, line in enumerate(lines):
            if line.startswith("| :---"):
                insert_idx = i + 1
                while insert_idx < len(lines) and lines[insert_idx].startswith("|"):
                    insert_idx += 1
                break
        if insert_idx is not None:
            lines.insert(insert_idx, new_row)
            lit_review.write_text("\n".join(lines))


def find_paper_files(paper_dir):
    paper_dir = Path(paper_dir)
    md_files = list(paper_dir.glob("*.md"))
    meta_files = list(paper_dir.glob("*_meta.json"))
    image_files = list(paper_dir.glob("*.jpeg")) + list(paper_dir.glob("*.png"))
    md_file = md_files[0] if md_files else None
    meta_file = meta_files[0] if meta_files else None
    return md_file, meta_file, image_files


def get_paper_title(meta_file):
    if not meta_file:
        return None
    with open(meta_file, "r", encoding="utf-8") as f:
        meta = json.load(f)
    toc = meta.get("table_of_contents", [])
    if toc:
        title = toc[0].get("title", "")
        return " ".join(title.split())
    return None


def process_paper(paper_dir, output_base="docs/references"):
    paper_dir = Path(paper_dir)
    md_file, meta_file, image_files = find_paper_files(paper_dir)

    if not md_file:
        print(f"No .md file found in {paper_dir}, skipping.")
        return

    paper_title = get_paper_title(meta_file) or md_file.stem
    paper_slug = slugify(md_file.stem)
    target_dir = Path(output_base) / paper_slug
    refs_dir = target_dir / "references"
    assets_dir = target_dir / "assets"

    target_dir.mkdir(parents=True, exist_ok=True)
    refs_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    for img in image_files:
        shutil.copy2(img, assets_dir / img.name)

    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    sections = re.split(r'\n(#{1,2}\s+.*)\n', content)
    header_map = []

    intro_content = sections[0].strip()
    if intro_content:
        intro_file = "00_introduction.md"
        with open(refs_dir / intro_file, "w") as f:
            f.write(intro_content)
        header_map.append(("Introduction", intro_file))

    for i in range(1, len(sections), 2):
        header_line = sections[i].strip()
        header_text = header_line.lstrip('#').strip()
        section_body = sections[i + 1].strip()

        slug = slugify(header_text)[:80]
        filename = f"{i // 2 + 1:02d}_{slug}.md"
        with open(refs_dir / filename, "w") as f:
            f.write(f"{header_line}\n\n{section_body}")
        header_map.append((header_text, filename))

    with open(target_dir / "CLAUDE.md", "w") as f:
        f.write(f"# Research Paper: {paper_title}\n\n")
        f.write("## Navigation Guide\n")
        f.write("| Section | Reference File |\n| :--- | :--- |\n")
        for title, fname in header_map:
            f.write(f"| {title} | `references/{fname}` |\n")
        f.write(f"\n## Assets\n- Check `assets/` for figures.\n")

    update_global_files(paper_title, target_dir)
    print(f"Organized '{paper_title}' into {target_dir}")


if __name__ == "__main__":
    incoming = Path("incoming_papers")
    if not incoming.exists():
        print("Folder 'incoming_papers' not found. Creating it...")
        incoming.mkdir()
    else:
        for subdir in sorted(incoming.iterdir()):
            if subdir.is_dir():
                process_paper(subdir)
