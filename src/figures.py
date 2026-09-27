"""Scientific & practical diagram library for the book.

Every figure draws itself on a reportlab canvas of a given (w, h) in points.
"""
import math
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import Paragraph

from theme import *  # noqa
from engine import Figure, FONT_SANS, FONT_SANS_B, FONT_SANS_M, FONT_SANS_SB, FONT_SERIF, FONT_SERIF_B, FONT_SERIF_IT
from dsl import register_figure


def _wrap(c, text, font, size, maxw, leading=None, align="c"):
    leading = leading or size * 1.25
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if c.stringWidth(t, font, size) > maxw and cur:
            lines.append(cur)
            cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines, leading


def _ctext(c, x, y, text, font, size, color, maxw, leading=None):
    """Centered multi-line text; returns height used."""
    lines, lead = _wrap(c, text, font, size, maxw)
    c.setFont(font, size)
    c.setFillColor(color)
    for ln in lines:
        c.drawCentredString(x, y, ln)
        y -= lead
    return len(lines) * lead


def _dtext(c, x, y, text, font, size, color, maxw):
    lines, lead = _wrap(c, text, font, size, maxw)
    c.setFont(font, size)
    c.setFillColor(color)
    for ln in lines:
        c.drawString(x, y, ln)
        y -= lead
    return len(lines) * lead


# =====================================================================
#  1. TUNTAS 7D — the master framework
# =====================================================================
def fig_tuntas_7d(active=None, compact=False):
    h = 62 * mm if not compact else 52 * mm

    def drawer(c, w, hh):
        steps = [
            ("D1", "Detect", "Kenali masalah"),
            ("D2", "Define", "Rumuskan tajam"),
            ("D3", "Dig", "Gali akar"),
            ("D4", "Design", "Rancang opsi"),
            ("D5", "Decide", "Pilih solusi"),
            ("D6", "Do", "Jalankan"),
            ("D7", "Drive", "Kunci hasil"),
        ]
        n = len(steps)
        gap = 2.4
        bw = (w - gap * (n - 1)) / n
        barh = 13 * mm
        base = hh - barh - 4
        # baseline ribbon
        for i, (code, label, sub) in enumerate(steps):
            x = i * (bw + gap)
            col = STEP_COLORS[code]
            dim = active and code not in active if isinstance(active, (list, tuple)) else (active and code != active)
            if dim:
                col = Color(col.red, col.green, col.blue, 0.35)
            c.setFillColor(col)
            c.roundRect(x, 0, bw, barh, 2.5, stroke=0, fill=1)
            c.setFillColor(PAPER)
            c.setFont(FONT_SANS_B, 9)
            c.drawCentredString(x + bw / 2.0, barh - 9, code)
            c.setFont(FONT_SANS, 6.4)
            c.drawCentredString(x + bw / 2.0, 3.2, label)
            # vertical guide + label above
            c.setStrokeColor(GREY_LIGHT)
            c.setLineWidth(0.5)
            c.setDash(1, 1.6)
            c.line(x + bw / 2.0, barh + 1, x + bw / 2.0, base)
            c.setDash()
            c.setFillColor(col)
            c.circle(x + bw / 2.0, base + 1.6, 1.9, stroke=0, fill=1)
            _ctext(c, x + bw / 2.0, base - 3, sub, FONT_SANS_M, 6.6,
                   INK if not dim else GREY, bw + 5, 8)
            if i < n - 1:
                c.setFillColor(GREY)
                c.setFont(FONT_SANS_B, 8)
                c.drawCentredString(x + bw + gap / 2.0, barh / 2.0 - 3, "\u203a")
        # arc title
        c.setFillColor(NAVY)
        c.setFont(FONT_SANS_B, 7.2)
        c.drawString(0, hh - 8, "ALUR TUNTAS 7D")
        c.setFont(FONT_SANS, 6.6)
        c.drawRightString(w, hh - 8, "dua langkah pertama = 50% keberhasilan")
    return Figure(h, drawer, bg=CREAM, pad=6, space_before=3, space_after=8)


# =====================================================================
#  2. Iceberg: gejala / masalah / akar
# =====================================================================
def fig_iceberg():
    h = 66 * mm

    def drawer(c, w, hh):
        c.setFillColor(None) if False else None
        cx = w * 0.42
        # water
        c.setFillColor(HexColor("#DCEBF5"))
        c.rect(0, 0, w, hh * 0.58, stroke=0, fill=1)
        c.setFillColor(HexColor("#EAF4FA"))
        c.rect(0, hh * 0.58, w, hh * 0.42, stroke=0, fill=1)
        c.setStrokeColor(HexColor("#9FC3DE"))
        c.setLineWidth(0.7)
        c.setDash(2, 2)
        c.line(0, hh * 0.58, w, hh * 0.58)
        c.setDash()
        c.setFillColor(HexColor("#3E7CA6"))
        c.setFont(FONT_SANS_B, 6.6)
        c.drawRightString(w - 3, hh * 0.58 + 2.5, "PERMUKAAN YANG TERLIHAT")
        c.drawRightString(w - 3, hh * 0.58 - 8, "DI BAWAH PERMUKAAN")
        # iceberg polygon
        c.setFillColor(HexColor("#9FC3DE"))
        p = c.beginPath()
        p.moveTo(cx - 26, hh * 0.58)      # waterline left
        p.lineTo(cx - 22, hh * 0.90)
        p.lineTo(cx, hh * 0.98)
        p.lineTo(cx + 22, hh * 0.90)
        p.lineTo(cx + 26, hh * 0.58)
        p.lineTo(cx + 34, hh * 0.30)
        p.lineTo(cx + 10, hh * 0.06)
        p.lineTo(cx - 14, hh * 0.10)
        p.lineTo(cx - 33, hh * 0.34)
        p.close()
        c.drawPath(p, stroke=0, fill=1)
        c.setFillColor(PAPER)
        c.setFont(FONT_SANS_B, 8.4)
        c.drawCentredString(cx, hh * 0.86, "GEJALA")
        c.setFont(FONT_SANS, 6.2)
        c.drawCentredString(cx, hh * 0.80, "yang dilaporkan")
        c.setFont(FONT_SANS_B, 8.4)
        c.setFillColor(NAVY)
        c.drawCentredString(cx, hh * 0.40, "MASALAH")
        c.setFont(FONT_SANS, 6.2)
        c.drawCentredString(cx, hh * 0.33, "yang terukur")
        c.setFillColor(ACCENT)
        c.setFont(FONT_SANS_B, 8.8)
        c.drawCentredString(cx, hh * 0.19, "AKAR")
        c.setFont(FONT_SANS, 6.2)
        c.drawCentredString(cx, hh * 0.12, "penyebab sistemik")
        # right annotation stack
        items = [("Gejala", "Komplain, error, keluhan, angka turun."),
                 ("Masalah", "Pola yang bisa diukur & diulang."),
                 ("Akar", "Struktur, proses, atau kebijakan.")]
        y = hh * 0.86
        for t, d in items:
            c.setFillColor(ACCENT)
            c.circle(w - 3, y + 1.5, 1.5, stroke=0, fill=1)
            hused = _dtext(c, w - 60 * mm if w > 60 * mm else w * 0.62, y,
                           "<b>%s</b> \u2014 %s" % (t, d), FONT_SANS, 6.4, INK, w * 0.36)
            y -= hused + 6
    return Figure(h, drawer, caption="Gambar. Gunakan analogi gunung es: yang kamu lihat setiap hari hampir selalu hanya ujungnya.",
                  bg=PAPER, pad=4)


