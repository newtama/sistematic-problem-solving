"""Reusable book components: openers, callouts, frameworks, worksheets, cases."""
import os
import segno
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    Paragraph, Spacer, Flowable, KeepTogether, PageBreak, NextPageTemplate,
    Table, TableStyle, Image,
)

from theme import *  # noqa
from engine import (
    styles, Boxed, HRule, PullQuote, Figure, para, bullets, numbered, sp,
    H, FONT_SANS, FONT_SANS_B, FONT_SANS_M, FONT_SANS_SB, FONT_SERIF,
    FONT_SERIF_B, FONT_SERIF_IT,
)

ASSET_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")
QR_DIR = os.path.join(ASSET_DIR, "qr")


# =====================================================================
#  Callout box presets
# =====================================================================
def callout(kind, title, body_flowables, icon=None):
    """kind: insight, tool, warning, practice, story, definition, keyidea"""
    presets = {
        "insight":   dict(bg=AMBER_SOFT, bar=AMBER, label="INSIGHT", color=AMBER),
        "tool":      dict(bg=TEAL_SOFT, bar=TEAL, label="TOOLS", color=TEAL),
        "warning":   dict(bg=RED_SOFT, bar=RED, label="JEBAKAN", color=RED),
        "practice":  dict(bg=GREEN_SOFT, bar=GREEN, label="PRAKTIK", color=GREEN),
        "story":     dict(bg=CREAM, bar=NAVY, label="KISAH", color=NAVY),
        "definition":dict(bg=VIOLET_SOFT, bar=VIOLET, label="DEFINISI", color=VIOLET),
        "keyidea":   dict(bg=ACCENT_SOFT, bar=ACCENT, label="IDE KUNCI", color=ACCENT),
        "research":  dict(bg=SOFT, bar=NAVY, label="BUKTI RISET", color=NAVY),
    }
    p = presets.get(kind, presets["insight"])
    st = styles()
    head = Paragraph(
        '<font color="%s">%s</font> &nbsp;&nbsp;<font color="%s">%s</font>' % (
            p["bar"].hexval().replace("0x", "#"), p["label"],
            INK.hexval().replace("0x", "#"), title),
        st["box_h"])
    content = [head] + list(body_flowables)
    return Boxed(content, pad=9, bg=p["bg"], border=None, bar=p["bar"], bar_w=3.0,
                 space_before=8, space_after=9)


def keyline(text, color=None):
    """Big single-line takeaway banner."""
    color = color or NAVY
    st = ParagraphStyle("kl", fontName=FONT_SANS_B, fontSize=11.4, leading=16.5,
                        textColor=PAPER, alignment=TA_LEFT)
    p = Paragraph(text, st)
    return _Banner(p, bg=color, pad=9)


class _Banner(Flowable):
    def __init__(self, para_obj, bg=NAVY, pad=9, sb=8, sa=9, radius=3):
        Flowable.__init__(self)
        self.p = para_obj
        self.bg = bg
        self.pad = pad
        self.sb = sb
        self.sa = sa
        self.radius = radius

    def wrap(self, aw, ah):
        self.width = aw
        w, h = self.p.wrap(aw - 2 * self.pad, 10 ** 6)
        self.ph = h
        self.height = h + 2 * self.pad
        return self.width, self.height

    def getSpaceBefore(self):
        return self.sb

    def getSpaceAfter(self):
        return self.sa

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(self.bg)
        c.roundRect(0, 0, self.width, self.height, self.radius, stroke=0, fill=1)
        c.translate(self.pad, self.pad)
        self.p.drawOn(c, 0, 0)
        c.restoreState()


