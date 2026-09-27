"""D7 - Drive: agar masalah yang sama tak terulang."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (h2, h3, h4, rule, caption, callout, keyline, StatRow,
                        QRPanel, tool_table, worksheet_block, case_study, WriteLines)
from stepchapter import Step, t

S = styles()

STEP = Step(
    "D7", "9", "Drive",
    "Langkah 7 dari 7 \u00b7 Agar masalah yang sama tak terulang",
    "Perbaikan yang tidak dijadikan standar hanya menunggu waktu untuk kembali.",
    ["Kenapa masalah kembali",
     "Standar kerja, pemilik, dan tinjauan",
     "Tool: Diagram Penggerak & Standar Kerja",
     "Studi kasus: pembakuan hasil di banyak cabang",
     "Worksheet TUNTAS D7 + QR toolkit"],
    STEP_COLORS["D7"])


def build():
    st = []
    st += STEP.opener()
    st += t("""
## Cerita pembuka: masalah yang kembali dalam enam bulan

Sebuah jaringan layanan berhasil menyelesaikan masalah pengembalian barang. Caranya elegan: satu perubahan pada cara pengecekan sebelum barang dikemas. Tingkat pengembalian turun dari 8% menjadi 2% di kantor pusat, tempat perubahan itu dirancang dan diuji.

Enam bulan kemudian, tingkat pengembalian naik lagi menjadi 6%. Tidak ada yang berubah pada prosedurnya. Yang berubah adalah orangnya. Tiga orang dari tim asal dipindahkan, tiga orang baru masuk, dan tidak satu pun dari mereka tahu kenapa pengecekan itu dilakukan dengan urutan tertentu. Mereka menjalankan prosedur lama karena itu yang tertulis di berkas pelatihan.

Perbaikan itu berhasil, tetapi tidak pernah dijadikan standar. Ia bergantung pada ingatan beberapa orang. Ketika orangnya berpindah, perbaikannya ikut pergi.
""")
    st.append(keyline("Perbaikan yang hanya ada di kepala beberapa orang bukan perbaikan, tapi keberuntungan."))
    st += t("""
## Kenapa masalah kembali

Masalah kembali karena empat hal, dan keempatnya bisa dicegah.

Pertama, tidak ada standar tertulis. Cara baru tidak pernah menggantikan cara lama dalam dokumen kerja. Kedua, tidak ada pemilik. Tidak ada nama yang merasa bertanggung jawab bila cara itu tidak dijalankan. Ketiga, tidak ada pengukuran lanjutan. Setelah proyek selesai, angkanya berhenti dipantau. Keempat, tidak ada tinjauan berkala, sehingga penyimpangan kecil tidak terlihat sampai menjadi besar.

Menutup keempat celah itu adalah pekerjaan langkah D7.
""")
    st.append(callout("research", "Mengapa pembakuan menentukan keberhasilan jangka panjang", [
        para("Salah satu temuan inti dari sistem perbaikan berkelanjutan adalah bahwa tanpa "
             "pembakuan, hasil perbaikan akan terkikis. Perbaikan tanpa standar baru dianggap "
             "sebagai penyimpangan sementara, dan seiring waktu orang kembali ke cara lama. "
             "Prinsipnya sering dirumuskan sebagai: tanpa standar, tidak ada dasar untuk "
             "memperbaiki."),
        para("Dari sisi perilaku, penelitian tentang kebiasaan organisasi menunjukkan bahwa "
             "praktik yang tidak didukung oleh prosedur, pelatihan, dan pengukuran cenderung "
             "hilang dalam beberapa bulan, bahkan ketika semua orang setuju bahwa praktik itu "
             "lebih baik."),
    ]))
    st += t("!fig std")

    st += t("""
## Empat pilar yang menahan hasil

### 1. Standar kerja
Dokumen singkat, satu halaman, yang menuliskan cara baru dengan jelas: apa yang dilakukan, dalam urutan apa, oleh siapa, dan apa yang menjadi penanda bahwa pekerjaan itu benar. Bukan dokumen tebal. Satu halaman yang benar-benar dipakai jauh lebih berguna daripada tiga puluh halaman yang tidak dibaca.

### 2. Pemilik yang jelas
Setiap standar punya satu nama. Pemilik bertugas memastikan standar itu hidup, bukan hanya ada. Ia juga yang berhak mengubah standar ketika keadaan berubah.