# =====================================================================
#  3. Bias map
# =====================================================================
def fig_bias_map():
    h = 72 * mm

    def drawer(c, w, hh):
        items = [
            ("Bias konfirmasi", "Mencari bukti yang membenarkan dugaan awal."),
            ("Efek jangkar", "Terpaku pada angka pertama yang kamu dengar."),
            ("Ketersediaan", "Solusi termudah yang paling ingat dianggap terbaik."),
            ("Kausalitas palsu", "Mengaitkan dua hal yang hanya kebetulan berdekatan."),
            ("Bias ahli", "Merasa sudah tahu, berhenti bertanya."),
            ("Kelompok", "Ikut suara mayoritas agar dianggap aman."),
        ]
        cols = 2
        cw = (w - 6) / cols
        rh = (hh - 8) / 3.0
        for i, (t, d) in enumerate(items):
            r, col = divmod(i, cols)
            x = col * (cw + 6)
            y = hh - (r + 1) * rh
            c.setFillColor(HexColor("#FDF0ED"))
            c.roundRect(x, y + 3, cw, rh - 6, 2.5, stroke=0, fill=1)
            c.setFillColor(ACCENT)
            c.rect(x, y + 3, 2.2, rh - 6, stroke=0, fill=1)
            _dtext(c, x + 7, y + rh - 12, t, FONT_SANS_B, 7.4, NAVY, cw - 12)
            _dtext(c, x + 7, y + rh - 22, d, FONT_SANS, 6.4, INK, cw - 12)
    return Figure(h, drawer, caption="Gambar. Enam jebakan berpikir paling sering yang membuat orang pintar mengambil keputusan keliru.",
                  bg=PAPER, pad=5)


# =====================================================================
#  4. Mindset triad
# =====================================================================
def fig_mindset():
    h = 68 * mm

    def drawer(c, w, hh):
        cx, cy, R = w / 2.0, hh * 0.55, 20 * mm
        tri = [("Curiosity", "Bertanya sebelum menjawab", ACCENT, -90),
               ("Clarity", "Memisahkan fakta dari cerita", TEAL, 30),
               ("Courage", "Berani mengubah, bukan menambal", VIOLET, 150)]
        pts = []
        for _, _, _, ang in tri:
            a = math.radians(ang)
            pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
        c.setFillColor(HexColor("#F2F5FA"))
        pth = c.beginPath()
        pth.moveTo(*pts[0])
        pth.lineTo(*pts[1])
        pth.lineTo(*pts[2])
        pth.close()
        c.drawPath(pth, stroke=0, fill=1)
        c.setStrokeColor(HexColor("#C7D2E3"))
        c.setLineWidth(0.8)
        c.drawPath(pth, stroke=1, fill=0)
        for (t, d, col, ang), (x, y) in zip(tri, pts):
            c.setFillColor(col)
            c.circle(x, y, 11 * mm, stroke=0, fill=1)
            c.setFillColor(PAPER)
            c.setFont(FONT_SANS_B, 8.0)
            c.drawCentredString(x, y + 1.5, t)
            c.setFont(FONT_SANS, 5.9)
            c.drawCentredString(x, y - 6, "MIND-SET")
        _ctext(c, cx, cy + 4, "TUNTAS", FONT_SERIF_B, 13, NAVY, 40 * mm)
        _ctext(c, cx, cy - 7, "3 sikap dasar", FONT_SANS_M, 6.8, GREY, 40 * mm)
        _dtext(c, 0, 6, "Curiosity \u2192 kumpulkan informasi jujur  \u00b7  Clarity \u2192 rumuskan tajam  \u00b7  Courage \u2192 eksekusi utuh",
               FONT_SANS_M, 6.4, GREY, w)
    return Figure(h, drawer, caption="Gambar. Tiga sikap dasar ini jauh lebih menentukan hasil daripada kecerdasan.",
                  bg=PAPER, pad=4)


# =====================================================================
#  5. Cynefin-lite: jenis masalah
# =====================================================================
def fig_problem_types():
    h = 70 * mm

    def drawer(c, w, hh):
        quads = [
            ("SEDERHANA", "Jawaban jelas, cukup ikuti SOP.", "#E4F3E9", GREEN),
            ("RUMIT", "Butuh analisis ahli, ada sebab-akibat.", "#E3F2EF", TEAL),
            ("KOMPLEKS", "Sebab-akibat baru terlihat setelah dicoba.", "#FDF3DC", AMBER),
            ("KACAU", "Prioritasnya hentikan kerugian dulu.", "#FBE7E3", RED),
        ]
        cw = w / 2.0
        rh = hh / 2.0
        for i, (t, d, bg, col) in enumerate(quads):
            r, cc = divmod(i, 2)
            x, y = cc * cw, hh - (r + 1) * rh
            c.setFillColor(HexColor(bg))
            c.rect(x, y, cw, rh, stroke=0, fill=1)
            c.setStrokeColor(PAPER)
            c.setLineWidth(1.4)
            c.rect(x, y, cw, rh, stroke=1, fill=0)
            c.setFillColor(col)
            c.circle(x + 8, y + rh - 10, 3, stroke=0, fill=1)
            _dtext(c, x + 15, y + rh - 13.5, t, FONT_SANS_B, 8.2, col, cw - 20)
            _dtext(c, x + 8, y + rh - 24, d, FONT_SANS, 6.6, INK, cw - 14)
        _ctext(c, w / 2.0, hh - 8, "4 JENIS MASALAH \u2014 4 PENDEKATAN BERBEDA",
               FONT_SANS_B, 7.0, NAVY, w)
    return Figure(h, drawer, caption="Gambar. Kesalahan umum: memakai pendekatan 'coba-coba' untuk masalah rumit, atau analisis panjang untuk masalah kacau yang menuntut tindakan cepat.",
                  bg=PAPER, pad=5)


# =====================================================================
#  6. 5 Whys ladder
# =====================================================================
def fig_5whys(chain=None):
    chain = chain or [
        ("Gejala", "Produk sering dikembalikan pelanggan"),
        ("Why 1", "Kemasan bocor saat pengiriman"),
        ("Why 2", "Segel tutup tidak menempel sempurna"),
        ("Why 3", "Mesin press berhenti sesaat saat proses segel"),
        ("Why 4", "Tidak ada alarm saat tekanan mesin turun"),
        ("Akar", "Perawatan preventif tidak terjadwal pada sensor tekanan"),
    ]
    h = 74 * mm

    def drawer(c, w, hh):
        n = len(chain)
        rh = (hh - 4) / n
        for i, (tag, txt) in enumerate(chain):
            y = hh - (i + 1) * rh
            last = i == n - 1
            col = ACCENT if last else TEAL
            c.setFillColor(HexColor("#FDF0ED") if last else HexColor("#EEF7F5"))
            c.roundRect(6, y + 2, w - 12, rh - 4.5, 2.5, stroke=0, fill=1)
            c.setFillColor(col)
            c.roundRect(6, y + 2, 3.2, rh - 4.5, 1.2, stroke=0, fill=1)
            c.setFillColor(col)
            c.setFont(FONT_SANS_B, 7.2)
            c.drawString(13, y + rh - 12.5, tag.upper())
            _dtext(c, 42, y + rh - 12.5, txt, FONT_SANS_M, 7.4, INK, w - 52)
            if i < n - 1:
                c.setFillColor(GREY)
                c.setFont(FONT_SANS_B, 7)
                c.drawCentredString(24, y + 2.5, "\u25bc")
    return Figure(h, drawer, caption="Gambar. Lima 'kenapa' cukup untuk mengubah pernyataan keluhan menjadi penyebab yang bisa diperbaiki.",
                  bg=PAPER, pad=4)