# =====================================================================
#  Stats row
# =====================================================================
class StatRow(Flowable):
    def __init__(self, items, sb=8, sa=9, color=ACCENT):
        """items: list of (number, label)"""
        Flowable.__init__(self)
        self.items = items
        self.sb = sb
        self.sa = sa
        self.color = color

    def wrap(self, aw, ah):
        self.width = aw
        n = len(self.items)
        self.cw = aw / float(n)
        stn = ParagraphStyle("sn", fontName=FONT_SANS_B, fontSize=17.5, leading=19,
                             textColor=self.color, alignment=TA_CENTER)
        stl = ParagraphStyle("sl", fontName=FONT_SANS, fontSize=7.1, leading=9.6,
                             textColor=GREY, alignment=TA_CENTER)
        self.cells = []
        maxh = 0
        for num, lab in self.items:
            p1 = Paragraph(num, stn)
            p2 = Paragraph(lab, stl)
            w1, h1 = p1.wrap(self.cw - 8, 10 ** 6)
            w2, h2 = p2.wrap(self.cw - 8, 10 ** 6)
            self.cells.append((p1, h1, p2, h2))
            maxh = max(maxh, h1 + h2 + 2)
        self.height = maxh + 8
        return self.width, self.height

    def getSpaceBefore(self):
        return self.sb

    def getSpaceAfter(self):
        return self.sa

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(SOFT)
        c.roundRect(0, 0, self.width, self.height, 3, stroke=0, fill=1)
        for i, (p1, h1, p2, h2) in enumerate(self.cells):
            x = i * self.cw
            if i:
                c.setStrokeColor(GREY_LIGHT)
                c.setLineWidth(0.6)
                c.line(x, 5, x, self.height - 5)
            c.saveState()
            c.translate(x, self.height - 4)
            p1.drawOn(c, 4, -h1)
            p2.drawOn(c, 4, -h1 - h2 - 1)
            c.restoreState()
        c.restoreState()


# =====================================================================
#  Chapter opener (full page)
# =====================================================================
class ChapterOpener(Flowable):
    def __init__(self, step, number, title, subtitle, promise, map_items,
                 color=ACCENT, kicker="BAGIAN 2"):
        Flowable.__init__(self)
        self.step = step
        self.number = number
        self.title = title
        self.subtitle = subtitle
        self.promise = promise
        self.map_items = map_items
        self.color = color
        self.kicker = kicker

    def wrap(self, aw, ah):
        self.width = aw
        self.height = ah
        return self.width, self.height

    def draw(self):
        from reportlab.lib.colors import Color, white
        c = self.canv
        W, Hh = self.width, self.height
        c.saveState()
        # background
        c.setFillColor(CREAM)
        c.rect(0, 0, W, Hh, stroke=0, fill=1)
        # top colour band
        c.setFillColor(self.color)
        c.rect(0, Hh - 58 * mm, W, 58 * mm, stroke=0, fill=1)
        # step medallion
        c.setFillColor(PAPER)
        c.circle(W - 24 * mm, Hh - 30 * mm, 17 * mm, stroke=0, fill=1)
        c.setFillColor(self.color)
        c.setFont(FONT_SANS_B, 27)
        c.drawCentredString(W - 24 * mm, Hh - 34 * mm, self.step.replace("D", ""))
        c.setFont(FONT_SANS_B, 8)
        c.drawCentredString(W - 24 * mm, Hh - 41.5 * mm, "LANGKAH")
        # kicker
        c.setFillColor(PAPER)
        c.setFont(FONT_SANS_B, 8)
        c.drawString(0, Hh - 14 * mm, self.kicker.upper())
        c.setFont(FONT_SANS, 8)
        c.drawString(0, Hh - 19 * mm, ("BAB %s" % self.number).upper())
        # title (wrap manually)
        c.setFillColor(PAPER)
        words = self.title.split()
        lines, cur = [], ""
        for w in words:
            t = (cur + " " + w).strip()
            c.setFont(FONT_SERIF_B, 25)
            if c.stringWidth(t, FONT_SERIF_B, 25) > W - 52 * mm:
                lines.append(cur)
                cur = w
            else:
                cur = t
        lines.append(cur)
        y = Hh - 30 * mm
        for ln in lines[:4]:
            c.setFont(FONT_SERIF_B, 25)
            c.drawString(0, y, ln)
            y -= 10.6 * mm
        # step label
        c.setFillColor(PAPER)
        c.setFont(FONT_SANS_M, 9.4)
        c.drawString(0, Hh - 52.5 * mm, self.subtitle)
        # promise block
        y2 = Hh - 58 * mm - 12 * mm
        ps = ParagraphStyle("pr", fontName=FONT_SERIF_IT, fontSize=11.4, leading=16.5,
                            textColor=NAVY)
        pp = Paragraph(self.promise, ps)
        w, h = pp.wrap(W - 6 * mm, 10 ** 6)
        c.setFillColor(PAPER)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.7)
        c.roundRect(0, y2 - h - 8, W - 6 * mm, h + 16, 3, stroke=1, fill=1)
        c.setFillColor(self.color)
        c.rect(0, y2 - h - 8, 3, h + 16, stroke=0, fill=1)
        pp.drawOn(c, 10, y2 - h - 1)
        # map
        y3 = y2 - h - 8 - 13 * mm
        c.setFillColor(NAVY)
        c.setFont(FONT_SANS_B, 9)
        c.drawString(0, y3, "PETA BAB INI")
        c.setStrokeColor(LINE)
        c.setLineWidth(0.6)
        c.line(0, y3 - 3.2, W, y3 - 3.2)
        yy = y3 - 9 * mm
        stm = ParagraphStyle("m", fontName=FONT_SANS_M, fontSize=8.8, leading=12.4,
                             textColor=INK)
        for item in self.map_items:
            c.setFillColor(self.color)
            c.circle(1.7 * mm, yy + 1.4, 1.7 * mm, stroke=0, fill=1)
            p = Paragraph(item, stm)
            w, h = p.wrap(W - 8 * mm, 10 ** 6)
            p.drawOn(c, 6.5 * mm, yy - h + 3.4)
            yy -= (h + 4.2)
        c.restoreState()


