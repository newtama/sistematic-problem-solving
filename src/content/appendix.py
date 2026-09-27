"""Lampiran: glosarium, kumpulan template kosong, dan indeks worksheet."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para
from dsl import render
from components import (tool_table, caption, callout, keyline, worksheet_block,
                        QRPanel, rule)

S = styles()


def build():
    st = [PageBreak()]
    st.append(H("Lampiran A: Glosarium Istilah", S["h2"], level=2,
                key="glosarium"))
    st += render("""
Istilah di kolom kiri dipakai sepanjang buku. Padanannya dalam bahasa sehari-hari ada di kolom kanan, supaya kamu bisa langsung memakainya tanpa harus mengingat istilah asingnya.
""")
    st.append(tool_table(
        ["Istilah", "Arti dalam buku ini"],
        [["Akar masalah (root cause)", "Penyebab yang bila dihilangkan membuat masalah berhenti "
          "muncul, bukan sekadar berkurang."],
         ["Gejala", "Yang terlihat pertama. Hampir selalu bukan akarnya."],
         ["Masalah", "Kesenjangan terukur antara keadaan sekarang dan keadaan yang diinginkan."],
         ["Rumusan masalah", "Satu kalimat berangka yang menyebut cakupan, ukuran, dan target."],
         ["Deteksi", "Langkah mengenali masalah dengan angka yang benar, sebelum menamainya."],
         ["Sebaran", "Bentuk penyebaran data. Rata-rata tunggal menyembunyikannya."],
         ["Pembanding", "Unit serupa yang tidak bermasalah; alat verifikasi akar paling murah."],
         ["Uji kematian", "Latihan menyebutkan penyebab gagal sebuah opsi sebelum menjalankannya."],
         ["Uji kecil", "Menjalankan perubahan pada skala minimum untuk belajar tanpa risiko besar."],
         ["Pemicu (trigger)", "Kebiasaan yang sudah ada yang ditempeli langkah baru."],
         ["Angka tunggal", "Satu ukuran utama yang dipantau harian, agar kemajuan terlihat."],
         ["Standar kerja", "Satu halaman yang menuliskan cara baru secara cukup jelas untuk "
          "dijalankan orang baru."],
         ["Pembakuan", "Menjadikan perbaikan sebagai standar resmi dengan pemilik dan ritme."],
         ["Ritme tinjauan", "Jadwal tetap memeriksa angka, penyimpangan, dan keputusan."],
         ["Siklus 30 hari", "Periode eksekusi dengan satu hasil, satu angka, satu langkah harian."],
         ["Bias kognitif", "Pola berpikir otomatis yang membuat penilaian menyimpang."],
         ["Penetapan dini", "Berhenti mencari setelah ide pertama muncul."],
         ["Kriteria", "Hal-hal yang penting bagi keputusan, ditetapkan sebelum menilai opsi."],
         ["Kartu Keputusan", "Satu lembar berisi keputusan, alasan, dan rencana cadangan."],
         ["Diagram Penggerak", "Peta penggerak yang membuat hasil bertahan."],
         ["TUNTAS 7D", "Kerangka tujuh langkah: Detect, Define, Dig, Design, Decide, Do, Drive."]],
        [0.30, 0.70]))

    st.append(PageBreak())
    st.append(H("Lampiran B: Indeks Worksheet", S["h2"], level=2, key="lampiran-b"))
    st += render("""
Semua worksheet dalam buku ini dikumpulkan di sini. Versi cetak bisa difotokopi, versi digital bisa diunduh dari toolkit.
""")
    st.append(tool_table(
        ["Kode", "Nama", "Dipakai untuk", "Langkah"],
        [["WS-0", "Tes Diagnostik Tipe Problem Solver", "Mengenali kecenderungan dirimu", "Pembuka"],
         ["WS-1A", "Peta Bias Pribadi", "Menemukan jebakan yang paling sering kamu alami", "Bab 1"],
         ["WS-1B", "Jurnal Berpikir Mingguan", "Melatih kebiasaan berpikir jernih", "Bab 1"],
         ["WS-2A", "Tiga Sikap Problem Solver", "Menilai dan merencanakan sikap", "Bab 2"],
         ["WS-2B", "Rencana Percakapan Sulit", "Menyiapkan percakapan yang dihindari", "Bab 2"],
         ["WS-D1", "Kanvas Deteksi Sinyal", "Mengenali masalah dengan benar", "D1"],
         ["WS-D2", "Kanvas Rumus Masalah", "Menajamkan kalimat masalah", "D2"],
         ["WS-D3", "Peta Akar Masalah", "Menemukan dan memverifikasi akar", "D3"],
         ["WS-D4", "Kanvas Rancangan Solusi", "Menghasilkan opsi sebelum memilih", "D4"],
         ["WS-D5", "Kartu Keputusan", "Memutuskan dengan kriteria", "D5"],
         ["WS-D6", "Kanvas Eksekusi 30 Hari", "Mengubah keputusan jadi langkah harian", "D6"],
         ["WS-D7", "Peta Pembakuan", "Mengunci hasil agar bertahan", "D7"],
         ["WS-CONTOH", "Lembar Ringkas Tujuh Langkah", "Untuk masalah kecil sehari-hari", "Contoh"],
         ["WS-FAS", "Lembar Persiapan Fasilitator", "Merencanakan workshop", "Bab 12"]],
        [0.14, 0.30, 0.42, 0.14]))

    st.append(PageBreak())
    st.append(H("Lampiran C: Enam Template Inti", S["h2"], level=2,
                key="lampiran-c"))
    st += render("""