# =====================================================================
#  7. Fishbone
# =====================================================================
def fig_fishbone():
    h = 72 * mm

    def drawer(c, w, hh):
        spine_y = hh * 0.46
        # spine
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.4)
        c.line(6, spine_y, w - 6, spine_y)
        # head
        c.setFillColor(ACCENT)
        c.roundRect(w - 46, spine_y - 7, 40, 14, 3, stroke=0, fill=1)
        c.setFillColor(PAPER)
        c.setFont(FONT_SANS_B, 7)
        c.drawCentredString(w - 26, spine_y - 2.5, "MASALAH")
        bones = [
            ("Metode", "Prosedur tidak baku", -1),
            ("Mesin", "Kalibrasi jarang", -1),
            ("Material", "Bahan tidak konsisten", -1),
            ("Manusia", "Pelatihan minim", 1),
            ("Ukuran", "KPI tidak jelas", 1),
            ("Lingkungan", "Ruang sempit", 1),
        ]
        n = len(bones) // 2
        x0 = 14.0
        step = (w - 80) / n
        for k in range(n):
            for j, (label, desc, side) in enumerate(bones):
                pass
        # upper bones (first half) and lower bones
        ups = bones[:3]
        downs = bones[3:]
        for k, (label, desc, _) in enumerate(ups):
            x = x0 + k * step
            y2 = hh - 6
            c.setStrokeColor(TEAL)
            c.setLineWidth(1.0)
            c.line(x, spine_y, x + 10, y2)
            _dtext(c, x - 2, y2 - 2, label, FONT_SANS_B, 7, TEAL, step)
            _dtext(c, x - 2, y2 - 11, desc, FONT_SANS, 6.1, GREY, step)
        for k, (label, desc, _) in enumerate(downs):
            x = x0 + 6 + k * step
            y2 = 6
            c.setStrokeColor(VIOLET)
            c.setLineWidth(1.0)
            c.line(x, spine_y, x + 10, y2 + 8)
            _dtext(c, x - 2, y2 + 12, label, FONT_SANS_B, 7, VIOLET, step)
            _dtext(c, x - 2, y2 + 3, desc, FONT_SANS, 6.1, GREY, step)
    return Figure(h, drawer, caption="Gambar. Diagram tulang ikan memaksa kamu memeriksa semua kategori sebab, bukan hanya kategori yang paling kamu kuasai.",
                  bg=PAPER, pad=4)


# =====================================================================
#  8. Pareto
# =====================================================================
def fig_pareto():
    h = 62 * mm

    def drawer(c, w, hh):
        data = [("A", 42), ("B", 26), ("C", 15), ("D", 9), ("E", 5), ("F", 3)]
        total = sum(v for _, v in data)
        cw = (w - 30) / len(data)
        base = 12.0
        top = hh - 16
        cum = 0
        pts = []
        for i, (lab, v) in enumerate(data):
            x = 24 + i * cw
            bh = (v / 45.0) * (top - base)
            c.setFillColor(TEAL if i < 2 else HexColor("#9FCFC6"))
            c.rect(x + 2, base, cw - 6, bh, stroke=0, fill=1)
            c.setFillColor(PAPER)
            c.setFont(FONT_SANS_B, 6.4)
            c.drawCentredString(x + cw / 2.0 - 1, base + bh - 8, str(v))
            c.setFillColor(INK)
            c.setFont(FONT_SANS, 6.4)
            c.drawCentredString(x + cw / 2.0 - 1, base - 7, lab)
            cum += v
            pts.append((x + cw / 2.0 - 1, base + (cum / total) * (top - base)))
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1.3)
        pth = c.beginPath()
        pth.moveTo(*pts[0])
        for p in pts[1:]:
            pth.lineTo(*p)
        c.drawPath(pth, stroke=1, fill=0)
        for p in pts:
            c.setFillColor(ACCENT)
            c.circle(p[0], p[1], 1.6, stroke=0, fill=1)
        # 80% marker
        y80 = base + 0.8 * (top - base)
        c.setStrokeColor(GREY)
        c.setDash(2, 2)
        c.setLineWidth(0.6)
        c.line(20, y80, w - 6, y80)
        c.setDash()
        c.setFillColor(ACCENT)
        c.setFont(FONT_SANS_B, 6.2)
        c.drawString(w - 42, y80 + 2.5, "80% dampak")
        c.setFillColor(GREY)
        c.setFont(FONT_SANS_B, 6.2)
        c.drawString(0, top + 2, "DAMPAK")
        c.drawString(0, base - 7, "SEBAB")
    return Figure(h, drawer, caption="Gambar. Prinsip Pareto: sekitar 80% dampak biasanya datang dari 20% penyebab. Tentukan target perbaikan dari batang tertinggi.",
                  bg=PAPER, pad=4)


# =====================================================================
#  9. Problem statement canvas (D2)
# =====================================================================
def fig_define_canvas():
    h = 74 * mm

    def drawer(c, w, hh):
        rows = [
            ("APA", "Apa yang salah / ingin diperbaiki?", "Kualitas"),
            ("SIAPA", "Siapa yang terdampak paling besar?", "Orang"),
            ("DI MANA", "Di bagian mana masalah terjadi?", "Tempat"),
            ("KAPAN", "Sejak kapan, seberapa sering?", "Waktu"),
            ("SEBERAPA BESAR", "Angka baseline vs target", "Dampak"),
            ("KENAPA PENTING", "Konsekuensi bila dibiarkan", "Nilai"),
        ]
        rh = (hh - 6) / len(rows)
        for i, (k, q, tag) in enumerate(rows):
            y = hh - (i + 1) * rh
            c.setFillColor(HexColor("#F6F4EF") if i % 2 == 0 else PAPER)
            c.rect(0, y + 1.5, w, rh - 3, stroke=0, fill=1)
            c.setFillColor(TEAL)
            c.setFont(FONT_SANS_B, 6.8)
            c.drawString(4, y + rh - 10, k)
            _dtext(c, 74, y + rh - 10, q, FONT_SERIF, 7.4, INK, w - 82)
            c.setFillColor(GREY)
            c.setFont(FONT_SANS, 6, 0) if False else None
            c.setFont(FONT_SANS_M, 6.0)
            c.drawRightString(w - 3, y + 4, tag)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.6)
        for i in range(1, len(rows)):
            y = hh - i * rh
            c.line(0, y, w, y)
    return Figure(h, drawer, caption="Gambar. Kerangka perumusan masalah. Isi keenam baris ini sebelum mencari solusi apa pun.",
                  bg=PAPER, pad=4)


# =====================================================================
#  10. Impact / effort matrix
# =====================================================================
def fig_impact_effort():
    h = 74 * mm

    def drawer(c, w, hh):
        pad = 16
        gw, gh = w - pad - 6, hh - pad - 6
        x0, y0 = pad, 6
        quads = [
            (0, 1, "QUICK WINS", "Dampak besar, usaha kecil \u2192 kerjakan sekarang", GREEN, "#E4F3E9"),
            (1, 1, "PROYEK BESAR", "Dampak besar, usaha besar \u2192 rencanakan", TEAL, "#E3F2EF"),
            (0, 0, "ISIAN KECIL", "Dampak kecil, usaha kecil \u2192 sambil lalu", GREY, "#F2F2F2"),
            (1, 0, "BUANG WAKTU", "Dampak kecil, usaha besar \u2192 tinggalkan", RED, "#FBE7E3"),
        ]
        for cx, cy, t, d, col, bg in quads:
            x = x0 + cx * gw / 2.0
            y = y0 + cy * gh / 2.0
            c.setFillColor(HexColor(bg))
            c.rect(x, y, gw / 2.0, gh / 2.0, stroke=0, fill=1)
            c.setStrokeColor(PAPER)
            c.setLineWidth(1.2)
            c.rect(x, y, gw / 2.0, gh / 2.0, stroke=1, fill=0)
            _dtext(c, x + 6, y + gh / 2.0 - 12, t, FONT_SANS_B, 7.4, col, gw / 2.0 - 12)
            _dtext(c, x + 6, y + gh / 2.0 - 22, d, FONT_SANS, 6.0, INK, gw / 2.0 - 12)
        c.setStrokeColor(INK)
        c.setLineWidth(1.0)
        c.line(x0, y0, x0, y0 + gh)
        c.line(x0, y0, x0 + gw, y0)
        c.setFillColor(GREY)
        c.setFont(FONT_SANS_B, 6.2)
        c.drawCentredString(w / 2.0, 0.0, "SUMBU X: USAHA / BIAYA \u2192 tinggi")
        c.drawCentredString(w / 2.0, hh - 6, "SUMBU Y: DAMPAK \u2192 tinggi ke atas")
    return Figure(h, drawer, caption="Gambar. Sebelum memilih solusi, petakan setiap opsi ke empat kuadran ini.",
                  bg=PAPER, pad=4)