# =====================================================================
#  Part divider
# =====================================================================
class PartDivider(Flowable):
    def __init__(self, kicker, title, blurb, color=NAVY, number=None):
        Flowable.__init__(self)
        self.kicker = kicker
        self.title = title
        self.blurb = blurb
        self.color = color
        self.number = number

    def wrap(self, aw, ah):
        self.width, self.height = aw, ah
        return self.width, self.height

    def draw(self):
        c = self.canv
        W, Hh = self.width, self.height
        c.saveState()
        c.setFillColor(self.color)
        c.rect(0, 0, W, Hh, stroke=0, fill=1)
        # decorative rings
        c.setStrokeColor(PAPER)
        c.setLineWidth(0.6)
        for i, r in enumerate((34, 48, 62)):
            c.circle(W - 6 * mm, Hh * 0.30, r * mm, stroke=1, fill=0)
        c.setFillColor(PAPER)
        c.setFont(FONT_SANS_B, 9)
        c.drawString(0, Hh * 0.72, self.kicker.upper())
        words = self.title.split()
        lines, cur = [], ""
        for w in words:
            t = (cur + " " + w).strip()
            c.setFont(FONT_SERIF_B, 31)
            if c.stringWidth(t, FONT_SERIF_B, 31) > W:
                lines.append(cur)
                cur = w
            else:
                cur = t
        lines.append(cur)
        y = Hh * 0.63
        for ln in lines[:4]:
            c.setFont(FONT_SERIF_B, 31)
            c.drawString(0, y, ln)
            y -= 13.2 * mm
        c.setStrokeColor(ACCENT)
        c.setLineWidth(2.2)
        c.line(0, y - 4 * mm, 26 * mm, y - 4 * mm)
        bs = ParagraphStyle("b", fontName=FONT_SERIF_IT, fontSize=12, leading=18,
                            textColor=PAPER)
        p = Paragraph(self.blurb, bs)
        w, h = p.wrap(W - 14 * mm, 10 ** 6)
        p.drawOn(c, 0, y - 14 * mm - h)
        c.restoreState()