Halaman berikut berisi enam template kosong yang paling sering dipakai. Fotokopi atau cetak halaman ini, dan kamu punya seluruh perangkat untuk memulai.
""")
    st.append(worksheet_block(
        "T1", "Kanvas Deteksi Sinyal", "Template kosong",
        [{"label": "Sinyal awal (apa yang kamu dengar/lihat)", "lines": 2},
         {"label": "Sumber sinyal", "lines": 1},
         {"label": "Ukuran sekarang", "lines": 1},
         {"label": "Ukuran tujuan", "lines": 1},
         {"label": "Sebaran (waktu / tempat / jenis)", "lines": 3},
         {"label": "Bukti yang masih hilang", "lines": 2}],
    ))
    st.append(worksheet_block(
        "T2", "Kanvas Rumus Masalah", "Template kosong",
        [{"label": "Pada (bagian persis), (ukuran) sekarang (angka), sejak (kapan)", "lines": 2},
         {"label": "Target & alasannya", "lines": 2},
         {"label": "Konsekuensi bila dibiarkan (berangka)", "lines": 1},
         {"label": "Pemilik masalah (satu nama)", "lines": 1}],
    ))
    st.append(PageBreak())
    st.append(worksheet_block(
        "T3", "Peta Akar Masalah", "Template kosong",
        [{"label": "Masalah (dari WS-D2)", "lines": 2},
         ("table", ["Dugaan", "Cara menguji", "Hasil uji"],
          [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""]],
          [0.36, 0.34, 0.30]),
         {"label": "Akar terverifikasi", "lines": 2},
         {"label": "Cara verifikasi (data / pembanding / uji matikan)", "lines": 2}],
    ))
    st.append(worksheet_block(
        "T4", "Kanvas Rancangan Solusi", "Template kosong",
        [{"label": "Akar yang harus disentuh", "lines": 1},
         ("table", ["Opsi", "Siapa", "Apa", "Sumber daya", "Dampak", "Kesulitan"],
          [["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]],
          [0.10, 0.16, 0.30, 0.19, 0.13, 0.12]),
         {"label": "Uji kematian tiap opsi", "lines": 3}],
    ))
    st.append(PageBreak())
    st.append(worksheet_block(
        "T5", "Kartu Keputusan", "Template kosong",
        [{"label": "Keputusan (satu kalimat) & pemilik", "lines": 2},
         ("table", ["Kriteria", "Bobot", "Opsi A", "Opsi B", "Opsi C"],
          [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""],
           ["Total", "100%", "", "", ""]],
          [0.40, 0.14, 0.15, 0.15, 0.16]),
         {"label": "Pilihan & alasan", "lines": 2},
         {"label": "Uji balik & rencana cadangan", "lines": 2}],
    ))
    st.append(worksheet_block(
        "T6", "Kanvas Eksekusi 30 Hari", "Template kosong",
        [{"label": "Hasil 30 hari & angka tunggal", "lines": 2},
         {"label": "Langkah kecil harian & pemicu", "lines": 2},
         {"label": "Pemilik & pengganti", "lines": 1},
         ("table", ["Minggu", "Angka", "Hambatan", "Perubahan kecil"],
          [["1", "", "", ""], ["2", "", "", ""], ["3", "", "", ""], ["4", "", "", ""]],
          [0.14, 0.20, 0.36, 0.30]),
         {"label": "Rencana pemulihan & standar (D7)", "lines": 2}],
    ))
    st.append(QRPanel("https://tuntas7d.id/toolkit/lampiran", "Toolkit Lampiran",
                      "Glosarium, semua template, dan versi cetak siap pakai",
                      "QR-LAMP"))
    return st