# =====================================================================
#  11. Decision matrix
# =====================================================================
def fig_decision_matrix():
    h = 68 * mm

    def drawer(c, w, hh):
        crit = [("Dampak", 0.35), ("Biaya", 0.20), ("Kecepatan", 0.15),
                ("Risiko", 0.15), ("Dukungan tim", 0.15)]
        alts = [("Opsi A", [5, 2, 4, 4, 5]), ("Opsi B", [4, 4, 3, 3, 4]),
                ("Opsi C", [3, 5, 5, 4, 3])]
        left = 44
        cw = (w - left - 6) / (len(crit) + 1)
        rh = 13
        top = hh - 20
        c.setFillColor(NAVY)
        c.roundRect(left, top, w - left - 6, rh, 0, stroke=0, fill=1)
        c.setFillColor(PAPER)
        c.setFont(FONT_SANS_B, 6.2)
        for i, (cn, wt) in enumerate(crit):
            c.drawCentredString(left + (i + 0.5) * cw, top + 4.5, cn[:8])
            c.setFont(FONT_SANS, 5.6)
            c.drawCentredString(left + (i + 0.5) * cw, top + 1.0, "%d%%" % int(wt * 100))
            c.setFont(FONT_SANS_B, 6.2)
        c.drawCentredString(left + (len(crit) + 0.5) * cw, top + 3, "TOTAL")
        best = None
        scores = []
        for ai, (an, vals) in enumerate(alts):
            y = top - (ai + 1) * rh
            tot = sum(v * wt for v, (_, wt) in zip(vals, crit))
            scores.append((tot, an))
            c.setFillColor(PAPER if ai % 2 else HexColor("#F6F4EF"))
            c.rect(left, y, w - left - 6, rh, stroke=0, fill=1)
            c.setFillColor(INK)
            c.setFont(FONT_SANS_B, 6.6)
            c.drawString(4, y + 4.5, an)
            for i, v in enumerate(vals):
                c.setFillColor(TEAL if v >= 4 else (AMBER if v == 3 else GREY))
                c.setFont(FONT_SANS_SB, 7)
                c.drawCentredString(left + (i + 0.5) * cw, y + 4.5, str(v))
            c.setFillColor(ACCENT)
            c.setFont(FONT_SANS_B, 7.4)
            c.drawCentredString(left + (len(crit) + 0.5) * cw, y + 4.5, "%.2f" % tot)
        best = max(scores)
        c.setFillColor(ACCENT_SOFT)
        c.roundRect(left, top - 3 * rh - 4, w - left - 6, 3, 0, stroke=0, fill=1)
        c.setFillColor(ACCENT)
        c.setFont(FONT_SANS_B, 6.6)
        c.drawString(4, top - 3 * rh - 13, "Pemenang: %s" % best[1])
        c.setFont(FONT_SANS, 6.0)
        c.drawRightString(w - 6, top - 3 * rh - 13, "skor 1\u20135 \u00d7 bobot kriteria")
    return Figure(h, drawer, caption="Gambar. Beri skor setiap opsi pada kriteria ber-bobot, lalu jumlahkan. Keputusan jadi bisa dipertanggungjawabkan.",
                  bg=PAPER, pad=4)


# =====================================================================
#  12. PDCA / D6 execution loop
# =====================================================================
def fig_pdca():
    h = 64 * mm

    def drawer(c, w, hh):
        cx, cy, R = w / 2.0, hh / 2.0, 20 * mm
        segs = [("PLAN", "Rencana mini", TEAL, 90, 180),
                ("DO", "Uji skala kecil", ACCENT, 0, 90),
                ("CHECK", "Ukur hasil", AMBER, 270, 360),
                ("ACT", "Bakukan / perbaiki", VIOLET, 180, 270)]
        for name, desc, col, a0, a1 in segs:
            c.setFillColor(col)
            c.setStrokeColor(PAPER)
            c.setLineWidth(1.2)
            p = c.beginPath()
            p.moveTo(cx, cy)
            p.arcTo(cx - R, cy - R, cx + R, cy + R, a0, a1)
            p.close()
            c.drawPath(p, stroke=1, fill=1)
        c.setFillColor(PAPER)
        c.circle(cx, cy, R * 0.45, stroke=0, fill=1)
        c.setFillColor(NAVY)
        c.setFont(FONT_SANS_B, 7.6)
        c.drawCentredString(cx, cy - 1, "SIKLUS")
        c.setFont(FONT_SANS, 6.2)
        c.drawCentredString(cx, cy - 8, "PERBAIKAN")
        labels = [("PLAN", cx, cy + R + 4), ("DO", cx + R + 4, cy + 4),
                  ("CHECK", cx, cy - R - 10), ("ACT", cx - R - 14, cy + 4)]
        for lab, x, y in labels:
            c.setFillColor(NAVY)
            c.setFont(FONT_SANS_B, 6.6)
            c.drawCentredString(x, y, lab)
    return Figure(h, drawer, caption="Gambar. Eksekusi terbaik berjalan berulang: uji kecil, ukur, perbaiki, lalu bakukan. Bukan satu proyek raksasa sekali jalan.",
                  bg=PAPER, pad=4)


# =====================================================================
#  13. Driver diagram (D7)
# =====================================================================
def fig_driver():
    h = 70 * mm

    def drawer(c, w, hh):
        goalx = w - 62
        c.setFillColor(ACCENT)
        c.roundRect(goalx, hh / 2.0 - 13, 60, 26, 3, stroke=0, fill=1)
        _ctext(c, goalx + 30, hh / 2.0 + 4, "SASARAN", FONT_SANS_B, 7.4, PAPER, 54)
        _dtext(c, goalx + 6, hh / 2.0 - 2, "Bertahan 6 bulan", FONT_SANS, 6.0, PAPER, 52)
        drivers = [("Pencegahan", ["Jadwal servis", "Checklist harian"]),
                   ("Deteksi cepat", ["Alarm sensor", "Laporan 1 jam"]),
                   ("Respon", ["Petugas jaga", "Spare part siap"])]
        rows_y = [hh - 40, hh / 2.0 - 14, 4]
        c.setFillColor(TEAL)
        c.setFont(FONT_SANS_B, 6.6)
        for i, (dv, acts) in enumerate(drivers):
            y = rows_y[i]
            c.setFillColor(TEAL)
            c.roundRect(58, y + 7, 52, 16, 2.5, stroke=0, fill=1)
            _ctext(c, 84, y + 15, dv, FONT_SANS_B, 6.6, PAPER, 48)
            c.setStrokeColor(TEAL)
            c.setLineWidth(0.9)
            c.line(110, y + 15, goalx, hh / 2.0)
            for j, ac in enumerate(acts):
                ax = 4
                ay = y + 7 + j * 8.6
                c.setFillColor(HexColor("#E3F2EF"))
                c.roundRect(ax, ay, 46, 7.2, 2, stroke=0, fill=1)
                _dtext(c, ax + 3, ay + 2.0, ac, FONT_SANS, 5.5, INK, 42)
        c.setFillColor(GREY)
        c.setFont(FONT_SANS_B, 6.2)
        c.drawString(4, hh - 8, "TINDAKAN")
        c.drawString(58, hh - 8, "PENGGERAK")
    return Figure(h, drawer, caption="Gambar. Diagram penggerak menghubungkan setiap tindakan dengan penggerak, dan setiap penggerak dengan satu sasaran yang jelas.",
                  bg=PAPER, pad=4)


