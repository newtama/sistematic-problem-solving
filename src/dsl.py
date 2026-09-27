"""A tiny markup -> flowables converter so chapters can be written as prose.

Markup
------
    ## Heading            level-2 heading (appears in TOC & outline)
    ### Heading           level-3 heading (in outline, not TOC)
    #### Heading          bold run-in sub-head
    - item                bullet
    1. item               numbered item (auto-increment, resets on non-number)
    > quote               pull quote
    [[text]]              key takeaway banner
    ---                   horizontal rule
    STAT num|label ; ...  stat row
    !insight Title | body         callout kinds: insight tool warn practice
    !tool ...                     story def key research
    !box Title | body             plain soft box
    !fig NAME                     named figure
    !qr URL | code | title | sub  QR download panel
    !check a; b; c                checklist
    !lines n                      blank ruled lines
    !ws ...                       worksheet placeholder (use components directly)
    !pagebreak
    blank line                    paragraph separator
    plain text                    paragraph
"""
import re
from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm

from theme import *  # noqa
from engine import styles, Boxed, HRule, Figure, PullQuote, para, sp
from components import (callout, keyline, StatRow, QRPanel, caption, rule,
                        WriteLines, tool_table, checklist as _checklist)


def _callout(kind, spec):
    title, _, body = spec.partition("|")
    title = title.strip()
    body = body.strip()
    items = _inline(body)
    if title:
        return callout(kind, title, items)
    return callout(kind, "", items)


def _inline(text):
    """Turn a compact body into flowables: << bullets, \\n paragraphs."""
    if not text:
        return []
    out = []
    blocks = re.split(r"\s*<<\s*", text)
    for bi, b in enumerate(blocks):
        b = b.strip()
        if not b:
            continue
        lines = [ln.strip() for ln in b.split("\n") if ln.strip()]
        if all(ln.startswith("- ") or ln.startswith("1. ") or
               re.match(r"^\d+\.\s", ln) for ln in lines) and lines:
            for ln in lines:
                m = re.match(r"^(?:-|\d+\.)\s+(.*)$", ln)
                marker = "\u2022" if ln.startswith("- ") else ln.split(".", 1)[0] + "."
                out.append(Paragraph(m.group(1), styles()["box_bullet_t"],
                                     bulletText=marker))
        else:
            joined = " ".join(ln if ln.startswith("- ") or re.match(r"^\d+\.\s", ln)
                              else ln for ln in lines)
            # mixed: treat each line that starts with a marker as bullet
            if any(ln.startswith("- ") or re.match(r"^\d+\.\s", ln) for ln in lines):
                for ln in lines:
                    m = re.match(r"^(?:-|(\d+)\.)\s+(.*)$", ln)
                    if m:
                        marker = "\u2022" if not m.group(1) else m.group(1) + "."
                        out.append(Paragraph(m.group(2), styles()["box_bullet_t"],
                                             bulletText=marker))
                    else:
                        out.append(Paragraph(ln, styles()["box_tight"]))
            else:
                out.append(Paragraph(" ".join(lines), styles()["box"]))
    return out


FIGURES = {}

# Bookmark keys must be unique across the whole document. render() is called
# many times and its local story length restarts at zero each time, so keys
# built from len(story) collide and create duplicate outline entries. A global
# counter gives every heading a unique key while staying deterministic across
# multiBuild passes.
_HEAD_KEY = [0]


def _next_head_key(prefix):
    _HEAD_KEY[0] += 1
    return "%s-%d" % (prefix, _HEAD_KEY[0])


def register_figure(name, factory):
    FIGURES[name] = factory


def render(text, figures=None):
    figures = figures if figures is not None else FIGURES
    story = []
    lines = text.split("\n")
    i = 0
    pending_para = []

    def flush():
        if pending_para:
            t = " ".join(pending_para).strip()
            if t:
                story.append(Paragraph(t, styles()["body"]))
            pending_para.clear()

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            flush()
            i += 1
            continue
        if s.startswith("## "):
            flush()
            from engine import H
            story.append(H(s[3:].strip(), styles()["h2"], level=2,
                           key=_next_head_key("h2")))
        elif s.startswith("### "):
            flush()
            from engine import H
            story.append(H(s[4:].strip(), styles()["h3"], level=3,
                           register=False, key=_next_head_key("h3")))
        elif s.startswith("#### "):
            flush()
            story.append(Paragraph(s[5:].strip(), styles()["h4"]))
        elif s.startswith("!pagebreak"):
            flush()
            story.append(PageBreak())
        elif s.startswith("!gap"):
            flush()
            story.append(Spacer(1, float(s.split()[1]) if len(s.split()) > 1 else 6))
        elif s.startswith("!rule"):
            flush()
            story.append(rule())
        elif s.startswith("!lines"):
            flush()
            n = int(s.split()[1]) if len(s.split()) > 1 else 3
            story.append(WriteLines(n))
        elif s.startswith("!check"):
            flush()
            body = s[6:].strip()
            items = [x.strip() for x in body.split(";") if x.strip()]
            for it in items:
                story.append(Paragraph(it, styles()["bullet"], bulletText="\u25a1"))
        elif s.startswith("!stat"):
            flush()
            body = s[5:].strip()
            items = []
            for chunk in body.split(";"):
                a, _, b = chunk.partition("|")
                items.append((a.strip(), b.strip()))
            story.append(StatRow(items))
        elif s.startswith("[[") and s.endswith("]]"):
            flush()
            story.append(keyline(s[2:-2].strip()))
        elif s.startswith("> "):
            flush()
            story.append(PullQuote(s[2:].strip()))
        elif s.startswith("!qr"):
            flush()
            parts = [x.strip() for x in s[3:].split("|")]
            url = parts[0]
            code = parts[1] if len(parts) > 1 else "QR"
            title = parts[2] if len(parts) > 2 else "Toolkit Digital"
            sub = parts[3] if len(parts) > 3 else "Pindai untuk mengunduh"
            story.append(QRPanel(url, title, sub, code))
        elif s.startswith("!fig"):
            flush()
            name = s[4:].strip()
            f = figures.get(name)
            if f is None:
                raise KeyError("unknown figure %r" % name)
            story.append(f() if callable(f) else f)
        elif s.startswith("!"):
            flush()
            m = re.match(r"!(\w+)\s*(.*)$", s, re.S)
            kind = m.group(1)
            spec = m.group(2)
            kk = {"insight": "insight", "tool": "tool", "warn": "warning",
                  "practice": "practice", "story": "story", "def": "definition",
                  "key": "keyidea", "research": "research"}
            if kind in kk:
                story.append(_callout(kk[kind], spec))
            elif kind == "box":
                title, _, body = spec.partition("|")
                story.append(Boxed([Paragraph(title.strip(), styles()["box_h"])]
                                   + _inline(body), pad=9, bg=SOFT,
                                   border=LINE, border_w=0.6))
            else:
                raise KeyError("unknown directive %r" % kind)
        elif s.startswith("- "):
            flush()
            acc = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                acc.append(lines[i].strip()[2:].strip())
                i += 1
            for a in acc:
                story.append(Paragraph(a, styles()["bullet"], bulletText="\u2022"))
            continue
        elif re.match(r"^\d+\.\s", s):
            flush()
            acc = []
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i].strip()):
                acc.append(re.sub(r"^\d+\.\s", "", lines[i].strip()))
                i += 1
            for k, a in enumerate(acc, 1):
                story.append(Paragraph(a, styles()["num"], bulletText="%d." % k))
            continue
        else:
            pending_para.append(s)
        i += 1
    flush()
    return story
