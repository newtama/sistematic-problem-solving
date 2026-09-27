"""Layout engine: fonts, document template, box flowables, TOC scaffolding."""
import os
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Flowable,
    KeepTogether,
)
from reportlab.platypus.tableofcontents import TableOfContents

from theme import *  # noqa

FONT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "fonts")

_REGISTERED = False


def register_fonts():
    global _REGISTERED
    if _REGISTERED:
        return
    reg = {
        FONT_SERIF: "Lora-Regular.ttf",
        FONT_SERIF_B: "Lora-Bold.ttf",
        FONT_SERIF_IT: "Lora-Italic.ttf",
        FONT_SERIF_BI: "Lora-BoldItalic.ttf",
        FONT_SANS: "Inter-Regular.ttf",
        FONT_SANS_M: "Inter-Medium.ttf",
        FONT_SANS_SB: "Inter-SemiBold.ttf",
        FONT_SANS_B: "Inter-Bold.ttf",
    }
    for name, fn in reg.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fn)))
    pdfmetrics.registerFontFamily(
        FONT_SERIF, normal=FONT_SERIF, bold=FONT_SERIF_B,
        italic=FONT_SERIF_IT, boldItalic=FONT_SERIF_BI)
    pdfmetrics.registerFontFamily(
        FONT_SANS, normal=FONT_SANS, bold=FONT_SANS_B,
        italic=FONT_SANS, boldItalic=FONT_SANS_B)
    _REGISTERED = True


# =====================================================================
#  TEXT STYLES
# =====================================================================
def build_styles():
    S = {}
    S["body"] = ParagraphStyle(
        "body", fontName=FONT_SERIF, fontSize=SIZE_BODY, leading=LEAD_BODY,
        textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6.5,
        hyphenationLang="id_ID", embeddedHyphenation=1, splitLongWords=1)
    S["body_first"] = ParagraphStyle("body_first", parent=S["body"], spaceAfter=6.5)
    S["lead"] = ParagraphStyle(
        "lead", fontName=FONT_SERIF, fontSize=11.6, leading=18, textColor=NAVY,
        alignment=TA_LEFT, spaceAfter=9)
    S["h2"] = ParagraphStyle(
        "h2", fontName=FONT_SANS_B, fontSize=SIZE_H2, leading=19, textColor=NAVY,
        spaceBefore=13, spaceAfter=7, alignment=TA_LEFT)
    S["h3"] = ParagraphStyle(
        "h3", fontName=FONT_SANS_B, fontSize=SIZE_H3, leading=15, textColor=INK,
        spaceBefore=10, spaceAfter=4.5, alignment=TA_LEFT)
    S["h4"] = ParagraphStyle(
        "h4", fontName=FONT_SANS_SB, fontSize=9.6, leading=14, textColor=TEAL,
        spaceBefore=8, spaceAfter=3)
    S["eyebrow"] = ParagraphStyle(
        "eyebrow", fontName=FONT_SANS_B, fontSize=7.6, leading=10,
        textColor=ACCENT, spaceAfter=4)
    S["bullet"] = ParagraphStyle(
        "bullet", parent=S["body"], leftIndent=11, bulletIndent=1.5,
        spaceAfter=4.2, alignment=TA_LEFT)
    S["bullet_tight"] = ParagraphStyle(
        "bullet_tight", parent=S["bullet"], spaceAfter=2.4)
    S["num"] = ParagraphStyle(
        "num", parent=S["body"], leftIndent=15, bulletIndent=1.5,
        spaceAfter=4.2, alignment=TA_LEFT)
    S["quote"] = ParagraphStyle(
        "quote", fontName=FONT_SERIF_IT, fontSize=SIZE_PULL, leading=20,
        textColor=NAVY, alignment=TA_LEFT)
    S["caption"] = ParagraphStyle(
        "caption", fontName=FONT_SANS, fontSize=SIZE_CAPTION, leading=12,
        textColor=GREY, alignment=TA_LEFT)
    S["caption_c"] = ParagraphStyle("caption_c", parent=S["caption"], alignment=TA_CENTER)
    S["box"] = ParagraphStyle(
        "box", parent=S["body"], fontSize=9.3, leading=14.2, spaceAfter=5.5)
    S["box_tight"] = ParagraphStyle("box_tight", parent=S["box"], spaceAfter=3)
    S["box_bullet"] = ParagraphStyle(
        "box_bullet", parent=S["box"], leftIndent=11, bulletIndent=1.5, spaceAfter=3.4)
    S["box_bullet_t"] = ParagraphStyle(
        "box_bullet_t", parent=S["box_bullet"], spaceAfter=1.6)
    S["box_h"] = ParagraphStyle(
        "box_h", fontName=FONT_SANS_B, fontSize=9.8, leading=13.5,
        textColor=INK, spaceAfter=4)
    S["label"] = ParagraphStyle(
        "label", fontName=FONT_SANS_B, fontSize=7.4, leading=10,
        textColor=TEAL, spaceAfter=3)
    S["tbl"] = ParagraphStyle("tbl", fontName=FONT_SERIF, fontSize=8.5, leading=12.2,
                              textColor=INK)
    S["tbl_b"] = ParagraphStyle("tbl_b", fontName=FONT_SANS_SB, fontSize=8.3,
                                leading=12, textColor=PAPER)
    S["tbl_h"] = ParagraphStyle("tbl_h", fontName=FONT_SANS_B, fontSize=8.2,
                                leading=11.6, textColor=NAVY)
    S["tbl_c"] = ParagraphStyle("tbl_c", parent=S["tbl"], alignment=TA_CENTER)
    S["stat"] = ParagraphStyle("stat", fontName=FONT_SANS_B, fontSize=19, leading=20,
                               textColor=ACCENT, alignment=TA_CENTER)
    S["stat_l"] = ParagraphStyle("stat_l", fontName=FONT_SANS, fontSize=7.4, leading=10,
                                 textColor=GREY, alignment=TA_CENTER)
    S["ws"] = ParagraphStyle("ws", fontName=FONT_SANS, fontSize=8.6, leading=13,
                             textColor=GREY)
    S["ws_h"] = ParagraphStyle("ws_h", fontName=FONT_SANS_B, fontSize=9.4, leading=13,
                               textColor=NAVY)
    S["fill"] = ParagraphStyle("fill", fontName=FONT_SANS, fontSize=8.6, leading=13,
                               textColor=INK)
    S["toc1"] = ParagraphStyle("toc1", fontName=FONT_SANS_B, fontSize=9.6, leading=15,
                               textColor=NAVY)
    S["toc2"] = ParagraphStyle("toc2", fontName=FONT_SANS, fontSize=8.8, leading=13.6,
                               textColor=INK, leftIndent=10)
    S["toc3"] = ParagraphStyle("toc3", fontName=FONT_SANS, fontSize=8.2, leading=12.6,
                               textColor=GREY, leftIndent=20)
    return S