# =====================================================================
#  14. Diagnostic radar (Bagian 0 self-test)
# =====================================================================
def fig_diagnostic_radar(scores=None):
    h = 78 * mm

    def drawer(c, w, hh):
        labels = ["Deteksi", "Rumus", "Analisis", "Ide", "Keputusan", "Eksekusi", "Konsistensi"]
        n = len(labels)
        cx, cy, R = w / 2.0, hh / 2.0, 25 * mm
        for ring in (0.25, 0.5, 0.75, 1.0):
            c.setStrokeColor(GREY_LIGHT)
            c.setLineWidth(0.5)
            p = c.beginPath()
            for k in range(n):
                a = math.radians(-90 + k * 360.0 / n)
                x, y = cx + R * ring * math.cos(a), cy + R * ring * math.sin(a)
                if k == 0:
                    p.moveTo(x, y)
                else:
                    p.lineTo(x, y)
            p.close()
            c.drawPath(p, stroke=1, fill=0)
        c.setStrokeColor(GREY_LIGHT)
        for k in range(n):
            a = math.radians(-90 + k * 360.0 / n)
            c.line(cx, cy, cx + R * math.cos(a), cy + R * math.sin(a))
        for k, lab in enumerate(labels):
            a = math.radians(-90 + k * 360.0 / n)
            c.setFillColor(NAVY)
            c.setFont(FONT_SANS_B, 6.0)
            lx, ly = cx + (R + 6) * math.cos(a), cy + (R + 6) * math.sin(a)
            if abs(math.cos(a)) < 0.2:
                c.drawCentredString(lx, ly - 2, lab)
            elif math.cos(a) > 0:
                c.drawString(lx, ly - 2, lab)
            else:
                c.drawRightString(lx, ly - 2, lab)
        if scores:
            c.setStrokeColor(ACCENT)
            c.setFillColor(Color(ACCENT.red, ACCENT.green, ACCENT.blue, 0.18))
            c.setLineWidth(1.4)
            p = c.beginPath()
            for k in range(n):
                a = math.radians(-90 + k * 360.0 / n)
                r = R * (scores[k] / 5.0)
                x, y = cx + r * math.cos(a), cy + r * math.sin(a)
                if k == 0:
                    p.moveTo(x, y)
                else:
                    p.lineTo(x, y)
            p.close()
            c.drawPath(p, stroke=1, fill=1)
        else:
            c.setFillColor(GREY)
            c.setFont(FONT_SANS, 6.2)
            c.drawCentredString(cx, cy - 2, "nilai 1\u20135")
            c.setFont(FONT_SANS_B, 6.6)
            c.drawCentredString(cx, cy - 10, "tiap dimensi")
    return Figure(h, drawer, caption="Gambar. Profil Problem Solver kamu. Skor rendah di satu dimensi menunjukkan langkah 7D mana yang perlu kamu latih lebih keras.",
                  bg=PAPER, pad=4)


# =====================================================================
#  15. Workshop agenda
# =====================================================================
def fig_workshop_agenda():
    h = 76 * mm

    def drawer(c, w, hh):
        blocks = [
            ("08.30", "Pembukaan & Kontrak Belajar", "20'", NAVY),
            ("08.50", "Tes Diagnostik + Refleksi", "25'", ACCENT),
            ("09.15", "Mindset Problem Solver", "35'", ACCENT),
            ("09.50", "Klinik D1\u2013D2: Pilih & Rumuskan Masalah", "60'", TEAL),
            ("10.50", "Istirahat", "15'", GREY),
            ("11.05", "Klinik D3\u2013D4: Akar & Alternatif", "70'", TEAL),
            ("12.15", "Makan siang", "45'", GREY),
            ("13.00", "Klinik D5: Keputusan Bersama", "45'", VIOLET),
            ("13.45", "Klinik D6\u2013D7: Rencana & Penguncian", "60'", VIOLET),
            ("14.45", "Presentasi Kelompok + Umpan Balik", "45'", AMBER),
            ("15.30", "Rencana Aksi 30 Hari & Penutup", "20'", NAVY),
        ]
        n = len(blocks)
        rh = (hh - 4) / n
        for i, (t, act, dur, col) in enumerate(blocks):
            y = hh - (i + 1) * rh
            c.setFillColor(HexColor("#F6F4EF") if i % 2 == 0 else PAPER)
            c.rect(0, y + 1, w, rh - 2, stroke=0, fill=1)
            c.setFillColor(col)
            c.roundRect(2, y + 1.6, 2.6, rh - 3.2, 1, stroke=0, fill=1)
            c.setFillColor(NAVY)
            c.setFont(FONT_SANS_B, 6.6)
            c.drawString(8, y + rh - 9, t)
            _dtext(c, 34, y + rh - 9, act, FONT_SANS, 6.8, INK, w - 66)
            c.setFillColor(GREY)
            c.setFont(FONT_SANS_M, 6.2)
            c.drawRightString(w - 3, y + rh - 9, dur)
    return Figure(h, drawer, caption="Gambar. Agenda workshop satu hari penuh yang sudah teruji untuk kelompok 12\u201324 orang.",
                  bg=PAPER, pad=4)


# =====================================================================
#  16. MECE / hypothesis tree
# =====================================================================
def fig_hypothesis_tree():
    h = 72 * mm

    def drawer(c, w, hh):
        root = ("Penjualan turun 12%", w / 2.0, hh - 12)
        c.setFillColor(NAVY)
        c.roundRect(root[1] - 52, root[2] - 6, 104, 15, 3, stroke=0, fill=1)
        _ctext(c, root[1], root[2] + 3, root[0], FONT_SANS_B, 7.0, PAPER, 98)
        kids = [("Traffic turun", w * 0.18), ("Konversi turun", w * 0.5), ("Harga tidak kompetitif", w * 0.82)]
        y2 = hh * 0.42
        c.setStrokeColor(GREY)
        c.setLineWidth(0.8)
        c.line(root[1], root[2] - 6, root[1], y2 + 18)
        for t, x in kids:
            c.line(x, y2 + 18, root[1], y2 + 18)
            c.line(x, y2 + 18, x, y2 + 14)
            c.setFillColor(TEAL)
            c.roundRect(x - 40, y2 + 1, 80, 14, 2.5, stroke=0, fill=1)
            _ctext(c, x, y2 + 8, t, FONT_SANS_B, 6.4, PAPER, 76)
            subs = ["Cek data kunjungan", "Cek funnel", "Cek kompetitor"]
            k = ["Traffic turun", "Konversi turun", "Harga tidak kompetitif"].index(t)
            _dtext(c, x - 40, y2 - 8, "\u2022 " + subs[k], FONT_SANS, 5.8, INK, 82)
            _dtext(c, x - 40, y2 - 16, "\u2022 uji dengan data", FONT_SANS, 5.8, GREY, 82)
    return Figure(h, drawer, caption="Gambar. Pecah dugaan besar menjadi beberapa dugaan kecil yang bisa diuji. Setiap cabang harus saling meniadakan (MECE).",
                  bg=PAPER, pad=4)


