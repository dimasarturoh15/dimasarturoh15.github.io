"""Sinkronkan riwayat commit sebuah repositori ke situs portofolio.

Dipanggil oleh hook post-commit di repositori proyek, misalnya:

    python tools/sync_commit.py --repo "D:/My Project/ChoraleStudio" --slug choralestudio --name ChoraleStudio

Yang diperbarui (selalu disusun ulang dari riwayat Git, jadi aman dijalankan berulang kali):
  1. Tabel "Log Pengerjaan" di akhir docs/projects/<slug>.md
  2. Halaman jurnal harian docs/journal/<tanggal>-<slug>-commit.md untuk tanggal commit terakhir
  3. Daftar entri di docs/journal/index.md
  4. Navigasi "Jurnal Belajar" di mkdocs.yml
  5. Daftar "Jurnal terkini" di docs/index.md
"""

from __future__ import annotations

import argparse
import html
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
DOCS = SITE / "docs"
MONTHS = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus",
          "September", "Oktober", "November", "Desember"]
SHORT_MONTHS = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
TRAILER = re.compile(r"^(Co-Authored-By|Signed-off-by|Reviewed-by):", re.I)
HOME_ITEMS = 6
SEP = "\x1f"
END = "\x1e"


@dataclass
class Commit:
    sha: str
    short: str
    date: str  # YYYY-MM-DD
    time: str  # HH:MM
    subject: str
    body: list[str]
    files: int = 0
    added: int = 0
    removed: int = 0


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, check=True,
                          encoding="utf-8", errors="replace").stdout


def commits(repo: Path) -> list[Commit]:
    """Semua commit cabang aktif (first-parent), dari yang terlama."""
    fmt = SEP.join(["%H", "%h", "%cd", "%s", "%b"]) + END
    out = git(repo, "log", "--first-parent", "--reverse", "--date=format:%Y-%m-%d %H:%M",
              f"--format={fmt}")
    result = []
    for raw in out.split(END):
        raw = raw.strip("\n")
        if not raw:
            continue
        sha, short, when, subject, body = raw.split(SEP, 4)
        lines = [ln.rstrip() for ln in body.strip().splitlines() if not TRAILER.match(ln.strip())]
        while lines and not lines[-1]:
            lines.pop()
        day, clock = when.split(" ")
        result.append(Commit(sha, short, day, clock, subject.strip(), lines))
    return result


def add_stats(repo: Path, commit: Commit) -> None:
    out = git(repo, "show", "--shortstat", "--format=", commit.sha)
    for count, kind in re.findall(r"(\d+) (file|insertion|deletion)", out):
        if kind == "file":
            commit.files = int(count)
        elif kind == "insertion":
            commit.added = int(count)
        else:
            commit.removed = int(count)


def web_url(repo: Path) -> str | None:
    try:
        url = git(repo, "remote", "get-url", "origin").strip()
    except subprocess.CalledProcessError:
        return None
    url = re.sub(r"^git@github\.com:", "https://github.com/", url)
    url = re.sub(r"\.git$", "", url)
    return url if url.startswith("https://github.com/") else None


def long_date(day: str) -> str:
    y, m, d = (int(x) for x in day.split("-"))
    return f"{d} {MONTHS[m - 1]} {y}"


def short_date(day: str) -> str:
    y, m, d = (int(x) for x in day.split("-"))
    return f"{d} {SHORT_MONTHS[m - 1]} {y}"


def md_escape(text: str) -> str:
    return text.replace("|", "\\|")


def commit_link(c: Commit, url: str | None) -> str:
    return f"[`{c.short}`]({url}/commit/{c.sha})" if url else f"`{c.short}`"


# 1. Tabel log di halaman proyek -------------------------------------------------------

