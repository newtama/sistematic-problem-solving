"""D6 - Do: dari rencana di kertas jadi hasil nyata."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (h2, h3, h4, rule, caption, callout, keyline, StatRow,
                        QRPanel, tool_table, worksheet_block, case_study, WriteLines)
from stepchapter import Step, t

S = styles()

STEP = Step(
    "D6", "8", "Do",
    "Langkah 6 dari 7 \u00b7 Dari rencana di kertas jadi hasil nyata",
    "Rencana yang tidak dipecah menjadi langkah kecil akan gagal di minggu kedua.",
    ["Kenapa rencana besar gagal",
     "Kanvas Eksekusi 30 Hari",
     "Tool: uji kecil, papan progres, pemicu",
     "Studi kasus: UMKM naik omzet 3x",
     "Worksheet TUNTAS D6 + QR toolkit"],
    STEP_COLORS["D6"])


def build():
    st = []
    st += STEP.opener()
    st += t("""
## Cerita pembuka: rencana tiga puluh halaman yang mati di minggu kedua

Sebuah organisasi menyusun rencana perbaikan yang sangat rapi. Tiga puluh halaman, dengan diagram, anggaran, jadwal enam bulan, dan pembagian tugas per departemen. Semua setuju dalam rapat peluncuran. Foto bersama diambil.

Dua minggu kemudian, kemajuannya hampir nol. Bukan karena tidak ada niat, tetapi karena setiap orang menunggu hal yang berbeda. Bagian teknologi menunggu spesifikasi dari operasi. Operasi menunggu alat dari pengadaan. Pengadaan menunggu anggaran yang ternyata belum disetujui. Di tengah semua penantian itu, satu departemen ternyata tidak pernah membaca bagian tugasnya.

Bulan ketiga, semangatnya habis. Rencana tiga puluh halaman itu tidak pernah menjadi pekerjaan sehari-hari. Semua isinya benar, tetapi tidak ada satu pun langkah kecil yang bisa dimulai hari itu.

Rencana berikutnya dibuat di atas satu lembar. Ia berisi tiga hal: hasil yang jelas, satu langkah kecil untuk besok pagi, dan nama yang bertanggung jawab. Ukuran keberhasilannya satu angka. Tiga minggu kemudian, kemajuannya terlihat.
""")
    st.append(keyline("Rencana besar gagal bukan karena salah, tetapi karena tidak bisa dimulai hari ini."))
    st += t("""
## Kenapa rencana besar gagal

Ada tiga sebab yang hampir selalu muncul. Pertama, jaraknya terlalu jauh antara hari ini dan hasil akhir, sehingga tidak ada langkah yang bisa dinilai setiap hari. Kedua, hasil akhir tidak dinyatakan dalam bentuk yang bisa diamati, sehingga setiap orang punya tafsiran sendiri tentang selesai. Ketiga, tidak ada pemicu yang menjadikan pekerjaan itu rutin, sehingga ia selalu dikalahkan oleh pekerjaan yang lebih mendesak.

Tiga sebab itu punya satu penawar yang sama: perkecil jaraknya sampai bisa disentuh.
""")
    st.append(callout("research", "Mengapa langkah kecil dan pengukuran mengubah perilaku", [
        para("Penelitian tentang penetapan tujuan menunjukkan pola yang konsisten: tujuan yang "
             "spesifik dan menantang menghasilkan kinerja lebih tinggi daripada tujuan yang "
             "kabur, tetapi hanya bila disertai umpan balik kemajuan. Tanpa umpan balik, tujuan "
             "tinggi justru menurunkan usaha karena orang tidak tahu apakah mereka mendekat."),
        para("Temuan kedua berhubungan dengan kebiasaan. Menyusun niat yang mengikat pada pemicu "
             "tertentu (\"setelah X, saya akan Y\") jauh lebih berhasil daripada mengandalkan "
             "motivasi. Artinya, alat eksekusi paling kuat bukan tekad, tetapi rancangan "
             "pemicu yang jelas."),
    ]))
    st += t("!fig pdca")

    st += t("""
## Alat: Kanvas Eksekusi 30 Hari

