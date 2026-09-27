"""Convert the ReportLab book story into a Word (DOCX) manuscript.

The book's content lives as ReportLab flowables produced by ``build.py``. Rather
than re-author everything for Word, this module captures the same story and maps
each flowable to a semantic Word equivalent.

Structure and paging
--------------------
The PDF's templates (``bleed`` cover, ``plain`` front matter, ``body``, ``opener``
full-page dividers) become Word *sections*. Each section carries its own page
numbering, headers and footers, which is exactly how a trade interior is built:

* Cover / half-title / title / colophon  -> no numbering, no running head
* Front matter (TOC, preface, prologue)  -> lower-roman folio
* Body                                     -> arabic folio, mirrored running heads

The colliding ``PageBreak``s in the source are ignored: every ``Heading 1``
already starts a new page via ``page_break_before``.

Output: ``output/TUNTAS-7D.docx``.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt

import docxkit as K
from docxkit import C, SANS, SANS_B, SERIF
from docxstyles import build_document

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_DIR = os.path.join(ROOT, "assets")
QR_DIR = os.path.join(ASSET_DIR, "qr")
FIG_DIR = os.path.join(ASSET_DIR, "fig")


# ------------------------------------------------------------------ capture
def capture_story(path="/tmp/_tuntas_capture.pdf"):
    import build as B
    from engine import BookDocTemplate
    box = {}
    original = BookDocTemplate.multiBuild

    def fake(self, story):
        box["story"] = list(story)

    BookDocTemplate.multiBuild = fake
    try:
        B.build(path)
    finally:
        BookDocTemplate.multiBuild = original
    return box["story"]


# ------------------------------------------------------------------ markup
_TAG = re.compile(r"(<[^>]+>)")


def parse_runs(html):
    """Split ReportLab mini-markup into (text, bold, italic, color, size, face)."""
    out = []
    b, i, col, sz, face = False, False, None, None, None
    stack = []
    for tok in _TAG.split(html):
        if not tok:
            continue
        if tok.startswith("<") and tok.endswith(">"):
            tag = tok[1:-1].strip().lower()
            if tag.startswith("/"):
                name = tag[1:].split()[0] if len(tag) > 1 else ""
                if name in ("b", "i", "font", "u") and stack:
                    b, i, col, sz, face = stack.pop()
                continue
            if tag == "b":
                stack.append((b, i, col, sz, face)); b = True
            elif tag == "i":
                stack.append((b, i, col, sz, face)); i = True
            elif tag == "u":
                stack.append((b, i, col, sz, face))
            elif tag.startswith("br"):
                out.append(("\n", b, i, col, sz, face))
            elif tag.startswith("font"):
                stack.append((b, i, col, sz, face))
                m = re.search(r'color="([^"]+)"', tok)
                if m:
                    col = m.group(1)
                m = re.search(r'face="([^"]+)"', tok)
                if m:
                    face = m.group(1)
                m = re.search(r'size="([0-9.]+)"', tok)
                if m:
                    sz = float(m.group(1))
            continue
        out.append((unescape(tok), b, i, col, sz, face))
    return out


def unescape(t):
    return (t.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<")
             .replace("&gt;", ">").replace("&quot;", '"'))


def plain(html):
    return "".join(x[0] for x in parse_runs(html)).strip()


def write_markup(p, html, font, size, color, bold=False, italic=False):
    for text, b, i, col, sz, face in parse_runs(html):
        if "\n" in text:
            for k, part in enumerate(text.split("\n")):
                if k:
                    K.add_break(p, "textWrapping")
                if part:
                    K.add_run(p, part, face or font, sz or size, bold=b or bold,
                              italic=i or italic, color=col or color)
        else:
            K.add_run(p, text, face or font, sz or size, bold=b or bold,
                      italic=i or italic, color=col or color)


def style_run(p, style_name, html, doc):
    st = doc.styles[style_name]
    f = st.font
    size = f.size.pt if f.size else 10.0
    color = C["ink"]
    if f.color is not None and f.color.type is not None:
        try:
            color = f.color.rgb
        except Exception:
            color = C["ink"]
    write_markup(p, html, f.name or SERIF, size, color,
                 bold=bool(f.bold), italic=bool(f.italic))
    return p


# ------------------------------------------------------------------ boxes
BOX_STYLES = {
    "insight":    dict(bg=C["amber_soft"], bar=C["amber"]),
    "tool":       dict(bg=C["teal_soft"], bar=C["teal"]),
    "warning":    dict(bg=C["red_soft"], bar=C["red"]),
    "practice":   dict(bg=C["green_soft"], bar=C["green"]),
    "story":      dict(bg=C["cream"], bar=C["navy"]),
    "definition": dict(bg=C["violet_soft"], bar=C["violet"]),
    "keyidea":    dict(bg=C["accent_soft"], bar=C["accent"]),
    "research":   dict(bg=C["soft"], bar=C["navy"]),
}


def hexcol(col):
    return "#%02X%02X%02X" % (int(col.red * 255), int(col.green * 255),
                              int(col.blue * 255))


def box_table(doc, bg, bar=None, border=None, width_mm=None):
    w = width_mm or K.LIVE_W
    barw = 1.2 if bar else 0.0
    t = doc.add_table(rows=1, cols=2 if bar else 1)
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    t.autofit = False
    K.no_table_borders(t)
    K.table_layout_fixed(t)
    widths = ([barw, w - barw] if bar else [w])
    for j, cw in enumerate(widths):
        K.cell_width(t.rows[0].cells[j], cw)
    for cell in t.rows[0].cells:
        K.cell_margins(cell, top=3, bottom=3, left=2.6, right=2.6)
        if bg:
            K.shade(cell._tc, bg)
    if border:
        for cell in t.rows[0].cells:
            K.cell_borders(cell, color=border, sz=4, top=border, bottom=border)
    if bar:
        K.shade(t.rows[0].cells[0]._tc, bar)
    body = t.rows[0].cells[-1]
    body.paragraphs[0].text = ""
    body.paragraphs[0].style = doc.styles["Callout"]
    return t, body


# ------------------------------------------------------------------ converter
class Converter:
    def __init__(self, doc):
        self.doc = doc
        self.body_started = False
        self.section = doc.sections[0]
        self.after_heading = True     # first body para sits flush, then indents

    # -------------------------------------------------------------- helpers
    def P(self, style, html=None):
        p = self.doc.add_paragraph(style=style)
        if html:
            style_run(p, style, html, self.doc)
        return p

    def body_style(self):
        """Indent every body paragraph except the one right after a heading."""
        return "Body First" if self.after_heading else "Body"

    def mark_heading(self):
        self.after_heading = True

    def mark_body(self):
        self.after_heading = False

    def page_break(self):
        """Hard page break as an empty, near-invisible paragraph."""
        p = self.doc.add_paragraph(style="Page Break")
        K.add_break(p, "page")
        return p

    def cell_para(self, cell, style, html=None):
        p = cell.add_paragraph(style=style)
        if html:
            style_run(p, style, html, self.doc)
        return p

    def add_section(self, fmt=None, start=None, mirrored=True):
        s = self.doc.add_section(WD_SECTION.NEW_PAGE)
        K.page_setup(s, mirrored=mirrored, fmt=fmt, start=start)
        for part in (s.header, s.footer, s.even_page_header, s.even_page_footer):
            part.is_linked_to_previous = False
            for p in part.paragraphs:
                p.text = ""
        self.section = s
        return s

    def start_front_matter(self):
        s = self.add_section(fmt="lowerRoman", start=1)
        # roman folio, centred, on the plain body frame
        for part in (s.footer, s.even_page_footer):
            part.is_linked_to_previous = False
            p = part.paragraphs[0]
            p.text = ""
            p.alignment = AL.CENTER
            K.add_field(p, "PAGE", "i", SANS, 8.5, C["grey"])

    def start_body(self):
        s = self.add_section(fmt="decimal", start=1)
        K.running_head(s, "TUNTAS 7D", "")
        K.add_folio(s)
        self.body_started = True

    # -------------------------------------------------------------- dispatch
    def run(self, story):
        pages = self.page_starts(story)
        for i, f in enumerate(story):
            self.one(f, first=True, start_page=(i in pages))
        return self.doc

    def page_starts(self, story):
        """Indices of flowables that should begin a fresh page.

        A ``PageBreak`` in the source only marks a page boundary when the item
        after it is *not* already page-breaking (a Heading 1, a new part, a full
        page divider). Filtering those out keeps the Word file free of the empty
        pages the source emits to mimic openers.
        """
        starts = set()
        for i, f in enumerate(story):
            if type(f).__name__ != "PageBreak":
                continue
            j = i + 1
            while j < len(story) and type(story[j]).__name__ in (
                    "PageBreak", "NextPageTemplate", "Spacer"):
                j += 1
            if j >= len(story):
                continue
            nxt = type(story[j]).__name__
            if nxt in ("H", "PartDivider", "ChapterOpener", "StatementPage",
                       "FrontCover", "TitlePage", "CreditsPage", "BackCoverPage",
                       "TableOfContents", "KeepTogether"):
                if nxt == "H":
                    if story[j].style.name == "h2" and \
                            not self.CHAPTER_RE.match(plain(story[j].text)):
                        starts.add(j)
                elif nxt in ("PartDivider", "ChapterOpener", "StatementPage"):
                    starts.add(j)
                else:
                    starts.add(j)
        return starts

    def one(self, f, first=False, start_page=False):
        name = type(f).__name__
        if start_page:
            self.page_break()
        if name == "NextPageTemplate":
            action = getattr(f, "action", None)
            tpl = None
            if action:
                try:
                    tpl = action[1]
                except Exception:
                    tpl = None
            if tpl == "body" and not self.body_started:
                self.start_body()
            return
        if name in ("PageBreak",):
            return
        if name == "Spacer":
            self.P("Gap")
            return
        if name in ("H", "Paragraph"):
            return self.heading_or_para(f, first)
        if name == "Boxed":
            return self.boxed(f)
        if name == "_Banner":
            return self.banner(f)
        if name == "StatRow":
            return self.statrow(f)
        if name == "PullQuote":
            p = self.P("Pull Quote")
            write_markup(p, getattr(f.para, "text", ""), SERIF, 14, C["navy"],
                         italic=True)
            return
        if name == "Figure":
            return self.figure(f)
        if name == "QRPanel":
            return self.qr(f)
        if name == "Table":
            return self.table(f)
        if name in ("WriteLines", "WSHeader", "_Grid"):
            return self.ws_primitive(f, name)
        if name == "HRule":
            p = self.P("Rule")
            K.para_border(p, color=C["line"], sz=6, bottom=True)
            K.add_run(p, "", SANS, 2, color=C["line"])
            return
        if name == "PartDivider":
            return self.part_divider(f)
        if name == "ChapterOpener":
            return self.chapter_opener(f)
        if name == "StatementPage":
            return self.statement(f)
        if name == "KeepTogether":
            for child in getattr(f, "_content", []):
                self.one(child, first)
            return
        if name == "TableOfContents":
            K.add_toc(self.doc, "1-3")
            return
        if name in ("FrontCover", "BackCoverPage", "TitlePage", "CreditsPage"):
            return self.front(name, f)
        if name in ("PageImage",):
            return
        txt = getattr(f, "text", None)
        if txt:
            st = self.body_style()
            self.mark_body()
            p = self.P(st)
            write_markup(p, txt, SERIF, 10, C["ink"])

    # -------------------------------------------------------------- headings
    CHAPTER_RE = re.compile(
        r"^(Bab \d|Prolog|Epilog|Kata Pengantar|Cara Membaca|Tes Diagnostik|"
        r"Peta lengkap|Bank Studi Kasus|Program 30|Daftar Pustaka|Indeks Alat|"
        r"Akses Toolkit|Tentang Penulis|Catatan Perjalanan|Lembar Kerja Cepat|"
        r"Lampiran |Penutup bagian)")

    def heading_or_para(self, f, first):
        style = getattr(f, "style", None)
        sname = style.name if style is not None else "body"
        html = getattr(f, "text", "")
        is_h = type(f).__name__ == "H"

        if sname == "h2":
            if is_h and getattr(f, "_key", None) == "toc-head":
                return
            txt = plain(html)
            self.mark_heading()
            if self.CHAPTER_RE.match(txt):
                return self.P("Heading 1", html)
            return self.P("Heading 2", html)
        if sname == "h3":
            self.mark_heading()
            return self.P("Heading 3", html)
        if sname == "h4":
            self.mark_heading()
            return self.P("Heading 4", html)
        if sname == "eyebrow":
            self.mark_heading()
            return self.P("Eyebrow", html)
        if sname == "lead":
            return self.P("Lead", html)
        if sname in ("caption", "caption_c"):
            return self.P("Caption Center" if sname == "caption_c" else "Caption", html)
        if sname in ("bullet", "bullet_tight"):
            p = self.P("Bullet")
            K.add_run(p, "\u2022\t", SERIF, 10, color=C["accent"])
            write_markup(p, html, SERIF, 10, C["ink"])
            return
        if sname == "num":
            marker = (getattr(f, "bulletText", None) or "1.") + "\t"
            p = self.P("Numbered")
            K.add_run(p, marker, SERIF, 10, color=C["accent"])
            write_markup(p, html, SERIF, 10, C["ink"])
            return
        if sname == "quote":
            return self.P("Pull Quote", html)
        if sname == "label":
            return self.P("Label", html)
        if sname in ("box", "box_tight"):
            return self.P("Callout" if sname == "box" else "Callout Tight", html)
        if sname == "box_h":
            return self.P("Callout Head", html)
        if sname in ("box_bullet", "box_bullet_t"):
            p = self.P("Callout Bullet")
            K.add_run(p, "\u2022\t", SERIF, 9.5, color=C["accent"])
            write_markup(p, html, SERIF, 9.5, C["ink"])
            return
        if sname == "ws_h":
            return self.P("WS Label", html)
        if sname == "ws":
            return self.P("WS Hint", html)
        if sname == "tbl":
            return self.P("Table Text", html)
        if sname == "tbl_h":
            return self.P("Table Head", html)
        if sname == "stat":
            return self.P("Stat Number", html)
        if sname == "stat_l":
            return self.P("Stat Label", html)
        if sname == "ct":
            return self.P("Case Title", html)
        st = self.body_style()
        self.mark_body()
        return self.P(st, html)

    # -------------------------------------------------------------- boxes
    def kind_of(self, f):
        if f.bar is None:
            return ""
        hx = hexcol(f.bar)
        for k, v in BOX_STYLES.items():
            if v["bar"] == hx:
                return k
        return ""

    def boxed(self, f):
        if f.bg is not None:
            bg = hexcol(f.bg)
        else:
            bg = BOX_STYLES.get(self.kind_of(f), {}).get("bg", C["soft"])
        bar = hexcol(f.bar) if f.bar is not None else BOX_STYLES.get(
            self.kind_of(f), {}).get("bar")
        t, body = box_table(self.doc, bg, bar=bar)
        first = True
        for child in f.content:
            self.into_cell(child, body, first)
            first = False
        self.trim_cell(body)

    def trim_cell(self, cell):
        ps = cell.paragraphs
        while len(ps) > 1 and not ps[-1].text and not ps[-1].runs:
            ps[-1]._p.getparent().remove(ps[-1]._p)
            ps = cell.paragraphs

    def into_cell(self, child, cell, first):
        name = type(child).__name__
        if name in ("H", "Paragraph"):
            sname = child.style.name
            html = getattr(child, "text", "")
            if sname == "box_h":
                return self.cell_para(cell, "Callout Head", html)
            if sname in ("h2", "h3"):
                return self.cell_para(cell, "Heading 3", html)
            if sname == "h4":
                return self.cell_para(cell, "Heading 4", html)
            if sname == "ct":
                return self.cell_para(cell, "Case Title", html)
            if sname == "label":
                return self.cell_para(cell, "Label", html)
            if sname in ("caption", "caption_c"):
                return self.cell_para(cell, "Caption", html)
            if sname in ("box_bullet", "box_bullet_t", "bullet", "bullet_tight"):
                p = self.cell_para(cell, "Callout Bullet")
                marker = getattr(child, "bulletText", None) or "\u2022"
                K.add_run(p, marker + "\t", SERIF, 9.5, color=C["accent"])
                write_markup(p, html, SERIF, 9.5, C["ink"])
                return p
            if sname == "ws_h":
                return self.cell_para(cell, "WS Label", html)
            if sname == "ws":
                return self.cell_para(cell, "WS Hint", html)
            if sname == "tbl":
                return self.cell_para(cell, "Table Text", html)
            return self.cell_para(
                cell, "Callout" if sname == "box" else "Callout Tight", html)
        if name == "Spacer":
            return self.cell_para(cell, "Gap")
        if name == "Table":
            return self.table(child, cell=cell)
        if name in ("WriteLines", "WSHeader", "_Grid"):
            return self.ws_primitive(child, name, cell=cell)
        if name == "QRPanel":
            return self.qr(child, cell=cell)
        if name == "HRule":
            p = self.cell_para(cell, "Rule")
            K.para_border(p, color=C["line"], sz=6, bottom=True)
            K.add_run(p, "", SANS, 2, color=C["line"])
            return
        if name == "Boxed":
            return self.boxed_cell(child, cell)
        if name == "KeepTogether":
            for c in getattr(child, "_content", []):
                self.into_cell(c, cell, first)
            return
        self.one(child, first)

    def boxed_cell(self, f, cell):
        bg = hexcol(f.bg) if f.bg is not None else C["soft"]
        bar = hexcol(f.bar) if f.bar is not None else None
        nt = cell.add_table(rows=1, cols=2 if bar else 1)
        nt.autofit = False
        K.no_table_borders(nt)
        K.table_layout_fixed(nt)
        widths = [1.2, K.LIVE_W - 6.0] if bar else [K.LIVE_W - 5.0]
        for j, cw in enumerate(widths):
            K.cell_width(nt.rows[0].cells[j], cw)
        for c in nt.rows[0].cells:
            K.shade(c._tc, bg)
            K.cell_margins(c, top=2, bottom=2, left=2, right=2)
        if bar:
            K.shade(nt.rows[0].cells[0]._tc, bar)
        body = nt.rows[0].cells[-1]
        body.paragraphs[0].text = ""
        first = True
        for child in f.content:
            self.into_cell(child, body, first)
            first = False
        self.trim_cell(body)

    def banner(self, f):
        bg = hexcol(f.bg) if getattr(f, "bg", None) is not None else C["navy"]
        t, body = box_table(self.doc, bg)
        p = body.paragraphs[0]
        p.style = self.doc.styles["Pull Quote"]
        write_markup(p, getattr(f.p, "text", ""), SANS_B, 11.2, C["paper"], bold=True)

    def statrow(self, f):
        n = len(f.items)
        t = self.doc.add_table(rows=2, cols=n)
        t.alignment = WD_TABLE_ALIGNMENT.LEFT
        t.autofit = False
        K.no_table_borders(t)
        K.keep_table_together(t)
        for j, (num, lab) in enumerate(f.items):
            wmm = K.LIVE_W / n
            K.cell_width(t.rows[0].cells[j], wmm)
            K.cell_width(t.rows[1].cells[j], wmm)
            K.shade(t.rows[0].cells[j]._tc, C["soft"])
            K.shade(t.rows[1].cells[j]._tc, C["soft"])
            p0 = t.rows[0].cells[j].paragraphs[0]
            p0.style = self.doc.styles["Stat Number"]
            write_markup(p0, num, SANS_B, 17, C["accent"], bold=True)
            p1 = t.rows[1].cells[j].paragraphs[0]
            p1.style = self.doc.styles["Stat Label"]
            write_markup(p1, lab, SANS, 7.1, C["grey"])

    # -------------------------------------------------------------- tables
    def table(self, tbl, cell=None):
        data = tbl._cellvalues
        nrows = len(data)
        ncols = len(data[0]) if data else 0
        total = K.LIVE_W - (0 if cell is None else 5.0)
        widths = list(tbl._colWidths or [total / ncols] * ncols)
        scale = total / sum(widths)
        widths = [w * scale for w in widths]
        hdr_fill = C["teal"]
        for c in getattr(tbl, "_bkgrndcmds", []):
            if isinstance(c, tuple) and c[0] == "BACKGROUND" and c[1][0] == 0:
                hdr_fill = hexcol(c[3])
        t = cell.add_table(rows=nrows, cols=ncols) if cell is not None \
            else self.doc.add_table(rows=nrows, cols=ncols)
        t.alignment = WD_TABLE_ALIGNMENT.LEFT
        t.autofit = False
        K.table_layout_fixed(t)
        K.keep_table_together(t)
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                c = t.rows[i].cells[j]
                K.cell_width(c, widths[j])
                K.cell_margins(c, top=1.8, bottom=1.8, left=2.0, right=2.0)
                p = c.paragraphs[0]
                p.style = self.doc.styles["Table Head" if i == 0 else "Table Text"]
                html = getattr(val, "text", str(val))
                write_markup(p, html, SANS_B if i == 0 else SERIF,
                             8.4 if i == 0 else 8.8,
                             C["paper"] if i == 0 else C["ink"])
                if i == 0:
                    K.shade(c._tc, hdr_fill)
                elif i % 2 == 0:
                    K.shade(c._tc, C["soft"])
                K.cell_borders(c, color=C["grey_light"], sz=4,
                               top=C["grey_light"], bottom=C["grey_light"])
        return t

    # -------------------------------------------------------------- worksheet
    def ws_primitive(self, f, name, cell=None):
        doc = self.doc
        if name == "WSHeader":
            t = (cell.add_table(rows=1, cols=1) if cell is not None
                 else doc.add_table(rows=1, cols=1))
            t.autofit = False
            K.no_table_borders(t)
            K.table_layout_fixed(t)
            c = t.rows[0].cells[0]
            K.cell_width(c, K.LIVE_W)
            K.shade(c._tc, C["deep"])
            K.cell_margins(c, top=3, bottom=3, left=3, right=3)
            p = c.paragraphs[0]
            p.style = doc.styles["WS Code"]
            K.add_run(p, f.code.upper(), SANS_B, 7.6, bold=True, color=C["accent"])
            q = c.add_paragraph(style="WS Head")
            K.add_run(q, f.title, SERIF, 14, bold=True, color=C["paper"])
            r = c.add_paragraph(style="WS Head")
            K.add_run(r, f.subtitle, SANS, 7.8, color="#B9C2D4")
            return t
        if name == "WriteLines":
            t = (cell.add_table(rows=f.n, cols=1) if cell is not None
                 else doc.add_table(rows=f.n, cols=1))
            t.autofit = False
            K.no_table_borders(t)
            K.table_layout_fixed(t)
            for row in t.rows:
                c = row.cells[0]
                K.cell_width(c, K.LIVE_W - (0 if cell is None else 5.0))
                c.paragraphs[0].style = doc.styles["Gap"]
                c.paragraphs[0].text = ""
                K.cell_margins(c, top=1.0, bottom=1.0, left=0, right=0)
                K.cell_borders(c, color=C["grey_light"], sz=4, bottom=C["grey_light"])
                trPr = row._tr.get_or_add_trPr()
                h = OxmlElement("w:trHeight")
                h.set(qn("w:val"), str(int(f.gap * 20)))
                h.set(qn("w:hRule"), "atLeast")
                trPr.append(h)
            return t
        if name == "_Grid":
            cols = f.cols
            rows = (f.n + cols - 1) // cols
            t = (cell.add_table(rows=rows, cols=cols) if cell is not None
                 else doc.add_table(rows=rows, cols=cols))
            t.autofit = False
            K.no_table_borders(t)
            K.table_layout_fixed(t)
            for row in t.rows:
                for c in row.cells:
                    K.cell_width(c, (K.LIVE_W - (0 if cell is None else 5.0)) / cols)
                    K.cell_borders(c, color=C["grey_light"], sz=4,
                                   top=C["grey_light"], bottom=C["grey_light"],
                                   left=C["grey_light"], right=C["grey_light"])
                    c.paragraphs[0].style = doc.styles["Gap"]
                    c.paragraphs[0].text = ""
                trPr = row._tr.get_or_add_trPr()
                h = OxmlElement("w:trHeight")
                h.set(qn("w:val"), str(int(13.5 * 20)))
                h.set(qn("w:hRule"), "atLeast")
                trPr.append(h)
            return t
        return None

    # -------------------------------------------------------------- QR
    def qr(self, panel, cell=None):
        path = qr_png(panel.url)
        if cell is not None:
            p = cell.add_paragraph(style="Callout")
            p.alignment = AL.LEFT
            r = p.add_run()
            r.add_picture(path, width=Mm(18))
            K.add_run(p, "  " + panel.code.upper(), SANS_B, 7.6, bold=True,
                      color=C["accent"], caps=True)
            q = cell.add_paragraph(style="Callout Head")
            K.add_run(q, panel.title, SERIF, 11, bold=True, color=C["navy"])
            r2 = cell.add_paragraph(style="Callout Tight")
            K.add_run(r2, panel.subtitle + "  \u2022  " + panel.url, SANS, 7.8,
                      color=C["grey"])
            return
        t = self.doc.add_table(rows=1, cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.LEFT
        t.autofit = False
        K.no_table_borders(t)
        K.table_layout_fixed(t)
        K.keep_table_together(t)
        c0, c1 = t.rows[0].cells
        K.cell_width(c0, 26)
        K.cell_width(c1, K.LIVE_W - 26)
        for c in (c0, c1):
            K.cell_margins(c, top=3, bottom=3, left=3, right=3)
            K.shade(c._tc, C["soft"])
        p = c0.paragraphs[0]
        p.style = self.doc.styles["Caption Center"]
        p.add_run().add_picture(path, width=Mm(20))
        c1.paragraphs[0].text = ""
        q = c1.paragraphs[0]
        q.style = self.doc.styles["Callout Tight"]
        K.add_run(q, panel.code.upper(), SANS_B, 7.6, bold=True, color=C["accent"],
                  caps=True)
        q2 = c1.add_paragraph(style="Callout Head")
        K.add_run(q2, panel.title, SERIF, 11.5, bold=True, color=C["navy"])
        q3 = c1.add_paragraph(style="Callout Tight")
        K.add_run(q3, panel.subtitle, SANS, 7.9, color=C["grey"])
        q4 = c1.add_paragraph(style="Callout Tight")
        K.add_run(q4, panel.url, SANS_B, 7.9, bold=True, color=C["teal"])
        self.trim_cell(c1)

    # -------------------------------------------------------------- openers
    def figure(self, f):
        img = self.render_figure(f)
        if img is None:
            return
        p = self.P("Caption Center")
        p.add_run().add_picture(img, width=Mm(141))
        if f.caption:
            c = self.P("Caption Center")
            write_markup(c, f.caption, SANS, 8.2, C["grey"])

    def render_figure(self, f):
        """Rasterise a ReportLab drawing callback so Word can show it."""
        import hashlib
        from reportlab.pdfgen import canvas as rl_canvas
        w = K.LIVE_W_PT                   # points, matches the text column
        h = max(10.0, float(f._fh))
        key = hashlib.md5()
        key.update(type(f).__name__.encode())
        key.update(repr(getattr(f, "caption", "")).encode())
        key.update(("%.1f" % h).encode())
        out = os.path.join(FIG_DIR, key.hexdigest()[:20] + ".png")
        if os.path.exists(out):
            return out
        os.makedirs(FIG_DIR, exist_ok=True)
        tmp = out + ".pdf"
        c = rl_canvas.Canvas(tmp, pagesize=(w, h))
        try:
            f.drawer(c, w, h)
        except Exception:
            return None
        c.showPage()
        c.save()
        import pypdfium2 as pdfium
        pdf = pdfium.PdfDocument(tmp)
        pdf[0].render(scale=3.2).to_pil().save(out)
        pdf.close()
        os.remove(tmp)
        return out

    def part_divider(self, f):
        self.start_body()
        self.P("Gap")
        self.P("Part Kicker", plain(f.kicker.upper()))
        self.P("Part Title", plain(f.title))
        if f.blurb:
            self.P("Part Blurb", plain(f.blurb))
        p = self.P("Rule")
        K.para_border(p, color=C["accent"], sz=12, bottom=True)
        K.add_run(p, "", SANS, 2, color=C["accent"])

    def chapter_opener(self, f):
        self.P("Gap"); self.P("Gap")
        self.P("Part Kicker", "%s  \u00b7  BAB %s" % (plain(f.kicker).upper(), f.number))
        self.P("Part Title", plain(f.title))
        self.P("Lead", plain(f.subtitle))
        t, body = box_table(self.doc, C["accent_soft"], bar=C["accent"])
        p = body.paragraphs[0]
        p.style = self.doc.styles["Pull Quote"]
        write_markup(p, f.promise, SERIF, 11.4, C["navy"], italic=True)
        self.P("Gap")
        p = self.P("Label")
        K.add_run(p, "PETA BAB INI", SANS_B, 7.8, bold=True, color=C["accent"])
        for item in f.map_items:
            b = self.P("Bullet")
            K.add_run(b, "\u2022\t", SERIF, 9.4, color=C["accent"])
            write_markup(b, item, SERIF, 9.4, C["ink"])

    def statement(self, f):
        self.P("Gap"); self.P("Gap")
        self.P("Part Kicker", plain(f.kicker.upper()))
        self.P("Part Title", plain(f.title))
        for para in re.split(r"\n\n+", str(f.body).strip()):
            self.P("Lead", plain(para))
        if f.foot:
            self.P("Caption", plain(f.foot))

    # -------------------------------------------------------------- front
    def front(self, name, f):
        if name == "FrontCover":
            self.P("Gap")
            self.P("Part Kicker", "PANDUAN PRAKTIS")
            p = self.P("Part Title")
            K.add_run(p, "TUNTAS ", SERIF, 44, bold=True, color=C["navy"])
            K.add_run(p, "7D", SERIF, 44, bold=True, color=C["accent"])
            self.P("Lead", "Solusi Sistematis")
            self.P("Lead", "Menyelesaikan Masalah dengan Cara yang Terbukti, "
                           "dari Akar sampai Hasil")
            self.P("Caption", "UNTUK INDIVIDU, TIM, DAN ORGANISASI")
            p = self.P("Label")
            K.add_run(p, "D1 Detect  \u00b7  D2 Define  \u00b7  D3 Dig  \u00b7  "
                         "D4 Design  \u00b7  D5 Decide  \u00b7  D6 Do  \u00b7  D7 Drive",
                      SANS_B, 9, bold=True, color=C["accent"])
            p = self.P("Caption")
            K.add_run(p, "12 studi kasus nyata  \u00b7  37 kerangka visual siap pakai  "
                         "\u00b7  14 worksheet latihan + toolkit QR  \u00b7  "
                         "1 agenda workshop", SANS, 8.6, color=C["ink"])
            p = self.P("Caption")
            K.add_run(p, "TUNTAS PRESS  \u00b7  Edisi Praktisi \u00b7 Bahasa Indonesia "
                         "\u00b7 B5", SANS, 8, color=C["grey"])
        elif name == "TitlePage":
            variant = getattr(f, "variant", "title")
            if variant == "halftitle":
                self.P("Gap")
                self.P("Part Title", "TUNTAS 7D")
                self.P("Lead", "Solusi Sistematis")
            else:
                self.P("Gap")
                self.P("Part Title", "TUNTAS 7D")
                self.P("Lead", "Solusi Sistematis")
                self.P("Caption", "Menyelesaikan Masalah dengan Cara yang Terbukti, "
                                  "dari Akar sampai Hasil")
                self.P("Caption", "TUNTAS PRESS \u00b7 Edisi Praktisi \u00b7 "
                                  "Bahasa Indonesia")
        elif name == "CreditsPage":
            for line in CREDITS:
                if line.startswith("# "):
                    self.P("Colophon Head", line[2:])
                elif line:
                    self.P("Colophon", line)
        elif name == "BackCoverPage":
            self.P("Gap")
            self.P("Part Title", "TUNTAS 7D")
            self.P("Lead", "Solusi Sistematis")
            self.P("Gap")
            for para in BACK_BLURB:
                self.P("Colophon", para)
            p = self.P("Label")
            K.add_run(p, "ISI UTAMA", SANS_B, 7.6, bold=True, color=C["accent"])
            for b in BACK_BULLETS:
                bp = self.P("Bullet")
                K.add_run(bp, "\u2022\t", SERIF, 9.6, color=C["accent"])
                write_markup(bp, b, SERIF, 9.6, C["ink"])
            self.P("Caption", "Cocok untuk: Manajer \u00b7 Konsultan \u00b7 Fasilitator "
                              "\u00b7 Pemilik usaha \u00b7 Praktisi perbaikan \u00b7 "
                              "Siapa saja yang lelah menambal gejala")
            self.P("Caption", "Praktikal, berbasis data, dan bisa langsung dijalankan "
                              "tanpa perangkat lunak.")
            path = qr_png("https://tuntas7d.id/toolkit")
            pc = self.P("Caption Center")
            pc.add_run().add_picture(path, width=Mm(22))
            self.P("Caption Center", "SCAN UNTUK TOOLKIT  \u00b7  tuntas7d.id/toolkit")
            p = self.P("Caption")
            K.add_run(p, "TUNTAS PRESS  \u00b7  Buku kerja praktis \u00b7 "
                         "Edisi Bahasa Indonesia \u00b7 B5", SANS, 7.6, color=C["grey"])


def qr_png(url):
    os.makedirs(QR_DIR, exist_ok=True)
    import segno
    fn = os.path.join(QR_DIR, re.sub(r"[^a-zA-Z0-9]", "_", url)[:60] + ".png")
    segno.make(url, error="m").save(fn, scale=12, border=1)
    return fn


# ------------------------------------------------------------------ text data
CREDITS = [
    "# Tentang buku ini",
    "Buku ini menawarkan satu kerangka kerja bernama TUNTAS 7D: tujuh langkah yang "
    "menyusun cara berpikir dan cara bekerja ketika menghadapi masalah. Pendekatannya "
    "menggabungkan tradisi perbaikan berkelanjutan, riset pengambilan keputusan, dan "
    "praktik konsultan internasional, lalu diterjemahkan menjadi alat yang bisa "
    "langsung dipakai.",
    "",
    "# Cara memakai",
    "Setiap bab langkah memakai urutan yang sama: cerita pembuka, konsep inti dengan "
    "gambar rangka, alat praktis langkah demi langkah, studi kasus nyata, dan "
    "worksheet. Untuk workshop, pakai Bab 12 sebagai panduan fasilitator.",
    "",
    "# Catatan tentang kasus",
    "Studi kasus dalam buku ini disusun dari pola yang berulang di banyak organisasi. "
    "Nama lembaga, angka, dan kutipan disajikan sebagai ilustrasi yang telah disusun "
    "ulang agar aman dipublikasikan. Pola masalah, logika analisis, dan bentuk "
    "solusinya mengikuti praktik yang lazim dipakai oleh praktisi perbaikan dan "
    "konsultan.",
    "",
    "# Referensi",
    "Daftar pustaka ilmiah dan sumber praktik tersedia di bagian penutup. Setiap alat "
    "yang diperkenalkan di buku ini dapat ditelusuri asal-usulnya melalui daftar "
    "tersebut.",
    "",
    "Versi digital buku ini dilengkapi tautan dan kode QR menuju worksheet, template, "
    "dan toolkit yang bisa diunduh.",
]

BACK_BLURB = [
    "Orang pintar sering gagal menyelesaikan masalah \u2014 bukan karena kurang cerdas, "
    "tetapi karena salah mendiagnosis. Buku ini mengubah cara Anda menghadapi masalah: "
    "dari melompat ke solusi menjadi menelusuri akar, memilih dengan kriteria, dan "
    "mengunci hasil agar tidak terulang.",
]

BACK_BULLETS = [
    "7 langkah teruji: Detect, Define, Dig, Design, Decide, Do, Drive",
    "12 studi kasus nyata lengkap dengan angka dan hasil",
    "14 worksheet latihan siap pakai + toolkit digital via QR",
    "Agenda workshop satu hari untuk langsung diterapkan ke tim",
    "Fondasi ilmiah: bias kognitif, analisis akar, dan pengambilan keputusan",
]


# ------------------------------------------------------------------ build
def build(out_path, story=None):
    doc = build_document()
    sec = doc.sections[0]
    K.page_setup(sec, mirrored=True)
    K.enable_even_odd_headers(doc)
    for part in (sec.header, sec.footer, sec.even_page_header, sec.even_page_footer):
        part.is_linked_to_previous = False
        for p in part.paragraphs:
            p.text = ""

    doc.core_properties.title = "TUNTAS 7D \u2014 Solusi Sistematis"
    doc.core_properties.author = "Tuntas Press"
    doc.core_properties.language = "id-ID"

    story = story or capture_story()
    conv = Converter(doc)
    conv.section = sec
    conv.run(story)
    doc.save(out_path)
    return out_path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        ROOT, "output", "TUNTAS-7D.docx")
    build(out)
    print("BUILT", out)