def update_project_log(slug: str, name: str, history: list[Commit], url: str | None) -> Path:
    page = DOCS / "projects" / f"{slug}.md"
    if page.is_file():
        text = page.read_text(encoding="utf-8")
    else:
        text = f"# {name}\n\n> Proyek dalam pengerjaan.\n\n"
    marker = "## Log Pengerjaan"
    head = text[: text.index(marker)] if marker in text else text.rstrip("\n") + "\n\n"
    rows = [marker, "", "Diperbarui otomatis dari riwayat Git setiap kali ada commit.", "",
            "| Waktu | Commit | Ringkasan Perubahan |", "|---|---|---|"]
    rows += [f"| {c.date} {c.time} | {commit_link(c, url)} | {md_escape(c.subject)} |" for c in history]
    page.write_text(head + "\n".join(rows) + "\n", encoding="utf-8")
    return page


# 2. Halaman jurnal harian --------------------------------------------------------------

def journal_slug(day: str, slug: str) -> str:
    return f"{day}-{slug}-commit"


def journal_title(name: str, count: int) -> str:
    return f"Catatan commit {name} ({count} commit)"


def write_journal_page(day: str, slug: str, name: str, todays: list[Commit], url: str | None) -> Path:
    page = DOCS / "journal" / f"{journal_slug(day, slug)}.md"
    total_files = sum(c.files for c in todays)
    lines = [f"# {long_date(day)}: {journal_title(name, len(todays))}", "",
             f"Halaman ini dibuat otomatis dari riwayat Git [{name}](../projects/{slug}.md) setiap kali "
             "ada commit. Isinya adalah pesan commit apa adanya.", "",
             "## Ringkasan", "",
             f"- Jumlah commit: {len(todays)}",
             f"- Perubahan: {total_files} berkas, +{sum(c.added for c in todays)} / "
             f"-{sum(c.removed for c in todays)} baris",
             f"- Rentang waktu: {todays[0].time} sampai {todays[-1].time}", "",
             "## Yang dikerjakan", ""]
    for c in todays:
        lines += [f"### {c.time} · {c.subject}", "",
                  f"Commit {commit_link(c, url)} · {c.files} berkas, +{c.added} / -{c.removed} baris", ""]
        if c.body:
            lines += [ln.replace("<", "&lt;") for ln in c.body] + [""]
    page.write_text("\n".join(lines).rstrip("\n") + "\n", encoding="utf-8")
    return page


# 3. Indeks jurnal ----------------------------------------------------------------------

INDEX_FRONT = "---\nhide:\n  - toc\n---\n\n"


@dataclass
class Entry:
    date: str
    href: str
    title: str  # sudah berupa HTML (di-escape)
    summary: str
    tags: list[str]


def parse_journal_index(text: str) -> tuple[str, list[Entry]]:
    """Bagian pembuka (judul + pengantar) dan semua entri, dari format lama maupun berkelompok."""
    starts = [i for i in (text.find('<div class="log-day"'), text.find('<ol class="log">')) if i >= 0]
    head = text[: min(starts)] if starts else text
    entries = []
    current = "0000-00-00"
    for m in re.finditer(r'data-date="(\d{4}-\d{2}-\d{2})"|<li>.*?</li>', text[len(head):], re.S):
        if m.group(1):
            current = m.group(1)
            continue
        block = m.group(0)
        own = re.search(r'datetime="(\d{4}-\d{2}-\d{2})"', block)
        link = re.search(r'<a (?:class="log-title" )?href="([^"]+)">(.*?)</a>', block, re.S)
        summary = re.search(r"<p>(.*?)</p>", block, re.S)
        if link:
            entries.append(Entry(own.group(1) if own else current, link.group(1), link.group(2),
                                 summary.group(1) if summary else "", re.findall(r"<span>(#[^<]+)</span>", block)))
    return head, entries


def render_journal_index(head: str, entries: list[Entry]) -> str:
    """Entri dikelompokkan per tanggal (terbaru di atas); urutan di dalam satu tanggal dipertahankan."""
    if not head.startswith("---"):
        head = INDEX_FRONT + head.lstrip()
    out = [head.rstrip("\n") + "\n"]
    for day in sorted({e.date for e in entries}, reverse=True):
        rows = []
        for e in (e for e in entries if e.date == day):
            tags = "".join(f"<span>{t}</span>" for t in e.tags)
            rows.append(f'  <li>\n    <a class="log-title" href="{e.href}">{e.title}</a>\n'
                        f'    <span class="tags">{tags}</span>\n    <p>{e.summary}</p>\n  </li>')
        out.append(f'\n<div class="log-day" data-date="{day}">\n'
                   f'<h2 class="log-date"><time datetime="{day}">{long_date(day)}</time></h2>\n'
                   f'<ol class="log">\n' + "\n".join(rows) + "\n</ol>\n</div>\n")
    return "".join(out)