# =====================================================================
#  Tool table
# =====================================================================
def tool_table(headers, rows, col_widths=None, accent=TEAL, zebra=True):
    st = styles()
    data = [[Paragraph(h, st["tbl_b"]) for h in headers]]
    for r in rows:
        data.append([Paragraph(str(x), st["tbl"]) for x in r])
    total = 176 * mm - 20 * mm - 16 * mm
    if col_widths:
        widths = [w * total for w in col_widths]
    else:
        widths = [total / len(headers)] * len(headers)
    t = Table(data, colWidths=widths, repeatRows=1)
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), accent),
        ("TEXTCOLOR", (0, 0), (-1, 0), PAPER),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, 0), 6),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        ("TOPPADDING", (0, 1), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -1), 0.5, GREY_LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.7, GREY_LIGHT),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                cmds.append(("BACKGROUND", (0, i), (-1, i), SOFT))
    t.setStyle(TableStyle(cmds))
    return t


# =====================================================================
#  Worksheet
# =====================================================================
class WriteLines(Flowable):
    def __init__(self, n=3, gap=11.5, sb=2, sa=4, color=GREY_LIGHT, first_label=None):
        Flowable.__init__(self)
        self.n = n
        self.gap = gap
        self.sb = sb
        self.sa = sa
        self.color = color
        self.first_label = first_label

    def wrap(self, aw, ah):
        self.width = aw
        self.height = self.n * self.gap
        return self.width, self.height

    def getSpaceBefore(self):
        return self.sb

    def getSpaceAfter(self):
        return self.sa

    def draw(self):
        c = self.canv
        c.saveState()
        c.setStrokeColor(self.color)
        c.setLineWidth(0.7)
        y = self.height - self.gap + 3
        for i in range(self.n):
            c.line(0, y, self.width, y)
            y -= self.gap
        c.restoreState()


class WSHeader(Flowable):
    def __init__(self, code, title, subtitle):
        Flowable.__init__(self)
        self.code = code
        self.title = title
        self.subtitle = subtitle

    def wrap(self, aw, ah):
        self.width = aw
        self.height = 20 * mm
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(NAVY_DEEP)
        c.roundRect(0, 0, self.width, self.height, 3, stroke=0, fill=1)
        c.setFillColor(ACCENT)
        c.rect(0, 0, 3.2, self.height, stroke=0, fill=1)
        c.setFillColor(ACCENT)
        c.setFont(FONT_SANS_B, 7.6)
        c.drawString(10, self.height - 7.5 * mm, self.code.upper())
        c.setFillColor(PAPER)
        c.setFont(FONT_SERIF_B, 14)
        c.drawString(10, self.height - 14 * mm, self.title)
        c.setFont(FONT_SANS, 7.8)
        c.setFillColor(HexColor("#B9C2D4"))
        c.drawRightString(self.width - 8, self.height - 7.5 * mm, self.subtitle)
        c.restoreState()


def worksheet_block(code, title, subtitle, fields, footer=None):
    """fields: list of dict(label=..., lines=n, hint=...) or ('table', headers, rows, widths)"""
    st = styles()
    out = [WSHeader(code, title, subtitle)]
    for f in fields:
        if isinstance(f, tuple) and f[0] == "table":
            _, headers, rows, widths = f
            out.append(sp(6))
            out.append(tool_table(headers, rows, widths, accent=TEAL))
            continue
        if isinstance(f, tuple) and f[0] == "grid":
            _, n, cols = f
            out.append(sp(6))
            out.append(_grid(n, cols))
            continue
        if isinstance(f, tuple) and f[0] == "note":
            out.append(sp(5))
            out.append(Paragraph(f[1], st["ws"]))
            continue
        lab = f.get("label", "")
        lines = f.get("lines", 2)
        hint = f.get("hint")
        out.append(sp(6))
        out.append(Paragraph(
            '<font color="%s">%s</font>' % (NAVY.hexval().replace("0x", "#"), lab),
            st["ws_h"]))
        if hint:
            out.append(Paragraph('<i>%s</i>' % hint, st["caption"]))
            out.append(sp(1))
        out.append(WriteLines(lines))
    if footer:
        out.append(sp(4))
        out.append(Paragraph(footer, st["ws"]))
    return KeepTogether([Boxed(out, pad=10, bg=PAPER, border=LINE, border_w=0.8,
                               space_before=8, space_after=9)])


