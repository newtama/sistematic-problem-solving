"""D4 - Design: dari buntu jadi banyak jalan."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (h2, h3, h4, rule, caption, callout, keyline, StatRow,
                        QRPanel, tool_table, worksheet_block, case_study, WriteLines)
from stepchapter import Step, t

S = styles()

STEP = Step(
    "D4", "6", "Design",
    "Langkah 4 dari 7 \u00b7 Dari buntu jadi banyak jalan",
    "Solusi pertama hampir selalu solusi terburuk yang terlihat baik. Rancang beberapa jalan sebelum memilih satu.",
    ["Kenapa ide pertama menipu",
     "Radar Opsi dan SCAMPER",
     "Tool: Kanvas Rancangan Solusi",
     "Studi kasus: antrean 3 jam jadi 30 menit",
     "Worksheet TUNTAS D4 + QR toolkit"],
    STEP_COLORS["D4"])


def build():
    st = []
    st += STEP.opener()
    st += t("""
## Cerita pembuka: ide pertama yang menelan biaya besar

Sebuah jaringan restoran menghadapi masalah yang sudah dirumuskan dengan tajam: pesanan salah saji naik dari 3% menjadi 7% dalam tiga bulan. Akarnya juga sudah ditemukan: pesanan yang diterima saat jam sibuk sering salah ditulis karena pelayan mencatat sambil berjalan, lalu memasukkannya ke sistem setelah kembali ke kasir.

Ide pertama muncul hampir seketika, dan semua orang menyukainya: beli tablet untuk setiap pelayan. Investasi besar, tetapi terasa modern dan meyakinkan. Rencana pengadaan mulai disusun.

Sebelum anggaran disetujui, seorang manajer mengusulkan sesuatu yang sederhana: tunggu satu minggu, mari kita rancang beberapa pilihan dulu. Ternyata ada empat pilihan lain. Yang akhirnya dipilih bukan tablet, tetapi satu perubahan urutan kerja: pesanan dicatat di meja lalu langsung dimasukkan di terminal terdekat sebelum pelayan berjalan ke meja berikutnya. Biayanya hampir nol. Kesalahan turun dari 7% menjadi 2,1% dalam sebulan.

Tablet itu tidak salah. Ia hanya lebih mahal, lebih lama dipasang, dan tidak menyentuh akar masalah yang sesungguhnya. Ide pertama hampir selalu berupa alat, karena alat paling mudah dibayangkan. Solusi yang benar sering berupa perubahan cara kerja.
""")
    st.append(keyline("Solusi pertama biasanya alat. Solusi terbaik biasanya urutan kerja."))
    st += t("""
## Kenapa ide pertama menipu

Otak kita menghasilkan ide pertama dari bahan yang paling mudah dijangkau: pengalaman terakhir, alat yang sedang populer, atau hal yang paling sering didengar. Ide pertama terasa istimewa karena ia satu-satunya yang kita punya pada saat itu. Begitu ia muncul, otak cenderung menutup pintu dan mulai mencari pembenaran.

Ini dikenal sebagai penetapan dini. Bahayanya bukan karena ide pertama selalu buruk, tetapi karena kita berhenti mencari begitu ia muncul.
""")
    st.append(callout("research", "Mengapa menghasilkan banyak opsi meningkatkan kualitas", [
        para("Penelitian tentang berpikir kreatif menemukan pola yang konsisten: jumlah ide yang "
             "dihasilkan berkorelasi dengan kualitas ide terbaik yang muncul. Orang dan kelompok "
             "yang memisahkan tahap menghasilkan ide dari tahap menilai ide menghasilkan lebih "
             "banyak gagasan berguna dibanding mereka yang menilai sambil menghasilkan."),
        para("Temuan kedua yang penting untuk praktik: ide yang muncul di paruh kedua sesi "
             "biasanya lebih orisinal daripada ide di paruh pertama. Artinya, berhenti setelah "
             "tiga ide berarti berhenti tepat sebelum bagian yang paling berharga."),
    ]))
    st += t("!fig funnel1")

    st += t("""
## Empat rute untuk menghasilkan opsi

