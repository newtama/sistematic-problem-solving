"""Covers, title pages, full-bleed section openers."""
import math
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import Paragraph, Flowable, PageBreak, NextPageTemplate

from theme import *  # noqa
from engine import (FONT_SANS, FONT_SANS_B, FONT_SANS_M, FONT_SANS_SB,
                    FONT_SERIF, FONT_SERIF_B, FONT_SERIF_IT, styles, Boxed, sp)


def _lines(c, text, font, size, maxw):
    words = text.split()
    out, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if c.stringWidth(t, font, size) > maxw and cur:
            out.append(cur)
            cur = w
        else:
            cur = t
    if cur:
        out.append(cur)
    return out


# =====================================================================
#  COVER (front)
# =====================================================================
class FrontCover(Flowable):
    def wrap(self, aw, ah):
        self.width, self.height = aw, ah
        return self.width, self.height

    def draw(self):
        c = self.canv
        W, H = self.width, self.height
        c.saveState()
        # base
        c.setFillColor(NAVY_DEEP)
        c.rect(0, 0, W, H, stroke=0, fill=1)
        # accent geometry: large rounded block top
        c.setFillColor(NAVY)
        c.rect(0, H - 96 * mm, W, 96 * mm, stroke=0, fill=1)
        # concentric arcs bottom-right
        c.setStrokeColor(Color(0.91, 0.31, 0.23, 0.30))
        c.setLineWidth(1.1)
        for r in (24, 38, 52, 66):
            c.circle(W + 6 * mm, H * 0.115, r * mm, stroke=1, fill=0)
        c.setStrokeColor(Color(0.91, 0.31, 0.23, 0.55))
        c.setLineWidth(2.4)
        c.line(0, H - 96 * mm, W, H - 96 * mm)
        # eyebrow
        c.setFillColor(ACCENT)
        c.setFont(FONT_SANS_B, 9.6)
        c.drawString(16 * mm, H - 26 * mm, "PANDUAN PRAKTIS")
        c.setFillColor(PAPER)
        c.setFont(FONT_SANS, 8.4)
        c.drawString(16 * mm, H - 32 * mm, "UNTUK INDIVIDU, TIM, DAN ORGANISASI")
        # title
        t1 = "TUNTAS"
        c.setFillColor(PAPER)
        c.setFont(FONT_SERIF_B, 76)
        c.drawString(15 * mm, H - 62 * mm, t1)
        c.setFillColor(ACCENT)
        c.setFont(FONT_SERIF_B, 30)
        c.drawString(16.5 * mm, H - 78 * mm, "7D")
        c.setFillColor(PAPER)
        c.setFont(FONT_SERIF_IT, 19)
        c.drawString(42 * mm, H - 77.5 * mm, "Solusi Sistematis")
        # title block
        subs = _lines(c, "Menyelesaikan Masalah dengan Cara yang Terbukti, dari Akar sampai Hasil",
                      FONT_SERIF, 15.5, W - 32 * mm)
        y = H - 112 * mm
        c.setFillColor(NAVY)
        for ln in subs:
            c.setFont(FONT_SERIF, 15.5)
            c.drawString(16 * mm, y, ln)
            y -= 8.2 * mm
        # 7D ribbon
        steps = [("D1", "Detect"), ("D2", "Define"), ("D3", "Dig"), ("D4", "Design"),
                 ("D5", "Decide"), ("D6", "Do"), ("D7", "Drive")]
        bw = (W - 32 * mm) / 7.0
        y0 = y - 16 * mm
        for i, (code, lab) in enumerate(steps):
            x = 16 * mm + i * bw
            c.setFillColor(STEP_COLORS[code])
            c.roundRect(x + 0.6, y0, bw - 1.4, 13.5 * mm, 1.6, stroke=0, fill=1)
            c.setFillColor(PAPER)
            c.setFont(FONT_SANS_B, 8.6)
            c.drawCentredString(x + bw / 2.0, y0 + 8 * mm, code)
            c.setFont(FONT_SANS, 5.6)
            c.drawCentredString(x + bw / 2.0, y0 + 3.2 * mm, lab)
        # lower panel: features
        py = y0 - 13 * mm
        c.setFillColor(Color(1, 1, 1, 0.08))
        c.roundRect(16 * mm, py - 62 * mm, W - 32 * mm, 62 * mm, 3, stroke=0, fill=1)
        feats = [
            ("12", "studi kasus nyata\ndengan angka & hasil"),
            ("37", "kerangka visual\nsiap pakai"),
            ("7", "worksheet latihan\n+ toolkit QR"),
            ("1", "agenda workshop\nsiap jalankan"),
        ]
        fw = (W - 32 * mm) / 4.0
        for i, (n, lab) in enumerate(feats):
            x = 16 * mm + i * fw + fw / 2.0
            c.setFillColor(ACCENT)
            c.setFont(FONT_SANS_B, 24)
            c.drawCentredString(x, py - 16 * mm, n)
            c.setFillColor(Color(1, 1, 1, 0.85))
            c.setFont(FONT_SANS_M, 7.0)
            yy = py - 24 * mm
            for ln in lab.split("\n"):
                c.drawCentredString(x, yy, ln)
                yy -= 4.2 * mm
            if i < 3:
                c.setStrokeColor(Color(1, 1, 1, 0.18))
                c.setLineWidth(0.7)
                c.line(16 * mm + (i + 1) * fw, py - 52 * mm, 16 * mm + (i + 1) * fw, py - 10 * mm)
        # bottom: author + badge
        c.setFillColor(PAPER)
        c.setFont(FONT_SERIF_B, 13)
        c.drawString(16 * mm, 22 * mm, "TUNTAS PRESS")
        c.setFillColor(Color(1, 1, 1, 0.65))
        c.setFont(FONT_SANS, 8)
        c.drawString(16 * mm, 16 * mm, "Edisi Praktisi \u00b7 Bahasa Indonesia")
        c.setFillColor(ACCENT)
        c.roundRect(W - 52 * mm, 14 * mm, 36 * mm, 11 * mm, 2, stroke=0, fill=1)
        c.setFillColor(PAPER)
        c.setFont(FONT_SANS_B, 7.4)
        c.drawCentredString(W - 34 * mm, 18 * mm, "B5 \u00b7 200 HALAMAN")
        c.restoreState()