class _Grid(Flowable):
    def __init__(self, n, cols=2, cell_h=13.5 * mm, sb=3, sa=4):
        Flowable.__init__(self)
        self.n = n
        self.cols = cols
        self.cell_h = cell_h
        self.sb, self.sa = sb, sa

    def wrap(self, aw, ah):
        self.width = aw
        self.rows = (self.n + self.cols - 1) // self.cols
        self.height = self.rows * self.cell_h
        return self.width, self.height

    def getSpaceBefore(self):
        return self.sb

    def getSpaceAfter(self):
        return self.sa

    def draw(self):
        c = self.canv
        cw = self.width / self.cols
        c.saveState()
        c.setStrokeColor(GREY_LIGHT)
        c.setLineWidth(0.7)
        for r in range(self.rows):
            for col in range(self.cols):
                i = r * self.cols + col
                if i >= self.n:
                    break
                c.rect(col * cw, self.height - (r + 1) * self.cell_h,
                       cw - 2, self.cell_h - 2, stroke=1, fill=0)
        c.restoreState()


def _grid(n, cols=2):
    return _Grid(n, cols)


# =====================================================================
#  Framework diagrams
# =====================================================================
def arrow_chain(steps, color=TEAL, height=23 * mm, caption=None):
    """steps: list of (code, label)"""
    def drawer(c, w, h):
        n = len(steps)
        gap = 3.0
        bw = (w - gap * (n - 1)) / n
        for i, (code, lab) in enumerate(steps):
            x = i * (bw + gap)
            c.setFillColor(color)
            c.roundRect(x, 0, bw, h, 3, stroke=0, fill=1)
            if i < n - 1:
                c.setFillColor(NAVY)
                c.setFont(FONT_SANS_B, 9)
                c.drawCentredString(x + bw + gap / 2.0, h / 2.0 - 3, "\u203a")
            c.setFillColor(PAPER)
            c.setFont(FONT_SANS_B, 10.5)
            c.drawCentredString(x + bw / 2.0, h - 10, code)
            c.setFont(FONT_SANS_M, 7.4)
            words = lab.split()
            yy = h - 17
            cur = ""
            for wd in words:
                t = (cur + " " + wd).strip()
                if c.stringWidth(t, FONT_SANS_M, 7.4) > bw - 6:
                    c.drawCentredString(x + bw / 2.0, yy, cur)
                    yy -= 8.4
                    cur = wd
                else:
                    cur = t
            c.drawCentredString(x + bw / 2.0, yy, cur)
    return Figure(height, drawer, caption, bg=SOFT, pad=6)


def qr_image(url, size=18 * mm, dark=NAVY, light=None):
    os.makedirs(QR_DIR, exist_ok=True)
    import re
    fn = os.path.join(QR_DIR, re.sub(r"[^a-zA-Z0-9]", "_", url)[:60] + ".png")
    q = segno.make(url, error="m")
    q.save(fn, scale=10, border=0, dark=dark.hexval().replace("0x", "#"),
           light=light or "#FFFFFF")
    return Image(fn, width=size, height=size)