Ketika kamu buntu, jangan menunggu inspirasi. Gunakan salah satu dari empat rute berikut. Masing-masing membuka arah yang berbeda.
""")
    st.append(tool_table(
        ["Rute", "Pertanyaan pembuka", "Contoh hasil"],
        [["Hilangkan", "Bagian mana yang bisa dihapus tanpa kehilangan hasil?", "Menghapus satu langkah persetujuan"],
         ["Ubah urutan", "Apa yang terjadi kalau urutannya dibalik?", "Masukkan pesanan sebelum pindah meja"],
         ["Ubah pembagian", "Siapa lain yang bisa mengerjakan bagian ini?", "Pekerjaan diserahkan ke unit lain"],
         ["Ubah aturan", "Aturan mana yang dibuat untuk kondisi yang sudah berubah?", "Batas koneksi untuk pengguna baru"]],
        [0.18, 0.46, 0.36]))

    st += t("""
## Alat 1: SCAMPER untuk memaksa ide keluar

SCAMPER adalah daftar tujuh pintu. Ketuk setiap pintu, dan ide akan muncul. Jangan menilai dulu, catat semua.
""")
    st.append(tool_table(
        ["Huruf", "Arti", "Pertanyaannya"],
        [["S", "Substitute (ganti)", "Bagian mana yang bisa diganti bahan, orang, atau alatnya?"],
         ["C", "Combine (gabung)", "Dua langkah mana yang bisa digabung menjadi satu?"],
         ["A", "Adapt (adaptasi)", "Siapa yang sudah menyelesaikan masalah serupa dengan cara berbeda?"],
         ["M", "Modify (ubah)", "Bagian mana yang bisa diperbesar, diperkecil, atau dipercepat?"],
         ["P", "Put to another use (pakai lain)", "Apakah ada sumber daya menganggur yang bisa dipakai?"],
         ["E", "Eliminate (hapus)", "Langkah mana yang bisa dihilangkan sepenuhnya?"],
         ["R", "Reverse (balik)", "Apa yang terjadi kalau prosesnya dibalik?"]],
        [0.10, 0.32, 0.58]))

    st += t("""
## Alat 2: Radar Opsi

Radar Opsi memetakan pilihanmu pada dua sumbu: dampak dan tingkat kesulitan. Semakin cepat kamu melihat sebarannya, semakin mudah menghindari dua jebakan: memilih yang mudah tetapi tidak berdampak, dan memilih yang berdampak tetapi tidak mungkin dijalankan sekarang.
""")
    st += t("!fig impact")

    st += t("""
## Langkah demi langkah menjalankan D4

### Langkah 1: Tulis ulang akar masalah di atas kertas
Semua peserta perancangan harus melihat akar yang sama. Kalau tiap orang mengingat akar yang berbeda, ide yang muncul akan tersebar tanpa arah.

### Langkah 2: Tetapkan aturan berbeda pendapat
Pisahkan sesi menghasilkan dan sesi menilai. Selama menghasilkan, tidak ada yang boleh bilang "itu tidak mungkin".

### Langkah 3: Jalankan minimal dua rute
Pakai empat rute atau daftar SCAMPER. Target minimum: delapan opsi kasar. Jangan berhenti di tiga.

### Langkah 4: Periksa opsi yang menyentuh akar
Buang opsi yang hanya memindahkan gejala. Tanyakan untuk setiap opsi: apakah ini mengurangi akar yang sudah terverifikasi?

### Langkah 5: Gambarkan di Radar Opsi
Letakkan setiap opsi di peta dampak dan kesulitan. Ini akan memperlihatkan kombinasi mana yang paling menjanjikan.

### Langkah 6: Susun menjadi tiga sampai lima opsi nyata
Gabungkan ide-ide kecil menjadi opsi yang bisa dibandingkan. Setiap opsi sebaiknya berupa rancangan utuh, bukan potongan.

