"""D2 - Define: jika definisi kabur, solusi pasti ngawur."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (h2, h3, h4, rule, caption, callout, keyline, StatRow,
                        QRPanel, tool_table, worksheet_block, case_study, WriteLines)
from stepchapter import Step, t

S = styles()

STEP = Step(
    "D2", "4", "Define",
    "Langkah 2 dari 7 \u00b7 Merumuskan masalah dengan tajam",
    "Jika definisi kabur, solusi pasti ngawur. Kalimat masalah yang tepat sudah setengah penyelesaian.",
    ["Kenapa masalah kabur menghasilkan solusi ngawur",
     "Anatomi kalimat masalah yang tajam",
     "Tool: Kanvas Rumus Masalah & uji SMART-Problem",
     "Studi kasus: fitur yang tidak dipakai",
     "Worksheet TUNTAS D2 + QR toolkit"],
    STEP_COLORS["D2"])


def build():
    st = []
    st += STEP.opener()
    st += t("""
## Cerita pembuka: rapat tiga jam yang berakhir tanpa keputusan

Sebuah tim produk berkumpul untuk membahas satu keluhan yang sudah lama menggantung: "aplikasi kita kurang disukai pengguna". Rapat dimulai pukul sembilan dan berakhir pukul dua belas. Dalam tiga jam itu muncul empat belas usulan: mengganti warna tombol, menambah fitur berbagi, membuat tutorial, mengubah halaman depan, menambah notifikasi.

Semua usulan terdengar masuk akal. Tidak ada yang bisa dibantah, karena tidak ada satu pun yang bisa diuji. "Kurang disukai" tidak bisa diukur, jadi setiap argumen sama kuatnya. Rapat berakhir dengan keputusan setengah hati: mengerjakan tiga dari empat belas usulan, berharap salah satunya berhasil.

Tiga bulan kemudian, tidak ada yang berubah. Angka penggunaan tetap sama.

Rapat berikutnya dibuka dengan cara berbeda. Fasilitator menulis satu baris di papan: "Pengguna baru yang menyelesaikan pendaftaran turun dari 62% menjadi 41% dalam dua bulan, khusus pada pengguna ponsel lama." Ruangan menjadi sunyi. Untuk pertama kalinya, tidak ada yang berdebat tentang apa masalahnya. Dan dalam dua puluh menit, semua sepakat bahwa yang harus diperiksa adalah halaman pendaftaran pada ponsel lama.
""")
    st.append(keyline("Masalah yang tidak bisa diukur tidak bisa diselesaikan, hanya bisa diperdebatkan."))
    st += t("""
## Kenapa definisi yang kabur begitu mahal

Definisi yang kabur terasa aman karena tidak ada yang bisa salah. Semua orang bisa setuju bahwa "kualitas perlu ditingkatkan" atau "komunikasi perlu diperbaiki". Tetapi keamanan semu itu dibayar mahal dalam tiga bentuk.

Pertama, diskusi tidak bisa selesai karena tidak ada ukuran untuk menentukan kapan selesai. Kedua, setiap orang punya tafsirannya sendiri, sehingga tim berjalan ke arah berbeda sambil merasa sudah sepakat. Ketiga, hasilnya tidak bisa dinilai, sehingga keberhasilan dan kegagalan sama-sama tidak terlihat.
""")
    st.append(callout("research", "Mengapa mendefinisikan masalah mengubah hasil", [
        para("Riset tentang pemecahan masalah kelompok menemukan pola yang konsisten: kelompok "
             "yang diminta mendefinisikan ulang dan mempertajam rumusan masalahnya menghasilkan "
             "solusi yang lebih orisinal dan lebih tepat, dibanding kelompok yang langsung "
             "membahas solusi. Proses mempertajam rumusan memaksa munculnya asumsi yang "
             "sebelumnya tersembunyi, dan asumsi yang terlihat jauh lebih mudah diperiksa."),
        para("Temuan lain yang sejalan: kualitas keputusan lebih ditentukan oleh ketepatan "
             "perumusan masalah daripada oleh kecanggihan metode analisis yang dipakai."),
    ]))
    st += t("!fig define")

    st += t("""
## Anatomi kalimat masalah yang tajam