def update_journal_index(day: str, slug: str, name: str, todays: list[Commit]) -> Path:
    index = DOCS / "journal" / "index.md"
    head, entries = parse_journal_index(index.read_text(encoding="utf-8"))
    href = f"{journal_slug(day, slug)}/"
    subjects = "; ".join(c.subject for c in todays[-3:])
    more = f" dan {len(todays) - 3} lainnya" if len(todays) > 3 else ""
    entry = Entry(day, href, html.escape(journal_title(name, len(todays))),
                  f"Dicatat otomatis dari Git: {html.escape(subjects)}{more}.",
                  [f"#{slug}", "#commit", "#otomatis"])
    pos = next((i for i, e in enumerate(entries) if e.href == href), None)
    if pos is not None:
        entries[pos] = entry
    else:
        # Entri terbaru di atas: sisipkan sebelum entri pertama yang tanggalnya sama atau lebih lama.
        pos = next((i for i, e in enumerate(entries) if e.date <= day), len(entries))
        entries.insert(pos, entry)
    index.write_text(render_journal_index(head, entries), encoding="utf-8")
    return index


# 4. Navigasi mkdocs.yml ----------------------------------------------------------------

def update_nav(day: str, slug: str, name: str) -> Path:
    cfg = SITE / "mkdocs.yml"
    lines = cfg.read_text(encoding="utf-8").splitlines(keepends=True)
    path = f"journal/{journal_slug(day, slug)}.md"
    entry = f'      - "{short_date(day)}: Commit {name}": {path}\n'
    if any(path in ln for ln in lines):
        return cfg
    start = next(i for i, ln in enumerate(lines) if ln.strip() == "- journal/index.md")
    pos = start + 1
    while pos < len(lines) and lines[pos].startswith("      - "):
        m = re.search(r"journal/(\d{4}-\d{2}-\d{2})", lines[pos])
        if m and m.group(1) <= day:
            break
        pos += 1
    lines.insert(pos, entry)
    cfg.write_text("".join(lines), encoding="utf-8")
    return cfg


# 5. Beranda ----------------------------------------------------------------------------

def update_home() -> Path:
    home = DOCS / "index.md"
    text = home.read_text(encoding="utf-8")
    _, entries = parse_journal_index((DOCS / "journal" / "index.md").read_text(encoding="utf-8"))
    entries.sort(key=lambda e: e.date, reverse=True)  # stabil: urutan dalam satu tanggal tetap
    items = [f'  <li><span class="date">{e.date}</span><a href="journal/{e.href}">{e.title}</a></li>\n'
             for e in entries[:HOME_ITEMS]]
    new = '<ul class="dated-list">\n' + "".join(items) + "</ul>"
    text = re.sub(r'<ul class="dated-list">\n.*?</ul>', lambda _: new, text, count=1, flags=re.S)
    home.write_text(text, encoding="utf-8")
    return home


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", type=Path, required=True, help="folder repositori proyek")
    parser.add_argument("--slug", required=True, help="nama berkas halaman proyek, mis. choralestudio")
    parser.add_argument("--name", required=True, help="nama proyek yang ditampilkan")
    parser.add_argument("--tanggal", help="tanggal jurnal YYYY-MM-DD (default: tanggal commit terakhir)")
    args = parser.parse_args()

    history = commits(args.repo)
    if not history:
        return 0
    url = web_url(args.repo)
    day = args.tanggal or history[-1].date
    todays = [c for c in history if c.date == day]
    for c in todays:
        add_stats(args.repo, c)

    changed = [update_project_log(args.slug, args.name, history, url)]
    if todays:
        changed += [write_journal_page(day, args.slug, args.name, todays, url),
                    update_journal_index(day, args.slug, args.name, todays),
                    update_nav(day, args.slug, args.name),
                    update_home()]
    for path in changed:
        print(path.relative_to(SITE).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