Semua perbaikan yang serius dipecah menjadi siklus tiga puluh hari. Satu siklus punya satu hasil, satu angka, dan satu langkah kecil harian.
""")
    st.append(tool_table(
        ["Bagian", "Isi", "Contoh"],
        [["Hasil 30 hari", "Keadaan yang bisa diamati", "\"Waktu tunggu rata-rata 40 menit\""],
         ["Angka tunggal", "Ukuran yang dipantau harian", "Rata-rata menit per hari"],
         ["Langkah kecil harian", "Satu tindakan 15\u201330 menit", "Catat waktu setiap loket, 15 menit"],
         ["Pemilik", "Satu nama", "Kepala layanan"],
         ["Pemicu", "Kapan pekerjaan ini terjadi", "Setiap pagi pukul 08.00, sebelum buka"],
         ["Kendala utama", "Apa yang paling mungkin menghentikannya", "Petugas sibuk pada jam itu"],
         ["Rencana jika gagal", "Langkah pemulihan", "Alihkan pencatatan ke petugas kedua"]],
        [0.24, 0.34, 0.42]))

    st += t("""
## Uji kecil sebelum perubahan besar

Tidak semua aksi harus dilakukan sekaligus. Uji kecil memungkinkan kamu belajar tanpa mempertaruhkan seluruh sumber daya. Aturan ujinya sederhana: mulai kecil, ukur dengan jelas, perluas bila berhasil, hentikan bila gagal.

Uji kecil yang baik punya tiga ciri: bisa dimulai dalam tujuh hari, hanya menggunakan sebagian kecil sumber daya, dan menghasilkan angka yang bisa dibandingkan.
""")
    st += t("!fig energy")

    st += t("""
## Langkah demi langkah menjalankan D6

### Langkah 1: Terjemahkan keputusan menjadi hasil yang bisa diamati
"Memperbaiki layanan" tidak bisa diamati. "Waktu tunggu rata-rata 40 menit pada akhir bulan" bisa.

### Langkah 2: Pilih satu angka untuk dipantau
Satu angka, bukan lima. Angka tunggal membuat semua orang tahu apakah hari ini lebih baik dari kemarin.

### Langkah 3: Rancang langkah kecil harian
Pecah sampai ada satu tindakan yang bisa dilakukan besok pagi. Kalau belum ada, pecah lagi.

### Langkah 4: Pasang pemicu
Tempelkan langkah itu pada rutinitas yang sudah ada. Setelah apa, sebelum apa, di mana. Pemicu mengalahkan niat.

### Langkah 5: Tunjuk satu pemilik dan satu pengganti
Pemilik bukan koordinator. Pemilik adalah orang yang merasakan langsung ketika langkah itu tidak terjadi.

### Langkah 6: Buat papan progres yang terlihat
Papan sederhana dengan angka harian jauh lebih kuat daripada laporan bulanan. Kumpulkan tim di depan papan itu setiap minggu, lima belas menit.

### Langkah 7: Siapkan rencana pemulihan
Apa yang terjadi kalau dua hari berturut-turut langkahnya tidak berjalan? Tuliskan jawabannya sebelum terjadi.