Kalimat masalah yang baik memuat lima unsur. Hilangkan salah satunya, dan solusimu akan melenceng.
""")
    st.append(tool_table(
        ["Unsur", "Pertanyaan", "Contoh buruk", "Contoh tajam"],
        [["Objek", "Apa yang bermasalah?", "\"Aplikasi kurang disukai\"", "\"Tingkat penyelesaian pendaftaran\""],
         ["Ukuran", "Angka berapa sekarang?", "\"Sangat rendah\"", "\"41%\""],
         ["Target & pembanding", "Angka berapa yang dianggap selesai?", "\"Harus naik\"", "\"Minimal 55% (sebelumnya 62%)\""],
         ["Cakupan", "Untuk siapa, di mana, sejak kapan?", "\"Semua pengguna\"", "\"Pengguna baru di ponsel lama, dua bulan terakhir\""],
         ["Konsekuensi", "Apa dampaknya kalau dibiarkan?", "\"Pengguna kecewa\"", "\"Kehilangan 340 pengguna baru per bulan\""]],
        [0.18, 0.24, 0.26, 0.32]))

    st += t("""
## Alat: uji PROBLEM (lima pertanyaan penajam)

Setelah kamu menulis kalimat masalah, uji dengan lima pertanyaan ini. Kalau satu saja tidak bisa dijawab, kembalilah ke D1.
""")
    st.append(tool_table(
        ["Uji", "Pertanyaan", "Kalau gagal"],
        [["P \u2014 Pihak", "Siapa yang terdampak paling besar?", "Tambah cakupan orang"],
         ["R \u2014 Rentang", "Sejak kapan dan seberapa sering?", "Tambah dimensi waktu"],
         ["O \u2014 Objek", "Bagian mana persisnya yang bermasalah?", "Perjelas bagian proses"],
         ["B \u2014 Baseline", "Angka awalnya berapa, terukur?", "Cari data dasar"],
         ["L \u2014 Limit", "Kapan kita anggap selesai? Berapa targetnya?", "Tetapkan target"],
         ["E \u2014 Efek", "Apa konsekuensinya bila dibiarkan?", "Hitung dampak"],
         ["M \u2014 Mandat", "Siapa pemilik masalah ini yang berwenang?", "Tunjuk pemilik"]],
        [0.20, 0.50, 0.30]))

    st += t("""
## Langkah demi langkah menjalankan D2

### Langkah 1: Hindari kata sifat
Kata sifat adalah musuh utama kejelasan. "Lambat", "buruk", "sering", "kurang", "tidak memuaskan". Setiap kali kamu menulis kata sifat, tanyakan: kalau lambat, berapa menit? Kalau sering, berapa kali per minggu?

### Langkah 2: Tetapkan objek yang paling spesifik
Kurangi cakupan sampai kamu bisa membayangkan satu tempat, satu kelompok orang, atau satu tahap proses. Kalau semua orang adalah objeknya, tidak ada satu orang pun yang merasa bertanggung jawab.

### Langkah 3: Pasang angka baseline
Tanpa angka awal, kamu tidak akan pernah tahu apakah usahamu berhasil. Kalau tidak ada data, ukur sekarang, sekecil apa pun. Sepuluh pengamatan lebih baik daripada nol.

### Langkah 4: Tetapkan target dan batas
Target memberi arah. Batas memberi rasa selesai. Target yang baik menantang tetapi masuk akal, dan punya alasan di belakangnya.

### Langkah 5: Hitung konsekuensi
Ketika masalah diterjemahkan menjadi biaya, waktu hilang, atau pelanggan yang kabur, ia berubah dari keluhan menjadi prioritas.

### Langkah 6: Tunjuk satu pemilik
Masalah tanpa pemilik akan hilang di antara rapat. Satu nama, bukan satu departemen.

### Langkah 7: Uji dengan lima pertanyaan penajam
Jalankan uji PROBLEM. Perbaiki kalimat problem statement sampai seluruh pertanyaan bisa dijawab.

