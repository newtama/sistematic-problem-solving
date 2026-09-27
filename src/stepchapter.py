"""Standardised builder for the seven TUNTAS 7D step chapters.

Every step chapter follows the best-seller rhythm:
  1. Chapter opener page (full page, colour-coded)
  2. Hook story                      ~1 page
  3. Core concept + framework         ~3 pages
  4. Practical tools, step by step    ~5 pages
  5. Real case study                  ~4 pages
  6. Worksheet + QR download          ~2 pages
"""
from reportlab.platypus import PageBreak, NextPageTemplate

from theme import *  # noqa
from engine import styles, H, sp, para
from dsl import render
from components import (h2, h3, h4, rule, caption, callout, keyline, StatRow,
                        QRPanel, tool_table, worksheet_block, case_study,
                        ChapterOpener)

S = styles()


class Step:
    def __init__(self, code, number, title, subtitle, promise, map_items,
                 color, kicker="Bagian 2 \u00b7 Inti \u2014 TUNTAS 7D"):
        self.code = code
        self.number = number
        self.title = title
        self.subtitle = subtitle
        self.promise = promise
        self.map_items = map_items
        self.color = color
        self.kicker = kicker

    def opener(self):
        return [NextPageTemplate("opener"), PageBreak(),
                ChapterOpener(self.code, self.number, self.title, self.subtitle,
                              self.promise, self.map_items, self.color,
                              self.kicker),
                NextPageTemplate("body")]

    def heading(self):
        return H("Bab %s (Langkah %s): %s" % (self.number, self.code[1], self.title),
                 S["h2"], level=2, key="bab%s" % self.number)


def t(text):
    return render(text)
