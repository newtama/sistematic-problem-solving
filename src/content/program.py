"""Program 30 hari dan panduan kelompok belajar."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para
from dsl import render
from components import (tool_table, caption, callout, keyline, worksheet_block,
                        QRPanel, rule)

S = styles()


def build():
    st = [PageBreak()]
    st.append(H("Program 30 Hari Menggunakan Buku Ini", S["h2"], level=2,
                key="program30"))
    st += render("""
Buku ini bisa dibaca dalam dua hari, tetapi ia dirancang untuk dikerjakan dalam tiga puluh hari. Alasannya sederhana: satu masalah nyata lebih berharga daripada seratus halaman yang dibaca cepat.

Ada dua cara memakai program ini. Cara pertama, satu orang mengerjakan masalahnya sendiri. Cara kedua, satu kelompok kecil mengerjakan masalah bersama. Keduanya mengikuti jadwal yang sama.
""")
    st.append(tool_table(
        ["Hari", "Fokus", "Bacaan", "Kerjakan"],
        [["1\u20133", "Mindset", "Bab 1\u20132", "WS-1A, WS-2A"],
         ["4\u20136", "D1 Detect", "Bab 3", "WS-D1"],
         ["7\u20139", "D2 Define", "Bab 4", "WS-D2"],
         ["10\u201313", "D3 Dig", "Bab 5", "WS-D3"],
         ["14\u201317", "D4 Design", "Bab 6", "WS-D4"],
         ["18\u201320", "D5 Decide", "Bab 7", "WS-D5"],
         ["21\u201326", "D6 Do", "Bab 8", "WS-D6 (jalankan uji kecil)"],
         ["27\u201330", "D7 Drive", "Bab 9", "WS-D7"]],
        [0.14, 0.22, 0.20, 0.44]))
    st.append(callout("insight", "Aturan satu masalah", [
        para("Selama tiga puluh hari, kerjakan satu masalah saja. Kalau muncul masalah lain "
             "yang terasa lebih mendesak, catat di daftar tunggu dan lanjutkan. Melompat "
             "antarmasalah adalah cara paling cepat membuat seluruh program ini berantakan."),
    ]))

    st.append(PageBreak())
    st.append(H("Panduan Kelompok Belajar", S["h3"], level=3, register=False))
    st += render("""
Program ini bekerja jauh lebih baik bila dijalankan bersama tiga sampai enam orang. Satu kelompok, satu masalah bersama, satu pertemuan seminggu selama lima minggu.
""")
    st.append(tool_table(
        ["Pertemuan", "Durasi", "Agenda", "Keluaran"],
        [["1", "90 menit", "Bab 1\u20132, sepakati satu masalah bersama, isi WS-D1",
          "Masalah & deteksi"],
         ["2", "90 menit", "WS-D2 & WS-D3, cari akar bersama dengan data",
          "Rumusan & akar"],
         ["3", "120 menit", "WS-D4 & WS-D5, sesi perancangan dan keputusan",
          "Opsi & keputusan"],
         ["4", "90 menit", "WS-D6, rancang uji kecil dan papan progres",
          "Rencana 30 hari"],
         ["5", "90 menit", "WS-D7, tinjau hasil uji, tetapkan standar",
          "Pembakuan"]],
        [0.14, 0.14, 0.46, 0.26]))
    st.append(keyline("Satu kelompok, satu masalah, satu pertemuan seminggu. Itu seluruh resepnya."))

    st.append(PageBreak())
    st.append(H("Sepuluh pertanyaan yang paling sering diajukan", S["h2"],
                level=2, key="faq"))
    st += render("""
Berikut pertanyaan yang paling sering muncul ketika pembaca mulai memakai tujuh langkah ini.
""")
    st.append(tool_table(
        ["Pertanyaan", "Jawaban"],
        [["Apakah tujuh langkah ini harus berurutan?",
          "Ya. Melompat dari keluhan langsung ke solusi adalah sumber kegagalan paling umum. "
          "Kalau waktumu terbatas, jalankan langkahnya cepat, tetapi jangan melompatinya."],
         ["Bagaimana kalau data tidak tersedia?",
          "Mulai dengan perkiraan kasar dan satu sumber. Data yang paling sering dibutuhkan "
          "sebenarnya sudah ada, hanya belum dirapikan."],
         ["Berapa lama satu siklus?",
          "Untuk masalah pribadi dan operasional kecil, 30 hari cukup. Untuk masalah besar, "
          "jalankan 30 hari pertama sebagai uji kecil sebelum melangkah lebih jauh."],
         ["Bagaimana kalau tidak ada yang mau mengakui masalahnya?",
          "Ubah dari tuduhan menjadi pertanyaan tentang proses. Akar masalah yang disajikan "
          "sebagai masalah sistem jauh lebih mudah diterima daripada sebagai kesalahan orang."],
         ["Apakah harus selalu diverifikasi dengan uji matikan?",
          "Tidak selalu. Uji matikan adalah cara terkuat, tetapi pembanding sering sudah cukup "
          "dan jauh lebih murah."],
         ["Bagaimana kalau dua akar sama kuatnya?",
          "Jalankan perbaikan yang menyentuh keduanya bila memungkinkan. Kalau tidak, mulai dari "
          "yang biayanya paling rendah dan hasilnya paling cepat terlihat."],
         ["Apakah 7D sama dengan kerangka yang dipakai konsultan?",
          "Semangatnya sama: rangkaian diagnostik sebelum keputusan. Buku ini menyajikannya "
          "dalam bentuk paling sederhana yang masih bisa dipertanggungjawabkan."],
         ["Bagaimana kalau perbaikan mengganggu pekerjaan sehari-hari?",
          "Perbesar langkahnya. Kalau langkah harian butuh lebih dari tiga puluh menit, ia "
          "terlalu besar untuk dijalankan bersamaan dengan pekerjaan tetap."],
         ["Apakah buku ini bisa dipakai untuk masalah pribadi?",
          "Ya, dan justru di sana ia paling berguna, karena masalah pribadi jarang dianalisis "
          "dengan jujur. Lihat Bab 11."],
         ["Kapan saya tahu sudah selesai?",
          "Ketika angka target tercapai, hasilnya bertahan tanpa kamu mengawasi setiap hari, "
          "dan orang baru bisa menjalankannya hanya dengan membaca standar."]],
        [0.36, 0.64]))

    st.append(PageBreak())
    st.append(H("Cara membaca buku ini dalam tiga kecepatan", S["h3"],
                level=3, register=False))
    st.append(tool_table(
        ["Kalau kamu\u2026", "Baca ini", "Perkiraan waktu"],
        [["Punya satu masalah mendesak", "Bab 3\u20139, langsung kerjakan worksheetnya",
          "3\u20134 jam"],
         ["Ingin memahami kerangkanya", "Bagian 0\u20131, lalu Bagian 2",
          "1 hari"],
         ["Akan memimpin perbaikan untuk tim", "Seluruh buku, khususnya Bab 10 & 12",
          "2\u20133 hari"],
         ["Ingin menjadikannya kebiasaan", "Bab 1\u20132, lalu ikuti Program 30 Hari",
          "30 hari"],
         ["Hanya ingin ringkasan alat", "Indeks Alat dan Lampiran C",
          "30 menit"]],
        [0.30, 0.48, 0.22]))
    return st
