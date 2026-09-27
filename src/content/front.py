"""Cover, title pages, table of contents scaffold."""
from reportlab.platypus import PageBreak, NextPageTemplate, Spacer
from reportlab.platypus.tableofcontents import TableOfContents

from theme import *  # noqa
from engine import styles, H, sp
from dsl import render
from components import h2, rule, caption
from frontmatter import FrontCover, TitlePage, CreditsPage


def build():
    story = []
    # ---- front cover (full bleed) - first template in the doc is already "bleed"
    story.append(FrontCover())
    story.append(PageBreak())
    story.append(TitlePage("halftitle"))
    story.append(PageBreak())
    story.append(TitlePage("title"))
    story.append(PageBreak())
    story.append(CreditsPage())

    # ---- table of contents
    story.append(NextPageTemplate("plain"))
    story.append(PageBreak())
    # register=False keeps this out of its own table of contents; the bookmark
    # (key) is still written by H.draw, so cross-references to it keep working.
    story.append(H("Daftar Isi", styles()["h2"], level=2, key="toc-head",
                   register=False))
    story.append(sp(4))
    toc = TableOfContents()
    toc.levelStyles = [
        styles()["toc1"], styles()["toc2"], styles()["toc3"],
    ]
    toc.dotsMinLevel = 0
    story.append(toc)
    return story