### Langkah 8: Tulis satu kalimat dan tempel
Satu kalimat. Tanpa anak kalimat yang panjang. Kalau tidak muat dalam satu baris, rumusannya belum tajam.
""")
    st.append(callout("insight", "Tiga pola kalimat masalah yang paling sering menipu", [
        para("<b>1. Menyebut solusi sebagai masalah.</b> \"Kita butuh sistem baru\" bukan masalah, "
             "itu usulan. Masalahnya adalah apa yang tidak bisa dilakukan sistem lama."),
        para("<b>2. Menyebut orang sebagai masalah.</b> \"Tim kurang disiplin\" bukan masalah, "
             "itu penilaian. Masalahnya adalah perilaku atau hasil yang bisa diukur."),
        para("<b>3. Menyebut terlalu banyak masalah sekaligus.</b> Kalau kalimatmu punya kata "
             "\"dan\" lebih dari satu, kamu sedang menyelesaikan tiga masalah dalam satu rencana. "
             "Pecah."),
    ]))

    st.append(sp(4))
    st.append(case_study(
        "3", "Tim Teknologi", "Fitur baru yang tidak dipakai",
        "Pola nyata \u00b7 aplikasi 180 ribu pengguna aktif",
        [("PERUMUSAN AWAL (KABUR)",
          "\"Pengguna kurang memanfaatkan fitur berbagi yang baru diluncurkan.\" Rapat "
          "menghasilkan usulan: kirim notifikasi, buat tutorial, ganti posisi tombol."),
         ("KENAPA MACET",
          "Tidak ada target, tidak ada baseline per segmen, tidak ada cakupan. Setiap usulan "
          "punya peluang sama untuk benar, dan tidak ada cara menilai hasilnya."),
         ("D2 \u00b7 PERUMUSAN TAJAM",
          "\"Tingkat penggunaan fitur berbagi pada pengguna baru angkatan tiga bulan terakhir "
          "hanya 4%, sementara pada pengguna lama 21%. Target minimal 12%, karena angkatan "
          "sebelumnya mencapai 18% pada periode yang sama.\""),
         ("EFEK DARI PERUMUSAN INI",
          "Pertanyaan otomatis berubah. Bukan lagi \"bagaimana membuat orang memakai fitur ini\", "
          "tetapi \"apa yang berbeda pada pengguna baru dibanding pengguna lama\"."),
         ("YANG DITEMUKAN",
          "Pengguna baru tidak pernah melihat fitur itu karena ia baru muncul setelah pengguna "
          "punya minimal sepuluh koneksi. Pengguna baru rata-rata punya tiga koneksi pada minggu "
          "pertama. Batas koneksi itu masuk akal untuk aplikasi lama, tetapi memblokir hampir "
          "semua pengguna baru."),
         ("HASIL",
          "Batas koneksi diubah untuk pengguna baru, dan fitur diperkenalkan lebih awal. "
          "Penggunaan naik dari 4% menjadi 14% dalam enam minggu tanpa satu pun notifikasi "
          "tambahan."),
         ("PELAJARAN",
          "Kalimat masalah yang tajam memuat sendiri arah pencarian solusinya. Perhatikan "
          "bagaimana kata \"pengguna baru\" langsung menyempitkan ruang pencarian."),
        ]))

    st += t("""
## Rangkuman bab

- Definisi yang kabur memastikan solusimu tidak bisa dinilai.
- Kalimat masalah yang tajam memuat objek, ukuran, target, cakupan, dan konsekuensi.
- Uji dengan lima pertanyaan penajam sebelum berpindah ke langkah berikutnya.
- Satu pemilik, satu kalimat, satu tempat menempelnya.
""")
    from content import extras
    st += extras.build("D2")
    from content import case2
    st += case2.build("D2")
    st.append(QRPanel("https://tuntas7d.id/toolkit/d2", "Toolkit D2: Define",
                      "Template kalimat masalah, uji penajam, contoh terisi",
                      "QR-D2"))
    st.append(worksheet_block(
        "WS-D2", "Kanvas Rumus Masalah", "Tajamkan kalimat masalahmu",
        [{"label": "Kalimat masalah awal (apa adanya, apa yang biasanya dikatakan orang)",
          "lines": 2},
         {"label": "Objek: bagian mana persisnya yang bermasalah?", "lines": 2},
         {"label": "Ukuran: angka hari ini (baseline)", "lines": 1},
         {"label": "Target: angka yang kamu anggap selesai", "lines": 1},
         {"label": "Cakupan: untuk siapa, di mana, sejak kapan", "lines": 2},
         {"label": "Konsekuensi: apa yang hilang kalau dibiarkan", "lines": 2},
         {"label": "Pemilik masalah (satu nama, bukan departemen)", "lines": 1},
         {"label": "KALIMAT MASALAH FINAL (satu baris)", "lines": 3,
          "hint": "Uji: apakah kalimat ini memuat angka dan cakupan? Apakah tanpa kata sifat?"}],
    ))
    return st