### Langkah 8: Tinjau dan sesuaikan mingguan
Tinjau tiga hal: angka, hambatan, dan satu perubahan kecil untuk minggu berikutnya. Tiga puluh menit cukup.
""")
    st.append(callout("insight", "Aturan dua hari", [
        para("Jangan pernah biarkan sebuah langkah terlewat dua hari berturut-turut. Satu hari "
             "terlewat adalah kecelakaan. Dua hari terlewat adalah kebiasaan baru. Begitu hari "
             "kedua terlewat, lakukan versi paling kecil dari langkah itu, sekecil apa pun, "
             "supaya rantainya tidak putus."),
    ]))
    st.append(callout("warning", "Empat jebakan paling umum di D6", [
        para("<b>1. Terlalu banyak indikator.</b> Ketika semuanya dipantau, tidak ada yang "
             "benar-benar diperhatikan."),
        para("<b>2. Langkah terlalu besar.</b> Kalau langkah pertamamu butuh tiga hari, ia belum "
             "cukup kecil."),
        para("<b>3. Tidak ada pemicu.</b> Tanpa pemicu, langkah baru selalu kalah oleh "
             "pekerjaan yang lebih mendesak."),
        para("<b>4. Tidak ada rencana pemulihan.</b> Kegagalan kecil yang tidak direncanakan "
             "berubah menjadi penghentian total."),
    ]))

    st.append(sp(4))
    st.append(case_study(
        "7", "UMKM Kuliner", "Omzet naik tiga kali dalam setahun",
        "Pola nyata \u00b7 satu gerai \u00b7 dua belas bulan",
        [("SITUASI",
          "Sebuah usaha makanan rumahan punya pelanggan setia tetapi omzetnya mandek. "
          "Pemiliknya sudah menambah menu, menambah jam buka, dan menambah promosi. Hasilnya "
          "naik sedikit lalu kembali."),
         ("MASALAH YANG DIRUMUSKAN (D2)",
          "\"Rata-rata pembelian per pelanggan hanya 1,1 porsi, sementara biaya tetap per "
          "pengiriman membuat pengiriman satu porsi hampir tidak menghasilkan laba. Target: "
          "rata-rata 1,6 porsi per transaksi.\""),
         ("AKAR (D3)",
          "Menu disusun per porsi tunggal, dan tidak ada satu pun paket yang menggabungkan "
          "makanan utama dengan minuman atau pendamping, padahal bahan pendamping sudah tersedia "
          "dan sering terbuang."),
         ("OPSI (D4)",
          "Tiga opsi: menaikkan harga, membuat paket bundling hemat, atau menambah minimum "
          "pembelian untuk pengiriman."),
         ("KEPUTUSAN (D5)",
          "Paket bundling dipilih karena menyentuh akar, tidak menaikkan harga satuan yang bisa "
          "mengusir pelanggan, dan langsung bisa dicoba. Minimum pembelian ditunda karena "
          "berisiko mengusir pelanggan kecil."),
         ("EKSEKUSI (D6)",
          "Hasil 30 hari: rata-rata 1,4 porsi per transaksi. Angka tunggal: porsi per transaksi, "
          "dicatat setiap malam. Langkah harian: menyebutkan paket bundling ketika pelanggan "
          "memesan, satu kalimat, oleh siapa pun yang menerima pesanan. Pemicu: setelah "
          "mencatat pesanan, sebelum menutup percakapan."),
         ("TINJAUAN MINGGUAN",
          "Setiap Minggu malam, pemilik mencatat porsi per transaksi dan memilih satu perubahan "
          "kecil. Minggu ketiga, nama paket diubah karena pelanggan bingung. Minggu keenam, "
          "paket ditawarkan juga saat pengiriman."),
         ("HASIL AKHIR TAHUN",
          "Rata-rata porsi per transaksi naik dari 1,1 menjadi 1,9. Karena biaya pengiriman "
          "tetap, laba per transaksi melonjak jauh lebih tinggi. Omzet bulanan naik sekitar "
          "tiga kali dibanding awal tahun tanpa menambah jam kerja."),
         ("PELAJARAN",
          "Perbaikan terbesar datang dari langkah kecil yang dijalankan konsisten, bukan dari "
          "rencana besar yang diumumkan sekali."),
        ]))

    st += t("""
## Rangkuman bab

- Rencana besar gagal karena jaraknya terlalu jauh dari pekerjaan hari ini.
- Gunakan siklus 30 hari: satu hasil, satu angka, satu langkah kecil harian.
- Pemicu mengalahkan niat. Tempelkan langkah baru pada rutinitas yang sudah ada.
- Uji kecil sebelum perubahan besar. Perluas bila berhasil, hentikan bila gagal.
""")
    from content import extras
    st += extras.build("D6")
    from content import case2
    st += case2.build("D6")
    st.append(QRPanel("https://tuntas7d.id/toolkit/d6", "Toolkit D6: Do",
                      "Kanvas 30 hari, papan progres, lembar tinjauan mingguan",
                      "QR-D6"))
    st.append(worksheet_block(
        "WS-D6", "Kanvas Eksekusi 30 Hari", "Ubah keputusanmu menjadi langkah hari ini",
        [{"label": "Hasil dalam 30 hari (bisa diamati)", "lines": 2},
         {"label": "Angka tunggal yang dipantau harian", "lines": 1},
         {"label": "Langkah kecil harian (15\u201330 menit)", "lines": 2},
         {"label": "Pemicu: setelah apa / sebelum apa / di mana", "lines": 2},
         {"label": "Pemilik dan pengganti", "lines": 1},
         ("table", ["Minggu", "Angka", "Hambatan", "Satu perubahan kecil"],
          [["1", "", "", ""], ["2", "", "", ""], ["3", "", "", ""], ["4", "", "", ""]],
          [0.14, 0.20, 0.36, 0.30]),
         {"label": "Rencana pemulihan bila langkah terlewat dua hari", "lines": 2}],
    ))
    return st