# =====================================================================
#  17. SBI feedback
# =====================================================================
def fig_sbi():
    h = 48 * mm

    def drawer(c, w, hh):
        items = [("S", "Situation", "Kapan & di mana kejadiannya", ACCENT),
                 ("B", "Behavior", "Perilaku yang bisa diamati", TEAL),
                 ("I", "Impact", "Dampak yang kamu rasakan", VIOLET)]
        bw = (w - 12) / 3.0
        for i, (k, t, d, col) in enumerate(items):
            x = i * (bw + 6)
            c.setFillColor(col)
            c.roundRect(x, 0, bw, hh - 8, 3, stroke=0, fill=1)
            c.setFillColor(PAPER)
            c.setFont(FONT_SANS_B, 17)
            c.drawCentredString(x + bw / 2.0, hh - 24, k)
            c.setFont(FONT_SANS_B, 7.6)
            c.drawCentredString(x + bw / 2.0, hh - 35, t)
            _ctext(c, x + bw / 2.0, hh - 46, d, FONT_SANS, 6.2, PAPER, bw - 10)
            if i < 2:
                c.setFillColor(GREY)
                c.setFont(FONT_SANS_B, 9)
                c.drawCentredString(x + bw + 3, hh / 2.0 - 6, "\u203a")
    return Figure(h, drawer, caption="Gambar. Pola umpan balik SBI: hindari menilai orang, sampaikan fakta lalu dampaknya.",
                  bg=PAPER, pad=4)


# =====================================================================
#  18. Cost of poor quality / 1-10-100
# =====================================================================
def fig_1_10_100():
    h = 52 * mm

    def drawer(c, w, hh):
        bars = [("Cegah di awal", 1, GREEN), ("Perbaiki saat ketahuan", 10, AMBER),
                ("Tangani setelah pelanggan kena", 100, RED)]
        bw = (w - 20) / 3.0
        base = 12
        top = hh - 12
        for i, (t, v, col) in enumerate(bars):
            x = 10 + i * bw
            bh = (math.log10(v) / 2.0) * (top - base)
            c.setFillColor(col)
            c.roundRect(x + 6, base, bw - 16, bh, 2.5, stroke=0, fill=1)
            c.setFillColor(col)
            c.setFont(FONT_SANS_B, 11)
            c.drawCentredString(x + bw / 2.0 - 2, base + bh + 4, "%d\u00d7" % v)
            _ctext(c, x + bw / 2.0 - 2, base - 6, t, FONT_SANS_M, 6.2, INK, bw - 10)
        c.setFillColor(GREY)
        c.setFont(FONT_SANS, 6.0)
        c.drawCentredString(w / 2.0, 1, "biaya relatif memperbaiki masalah di tiap tahap")
    return Figure(h, drawer, caption="Gambar. Aturan 1\u201310\u2013100: makin lama masalah dibiarkan, makin mahal biaya memperbaikinya.",
                  bg=PAPER, pad=4)


# =====================================================================
#  19. Control chart (D7)
# =====================================================================
def fig_control_chart():
    h = 58 * mm

    def drawer(c, w, hh):
        import random
        random.seed(7)
        base = 14
        top = hh - 14
        n = 20
        cw = (w - 24) / n
        vals = [3.0, 2.6, 3.4, 2.8, 3.1, 2.5, 4.6, 4.9, 4.7, 3.0, 2.7, 2.9,
                3.2, 2.8, 5.4, 5.6, 5.2, 2.6, 2.4, 2.7]
        mx = 6.0
        c.setStrokeColor(GREY_LIGHT)
        c.setLineWidth(0.6)
        c.line(20, base, w - 4, base)
        c.line(20, top, w - 4, top)
        c.setStrokeColor(RED)
        c.setDash(2, 2)
        c.line(20, top - 2, w - 4, top - 2)
        c.setStrokeColor(NAVY)
        c.setDash(2, 2)
        c.line(20, base + 8, w - 4, base + 8)
        c.setDash()
        pts = []
        for i, v in enumerate(vals):
            x = 22 + i * cw
            y = base + (v / mx) * (top - base - 4)
            pts.append((x, y))
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.2)
        p = c.beginPath()
        p.moveTo(*pts[0])
        for q in pts[1:]:
            p.lineTo(*q)
        c.drawPath(p, stroke=1, fill=0)
        for i, q in enumerate(pts):
            c.setFillColor(RED if vals[i] > 4.3 else TEAL)
            c.circle(q[0], q[1], 1.7, stroke=0, fill=1)
        c.setFillColor(RED)
        c.setFont(FONT_SANS_B, 5.8)
        c.drawString(w - 44, top - 2, "batas atas")
        c.setFillColor(NAVY)
        c.drawString(w - 44, base + 8, "rata-rata")
        c.setFillColor(ACCENT)
        c.setFont(FONT_SANS_B, 6.4)
        c.drawString(22, top + 3, "3 lonjakan = sinyal sistem masih bocor")
    return Figure(h, drawer, caption="Gambar. Setelah perbaikan, pantau beberapa bulan. Lonjakan di luar batas berarti akar masalah belum benar-benar tertutup.",
                  bg=PAPER, pad=4)


# =====================================================================
#  20. UMKM 3x case funnel
# =====================================================================
def fig_umkm_funnel():
    h = 60 * mm

    def drawer(c, w, hh):
        stages = [("100 orang lewat", 100), ("30 masuk", 30), ("9 bertanya", 9), ("3 beli", 3)]
        bw0 = w - 40
        top = hh - 8
        for i, (t, v) in enumerate(stages):
            frac = 1 - i * 0.24
            bw = bw0 * frac
            bh = (top - 10) / 4.0 - 3
            y = top - (i + 1) * ((top - 10) / 4.0)
            x = (w - bw) / 2.0
            col = [TEAL, HexColor("#2F8F5B"), AMBER, ACCENT][i]
            c.setFillColor(col)
            c.roundRect(x, y, bw, bh, 2, stroke=0, fill=1)
            _ctext(c, w / 2.0, y + bh / 2.0 - 2, t, FONT_SANS_B, 6.8, PAPER, bw - 8)
            if i < 3:
                c.setFillColor(GREY)
                c.setFont(FONT_SANS_B, 6.4)
                nc = stages[i + 1][1]
                c.drawString(w - 36, y - 2, "\u2193 %d%%" % int(nc / float(v) * 100))
    return Figure(h, drawer, caption="Gambar. Perbaikan tidak harus menambah pengunjung. Memperbaiki satu kebocoran di tengah funnel sering memberi hasil berkali lipat.",
                  bg=PAPER, pad=4)


# =====================================================================
#  21. Burnout / energy quadrant
# =====================================================================
def fig_energy():
    h = 62 * mm

    def drawer(c, w, hh):
        quads = [("ZONA BAKAR", "Beban tinggi, dukungan rendah", RED, "#FBE7E3", "bakar"),
                 ("ZONA TUMBUH", "Beban tinggi, dukungan tinggi", GREEN, "#E4F3E9", "tumbuh"),
                 ("ZONA BOSAN", "Beban rendah, dukungan rendah", GREY, "#F2F2F2", "bosan"),
                 ("ZONA NYAMAN", "Beban rendah, dukungan tinggi", TEAL, "#E3F2EF", "nyaman")]
        cw, rh = w / 2.0, hh / 2.0
        for i, (t, d, col, bg, _) in enumerate(quads):
            r, cc = divmod(i, 2)
            x, y = cc * cw, hh - (r + 1) * rh
            c.setFillColor(HexColor(bg))
            c.rect(x, y, cw, rh, stroke=0, fill=1)
            c.setStrokeColor(PAPER)
            c.setLineWidth(1.2)
            c.rect(x, y, cw, rh, stroke=1, fill=0)
            _dtext(c, x + 7, y + rh - 14, t, FONT_SANS_B, 7.4, col, cw - 12)
            _dtext(c, x + 7, y + rh - 24, d, FONT_SANS, 6.0, INK, cw - 12)
        c.setFillColor(GREY)
        c.setFont(FONT_SANS_B, 6.0)
        c.drawCentredString(w / 2.0, 1.0, "SUMBU X: DUKUNGAN & OTONOMI \u2192 tinggi")
        c.drawCentredString(w / 2.0, hh - 7, "SUMBU Y: BEBAN \u2192 tinggi ke atas")
    return Figure(h, drawer, caption="Gambar. Burnout bukan soal malas, tapi soal rasio beban terhadap dukungan. Perbaikannya ada di sisi mana yang paling mudah digeser.",
                  bg=PAPER, pad=4)