# =====================================================================
#  Back cover
# =====================================================================
class BackCoverPage(Flowable):
    def wrap(self, aw, ah):
        self.width, self.height = aw, ah
        return self.width, self.height

    def draw(self):
        import os
        c = self.canv
        W, H = self.width, self.height
        c.saveState()
        c.setFillColor(NAVY_DEEP)
        c.rect(0, 0, W, H, stroke=0, fill=1)
        c.setFillColor(NAVY)
        c.rect(0, H - 54 * mm, W, 54 * mm, stroke=0, fill=1)
        c.setStrokeColor(ACCENT)
        c.setLineWidth(2.4)
        c.line(0, H - 54 * mm, W, H - 54 * mm)

        c.setFillColor(PAPER)
        c.setFont(FONT_SERIF_B, 34)
        c.drawString(16 * mm, H - 30 * mm, "TUNTAS")
        c.setFillColor(ACCENT)
        c.setFont(FONT_SERIF_B, 15)
        c.drawString(16.6 * mm, H - 39 * mm, "7D")
        c.setFillColor(PAPER)
        c.setFont(FONT_SERIF_IT, 12)
        c.drawString(31 * mm, H - 38.5 * mm, "Solusi Sistematis")

        y = H - 72 * mm
        c.setFillColor(Color(1, 1, 1, 0.92))
        c.setFont(FONT_SERIF, 11.4)
        pg = ("Orang pintar sering gagal menyelesaikan masalah \u2014 bukan karena kurang "
              "cerdas, tetapi karena salah mendiagnosis. Buku ini mengubah cara Anda "
              "menghadapi masalah: dari melompat ke solusi menjadi menelusuri akar, "
              "memilih dengan kriteria, dan mengunci hasil agar tidak terulang.")
        for ln in _lines(c, pg, FONT_SERIF, 11.4, W - 32 * mm):
            c.drawString(16 * mm, y, ln)
            y -= 6.1 * mm

        y -= 6 * mm
        bullets = [
            "7 langkah teruji: Detect, Define, Dig, Design, Decide, Do, Drive",
            "12 studi kasus nyata lengkap dengan angka dan hasil",
            "14 worksheet latihan siap pakai + toolkit digital via QR",
            "Agenda workshop satu hari untuk langsung diterapkan ke tim",
            "Fondasi ilmiah: bias kognitif, analisis akar, dan pengambilan keputusan",
        ]
        c.setFont(FONT_SANS, 9.4)
        for b in bullets:
            c.setFillColor(ACCENT)
            c.drawString(16 * mm, y, "\u25aa")
            c.setFillColor(Color(1, 1, 1, 0.88))
            c.drawString(21 * mm, y, b)
            y -= 6.6 * mm

        y -= 4 * mm
        c.setFillColor(Color(1, 1, 1, 0.10))
        c.roundRect(16 * mm, y - 26 * mm, W - 32 * mm, 26 * mm, 3, stroke=0, fill=1)
        c.setFillColor(ACCENT)
        c.setFont(FONT_SANS_B, 7.6)
        c.drawString(21 * mm, y - 8 * mm, "COCOK UNTUK")
        c.setFillColor(Color(1, 1, 1, 0.85))
        c.setFont(FONT_SANS, 8.6)
        c.drawString(21 * mm, y - 14 * mm,
                     "Manajer \u00b7 Konsultan \u00b7 Fasilitator \u00b7 Pemilik usaha \u00b7 "
                     "Praktisi perbaikan \u00b7 Siapa saja yang lelah menambal gejala")
        c.drawString(21 * mm, y - 20 * mm,
                     "Praktikal, berbasis data, dan bisa langsung dijalankan tanpa perangkat lunak.")

        # QR placeholder + badge
        box = 26 * mm
        bx, by = W - 16 * mm - box, 26 * mm
        c.setFillColor(Color(1, 1, 1, 0.94))
        c.roundRect(bx, by, box, box, 2, stroke=0, fill=1)
        try:
            from components import qr_image
            qr = qr_image("https://tuntas7d.id/toolkit", size=box - 3.2 * mm)
            qr.drawOn(c, bx + 1.6 * mm, by + 1.6 * mm)
        except Exception:
            c.setFillColor(NAVY)
            c.setFont(FONT_SANS_B, 7)
            c.drawCentredString(bx + box / 2.0, by + box / 2.0, "QR TOOLKIT")
        c.setFillColor(ACCENT)
        c.setFont(FONT_SANS_B, 7.2)
        c.drawCentredString(bx + box / 2.0, by - 4.4 * mm, "SCAN UNTUK TOOLKIT")
        c.setFillColor(Color(1, 1, 1, 0.6))
        c.setFont(FONT_SANS, 7)
        c.drawCentredString(bx + box / 2.0, by - 8.2 * mm, "tuntas7d.id/toolkit")

        c.setFillColor(PAPER)
        c.setFont(FONT_SERIF_B, 11)
        c.drawString(16 * mm, 20 * mm, "TUNTAS PRESS")
        c.setFillColor(Color(1, 1, 1, 0.6))
        c.setFont(FONT_SANS, 7.6)
        c.drawString(16 * mm, 15 * mm, "Buku kerja praktis \u00b7 Edisi Bahasa Indonesia \u00b7 B5")
        c.restoreState()