### Langkah 7: Uji dulu di atas kertas
Sebelum memilih, jalankan "uji kematian": apa yang paling mungkin menggagalkan opsi ini? Kalau kamu bisa menyebutkan penyebabnya di depan, kamu sudah siap memilih di D5.
""")
    st.append(callout("insight", "Aturan tiga opsi minimum", [
        para("Selalu rancang paling tidak tiga opsi yang benar-benar berbeda, bukan tiga variasi "
             "dari satu ide. Perbedaannya harus terasa pada cara kerja, bukan pada merek atau "
             "harga. Kalau tiga opsimu bisa dijalankan bersamaan tanpa konflik, sebenarnya kamu "
             "hanya punya satu opsi."),
    ]))
    st.append(callout("warning", "Tiga jebakan paling umum di D4", [
        para("<b>1. Menilai terlalu dini.</b> Begitu satu orang bilang \"terlalu mahal\", aliran "
             "ide berhenti. Pisahkan tahapnya."),
        para("<b>2. Tersihir oleh teknologi.</b> Alat baru terasa paling meyakinkan, padahal "
             "sering paling mahal dan paling lama dipasang. Tanyakan: bisakah akar ini "
             "disentuh dengan perubahan cara kerja?"),
        para("<b>3. Opsi yang belum utuh.</b> Sepotong ide sulit dibandingkan. Rancang sampai "
             "bentuknya jelas: siapa mengerjakan apa, kapan, dengan sumber daya apa."),
    ]))

    st.append(sp(4))
    st.append(case_study(
        "5", "Rumah Sakit Umum", "Antrean 3 jam menjadi 30 menit",
        "Pola nyata \u00b7 poliklinik rawat jalan \u00b7 900 pasien per hari",
        [("MASALAH",
          "Waktu tunggu pasien rawat jalan sangat tidak nyaman, dengan keluhan puncak mencapai "
          "tiga jam pada pagi hari. Survei kepuasan turun ke titik terendah dalam lima tahun."),
         ("AKAR (D3)",
          "Dua akar terverifikasi: pendaftaran dan penjadwalan tidak tersinkron dengan jam "
          "praktik dokter, sehingga pasien menumpuk di awal; dan sebagian besar pasien datang "
          "tanpa memastikan berkas asuransi lengkap, sehingga terjadi pengulangan administrasi."),
         ("OPSI YANG DIRANCANG (D4)",
          "Opsi A: bangun gedung tunggu baru. Opsi B: buat pendaftaran daring dengan slot waktu. "
          "Opsi C: pisahkan jalur pasien berkas lengkap dan belum lengkap. Opsi D: ubah jam "
          "kedatangan dokter agar lebih tersebar. Opsi E: gabungkan B, C, dan satu perubahan "
          "alur berkas."),
         ("HASIL PETA RADAR",
          "Opsi A punya dampak tinggi tetapi kesulitan ekstrem dan waktu paling lama. Opsi B "
          "berdampak tinggi dengan kesulitan sedang. Opsi C berdampak sedang tetapi sangat "
          "mudah dan cepat. Opsi D berdampak sedang, kesulitan sedang."),
         ("YANG DIPILIH",
          "Opsi E sebagai arah jangka menengah, dengan Opsi C dijalankan lebih dulu sebagai "
          "langkah cepat dua minggu."),
         ("HASIL",
          "Dalam enam minggu, waktu tunggu rata-rata turun dari sekitar 100 menit menjadi 30 "
          "menit, dan puncaknya tidak lagi melewati satu jam. Kepuasan pasien kembali ke "
          "tingkat tertinggi dan melewatinya."),
         ("PELAJARAN",
          "Opsi yang menang bukan yang paling megah, tetapi yang menyentuh kedua akar sekaligus "
          "dan bisa dimulai minggu depan. Membangun gedung baru akan menghabiskan dua tahun dan "
          "tidak menyentuh akar administrasi sama sekali."),
        ]))

    st += t("""
## Rangkuman bab

- Ide pertama hampir selalu alat, dan hampir selalu lebih mahal daripada yang diperlukan.
- Hasilkan banyak opsi sebelum menilai. Gunakan SCAMPER atau empat rute.
- Petakan opsi dengan Radar Opsi: dampak melakukan, kesulitan menyamping.
- Rancang minimal tiga opsi utuh yang benar-benar berbeda.
""")
    from content import extras
    st += extras.build("D4")
    from content import case2
    st += case2.build("D4")
    st.append(QRPanel("https://tuntas7d.id/toolkit/d4", "Toolkit D4: Design",
                      "Kartu SCAMPER, Radar Opsi, daftar 100 pertanyaan perancangan",
                      "QR-D4"))
    st.append(worksheet_block(
        "WS-D4", "Kanvas Rancangan Solusi", "Hasilkan opsi sebelum memilih",
        [{"label": "Akar masalah yang harus disentuh (dari D3)", "lines": 2},
         ("table", ["SCAMPER", "Ide yang muncul"],
          [["S \u2014 ganti", ""],
           ["C \u2014 gabung", ""],
           ["A \u2014 adaptasi", ""],
           ["M \u2014 ubah ukuran/kecepatan", ""],
           ["P \u2014 pakai lain", ""],
           ["E \u2014 hapus", ""],
           ["R \u2014 balik urutan", ""]],
          [0.32, 0.68]),
         {"label": "Opsi 1 (utuh: siapa, apa, kapan, sumber daya)", "lines": 3},
         {"label": "Opsi 2", "lines": 3},
         {"label": "Opsi 3", "lines": 3},
         {"label": "Uji kematian: apa yang bisa menggagalkan setiap opsi?", "lines": 3}],
    ))
    return st