# =====================================================================
#  22. Kids screentime family system
# =====================================================================
def fig_family_system():
    h = 66 * mm

    def drawer(c, w, hh):
        cx, cy, R = w / 2.0, hh / 2.0, 21 * mm
        nodes = [("Anak", "Cari hiburan", ACCENT),
                 ("Orang tua", "Sibuk kerja", TEAL),
                 ("Aturan", "Belum ada kesepakatan", AMBER),
                 ("Kegiatan lain", "Terbatas", VIOLET)]
        positions = [(-90, 1.0), (150, 1.0), (30, 0.62)]
        angs = [-90, 150, 30, 270]
        for i, ((t, d, col), ang) in enumerate(zip(nodes, angs)):
            a = math.radians(ang)
            x = cx + R * math.cos(a)
            y = cy + R * math.sin(a)
            c.setFillColor(col)
            c.roundRect(x - 26, y - 11, 52, 22, 3, stroke=0, fill=1)
            _ctext(c, x, y + 3, t, FONT_SANS_B, 6.8, PAPER, 48)
            _ctext(c, x, y - 4, d, FONT_SANS, 5.4, PAPER, 48)
        c.setStrokeColor(GREY_LIGHT)
        c.setLineWidth(1.0)
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                a1 = math.radians(angs[i])
                a2 = math.radians(angs[j])
                c.line(cx + R * math.cos(a1), cy + R * math.sin(a1),
                       cx + R * math.cos(a2), cy + R * math.sin(a2))
        c.setFillColor(SOFT)
        c.circle(cx, cy, 13 * mm, stroke=0, fill=1)
        _ctext(c, cx, cy + 3, "SISTEM", FONT_SANS_B, 7.0, NAVY, 24 * mm)
        _ctext(c, cx, cy - 4, "keluarga", FONT_SANS, 5.8, GREY, 24 * mm)
    return Figure(h, drawer, caption="Gambar. Perilaku anak hampir selalu bagian dari sistem keluarga. Mengubah satu simpul tanpa menyentuh simpul lain biasanya gagal.",
                  bg=PAPER, pad=4)


# =====================================================================
#  23. Funnel retail / promo
# =====================================================================
def fig_retail_funnel():
    h = 58 * mm

    def drawer(c, w, hh):
        rows = [("Kunjungan toko", "naik 20%", TEAL, 1.0),
                ("Melihat display", "turun 5%", GREY, 0.85),
                ("Mencoba / tanya", "naik 8%", TEAL, 0.7),
                ("Transaksi", "turun 12%", RED, 0.55),
                ("Pembelian ulang", "turun 18%", RED, 0.4)]
        for i, (t, v, col, frac) in enumerate(rows):
            bh = (hh - 8) / len(rows) - 2.5
            y = hh - (i + 1) * ((hh - 8) / len(rows))
            bw = (w - 60) * frac
            c.setFillColor(col)
            c.roundRect(0, y, bw, bh, 2, stroke=0, fill=1)
            _dtext(c, 5, y + bh / 2.0 - 2, t, FONT_SANS_B, 6.4, PAPER, bw - 10)
            c.setFillColor(col)
            c.setFont(FONT_SANS_SB, 6.6)
            c.drawString(bw + 5, y + bh / 2.0 - 2, v)
        c.setFillColor(GREY)
        c.setFont(FONT_SANS, 5.8)
        c.drawString(0, 1, "panah merah = tahap yang perlu diperiksa lebih dulu")
    return Figure(h, drawer, caption="Gambar. Promo yang gencar hanya menambah kunjungan. Bila transaksi turun, masalahnya biasanya di penawaran, harga, atau pelayanan.",
                  bg=PAPER, pad=4)


# =====================================================================
#  24. Karir: skill-value overlap
# =====================================================================
def fig_skill_value():
    h = 62 * mm

    def drawer(c, w, hh):
        cx, cy, R = w / 2.0, hh / 2.0, 19 * mm
        cols = [Color(ACCENT.red, ACCENT.green, ACCENT.blue, 0.20),
                Color(TEAL.red, TEAL.green, TEAL.blue, 0.20),
                Color(VIOLET.red, VIOLET.green, VIOLET.blue, 0.20)]
        pos = [(cx - R * 0.48, cy + R * 0.30), (cx + R * 0.48, cy + R * 0.30),
               (cx, cy - R * 0.46)]
        names = [("Keahlian\nteknis", ACCENT), ("Peran\nkepemimpinan", TEAL),
                 ("Dampak\nbisnis", VIOLET)]
        for (x, y), col in zip(pos, cols):
            c.setFillColor(col)
            c.circle(x, y, R * 0.70, stroke=0, fill=1)
        for (x, y), (nm, cc) in zip(pos, names):
            c.setFillColor(cc)
            c.setFont(FONT_SANS_B, 6.2)
            for k, ln in enumerate(nm.split("\n")):
                c.drawCentredString(x, y + 2 - k * 7.6, ln)
        c.setFillColor(NAVY)
        c.setFont(FONT_SANS_B, 6.6)
        c.drawCentredString(cx, cy + R * 0.30 + 2, "PROMOSI")
        c.setFillColor(GREY)
        c.setFont(FONT_SANS, 5.5)
        c.drawCentredString(cx, cy + R * 0.30 - 6, "butuh irisan")
        c.drawCentredString(cx, cy + R * 0.30 - 12, "ketiganya")
    return Figure(h, drawer, caption="Gambar. Bekerja keras saja tidak cukup. Promosi terjadi ketika keahlian, kebutuhan peran, dan dampak bisnis saling beririsan.",
                  bg=PAPER, pad=4)


# =====================================================================
#  25. 1-page A3 style template
# =====================================================================
def fig_a3_template():
    h = 76 * mm

    def drawer(c, w, hh):
        boxes = [
            (0.0, 0.58, 0.55, 0.42, "LATAR BELAKANG", "Kenapa masalah ini penting sekarang"),
            (0.56, 0.58, 0.44, 0.42, "KONDISI SAAT INI", "Data baseline + grafik"),
            (0.0, 0.30, 0.55, 0.26, "ANALISIS AKAR", "5 Whys / Pareto / fishbone"),
            (0.56, 0.30, 0.44, 0.26, "KONDISI TARGET", "Angka yang ingin dicapai"),
            (0.0, 0.0, 0.42, 0.28, "TINDAKAN", "Siapa, apa, kapan"),
            (0.43, 0.0, 0.30, 0.28, "HASIL", "Bukti perubahan"),
            (0.74, 0.0, 0.26, 0.28, "BAKU", "Standar & pemilik"),
        ]
        for x, y, bw, bh, t, d in boxes:
            X, Y = x * w, y * hh
            BW, BH = bw * w - 3, bh * hh - 3
            c.setFillColor(PAPER)
            c.setStrokeColor(NAVY)
            c.setLineWidth(0.8)
            c.rect(X, Y, BW, BH, stroke=1, fill=1)
            c.setFillColor(NAVY)
            c.setFont(FONT_SANS_B, 6.2)
            c.drawString(X + 4, Y + BH - 10, t)
            _dtext(c, X + 4, Y + BH - 19, d, FONT_SERIF_IT, 6.0, GREY, BW - 8)
        c.setFillColor(ACCENT)
        c.setFont(FONT_SANS_B, 6.8)
        c.drawString(0, 1.5, "SATU HALAMAN A3 — SEMUA CERITA, SATU LEMBAR")
    return Figure(h, drawer, caption="Gambar. Format satu halaman ala Toyota: seluruh cerita masalah dan solusinya harus muat di satu lembar.",
                  bg=PAPER, pad=4)


