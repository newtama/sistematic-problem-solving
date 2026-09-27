"""BAGIAN 2 - Inti: TUNTAS 7D."""
from reportlab.platypus import PageBreak, NextPageTemplate

from theme import *  # noqa
from engine import styles, H, sp
from dsl import render
from components import PartDivider, keyline, tool_table, caption, callout, para

S = styles()


def build():
    st = []
    st.append(NextPageTemplate("opener"))
    st.append(PageBreak())
    st.append(PartDivider(
        "Bagian 2",
        "TUNTAS 7D",
        "Tujuh langkah yang mengubah masalah rumit menjadi solusi yang tuntas dan bertahan. Inilah jantung buku ini.",
        color=ACCENT))
    st.append(NextPageTemplate("body"))
    st.append(PageBreak())
    st.append(H("Kerangka TUNTAS 7D", S["h2"], level=2, key="peta-7d"))
    st.append(sp(2))
    st += render("""
Tujuh langkah ini bukan daftar keinginan. Ia adalah urutan yang harus dijaga. Setiap langkah mempersempit kebebasan bergerak sampai akhirnya hanya satu jalur solusi yang masuk akal, dan itulah yang dieksekusi.
""")
    st += render("!fig tuntas7d")
    st += render("""
## Tujuh langkah dan pertanyaan intinya

Setiap langkah punya satu pertanyaan inti, satu alat utama, dan satu bukti selesai. Pakai tabel ini sebagai peta cepat.
""")
    st.append(tool_table(
        ["Langkah", "Pertanyaan inti", "Alat utama", "Bukti selesai"],
        [["D1 Detect", "Sebenarnya apa yang sedang terjadi?", "Kanvas Deteksi Sinyal", "Pernyataan deteksi berangka"],
         ["D2 Define", "Bagaimana masalah ini dirumuskan dengan tajam?", "Kanvas Rumus Masalah", "Kalimat masalah satu baris"],
         ["D3 Dig", "Apa akar penyebabnya, bukan gejalanya?", "5 Whys, fishbone, Pareto", "Akar terverifikasi dengan data"],
         ["D4 Design", "Pilihan apa saja yang mungkin, bukan yang pertama?", "Radar Opsi, SCAMPER", "Tiga sampai lima opsi nyata"],
         ["D5 Decide", "Dengan kriteria apa kita memilih, dan kenapa?", "Matriks Keputusan", "Keputusan beralasan & tertulis"],
         ["D6 Do", "Bagaimana rencananya menjadi hasil nyata?", "Kanvas Eksekusi 30 Hari", "Hasil terukur pada uji kecil"],
         ["D7 Drive", "Bagaimana hasil ini tidak kembali lagi?", "Standar Kerja + Diagram Penggerak", "Standar & pemilik yang jelas"]],
        [0.16, 0.30, 0.28, 0.26]))
    st.append(keyline("Langkah yang dilewati akan menagih dirinya sendiri di langkah berikutnya."))
    st += render("""
## Cara memakai tujuh langkah ini

Kerangka ini bisa dipakai untuk masalah besar maupun kecil, tetapi dosisnya berbeda. Untuk masalah yang mengganggu harian dan sederhana, tujuh langkah bisa diselesaikan dalam satu jam di atas satu lembar kertas. Untuk masalah organisasi yang besar, setiap langkah bisa memakan beberapa hari.

Yang harus kamu jaga adalah urutannya. Melompat dari D1 ke D4 adalah kesalahan paling umum, dan itu sebabnya begitu banyak solusi terlihat hebat tetapi tidak mengubah apa pun.

Pada setiap bab langkah berikutnya, kamu akan menemukan lima bagian tetap: cerita pembuka, konsep inti dan gambar rangka, alat praktis, studi kasus nyata, lalu worksheet. Kerjakan worksheet-nya sambil membaca. Buku ini dirancang untuk dipakai, bukan hanya dibaca.
""")
    st += render("""
## Diagnostik cepat: jenis masalah menentukan pendekatan

Tidak semua masalah dilayani oleh cara yang sama. Gunakan gambar berikut untuk memutuskan seberapa berat analisis yang kamu butuhkan.
""")
    st += render("!fig ptypes")

    from content.steps import d1, d2, d3, d4, d5, d6, d7
    for mod in (d1, d2, d3, d4, d5, d6, d7):
        st += mod.build()

    from content import worked
    st += worked.build()
    return st
