"""Word (DOCX) layout toolkit for the TUNTAS 7D interior.

This is the DOCX counterpart to ``theme`` + ``engine``: page geometry, named
paragraph styles, and the low-level OOXML helpers Word needs for a book-quality
interior (mirrored margins, running heads, shaded callout boxes, leader-dot TOC,
lower-roman front matter).

Design follows standard trade-publishing practice:

* Body text is a serif, justified, with a first-line indent and *no* extra space
  between paragraphs (a blank line plus an indent would double the separation).
* Every paragraph indent is applied through the style, never with tabs or spaces,
  so the file stays clean if it is re-flowed in InDesign later.
* Headings use a sans face for contrast; chapter titles start on a new page.
* Callouts, tables and worksheets are real Word tables/frames, not text art.
"""
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt, RGBColor

# ------------------------------------------------------------------ geometry
PAGE_W = 176.0          # B5 width, mm
PAGE_H = 250.0          # B5 height, mm
MARGIN_INNER = 20.0     # spine side
MARGIN_OUTER = 15.0
MARGIN_TOP = 17.0
MARGIN_BOTTOM = 17.0
GUTTER = 0.0
LIVE_W = PAGE_W - MARGIN_INNER - MARGIN_OUTER
LIVE_W_PT = LIVE_W * 72.0 / 25.4      # same column, in PostScript points

# ------------------------------------------------------------------ palette
C = {
    "ink": "#141821",
    "navy": "#152746",
    "deep": "#0C1B33",
    "accent": "#E8503A",
    "accent_soft": "#FDEAE6",
    "teal": "#0F7B6C",
    "teal_soft": "#E3F2EF",
    "amber": "#C98A0B",
    "amber_soft": "#FDF3DC",
    "violet": "#5B4B9E",
    "violet_soft": "#EDE9F7",
    "grey": "#6C7480",
    "grey_light": "#E4E7EC",
    "paper": "#FFFFFF",
    "soft": "#F6F4EF",
    "cream": "#FBF9F4",
    "line": "#D8D3C7",
    "green": "#1E7A45",
    "green_soft": "#E4F3E9",
    "red": "#B3331F",
    "red_soft": "#FBE7E3",
}

SERIF = "Lora"
SERIF_IT = "Lora"
SANS = "Inter"
SANS_B = "Inter"

# ------------------------------------------------------------------ fonts
# ``register_fonts`` in engine.py loads the TTFs for ReportLab. Word reads fonts
# by name from the host, so here we only need the family names above. The
# bundled files in assets/fonts are the ones a reader should install to see the
# book exactly as designed (both are free Google fonts).


def rgb(hexstr):
    if isinstance(hexstr, RGBColor):
        return hexstr
    h = str(hexstr).lstrip("#")
    if len(h) != 6:
        h = h.ljust(6, "0")[:6]
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def _set(el, tag, **attrs):
    child = OxmlElement(tag)
    for k, v in attrs.items():
        child.set(qn("w:" + k), str(v))
    el.append(child)
    return child


def _rpr_fonts(rpr, name, mono=None):
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        rpr.insert(0, fonts)
    for a in ("ascii", "hAnsi", "cs", "eastAsia"):
        fonts.set(qn("w:" + a), name)


def style_font(style, name, size=None, bold=None, italic=None, color=None,
               caps=False, spacing=None):
    """Configure a named style's type."""
    f = style.font
    f.name = name
    if size is not None:
        f.size = Pt(size)
    if bold is not None:
        f.bold = bold
    if italic is not None:
        f.italic = italic
    if color is not None:
        f.color.rgb = rgb(color)
    rpr = style.element.get_or_add_rPr()
    _rpr_fonts(rpr, name)
    if caps:
        _set(rpr, "w:caps", val="1")
    if spacing is not None:
        _set(rpr, "w:spacing", val=str(int(spacing * 20)))


def style_para(style, align=None, before=None, after=None, line=None,
               first_indent=None, left=None, right=None, keep_next=False,
               keep_lines=False, widow=True, contextual=False,
               page_break_before=False):
    p = style.paragraph_format
    if align is not None:
        p.alignment = align
    if before is not None:
        p.space_before = Pt(before)
    if after is not None:
        p.space_after = Pt(after)
    if line is not None:
        p.line_spacing = line
        p.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    if first_indent is not None:
        p.first_line_indent = Mm(first_indent)
    if left is not None:
        p.left_indent = Mm(left)
    if right is not None:
        p.right_indent = Mm(right)
    if page_break_before:
        p.page_break_before = True
    p.keep_with_next = keep_next
    p.keep_together = keep_lines
    p.widow_control = widow
    if contextual:
        _set(style.element.get_or_add_pPr(), "w:contextualSpacing", val="1")


