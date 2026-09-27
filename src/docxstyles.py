"""Named paragraph/character styles for the TUNTAS 7D Word interior.

All indentation and spacing lives in these styles so the manuscript carries no
stray tabs or blank lines. Body paragraphs get a "ketukan" (first-line indent)
worth exactly three spaces of the 10 pt Lora body face — applied as a paragraph
style indent, which is what trade-book editors expect rather than literal
spaces or tabs. The built-in ``Heading 1/2/3`` styles are restyled in place so
Word's automatic table of contents (``TOC \\o "1-3"``) picks up the chapter and
section structure.
"""
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Mm, Pt

import docxkit as K
from docxkit import C, SANS, SANS_B, SERIF, style_font, style_para

BODY_SIZE = 10.0
BODY_LEAD = 1.28          # multiple of single line height (~12.8pt from 10pt)
# First-line indent ("ketukan") equal to three spaces of the 10 pt Lora body
# face, in millimetres. Kept as a style property, not literal spaces.
INDENT_3SP = 2.7834


def _update_fields_on_open(doc):
    """Ask Word to refresh the table of contents when the file is opened."""
    settings = doc.settings.element
    if settings.find(qn("w:updateFields")) is None:
        el = OxmlElement("w:updateFields")
        el.set(qn("w:val"), "true")
        settings.append(el)


