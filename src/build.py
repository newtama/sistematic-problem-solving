"""Assemble the full book PDF."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.platypus import PageBreak, NextPageTemplate, Spacer, Flowable

from theme import *  # noqa
from engine import BookDocTemplate, register_fonts, styles
import figures
from figures import register_all
from frontmatter import FrontCover, TitlePage, CreditsPage, StatementPage

register_fonts()
register_all()
S = styles()

import content.front as C_front
import content.part0 as C_p0
import content.part1 as C_p1
import content.part2 as C_p2
import content.part3 as C_p3
import content.back as C_back


def build(path):
    doc = BookDocTemplate(path, title="TUNTAS 7D - Solusi Sistematis",
                          author="Tuntas Press")
    story = []
    story += C_front.build()
    story += C_p0.build()
    story += C_p1.build()
    story += C_p2.build()
    story += C_p3.build()
    story += C_back.build()
    doc.multiBuild(story)
    return path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/workspace/project/output/TUNTAS-7D.pdf"
    build(out)
    from pypdf import PdfReader
    r = PdfReader(out)
    print("BUILT", out, "-", len(r.pages), "pages")