# =====================================================================
#  Simple full-bleed statement page
# =====================================================================
class StatementPage(Flowable):
    def __init__(self, kicker, title, body, color=NAVY, accent=ACCENT, foot=None):
        Flowable.__init__(self)
        self.kicker = kicker
        self.title = title
        self.body = body
        self.color = color
        self.accent = accent
        self.foot = foot

    def wrap(self, aw, ah):
        self.width, self.height = aw, ah
        return self.width, self.height

    def draw(self):
        c = self.canv
        W, H = self.width, self.height
        c.saveState()
        c.setFillColor(self.color)
        c.rect(0, 0, W, H, stroke=0, fill=1)
        c.setStrokeColor(Color(1, 1, 1, 0.14))
        c.setLineWidth(0.7)
        for r in (30, 48, 66, 84):
            c.circle(0, H * 0.88, r * mm, stroke=1, fill=0)
        c.setFillColor(self.accent)
        c.setFont(FONT_SANS_B, 9)
        c.drawString(MARGIN_OUTER, H * 0.80, self.kicker.upper())
        c.setStrokeColor(self.accent)
        c.setLineWidth(2.2)
        c.line(MARGIN_OUTER, H * 0.785, MARGIN_OUTER + 24 * mm, H * 0.785)
        # title
        maxw = W - MARGIN_OUTER - MARGIN_OUTER
        y = H * 0.70
        c.setFillColor(PAPER)
        for ln in _lines(c, self.title, FONT_SERIF_B, 30, maxw):
            c.setFont(FONT_SERIF_B, 30)
            c.drawString(MARGIN_OUTER, y, ln)
            y -= 13 * mm
        # body
        y -= 4 * mm
        ps = ParagraphStyle("sb", fontName=FONT_SERIF, fontSize=12.4, leading=19.5,
                            textColor=Color(1, 1, 1, 0.88))
        p = Paragraph(self.body, ps)
        w, h = p.wrap(maxw, 10 ** 6)
        p.drawOn(c, MARGIN_OUTER, y - h)
        if self.foot:
            c.setFillColor(Color(1, 1, 1, 0.5))
            c.setFont(FONT_SANS, 8)
            c.drawString(MARGIN_OUTER, 20 * mm, self.foot)
        c.restoreState()