### 3. Pengukuran lanjutan
Angka yang dipakai di D6 tidak boleh berhenti dipantau. Turunkan frekuensinya, tetapi jangan hentikan. Pengukuran lanjutan adalah alarm yang memberi tahu lebih awal bila hasil mulai terkikis.

### 4. Tinjauan berkala
Satu pertemuan singkat setiap bulan untuk memeriksa angka dan memutuskan apakah standar perlu diperbarui. Tinjauan ini bukan rapat evaluasi orang, tetapi rapat pemeriksaan sistem.
""")

    st += t("""
## Alat: Diagram Penggerak

Hasil jarang bertahan karena satu sebab tunggal. Ia bertahan karena beberapa penggerak bekerja bersamaan. Diagram Penggerak membantu memastikan tidak ada penggerak yang tertinggal.
""")
    st += t("!fig driver")
    st.append(tool_table(
        ["Penggerak", "Pertanyaan", "Kalau tidak ada"],
        [["Standar", "Apakah cara baru sudah tertulis dan mudah diakses?", "Orang kembali ke cara lama"],
         ["Pelatihan", "Apakah orang baru diajari cara baru sejak hari pertama?", "Pengetahuan hilang saat orang pindah"],
         ["Pemilik", "Apakah ada satu nama yang menjaga?", "Tidak ada yang sadar ketika menyimpang"],
         ["Pengukuran", "Apakah angkanya masih dipantau?", "Penyimpangan baru terlihat setelah merugikan"],
         ["Tinjauan", "Apakah ada jadwal memeriksa dan memperbarui?", "Standar menua dan ditinggalkan"],
         ["Apresiasi", "Apakah orang yang menjaga standar dihargai?", "Menjalankan standar terasa tidak dihargai"]],
        [0.16, 0.50, 0.34]))

    st += t("""
## Langkah demi langkah menjalankan D7

### Langkah 1: Tuliskan standar kerja satu halaman
Gunakan bahasa kerja, bukan bahasa laporan. Sertakan penanda bahwa pekerjaan itu benar.

### Langkah 2: Perbarui semua dokumen lama
Cara lama harus diganti, bukan ditambahkan. Jika tidak, akan ada dua cara yang beredar dan orang akan memilih yang paling mudah.

### Langkah 3: Masukkan ke pelatihan orang baru
Pastikan orang yang bergabung setelah perbaikan mendapat cara baru sebagai kebiasaan sejak hari pertama.

### Langkah 4: Tunjuk pemilik standar
Satu nama. Tuliskan juga apa yang dilakukan pemilik ketika standar dilanggar, dan apa yang dilakukan bila standar justru salah.

### Langkah 5: Tetapkan ritme pengukuran
Angka utama tetap dipantau, frekuensinya boleh lebih jarang. Tentukan juga batas yang memicu tindakan.

### Langkah 6: Jadwalkan tinjauan bulanan
Agenda tetap: angka terbaru, satu penyimpangan yang ditemukan, satu keputusan perbaikan.

