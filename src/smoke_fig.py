import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.platypus import PageBreak
from engine import BookDocTemplate, register_fonts, styles, para, sp
import figures
from figures import register_all
from dsl import render

register_fonts()
register_all()

names = ["tuntas7d", "iceberg", "bias", "mindset", "ptypes", "whys", "fishbone",
         "pareto", "define", "impact", "decide", "pdca", "driver", "radar",
         "agenda", "tree", "sbi", "cost", "chart", "funnel1", "energy", "family",
         "retail", "skill", "a3", "std", "meeting", "room"]
story = []
for i, n in enumerate(names):
    story.append(para("<b>%s</b>" % n, "h3"))
    story.extend(render("!fig %s" % n))
    if i % 2 == 1:
        story.append(PageBreak())
doc = BookDocTemplate("/workspace/project/output/figs.pdf", title="FIGS")
doc.multiBuild(story)
print("built figs.pdf")
