import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reportlab.platypus import PageBreak, NextPageTemplate
from engine import BookDocTemplate, register_fonts, styles, para, bullets, sp
from theme import *
from components import (ChapterOpener, PartDivider, callout, keyline, StatRow,
                        tool_table, worksheet_block, case_study, arrow_chain,
                        QRPanel, PullQuote, caption, h2, h3, h4, rule, WriteLines)

register_fonts()
S = styles()

doc = BookDocTemplate("/workspace/project/output/smoke.pdf", title="SMOKE")

story = []
story.append(NextPageTemplate("cover"))
story.append(PartDivider("BAGIAN 2", "Inti: TUNTAS 7D", "Tujuh langkah yang mengubah masalah rumit menjadi solusi yang tuntas.", ACCENT))
story.append(NextPageTemplate("body"))
story.append(PageBreak())
story.append(ChapterOpener("D1", "3", "Detect: Salah Diagnosis, Salah Obat",
                           "Langkah 1 dari 7", "Setiap solusi yang gagal dimulai dari masalah yang tidak pernah benar-benar dikenali.",
                           ["Kenapa kita sering salah membaca masalah",
                            "Tiga lapis gejala, masalah, dan akar",
                            "Tool: Gejala vs Masalah Matrix",
                            "Studi kasus: Gojek",
                            "Worksheet TUNTAS D1"], ACCENT))
story.append(PageBreak())
story.append(h2("Konsep Inti", key="smoke1"))
story.append(para("Ini adalah paragraf uji dengan <b>huruf tebal</b>, <i>miring</i>, dan teks normal untuk memastikan font Lora ter-render dengan benar pada ukuran B5. " * 4))
story.append(keyline("Masalah yang salah dirumuskan tidak akan pernah selesai."))
story.append(callout("insight", "Bias Konfirmasi",
                     [para("Kita mencari bukti yang mendukung dugaan awal, bukan yang membantahnya.")]))
story.append(StatRow([("3\u00d7", "Kenaikan omzet"), ("60%", "Cacat turun"), ("30 mnt", "Antrian turun")]))
story.append(tool_table(["Tool", "Kapan dipakai", "Output"],
                        [["5 Whys", "Gejala dangkal", "Akar kausal"],
                         ["Fishbone", "Banyak kemungkinan", "Peta sebab"]], [0.3, 0.4, 0.3]))
story.append(arrow_chain([("D1", "Detect"), ("D2", "Define"), ("D3", "Dig"), ("D4", "Design")]))
story.append(h3("Sub-bab Uji"))
story.append(PullQuote("Buku ini bukan tentang berpikir lebih keras, tapi tentang berpikir lebih jernih."))
story.append(worksheet_block("WS-D1", "Peta Masalah", "Worksheet Latihan",
                             [{"label": "Gejala yang kamu lihat", "lines": 3},
                              ("grid", 4, 2),
                              {"label": "Dugaan akar", "lines": 2}]))
story.append(case_study("1", "Gojek", "Komplain driver terlambat",
                        "2024 \u00b7 Operations \u00b7 Jakarta",
                        [("MASALAH", "Waktu tunggu meningkat."),
                         ("PROSES 7D", bullets(["D1: Data tunggu", "D3: Analisis rute"]))]))
story.append(QRPanel("https://example.com/toolkit/d1", "Toolkit D1", "QR Download", "QR-D1"))
story.append(PageBreak())
story.append(h2("Halaman Kedua", key="smoke2"))
for i in range(40):
    story.append(para("Paragraf %d. Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " % i * 2))

doc.multiBuild(story)
print("built smoke.pdf")