# =====================================================================
#  26. Habit loop / standard work
# =====================================================================
def fig_standard_work():
    h = 52 * mm

    items = [("1", "Bakukan", "dokumentasi 1 halaman", TEAL),
             ("2", "Latih", "semua pelaksana", ACCENT),
             ("3", "Pantau", "indikator mingguan", AMBER),
             ("4", "Tinjau", "setiap kuartal", VIOLET),
             ("5", "Perbaiki", "bila standar gagal", GREEN)]

    def drawer(c, w, hh):
        n = len(items)
        bw = w / n
        for i, (num, t, d, col) in enumerate(items):
            x = i * bw
            c.setFillColor(col)
            c.roundRect(x + 2, hh - 20, bw - 5, 18, 3, stroke=0, fill=1)
            c.setFillColor(PAPER)
            c.setFont(FONT_SANS_B, 10)
            c.drawCentredString(x + bw / 2.0 - 1, hh - 15, num)
            c.setFillColor(col)
            c.setFont(FONT_SANS_B, 7.2)
            c.drawCentredString(x + bw / 2.0 - 1, hh - 28, t)
            _ctext(c, x + bw / 2.0 - 1, hh - 37, d, FONT_SANS, 6.0, GREY, bw - 8)
            if i < n - 1:
                c.setFillColor(GREY_LIGHT)
                c.setFont(FONT_SANS_B, 8)
                c.drawCentredString(x + bw - 2, hh - 14, "\u203a")
        c.setFillColor(NAVY)
        c.setFont(FONT_SANS_B, 6.4)
        c.drawString(0, hh - 50, "STANDAR KERJA MEMBUAT PERBAIKAN BERTAHAN")
    return Figure(h, drawer, caption="Gambar. Perbaikan tanpa standar akan menguap dalam beberapa minggu. Lima langkah ini yang mengunci hasil.",
                  bg=PAPER, pad=4)


# =====================================================================
#  27. Fotografi kecil: faceless people / scene (simple vector scenes)
# =====================================================================
def _person(c, x, y, h=20, body=NAVY, head=None, label=None, col2=None):
    head = head or body
    c.setFillColor(head)
    c.circle(x, y + h, h * 0.22, stroke=0, fill=1)
    p = c.beginPath()
    p.moveTo(x - h * 0.30, y)
    p.lineTo(x - h * 0.22, y + h * 0.72)
    p.lineTo(x + h * 0.22, y + h * 0.72)
    p.lineTo(x + h * 0.30, y)
    p.close()
    c.setFillColor(body)
    c.drawPath(p, stroke=0, fill=1)
    if label:
        c.setFillColor(INK)
        c.setFont(FONT_SANS_M, 6.0)
        c.drawCentredString(x, y - 8, label)


def fig_meeting_scene():
    h = 46 * mm

    def drawer(c, w, hh):
        c.setFillColor(HexColor("#F6F4EF"))
        c.rect(0, 0, w, hh, stroke=0, fill=1)
        c.setStrokeColor(GREY_LIGHT)
        c.setLineWidth(0.7)
        c.line(0, 6, w, 6)
        people = [(0.18, NAVY, "Fasilitator"), (0.42, TEAL, "Tim"),
                  (0.62, ACCENT, "Pelanggan"), (0.84, VIOLET, "Pemilik proses")]
        for fx, col, lab in people:
            _person(c, w * fx, 12, h=22, body=col, label=lab)
        # whiteboard
        c.setFillColor(PAPER)
        c.setStrokeColor(GREY)
        c.rect(w * 0.30, hh - 26, w * 0.42, 20, stroke=1, fill=1)
        c.setFillColor(TEAL)
        c.setFont(FONT_SANS_B, 6.0)
        c.drawString(w * 0.30 + 4, hh - 11, "GEJALA \u2192 AKAR \u2192 UJI")
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1)
        c.line(w * 0.30 + 4, hh - 20, w * 0.30 + 46, hh - 20)
    return Figure(h, drawer, caption="Gambar. Ruang perbaikan yang baik punya satu papan bersama, satu masalah, dan satu pemilik.",
                  bg=PAPER, pad=3)


def fig_workshop_room():
    h = 52 * mm

    def drawer(c, w, hh):
        c.setFillColor(HexColor("#F2F5FA"))
        c.rect(0, 0, w, hh, stroke=0, fill=1)
        # tables
        for i, (fx, col, lab) in enumerate([(0.05, TEAL, "Kelompok 1"),
                                            (0.38, ACCENT, "Kelompok 2"),
                                            (0.71, VIOLET, "Kelompok 3")]):
            x = w * fx
            c.setFillColor(PAPER)
            c.setStrokeColor(GREY)
            c.setLineWidth(0.6)
            c.rect(x, 8, w * 0.26, 14, stroke=1, fill=1)
            c.setFillColor(col)
            c.setFont(FONT_SANS_B, 6.0)
            c.drawString(x + 4, 25, lab)
            for j in range(3):
                _person(c, x + 8 + j * 14, 23, h=13, body=col)
        c.setFillColor(NAVY)
        c.setFont(FONT_SANS_B, 6.4)
        c.drawString(4, hh - 10, "PAPAN UTAMA: satu masalah per kelompok, satu halaman A3 per kelompok")
    return Figure(h, drawer, caption="Gambar. Tiga kelompok kerja, satu template yang sama, satu jam presentasi.",
                  bg=PAPER, pad=3)


# =====================================================================
#  register figures
# =====================================================================
def register_all():
    register_figure("tuntas7d", lambda: fig_tuntas_7d())
    register_figure("tuntas7d_d1", lambda: fig_tuntas_7d("D1"))
    register_figure("tuntas7d_d2", lambda: fig_tuntas_7d("D2"))
    register_figure("tuntas7d_d3", lambda: fig_tuntas_7d("D3"))
    register_figure("tuntas7d_d4", lambda: fig_tuntas_7d("D4"))
    register_figure("tuntas7d_d5", lambda: fig_tuntas_7d("D5"))
    register_figure("tuntas7d_d6", lambda: fig_tuntas_7d("D6"))
    register_figure("tuntas7d_d7", lambda: fig_tuntas_7d("D7"))
    register_figure("iceberg", fig_iceberg)
    register_figure("bias", fig_bias_map)
    register_figure("mindset", fig_mindset)
    register_figure("ptypes", fig_problem_types)
    register_figure("whys", fig_5whys)
    register_figure("fishbone", fig_fishbone)
    register_figure("pareto", fig_pareto)
    register_figure("define", fig_define_canvas)
    register_figure("impact", fig_impact_effort)
    register_figure("decide", fig_decision_matrix)
    register_figure("pdca", fig_pdca)
    register_figure("driver", fig_driver)
    register_figure("radar", fig_diagnostic_radar)
    register_figure("agenda", fig_workshop_agenda)
    register_figure("tree", fig_hypothesis_tree)
    register_figure("sbi", fig_sbi)
    register_figure("cost", fig_1_10_100)
    register_figure("chart", fig_control_chart)
    register_figure("funnel1", fig_umkm_funnel)
    register_figure("energy", fig_energy)
    register_figure("family", fig_family_system)
    register_figure("retail", fig_retail_funnel)
    register_figure("skill", fig_skill_value)
    register_figure("a3", fig_a3_template)
    register_figure("std", fig_standard_work)
    register_figure("meeting", fig_meeting_scene)
    register_figure("room", fig_workshop_room)