# =====================================================================
#  Title page (half title + imprint)
# =====================================================================
class TitlePage(Flowable):
    def __init__(self, variant="title"):
        Flowable.__init__(self)
        self.variant = variant

    def wrap(self, aw, ah):
        self.width, self.height = aw, ah
        return self.width, self.height

    def draw(self):
        c = self.canv
        W, H = self.width, self.height
        c.saveState()
        if self.variant == "halftitle":
            c.setFillColor(PAPER)
            c.rect(0, 0, W, H, stroke=0, fill=1)
            c.setFillColor(NAVY)
            c.setFont(FONT_SERIF_B, 34)
            c.drawString(MARGIN_OUTER, H * 0.62, "TUNTAS")
            c.setFillColor(ACCENT)
            c.setFont(FONT_SERIF_B, 17)
            c.drawString(MARGIN_OUTER + 2, H * 0.575, "7D")
            c.setFillColor(GREY)
            c.setFont(FONT_SERIF_IT, 11.5)
            c.drawString(MARGIN_OUTER + 20 * mm, H * 0.577, "Solusi Sistematis")
            c.setStrokeColor(ACCENT)
            c.setLineWidth(2)
            c.line(MARGIN_OUTER, H * 0.545, MARGIN_OUTER + 30 * mm, H * 0.545)
            c.setFillColor(GREY)
            c.setFont(FONT_SANS, 8.5)
            c.drawString(MARGIN_OUTER, H * 0.50,
                         "Panduan praktis menyelesaikan masalah dari akar sampai hasil.")
            c.drawString(MARGIN_OUTER, H * 0.50 - 5 * mm,
                         "Dilengkapi 12 studi kasus, worksheet latihan, dan agenda workshop.")
        else:
            c.setFillColor(PAPER)
            c.rect(0, 0, W, H, stroke=0, fill=1)
            y = H * 0.68
            c.setFillColor(NAVY)
            c.setFont(FONT_SERIF_B, 40)
            c.drawString(MARGIN_OUTER, y, "TUNTAS")
            c.setFillColor(ACCENT)
            c.setFont(FONT_SERIF_B, 20)
            c.drawString(MARGIN_OUTER + 2, y - 12 * mm, "7D")
            c.setFillColor(NAVY)
            c.setFont(FONT_SERIF_IT, 13)
            c.drawString(MARGIN_OUTER + 22 * mm, y - 11.6 * mm, "Solusi Sistematis")
            c.setStrokeColor(ACCENT)
            c.setLineWidth(2.2)
            c.line(MARGIN_OUTER, y - 17 * mm, MARGIN_OUTER + 34 * mm, y - 17 * mm)
            ps = ParagraphStyle("tp", fontName=FONT_SERIF, fontSize=12, leading=18,
                                textColor=INK)
            p = Paragraph("Buku kerja untuk individu, tim, dan organisasi yang ingin "
                          "berhenti menambal gejala dan mulai menyelesaikan akar masalah.",
                          ps)
            w, h = p.wrap(W - 2 * MARGIN_OUTER, 10 ** 6)
            p.drawOn(c, MARGIN_OUTER, y - 27 * mm - h)
            c.setFillColor(GREY)
            c.setFont(FONT_SANS_B, 9)
            c.drawString(MARGIN_OUTER, H * 0.22, "TUNTAS PRESS")
            c.setFont(FONT_SANS, 8)
            lines = [
                "Edisi pertama \u00b7 Bahasa Indonesia",
                "Format B5 \u00b7 200 halaman",
                "Dilengkapi toolkit digital dan worksheet yang dapat diunduh",
            ]
            for i, ln in enumerate(lines):
                c.drawString(MARGIN_OUTER, H * 0.22 - 6 * mm - i * 4.6 * mm, ln)
            c.setFillColor(GREY_LIGHT)
            c.setFont(FONT_SANS, 7.2)
            c.drawString(MARGIN_OUTER, 26 * mm,
                         "Dilarang memperbanyak sebagian atau seluruh isi buku tanpa izin tertulis dari penerbit.")
        c.restoreState()