### Langkah 7: Rayakan dan sebarkan
Perbaikan yang berhasil layak diketahui organisasi. Bagikan sebagai kisah, bukan sebagai laporan. Lalu tanyakan: di mana lagi cara ini bisa dipakai?
""")
    st.append(callout("insight", "Uji dua puluh tahun", [
        para("Sebelum menutup sebuah perbaikan, ajukan satu pertanyaan: kalau seluruh tim yang "
             "ada sekarang berganti dalam dua puluh tahun, apakah perbaikan ini tetap berjalan? "
             "Kalau jawabannya tidak, perbaikan itu belum menjadi standar. Ia masih bergantung "
             "pada orang."),
    ]))
    st.append(callout("warning", "Empat jebakan paling umum di D7", [
        para("<b>1. Standar yang terlalu tebal.</b> Kalau standarnya tidak bisa dibaca dalam "
             "lima menit, ia tidak akan dipakai."),
        para("<b>2. Standar tanpa pemilik.</b> Dokumen tanpa nama akan ditafsirkan sebagai "
             "tidak penting."),
        para("<b>3. Berhenti mengukur.</b> Perayaan selesainya proyek sering menjadi awal "
             "terkikisnya hasil."),
        para("<b>4. Tidak memperbarui standar.</b> Standar yang tidak pernah berubah akan "
             "tertinggal oleh keadaan dan akhirnya dilanggar tanpa rasa bersalah."),
    ]))

    st.append(sp(4))
    st.append(case_study(
        "8", "Jaringan Layanan", "Hasil yang bertahan di 60 cabang",
        "Pola nyata \u00b7 60 cabang \u00b7 dua tahun",
        [("SITUASI AWAL",
          "Perbaikan waktu layanan berhasil di lima cabang percontohan, tetapi gagal menyebar. "
          "Cabang lain kembali ke cara lama dalam hitungan bulan."),
         ("KENAPA GAGAL MENYEBAR (D7)",
          "Perbaikan hanya hidup dalam bentuk pelatihan lisan dan ingatan kepala cabang "
          "percontohan. Tidak ada standar tertulis, tidak ada pemilik di tingkat jaringan, dan "
          "tidak ada pengukuran lanjutan."),
         ("STANDAR KERJA YANG DIBUAT",
          "Satu halaman: urutan lima langkah pelayanan, penanda bahwa langkah sudah benar, dan "
          "tiga situasi pengecualian beserta cara menanganinya."),
         ("PEMILIK & RITME",
          "Setiap cabang punya pemilik standar. Tingkat jaringan punya pengelola standar yang "
          "memeriksa satu cabang setiap minggu dan mengumpulkan angka setiap bulan."),
         ("PENGUKURAN LANJUTAN",
          "Satu angka utama dipantau bulanan di semua cabang, dengan batas peringatan yang "
          "jelas. Bila angka melewati batas, pemilik standar turun tangan dalam tujuh hari."),
         ("TINJAUAN",
          "Rapat bulanan tiga puluh menit: angka terbaru, satu penyimpangan, satu keputusan "
          "perbaikan. Standar diperbarui setiap kuartal berdasarkan temuan."),
         ("HASIL DUA TAHUN",
          "Perbaikan awal bertahan di seluruh 60 cabang, dan beberapa cabang justru "
          "menghasilkan perbaikan lanjutan sendiri. Perbaikan kedua dan ketiga lebih mudah, "
          "karena standar dan ritme sudah ada."),
         ("PELAJARAN",
          "Kecepatan menyebar bukan ditentukan oleh besarnya perubahan, tetapi oleh kuatnya "
          "standar, pemilik, dan ritme."),
        ]))

    st += t("""
## Rangkuman bab

- Perbaikan yang tidak dijadikan standar akan terkikis oleh waktu dan pergantian orang.
- Empat pilar: standar kerja, pemilik, pengukuran lanjutan, dan tinjauan berkala.
- Gunakan Diagram Penggerak untuk memastikan tidak ada pilar yang tertinggal.
- Uji dua puluh tahun: kalau perbaikannya hilang saat orang berganti, itu belum standar.

## Penutup bagian inti

Kamu sudah melewati tujuh langkah. Kalau kamu mengerjakan worksheet-nya sambil membaca, kamu sekarang punya satu masalah nyata yang sudah dikenali, dirumuskan, dianalisis, dirancang, diputuskan, dieksekusi, dan dibakukan.

Perhatikan bahwa tidak satu pun langkah itu membutuhkan kecerdasan luar biasa. Yang dibutuhkan adalah urutan, kejujuran pada data, dan kemauan untuk tidak berhenti di lapis pertama.
""")
    from content import extras
    st += extras.build("D7")
    from content import case2
    st += case2.build("D7")
    st.append(QRPanel("https://tuntas7d.id/toolkit/d7", "Toolkit D7: Drive",
                      "Template standar kerja, Diagram Penggerak, agenda tinjauan",
                      "QR-D7"))
    st.append(worksheet_block(
        "WS-D7", "Peta Pembakuan", "Pastikan hasilmu bertahan",
        [{"label": "Perbaikan yang perlu dibakukan", "lines": 2},
         {"label": "Standar kerja: langkah-langkahnya (ringkas, satu halaman)", "lines": 4},
         {"label": "Penanda bahwa pekerjaan sudah benar", "lines": 2},
         {"label": "Pemilik standar (satu nama)", "lines": 1},
         {"label": "Angka utama & ritme pemantauan", "lines": 2},
         {"label": "Jadwal tinjauan bulanan & agenda tetapnya", "lines": 2},
         ("table", ["Penggerak", "Sudah ada?", "Apa yang perlu dilengkapi"],
          [["Standar", "", ""], ["Pelatihan", "", ""], ["Pemilik", "", ""],
           ["Pengukuran", "", ""], ["Tinjauan", "", ""], ["Apresiasi", "", ""]],
          [0.22, 0.20, 0.58]),
         {"label": "Uji dua puluh tahun: apa yang akan hilang bila orang berganti?", "lines": 3}],
    ))
    return st