STYLES = None


def styles():
    global STYLES
    if STYLES is None:
        register_fonts()
        STYLES = build_styles()
    return STYLES


# =====================================================================
#  HEADINGS WITH TOC HOOKS
# =====================================================================
class H(Paragraph):
    """Paragraph that also registers a TOC entry and a PDF bookmark."""

    def __init__(self, text, style, level=2, toc_text=None, key=None, register=True):
        Paragraph.__init__(self, text, style)
        self._toc_level = level
        self._toc_text = toc_text if toc_text is not None else text
        self._key = key
        self._register = register

    def draw(self):
        c = self.canv
        # multiBuild rebuilds the story on every pass; the flowables are reused,
        # so guard against registering the same bookmark twice inside one pass
        # (the outline keeps its own per-document registry of destinations).
        if self._key:
            outline = c._doc.outline
            seen = getattr(outline, "destinationnamestotitles", {})
            if self._key in seen:
                Paragraph.draw(self)
                return
            c.bookmarkPage(self._key)
            lvl = max(0, self._toc_level - 1)
            try:
                cur = c._doc.outline.currentlevel
            except Exception:
                cur = -1
            if lvl > cur + 1:
                lvl = cur + 1
            c.addOutlineEntry(_plain(self._toc_text), self._key,
                              level=lvl, closed=False)
        Paragraph.draw(self)


def _plain(t):
    import re
    t = re.sub(r"<[^>]+>", "", t)
    return " ".join(t.split())