def shade(element, fill):
    """Apply ``w:shd`` to a cell's tcPr or a paragraph's pPr."""
    if element.tag == qn("w:tc"):
        pr = element.get_or_add_tcPr()
    else:
        pr = element.get_or_add_pPr()
    _set(pr, "w:shd", val="clear", color="auto", fill=fill.lstrip("#"))


def cell_margins(cell, top=0, bottom=0, left=0, right=0):
    tcPr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for tag, val in (("top", top), ("start", left), ("bottom", bottom),
                     ("end", right)):
        m = OxmlElement("w:" + tag)
        m.set(qn("w:w"), str(int(val * 56.7)))   # mm -> twips (approx)
        m.set(qn("w:type"), "dxa")
        mar.append(m)
    tcPr.append(mar)


def cell_borders(cell, color=None, sz=6, left=None, left_sz=None,
                 top=None, bottom=None, right=None):
    """Borders on a table cell; ``left`` may carry an accent bar."""
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    spec = {"top": top, "bottom": bottom, "start": left, "end": right}
    for edge, col in spec.items():
        e = OxmlElement("w:" + edge)
        if col:
            e.set(qn("w:val"), "single")
            e.set(qn("w:sz"), str(left_sz if edge == "start" and left_sz else sz))
            e.set(qn("w:space"), "0")
            e.set(qn("w:color"), col.lstrip("#"))
        else:
            e.set(qn("w:val"), "nil")
        borders.append(e)
    # vertical inside borders off by default
    tcPr.append(borders)


def no_table_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "start", "bottom", "end", "insideH", "insideV"):
        e = OxmlElement("w:" + edge)
        e.set(qn("w:val"), "nil")
        borders.append(e)
    tblPr.append(borders)


def keep_table_together(table):
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        _set(trPr, "w:cantSplit", val="1")


def cell_width(cell, mm):
    cell.width = Mm(mm)


def table_layout_fixed(table):
    tblPr = table._tbl.tblPr
    _set(tblPr, "w:tblLayout", type="fixed")


# ------------------------------------------------------------------ sections
def page_setup(section, mirrored=True, fmt=None, start=None):
    s = section
    s.page_width = Mm(PAGE_W)
    s.page_height = Mm(PAGE_H)
    if mirrored:
        s.left_margin = Mm(MARGIN_INNER)
        s.right_margin = Mm(MARGIN_OUTER)
        s.gutter = Mm(GUTTER)
        _set(s._sectPr, "w:mirrorMargins")
    else:
        s.left_margin = Mm(MARGIN_OUTER)
        s.right_margin = Mm(MARGIN_OUTER)
    s.top_margin = Mm(MARGIN_TOP)
    s.bottom_margin = Mm(MARGIN_BOTTOM)
    s.header_distance = Mm(9)
    s.footer_distance = Mm(9)
    if fmt or start is not None:
        pg = _set(s._sectPr, "w:pgNumType", fmt=fmt or "decimal")
        if start is not None:
            pg.set(qn("w:start"), str(start))


def columns(section, num=1, space_mm=6.0):
    sectPr = section._sectPr
    old = sectPr.find(qn("w:cols"))
    if old is not None:
        sectPr.remove(old)
    cols = OxmlElement("w:cols")
    cols.set(qn("w:num"), str(num))
    cols.set(qn("w:space"), str(int(space_mm * 56.7)))
    cols.set(qn("w:equalWidth"), "1")
    sectPr.append(cols)


def running_head(section, book_title, chapter, odd=True):
    """Set one header variant. Row of text with an outer page number."""
    hdr = section.header
    hdr.is_linked_to_previous = False
    p = hdr.paragraphs[0]
    p.text = ""
    pf = p.paragraph_format
    pf.space_after = Pt(0)
    pf.space_before = Pt(0)
    # tab stop at the far right of the live area
    p.paragraph_format.tab_stops.add_tab_stop(Mm(LIVE_W), WD_TAB_ALIGNMENT.RIGHT)
    add_run(p, book_title.upper() if odd else chapter.upper(),
            SANS, 6.8, color=C["grey"], spacing=0.2)
    add_run(p, "\t" + (chapter.upper() if odd else book_title.upper()),
            SANS, 6.8, color=C["grey"], spacing=0.2)
    set_header_rule(p)


def add_folio(section, roman=False):
    """Paragraph-number footer at the outer edge."""
    ftr = section.footer
    ftr.is_linked_to_previous = False
    p = ftr.paragraphs[0]
    p.text = ""
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    add_run(p, "", SANS, 7.6, color=C["grey"])
    add_field(p, "PAGE", "1", SANS, 7.6, color=C["grey"])