# =====================================================================
#  Copyright / credits page
# =====================================================================
class CreditsPage(Flowable):
    def wrap(self, aw, ah):
        self.width, self.height = aw, ah
        return self.width, self.height

    def draw(self):
        c = self.canv
        W, H = self.width, self.height
        c.saveState()
        c.setFillColor(PAPER)
        c.rect(0, 0, W, H, stroke=0, fill=1)
        c.setFillColor(NAVY)
        c.setFont(FONT_SANS_B, 8)
        c.drawString(MARGIN_OUTER, H - 30 * mm, "TUNTAS 7D \u2014 SOLUSI SISTEMATIS")
        c.setFillColor(INK)
        c.setFont(FONT_SERIF, 9.2)
        blocks = [
            ("Tentang buku ini",
             "Buku ini menawarkan satu kerangka kerja bernama TUNTAS 7D: tujuh langkah "
             "yang menyusun cara berpikir dan cara bekerja ketika menghadapi masalah. "
             "Pendekatannya menggabungkan tradisi perbaikan berkelanjutan, riset "
             "pengambilan keputusan, dan praktik konsultan internasional, lalu "
             "diterjemahkan menjadi alat yang bisa langsung dipakai."),
            ("Cara memakai",
             "Setiap bab langkah memakai urutan yang sama: cerita pembuka, konsep inti "
             "dengan gambar rangka, alat praktis langkah demi langkah, studi kasus nyata, "
             "dan worksheet. Untuk workshop, pakai Bab 12 sebagai panduan fasilitator."),
            ("Catatan tentang kasus",
             "Studi kasus dalam buku ini disusun dari pola yang berulang di banyak "
             "organisasi. Nama lembaga, angka, dan kutipan disajikan sebagai ilustrasi "
             "yang telah disusun ulang agar aman dipublikasikan. Pola masalah, logika "
             "analisis, dan bentuk solusinya mengikuti praktik yang lazim dipakai oleh "
             "praktisi perbaikan dan konsultan."),
            ("Referensi",
             "Daftar pustaka ilmiah dan sumber praktik tersedia di bagian penutup. "
             "Setiap alat yang diperkenalkan di buku ini dapat ditelusuri asal-usulnya "
             "melalui daftar tersebut."),
        ]
        y = H - 42 * mm
        st = ParagraphStyle("cr", fontName=FONT_SERIF, fontSize=9.0, leading=13.6,
                            textColor=INK)
        for title, body in blocks:
            c.setFillColor(TEAL)
            c.setFont(FONT_SANS_B, 8.4)
            c.drawString(MARGIN_OUTER, y, title)
            y -= 5.4 * mm
            p = Paragraph(body, st)
            w, h = p.wrap(W - 2 * MARGIN_OUTER, 10 ** 6)
            p.drawOn(c, MARGIN_OUTER, y - h)
            y -= h + 8
        c.setFillColor(GREY)
        c.setFont(FONT_SANS, 7.4)
        c.drawString(MARGIN_OUTER, 28 * mm,
                     "Versi digital buku ini dilengkapi tautan dan kode QR menuju worksheet, "
                     "template, dan toolkit yang bisa diunduh.")
        c.restoreState()


# =====================================================================
#  Section openers for front matter
# =====================================================================
def section_banner(kicker, title, blurb, color=NAVY, accent=ACCENT):
    return StatementPage(kicker, title, blurb, color=color, accent=accent)