# =====================================================================
#  GENERIC CONTENT BOX (splittable)
# =====================================================================
class Boxed(Flowable):
    """A padded, optionally coloured container around a list of flowables.

    Supports splitting across pages so long callouts never overflow.
    """

    def __init__(self, content, pad=8, bg=None, border=None, border_w=0.7,
                 radius=3.5, bar=None, bar_w=3.2, hairline=True,
                 space_before=7, space_after=8, continued=False):
        Flowable.__init__(self)
        self.content = list(content)
        self.pad = pad
        self.bg = bg
        self.border = border
        self.border_w = border_w
        self.radius = radius
        self.bar = bar
        self.bar_w = bar_w if bar else 0
        self.hairline = hairline
        self.space_before = space_before
        self.space_after = space_after
        self.continued = continued
        self.width = 0
        self.height = 0

    # -- measurement ---------------------------------------------------
    def _inner_width(self, aw):
        return aw - 2 * self.pad - self.bar_w

    def _items(self, iw):
        out = []
        for f in self.content:
            sb = f.getSpaceBefore() if hasattr(f, "getSpaceBefore") else 0
            sa = f.getSpaceAfter() if hasattr(f, "getSpaceAfter") else 0
            w, h = f.wrap(iw, 10 ** 6)
            out.append((f, sb, h, sa))
        return out

    def wrap(self, aw, ah):
        self.width = aw
        iw = self._inner_width(aw)
        items = self._items(iw)
        self._measured = items
        h = sum(sb + fh + sa for (_, sb, fh, sa) in items)
        self.height = h + 2 * self.pad
        return self.width, self.height

    def getSpaceBefore(self):
        return self.space_before

    def getSpaceAfter(self):
        return self.space_after

    # -- splitting -----------------------------------------------------
    def _make(self, kids, sb, sa, pad=None):
        return Boxed(kids, pad=self.pad if pad is None else pad, bg=self.bg,
                     border=self.border, border_w=self.border_w, radius=self.radius,
                     bar=self.bar, bar_w=self.bar_w, hairline=self.hairline,
                     space_before=sb, space_after=sa, continued=True)

    def split(self, aw, ah):
        self.wrap(aw, ah)
        if self.height <= ah:
            return [self]
        iw = self._inner_width(aw)
        items = self._measured
        # usable content height for this fragment
        avail = ah - 2 * self.pad
        if avail <= 14:
            return []          # no room at all -> try again on a fresh page
        take = []
        used = 0.0
        leftover = None        # tail of a split child item
        n = len(items)
        idx = 0
        while idx < n:
            f, sb, fh, sa = items[idx]
            if used + sb + fh <= avail:
                take.append(f)
                used += sb + fh + sa
                idx += 1
                continue
            # does not fit whole. try to split the child itself.
            room = avail - used - sb
            if room > 16 and hasattr(f, "split"):
                try:
                    parts = f.split(iw, room)
                except Exception:
                    parts = []
                if parts and len(parts) == 2 and parts[0] is not f:
                    take.append(parts[0])
                    leftover = (parts[1], sa)
                    idx += 1
                break
            break
        if not take and leftover is None:
            return []
        rest = []
        if leftover is not None:
            tail, sa = leftover
            if isinstance(tail, (list, tuple)):
                rest.extend(tail)
            else:
                rest.append(tail)
        rest.extend(f for (f, _, _, _) in items[idx:])
        a = self._make(take, self.space_before, 0)
        # The greedy pass may have consumed every child, yet padding and spacing
        # can still push the box past the frame. Push trailing children over
        # until the first fragment genuinely fits.
        while take and a.wrap(aw, ah)[1] > ah + 0.1:
            rest.insert(0, take.pop())
        if not take:
            return []
        b = self._make(rest, 0, self.space_after)
        a.wrap(aw, ah)
        b.wrap(aw, ah)
        if a.height > ah + 0.1 or b.height >= self.height:
            return []
        return [a, b]

    # -- drawing -------------------------------------------------------
    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.saveState()
        if self.bg is not None:
            c.setFillColor(self.bg)
            if self.bg and self.radius:
                c.roundRect(0, 0, w, h, self.radius, stroke=0, fill=1)
            else:
                c.rect(0, 0, w, h, stroke=0, fill=1)
        if self.border is not None and self.border_w:
            c.setStrokeColor(self.border)
            c.setLineWidth(self.border_w)
            if self.hairline and not self.bar:
                c.roundRect(0.35, 0.35, w - 0.7, h - 0.7, self.radius, stroke=1, fill=0)
            elif self.hairline:
                c.roundRect(0.35, 0.35, w - 0.7, h - 0.7, self.radius, stroke=1, fill=0)
        if self.bar:
            c.setFillColor(self.bar)
            c.roundRect(0, 0, self.bar_w, h, 1.4, stroke=0, fill=1)
        # content
        left = self.pad + self.bar_w
        iw = self._inner_width(w)
        y = h - self.pad
        for f, sb, fh, sa in self._measured:
            y -= sb + fh
            c.saveState()
            c.translate(left, y)
            try:
                f.drawOn(c, 0, 0)
            except Exception:
                f.draw()
            c.restoreState()
            y -= sa
        c.restoreState()