def clear_header_footer(section):
    for part in (section.header, section.footer):
        part.is_linked_to_previous = False
        for p in part.paragraphs:
            p.text = ""


def set_header_rule(p):
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "4")
    bottom.set(qn("w:space"), "4")
    bottom.set(qn("w:color"), C["grey_light"].lstrip("#"))
    pbdr.append(bottom)
    pPr.append(pbdr)


def enable_even_odd_headers(doc):
    settings = doc.settings.element
    _set(settings, "w:evenAndOddHeaders")


def blank_section(doc, before_index):
    """Insert a page break *within* a section (no new sectPr)."""
    p = doc.add_paragraph()
    add_break(p, "page")
    return p


def add_break(paragraph, kind="page"):
    run = paragraph.add_run()
    br = OxmlElement("w:br")
    br.set(qn("w:type"), kind)
    run._r.append(br)
    return run


# ------------------------------------------------------------------ runs/text
def add_run(p, text, font=None, size=None, bold=None, italic=None,
            color=None, caps=False, spacing=None, underline=None, strike=None):
    r = p.add_run(text)
    if font:
        r.font.name = font
        _rpr_fonts(r._r.get_or_add_rPr(), font)
    if size is not None:
        r.font.size = Pt(size)
    if bold is not None:
        r.font.bold = bold
    if italic is not None:
        r.font.italic = italic
    if color:
        r.font.color.rgb = rgb(color)
    if underline:
        r.font.underline = True
    if strike:
        r.font.strike = True
    rpr = r._r.get_or_add_rPr()
    if caps:
        _set(rpr, "w:caps", val="1")
    if spacing is not None:
        _set(rpr, "w:spacing", val=str(int(spacing * 20)))
    return r


def add_field(p, instr, placeholder="1", font=None, size=None, color=None):
    r1 = p.add_run()
    fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), "begin")
    r1._r.append(fc)
    r2 = p.add_run()
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve")
    it.text = " %s " % instr
    r2._r.append(it)
    r3 = p.add_run()
    fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), "separate")
    r3._r.append(fc)
    r4 = p.add_run(placeholder)
    r5 = p.add_run()
    fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), "end")
    r5._r.append(fc)
    for r in (r4,):
        if font:
            r.font.name = font
            _rpr_fonts(r._r.get_or_add_rPr(), font)
        if size is not None:
            r.font.size = Pt(size)
        if color:
            r.font.color.rgb = rgb(color)
    return p


def add_toc(doc, levels="1-3", switch_columns=False):
    p = doc.add_paragraph()
    p.style = doc.styles["TOC Heading"]
    add_run(p, "Daftar Isi", SANS_B, 17, color=C["navy"])
    body = doc.add_paragraph()
    body.paragraph_format.space_after = Pt(0)
    add_field(body, 'TOC \\o "%s" \\h \\z \\u' % levels,
              "Klik kanan lalu pilih \u201cUpdate Field\u201d untuk memuat daftar isi.",
              SANS, 9.6, color=C["ink"])
    return body


def _pPr_of(el):
    """Return the ``w:pPr`` of a paragraph *or* a paragraph style element."""
    if not hasattr(el, "tag"):          # a python-docx Paragraph wrapper
        el = el._p
    if el.tag == qn("w:p"):
        return el.get_or_add_pPr()
    pr = el.find(qn("w:pPr"))
    if pr is not None:
        return pr
    pr = OxmlElement("w:pPr")
    rpr = el.find(qn("w:rPr"))
    if rpr is not None:
        rpr.addprevious(pr)
    else:
        el.append(pr)
    return pr


def ruled(p, side="left", color=None, sz=18, space=8):
    pPr = _pPr_of(p)
    pbdr = pPr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = OxmlElement("w:pBdr")
        pPr.append(pbdr)
    e = OxmlElement("w:" + side)
    e.set(qn("w:val"), "single")
    e.set(qn("w:sz"), str(sz))
    e.set(qn("w:space"), str(space))
    e.set(qn("w:color"), (color or C["accent"]).lstrip("#"))
    pbdr.append(e)


def para_border(p, color=None, sz=6, top=False, bottom=False):
    pPr = _pPr_of(p)
    pbdr = pPr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = OxmlElement("w:pBdr")
        pPr.append(pbdr)
    for on, tag in ((top, "top"), (bottom, "bottom")):
        if not on:
            continue
        e = OxmlElement("w:" + tag)
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), str(sz))
        e.set(qn("w:space"), "4")
        e.set(qn("w:color"), (color or C["line"]).lstrip("#"))
        pbdr.append(e)