def build_document():
    doc = Document()
    _update_fields_on_open(doc)

    # ---------------------------------------------------------------- base
    normal = doc.styles["Normal"]
    style_font(normal, SERIF, BODY_SIZE, color=C["ink"])
    style_para(normal, align=AL.JUSTIFY, before=0, after=0, line=BODY_LEAD)
    normal.paragraph_format.first_line_indent = Mm(5.0)

    doc.styles["Default Paragraph Font"].font.name = SERIF

    def new(name, base="Normal"):
        if name in [s.name for s in doc.styles]:
            st = doc.styles[name]
            if base:
                st.base_style = doc.styles[base]
            return st
        st = doc.styles.add_style(name, 1)     # 1 = PARAGRAPH
        if base:
            st.base_style = doc.styles[base]
        st.quick_style = False
        return st

    def mk(name, font=SERIF, size=BODY_SIZE, *, bold=None, italic=None,
           color=C["ink"], align=AL.JUSTIFY, before=0, after=0, line=BODY_LEAD,
           indent=None, left=None, right=None, keep_next=False, keep=False,
           caps=False, spacing=None, contextual=False, base="Normal",
           page_break_before=False):
        st = new(name, base)
        style_font(st, font, size, bold=bold, italic=italic, color=color,
                   caps=caps, spacing=spacing)
        style_para(st, align=align, before=before, after=after, line=line,
                   first_indent=indent, left=left, right=right,
                   keep_next=keep_next, keep_lines=keep, contextual=contextual,
                   page_break_before=page_break_before)
        return st

    # ---------------------------------------------------------------- body
    # "Body" indents the first line by three spaces of the body face (the
    # requested "ketukan 3 spasi"); the paragraph right after a heading uses
    # "Body First", which sits flush.
    mk("Body", indent=INDENT_3SP)
    mk("Body First", indent=0)
    mk("Body Flush", align=AL.LEFT, indent=0)
    mk("Lead", size=11.6, color=C["navy"], align=AL.LEFT, line=1.25, after=6,
       indent=0)
    mk("Eyebrow", SANS_B, 7.6, bold=True, color=C["accent"], align=AL.LEFT,
       caps=True, spacing=0.6, after=4, indent=0)
    mk("Source", SANS, 8.0, color=C["grey"], align=AL.LEFT, indent=0, after=6)

    # ---------------------------------------------------------------- heads
    mk("Heading 1", SANS_B, 17, bold=True, color=C["navy"], align=AL.LEFT,
       before=0, after=10, line=1.05, indent=0, keep_next=True,
       page_break_before=True)
    mk("Heading 2", SANS_B, 12.5, bold=True, color=C["ink"], align=AL.LEFT,
       before=14, after=4, line=1.1, indent=0, keep_next=True)
    mk("Heading 3", SANS_B, 10.0, bold=True, color=C["teal"], align=AL.LEFT,
       before=10, after=2, line=1.1, indent=0, keep_next=True)
    mk("Heading 4", SANS_B, 9.2, bold=True, color=C["navy"], align=AL.LEFT,
       before=8, after=1, line=1.1, indent=0, keep_next=True)
    mk("Part Kicker", SANS_B, 9, bold=True, color=C["accent"], align=AL.LEFT,
       caps=True, spacing=1.4, indent=0, after=6)
    mk("Part Title", SERIF, 26, bold=True, color=C["navy"], align=AL.LEFT,
       before=0, after=10, line=1.04, indent=0, keep_next=True)
    mk("Part Blurb", SERIF, 12, italic=True, color=C["ink"], align=AL.LEFT,
       indent=0, after=8, line=1.3)

    # ---------------------------------------------------------------- lists
    bullet = mk("Bullet", align=AL.LEFT, left=6.5, indent=-3.5, after=0,
               contextual=True, line=1.22)
    bullet.paragraph_format.tab_stops.add_tab_stop(Mm(6.5))
    num = mk("Numbered", align=AL.LEFT, left=7.5, indent=-4.5, after=0,
             contextual=True, line=1.22)
    num.paragraph_format.tab_stops.add_tab_stop(Mm(7.5))

    # ---------------------------------------------------------------- quotes
    q = mk("Pull Quote", SERIF, 14, italic=True, color=C["navy"],
           align=AL.LEFT, left=6, right=3, before=10, after=10, line=1.3,
           indent=0, keep=True)
    K.ruled(q.element, "left", C["accent"], sz=18, space=10)

    mk("Caption", SANS, 8.2, color=C["grey"], align=AL.LEFT, before=3,
       after=6, line=1.15, indent=0)
    mk("Caption Center", SANS, 8.2, color=C["grey"], align=AL.CENTER, before=3,
       after=6, line=1.15, indent=0)

    # ---------------------------------------------------------------- callout
    mk("Callout Head", SANS_B, 9.6, bold=True, color=C["ink"],
       align=AL.LEFT, indent=0, after=3, line=1.12)
    mk("Callout", SERIF, 9.5, align=AL.JUSTIFY, indent=0, after=4, line=1.22,
       contextual=True)
    mk("Callout Tight", SERIF, 9.5, align=AL.JUSTIFY, indent=0, after=1,
       line=1.22)
    mk("Callout Bullet", align=AL.LEFT, left=5.5, indent=-3.5, after=2,
       line=1.2)
    mk("Label", SANS_B, 7.4, bold=True, color=C["teal"], caps=True,
       align=AL.LEFT, indent=0, after=2, spacing=0.4)
    mk("Case Title", SERIF, 11.6, bold=True, color=C["navy"], align=AL.LEFT,
       indent=0, after=3, line=1.15)

    # ---------------------------------------------------------------- table
    mk("Table Text", SERIF, 8.8, align=AL.LEFT, indent=0, after=0, line=1.15)
    mk("Table Text C", SERIF, 8.8, align=AL.CENTER, indent=0, after=0, line=1.15)
    mk("Table Head", SANS_B, 8.4, bold=True, color=C["paper"], align=AL.LEFT,
       indent=0, after=0, line=1.1)
    mk("Stat Number", SANS_B, 17, bold=True, color=C["accent"],
       align=AL.CENTER, indent=0, after=0, line=1.0)
    mk("Stat Label", SANS, 7.1, color=C["grey"], align=AL.CENTER, indent=0,
       after=0, line=1.1)

    # ---------------------------------------------------------------- worksheet
    mk("WS Head", SANS_B, 10, bold=True, color=C["paper"], align=AL.LEFT,
       indent=0, after=0, line=1.1)
    mk("WS Code", SANS_B, 7.4, bold=True, color=C["accent"], caps=True,
       align=AL.LEFT, indent=0, after=1, spacing=0.6)
    mk("WS Label", SANS_B, 8.6, bold=True, color=C["navy"], align=AL.LEFT,
       indent=0, after=1, line=1.15)
    mk("WS Hint", SANS, 8.0, italic=True, color=C["grey"], align=AL.LEFT,
       indent=0, after=1)
    mk("Fill Line", SANS, 8.6, color=C["grey"], align=AL.LEFT, indent=0,
       after=0, line=1.0)
    mk("Checklist", SANS, 9.2, align=AL.LEFT, left=6, indent=-4.5, after=1,
       line=1.3)

    # ---------------------------------------------------------------- misc
    # invisible filler used to reproduce deliberate vertical space
    g =     mk("Gap", SANS, 1, align=AL.LEFT, indent=0, after=0, line=1.0)
    mk("Page Break", SANS, 1, align=AL.LEFT, indent=0, after=0, line=1.0)
    mk("Rule", SANS, 1, align=AL.LEFT, indent=0, after=0, line=1.0)
    mk("Colophon", SERIF, 9.2, align=AL.LEFT, indent=0, after=5, line=1.25)
    mk("Colophon Head", SANS_B, 8.4, bold=True, color=C["navy"],
       align=AL.LEFT, indent=0, before=8, after=2, caps=True, spacing=0.5)

    # TOC heading restyle
    t = doc.styles["TOC Heading"]
    style_font(t, SANS_B, 17, bold=True, color=C["navy"])
    style_para(t, align=AL.LEFT, before=0, after=10, first_indent=0, keep_next=True)

    return doc