class HRule(Flowable):
    def __init__(self, width=None, thickness=0.7, color=LINE, space_before=5,
                 space_after=5, dash=None):
        Flowable.__init__(self)
        self._w = width
        self.t = thickness
        self.color = color
        self.sb = space_before
        self.sa = space_after
        self.dash = dash

    def wrap(self, aw, ah):
        self.width = self._w or aw
        self.height = self.t
        return self.width, self.height

    def getSpaceBefore(self):
        return self.sb

    def getSpaceAfter(self):
        return self.sa

    def draw(self):
        c = self.canv
        c.saveState()
        c.setStrokeColor(self.color)
        c.setLineWidth(self.t)
        if self.dash:
            c.setDash(self.dash)
        c.line(0, 0, self.width, 0)
        c.restoreState()


class PullQuote(Flowable):
    def __init__(self, text, color=ACCENT, width=None, pad=9, fill=None,
                 space_before=8, space_after=9, size=None):
        Flowable.__init__(self)
        st = ParagraphStyle("pq", fontName=FONT_SERIF_IT,
                            fontSize=size or SIZE_PULL, leading=(size or SIZE_PULL) * 1.38,
                            textColor=NAVY)
        self.para = Paragraph(text, st)
        self.color = color
        self.fill = fill
        self.pad = pad
        self.sb = space_before
        self.sa = space_after

    def wrap(self, aw, ah):
        self.width = aw
        self.iw = aw - self.pad - 6
        w, h = self.para.wrap(self.iw, 10 ** 6)
        self.height = h + 2 * self.pad
        self.ph = h
        return self.width, self.height

    def getSpaceBefore(self):
        return self.sb

    def getSpaceAfter(self):
        return self.sa

    def draw(self):
        c = self.canv
        c.saveState()
        if self.fill is not None:
            c.setFillColor(self.fill)
            c.rect(0, 0, self.width, self.height, stroke=0, fill=1)
        c.setFillColor(self.color)
        c.rect(0, 0, 2.6, self.height, stroke=0, fill=1)
        c.translate(self.pad, self.pad)
        self.para.drawOn(c, 0, 0)
        c.restoreState()


class Figure(Flowable):
    """Reserves space and lets a callback paint a diagram."""

    def __init__(self, height, drawer, caption=None, space_before=6, space_after=8,
                 bg=None, border=None, radius=4, pad=6):
        Flowable.__init__(self)
        self._fh = height
        self.drawer = drawer
        self.caption = caption
        self.sb = space_before
        self.sa = space_after
        self.bg = bg
        self.border = border
        self.radius = radius
        self.pad = pad

    def wrap(self, aw, ah):
        self.width = aw
        self.cap_para = None
        caph = 0
        if self.caption:
            from reportlab.lib.styles import ParagraphStyle as PS
            st = PS("cap", fontName=FONT_SANS, fontSize=7.9, leading=11.6, textColor=GREY)
            self.cap_para = Paragraph(self.caption, st)
            w, caph = self.cap_para.wrap(aw, 10 ** 6)
        self.caph = caph
        self.height = self._fh + (caph + 4 if caph else 0)
        return self.width, self.height

    def getSpaceBefore(self):
        return self.sb

    def getSpaceAfter(self):
        return self.sa

    def draw(self):
        c = self.canv
        c.saveState()
        top = self.height - self.caph - (4 if self.caph else 0)
        if self.bg is not None:
            c.setFillColor(self.bg)
            c.roundRect(0, self.height - self._fh, self.width, self._fh, self.radius,
                        stroke=0, fill=1)
        c.saveState()
        c.translate(0, self.height - self._fh)
        self.drawer(c, self.width, self._fh)
        c.restoreState()
        if self.cap_para:
            c.translate(0, 0)
            self.cap_para.drawOn(c, 0, 0)
        c.restoreState()


class PageImage(Flowable):
    """A pre-rendered PNG/JPG drawn full-frame."""

    def __init__(self, path, w, h):
        Flowable.__init__(self)
        self.path = path
        self.width = w
        self.height = h

    def wrap(self, aw, ah):
        return self.width, self.height

    def draw(self):
        self.canv.drawImage(self.path, 0, 0, width=self.width, height=self.height,
                            mask="auto")