class QRPanel(Flowable):
    def __init__(self, url, title, subtitle, code, sb=8, sa=9):
        Flowable.__init__(self)
        self.url = url
        self.title = title
        self.subtitle = subtitle
        self.code = code
        self.sb, self.sa = sb, sa
        self.qr = qr_image(url, size=20 * mm)

    def wrap(self, aw, ah):
        self.width = aw
        self.height = 26 * mm
        return self.width, self.height

    def getSpaceBefore(self):
        return self.sb

    def getSpaceAfter(self):
        return self.sa

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(SOFT)
        c.roundRect(0, 0, self.width, self.height, 3, stroke=0, fill=1)
        c.setFillColor(ACCENT)
        c.rect(0, 0, 3.0, self.height, stroke=0, fill=1)
        # QR
        self.qr.drawOn(c, 8, (self.height - 20 * mm) / 2.0)
        c.setFillColor(ACCENT)
        c.setFont(FONT_SANS_B, 7.4)
        c.drawString(33 * mm, self.height - 9.5 * mm, self.code.upper())
        c.setFillColor(NAVY)
        c.setFont(FONT_SERIF_B, 11.5)
        c.drawString(33 * mm, self.height - 16 * mm, self.title)
        c.setFillColor(GREY)
        c.setFont(FONT_SANS, 7.6)
        c.drawString(33 * mm, self.height - 21.5 * mm, self.subtitle)
        c.restoreState()


# =====================================================================
#  Case study
# =====================================================================
def case_study(number, org, title, meta, sections, color=NAVY, tag="STUDI KASUS"):
    """sections: list of (label, text_or_flowables)"""
    st = styles()
    head = Paragraph(
        '<font color="%s">%s %s</font> &nbsp;|&nbsp; <font color="%s">%s</font>' % (
            color.hexval().replace("0x", "#"), tag, number,
            ACCENT.hexval().replace("0x", "#"), org),
        st["box_h"])
    content = [head]
    if title:
        content.append(Paragraph(
            '<font color="%s">%s</font>' % (NAVY.hexval().replace("0x", "#"), title),
            ParagraphStyle("ct", fontName=FONT_SERIF_B, fontSize=11.6, leading=16,
                           textColor=NAVY, spaceAfter=4)))
    if meta:
        content.append(Paragraph(meta, st["caption"]))
        content.append(sp(3))
    for label, val in sections:
        content.append(Paragraph(
            '<font color="%s">%s</font>' % (color.hexval().replace("0x", "#"), label),
            st["label"]))
        if isinstance(val, str):
            content.append(Paragraph(val, st["box"]))
        else:
            content.extend(val)
    return Boxed(content, pad=10, bg=PAPER, border=color, border_w=0.8,
                 bar=color, bar_w=3.0, space_before=8, space_after=10)


# =====================================================================
#  misc
# =====================================================================
def caption(text):
    return Paragraph(text, styles()["caption"])


def h2(text, level=2, toc_text=None, key=None):
    return H(text, styles()["h2"], level=level, toc_text=toc_text, key=key)


def h3(text):
    return H(text, styles()["h3"], level=3, register=False)


def h4(text):
    return Paragraph(text, styles()["h4"])


def rule(color=LINE, sb=6, sa=6, dash=None, thickness=0.7):
    return HRule(color=color, space_before=sb, space_after=sa, dash=dash,
                 thickness=thickness)


def gap(h):
    return Spacer(1, h)


def checklist(items, color=TEAL):
    """items: list of strings; renders empty checkbox squares."""
    st = ParagraphStyle("ck", fontName=FONT_SANS, fontSize=9.1, leading=15.4,
                        textColor=INK, leftIndent=13, bulletIndent=0)
    out = []
    for it in items:
        p = Paragraph('<font color="%s">\u25a1</font>' % color.hexval().replace("0x", "#"),
                      st)
        p = Paragraph(it, st)
        # draw box separately: use bullet text
        out.append(Paragraph(it, st, bulletText="\u25a1"))
    return out