# =====================================================================
#  DOCUMENT
# =====================================================================
class BookDocTemplate(BaseDocTemplate):
    def __init__(self, filename, title="TUNTAS", author="", **kw):
        self.book_title = title
        self.book_author = author
        self.chapter_running = ""
        self.part_running = ""
        self.opener_hook = None
        BaseDocTemplate.__init__(
            self, filename, pagesize=(PAGE_W, PAGE_H),
            leftMargin=MARGIN_OUTER, rightMargin=MARGIN_OUTER,
            topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
            title=title, author=author, **kw)
        fw = PAGE_W - MARGIN_OUTER * 2
        fh = PAGE_H - MARGIN_TOP - MARGIN_BOTTOM
        body_frame = Frame(MARGIN_OUTER, MARGIN_BOTTOM, fw, fh, id="body",
                           leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        full_frame = Frame(MARGIN_OUTER, MARGIN_BOTTOM, fw, fh, id="full",
                           leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        bleed_frame = Frame(0, 0, PAGE_W, PAGE_H, id="bleed",
                            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        # First template in the list is the one used by page 1.
        self.addPageTemplates([
            PageTemplate(id="bleed", frames=[bleed_frame], onPage=self._decorate_blank),
            PageTemplate(id="plain", frames=[body_frame], onPage=self._decorate_plain),
            PageTemplate(id="body", frames=[body_frame], onPage=self._decorate_body),
            PageTemplate(id="opener", frames=[full_frame], onPage=self._decorate_blank),
        ])
        self._toc = None

    # ------------------------------------------------------------------
    def _decorate_blank(self, c, doc):
        pass

    def _decorate_plain(self, c, doc):
        """Front matter: quiet folio, no running head."""
        if doc.page <= 2:
            return
        c.saveState()
        c.setFont(FONT_SANS, 7.6)
        c.setFillColor(GREY)
        c.drawCentredString(PAGE_W / 2.0, MARGIN_BOTTOM - 10.5 * mm, str(doc.page))
        c.restoreState()

    def _decorate_body(self, c, doc):
        pn = doc.page
        c.saveState()
        y = PAGE_H - 12.5 * mm
        c.setFont(FONT_SANS, 7.1)
        c.setFillColor(GREY)
        right = PAGE_W - MARGIN_OUTER
        left = MARGIN_OUTER
        # running head: left = book title, right = chapter
        c.setFont(FONT_SANS_M, 7.1)
        c.setFillColor(GREY)
        c.drawString(left, y, self.book_title.upper())
        if self.chapter_running:
            c.drawRightString(right, y, self.chapter_running.upper())
        if self.book_title.upper() or self.chapter_running:
            c.setStrokeColor(GREY_LIGHT)
            c.setLineWidth(0.6)
            c.line(left, y - 3.4, right, y - 3.4)
        # folio
        c.setFont(FONT_SANS_B, 8.4)
        c.setFillColor(NAVY)
        c.drawCentredString(PAGE_W / 2.0, MARGIN_BOTTOM - 10.5 * mm, str(pn))
        # small tick around folio
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1.1)
        c.line(PAGE_W / 2.0 - 7.2 * mm, MARGIN_BOTTOM - 10.5 * mm + 2.6,
               PAGE_W / 2.0 - 7.2 * mm, MARGIN_BOTTOM - 10.5 * mm - 2.6)
        c.line(PAGE_W / 2.0 + 7.2 * mm, MARGIN_BOTTOM - 10.5 * mm + 2.6,
               PAGE_W / 2.0 + 7.2 * mm, MARGIN_BOTTOM - 10.5 * mm - 2.6)
        c.restoreState()

    # ------------------------------------------------------------------
    def afterFlowable(self, flowable):
        lvl = getattr(flowable, "_toc_level", None)
        if lvl is None or not getattr(flowable, "_register", False):
            return
        key = getattr(flowable, "_key", None)
        txt = getattr(flowable, "_toc_text", "")
        if key is None:
            key = "toc-%d-%d" % (self.page, id(flowable))
            flowable._key = key
            self.canv.bookmarkPage(key)
        self.notify("TOCEntry", (lvl, _plain(txt), self.page, key))
        # update running head
        if lvl == 1:
            self.part_running = _plain(txt)
            self.chapter_running = ""
        elif lvl == 2:
            self.chapter_running = _plain(txt)


# =====================================================================
#  SMALL HELPERS
# =====================================================================
def sp(h):
    return Spacer(1, h)


def para(text, style="body"):
    return Paragraph(text, styles()[style])


def bullets(items, style="bullet", marker="\u2022"):
    out = []
    for it in items:
        out.append(Paragraph(it, styles()[style], bulletText=marker))
    return out


def numbered(items, style="num", start=1):
    out = []
    for i, it in enumerate(items, start):
        out.append(Paragraph(it, styles()[style], bulletText="%d." % i))
    return out
