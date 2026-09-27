"""D5 - Decide: seni memilih tanpa menyesal."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (h2, h3, h4, rule, caption, callout, keyline, StatRow,
                        QRPanel, tool_table, worksheet_block, case_study, WriteLines)
from stepchapter import Step, t

S = styles()

STEP = Step(
    "D5", "7", "Decide",
    "Langkah 5 dari 7 \u00b7 Seni memilih tanpa menyesal",
    "Keputusan yang baik lahir dari kriteria yang jelas, bukan dari suara yang paling keras.",
    ["Kenapa keputusan terasa berat",
     "Kriteria, bobot, dan Matriks Keputusan",
     "Tool: Kartu Keputusan & catatan alasan",
     "Studi kasus: memilih arah pemulihan layanan",
     "Worksheet TUNTAS D5 + QR toolkit"],
    STEP_COLORS["D5"])


def build():
    st = []
    st += STEP.opener()
    st += t("""
## Cerita pembuka: dua pilihan yang sama-sama benar

Seorang pemilik usaha distribusi kecil menghadapi keputusan yang membuatnya tidak bisa tidur. Perusahaannya punya dua jalan. Jalan pertama: menerima pesanan besar dari satu pembeli yang akan mengisi seluruh kapasitas selama enam bulan, dengan margin tipis dan syarat pembayaran lambat. Jalan kedua: menolak pembeli itu dan mengembangkan tiga puluh pelanggan kecil, dengan margin lebih baik tetapi bulan-bulan pertama pasti berat.

Ia sudah meminta pendapat lima orang. Dua bilang ambil pesanan besar, karena kasnya aman. Dua bilang kembangkan pelanggan kecil, karena marginnya sehat. Satu orang bilang menunggu. Setiap saran terdengar benar, dan justru itu masalahnya. Pendapat tanpa kriteria hanya menambah kebisingan, bukan menambah kejelasan.

Yang akhirnya membuat ia bisa memutuskan bukan saran baru, tetapi empat lembar kertas. Di situ ia menuliskan empat hal yang benar-benar penting baginya dalam dua tahun: kelangsungan kas, ketergantungan pada satu pembeli, kemampuan tumbuh, dan waktu bersama keluarga. Lalu ia menilai kedua jalan pada keempat hal itu. Hasilnya jelas, dan ia memutuskan dalam dua puluh menit setelah berbulan-bulan ragu.
""")
    st.append(keyline("Keputusan berat biasanya bukan tanda kurang informasi, tetapi tanda kurang kriteria."))
    st += t("""
## Kenapa keputusan terasa berat

Keputusan terasa berat karena kita mencampur tiga hal yang seharusnya dipisah: kriteria (apa yang penting), data (apa yang kita tahu), dan suara (siapa yang paling berani bicara). Ketika ketiganya dicampur, pertemuan berubah menjadi kontes keyakinan.

Cara keluar dari kebisingan itu sederhana, tetapi menuntut disiplin. Tetapkan dulu apa yang penting, baru nilai pilihanmu.
""")
    st.append(callout("research", "Mengapa menetapkan kriteria lebih dulu mengubah kualitas keputusan", [
        para("Riset tentang pengambilan keputusan menunjukkan bahwa orang lebih konsisten dan "
             "lebih puas dengan pilihannya ketika kriteria ditetapkan sebelum pilihan "
             "dievaluasi. Sebaliknya, ketika pilihan dilihat lebih dulu, penilaian cenderung "
             "disesuaikan agar pilihan favorit menang. Fenomena ini menyerupai cara kerja "
             "bias konfirmasi, tetapi berskala keputusan besar."),
        para("Temuan lain yang sering dikutip: kita menyesali keputusan yang diambil karena "
             "tekanan sesaat jauh lebih lama daripada keputusan yang diambil karena alasan yang "
             "jelas, meski hasilnya tidak selalu lebih baik. Artinya, kualitas proses "
             "memengaruhi rasa puas, bukan hanya hasilnya."),
    ]))

    st += t("""
## Empat sumber beratnya keputusan

- **Terlalu banyak pilihan.** Semakin banyak opsi, semakin lama memilih, dan semakin rendah kepuasan. Solusinya: saring dulu menjadi tiga dengan kriteria kaku.
- **Takut kehilangan.** Kita lebih takut kehilangan yang sudah ada daripada tertarik pada yang mungkin didapat. Solusinya: hitung biaya membiarkan keadaan sekarang, bukan hanya risiko perubahan.
- **Ingin kepastian.** Sebagian besar keputusan tidak bisa dibuat pasti. Yang bisa dilakukan adalah membuatnya bisa diperbaiki. Pilih jalur yang paling mudah dikoreksi.
- **Tekanan sosial.** Suara atasan, suara mayoritas, atau suara paling lantang. Solusinya: pisahkan sesi penilaian dari sesi pendapat.

## Alat: Matriks Keputusan berbobot

Cara kerjanya sederhana. Tuliskan kriteria, beri bobot sesuai kepentingannya, lalu nilailah setiap opsi. Angka akhirnya bukan kebenaran mutlak, tetapi ia memaksa alasan menjadi terbuka.
""")
    st.append(tool_table(
        ["Kriteria", "Bobot", "Opsi A", "Opsi B", "Opsi C"],
        [["Dampak pada akar masalah", "35%", "5", "4", "2"],
         ["Biaya & sumber daya", "20%", "2", "4", "5"],
         ["Kecepatan hasil", "20%", "3", "4", "5"],
         ["Risiko kegagalan", "15%", "3", "3", "2"],
         ["Kemudahan dirawat jangka panjang", "10%", "4", "4", "3"],
         ["Skor total (berbobot)", "100%", "3,65", "3,85", "3,20"]],
        [0.40, 0.14, 0.15, 0.15, 0.16]))
    st.append(caption("Tabel. Perhatikan bahwa opsi dengan dampak tertinggi tidak otomatis menang. "
                      "Bobotlah kriteria sebelum menilai, bukan sesudah."))

    st += t("""
## Alat: Kartu Keputusan (satu lembar untuk satu keputusan)

Setiap keputusan penting layak mendapat satu lembar. Kartu ini menyimpan alasan, sehingga enam bulan lagi kamu bisa menilai apakah keputusanmu bagus karena alasan yang tepat, bukan hanya karena hasilnya kebetulan baik.
""")
    st.append(tool_table(
        ["Bagian kartu", "Isi"],
        [["Keputusan", "Apa yang diputuskan, dalam satu kalimat"],
         ["Pemilik", "Siapa yang memutuskan dan siapa yang terdampak"],
         ["Kriteria & bobot", "Apa yang penting, dan seberapa penting"],
         ["Opsi yang dipertimbangkan", "Termasuk opsi yang tidak dipilih, dan alasannya"],
         ["Pilihan", "Yang dipilih dan tiga alasan teratasnya"],
         ["Uji balik", "Kapan kita akan menilai ulang, dan pakai ukuran apa"],
         ["Rencana cadangan", "Apa yang dilakukan bila hasilnya menyimpang"]],
        [0.30, 0.70]))

    st += t("""
## Langkah demi langkah menjalankan D5

### Langkah 1: Pastikan opsi sudah utuh
Jangan menilai opsi yang belum jelas bentuknya. Kalau masih berupa potongan, kembali ke D4.

### Langkah 2: Tetapkan tiga sampai lima kriteria sebelum melihat nilai
Kriteria harus sedikit, agar bisa diingat, dan harus benar-benar relevan dengan tujuan.

### Langkah 3: Beri bobot, lalu periksa kewajarannya
Jumlahkan bobot menjadi 100%. Kalau satu kriteria mengambil lebih dari separuh, tanyakan apakah kamu sedang mengukur satu hal saja.

### Langkah 4: Nilai setiap opsi satu per satu, bukan baris per baris
Menilai baris demi baris memudahkan membandingkan. Menilai opsi secara utuh mencegah pengaruh urutan.

### Langkah 5: Periksa hasil ekstrem
Kalau satu opsi menang telak, curigai bobot atau penilaianmu. Kalau dua opsi hampir sama, pilih yang paling mudah dikoreksi.

### Langkah 6: Tanyakan pertanyaan terakhir
Sebelum memutuskan, tanyakan: "Kalau pilihan ini salah, bagaimana saya akan tahu, dan seberapa cepat?" Keputusan yang tidak punya cara mendeteksi kesalahan adalah keputusan yang berbahaya.

### Langkah 7: Tuliskan di Kartu Keputusan dan umumkan
Keputusan yang tidak ditulis akan diingat berbeda oleh setiap orang. Tuliskan, lalu sampaikan kepada yang terdampak.
""")
    st.append(callout("insight", "Kapan berhenti mengumpulkan data", [
        para("Keputusan macet biasanya bukan karena kurang data, tetapi karena tidak ada batas "
             "kapan harus berhenti. Tentukan batas itu di depan: tanggal keputusan dan jumlah "
             "data minimal. Setelah keduanya tercapai, putuskan. Data tambahan jarang mengubah "
             "arah, tetapi hampir selalu menunda hasil."),
    ]))
    st.append(callout("warning", "Jebakan keputusan yang paling umum", [
        para("<b>1. Menilai sebelum menentukan kriteria.</b> Hasilnya, kriteria disesuaikan "
             "untuk membenarkan pilihan favorit."),
        para("<b>2. Menyamakan pendapat dengan data.</b> Yang paling lantang bukan yang paling "
             "benar. Catat pendapat, uji dengan data."),
        para("<b>3. Menghindari keputusan.</b> Menunda juga keputusan, dan punya biaya. "
             "Hitung biaya menunggu seperti kamu menghitung biaya bertindak."),
        para("<b>4. Tidak mencatat alasan.</b> Tanpa catatan, keputusan yang berhasil karena "
             "keberuntungan akan dianggap sebagai kebijaksanaan, dan keputusan benar yang "
             "hasilnya belum terlihat akan dibatalkan terlalu cepat."),
    ]))

    st.append(sp(4))
    st.append(case_study(
        "6", "Layanan Publik", "Memilih arah pemulihan yang tidak populer",
        "Pola nyata \u00b7 14 kantor layanan \u00b7 keputusan enam bulan",
        [("SITUASI",
          "Kepuasan layanan turun. Tiga opsi muncul: menambah petugas di semua kantor, "
          "menerapkan sistem janji temu, atau menutup sementara tiga kantor berkinerja paling "
          "rendah dan memindahkan sumber dayanya."),
         ("KENAPA SULIT",
          "Opsi ketiga paling tidak populer, karena menyentuh harga diri kantor dan kepala "
          "daerah. Namun opsi pertama dan kedua membutuhkan anggaran yang belum tentu ada."),
         ("KRITERIA YANG DISEPAKATI LEBIH DULU",
          "Empat kriteria ditetapkan sebelum menilai: dampak pada waktu tunggu (35%), "
          "ketersediaan anggaran (25%), kecepatan hasil (20%), dan risiko gangguan layanan (20%)."),
         ("HASIL PENILAIAN BERBOBOT",
          "Opsi janji temu menang pada dampak dan biaya sedang. Opsi penambahan petugas kalah "
          "karena anggarannya tidak tersedia. Opsi penutupan kantor punya dampak tinggi tetapi "
          "risiko gangguan layanan sangat besar."),
         ("YANG DIPUTUSKAN",
          "Janji temu diterapkan di tiga kantor dengan tunggu terburuk sebagai percontohan, "
          "dengan kriteria keberhasilan yang jelas dan tenggat delapan minggu sebelum diperluas."),
         ("PENGAMANAN",
          "Rencana cadangan ditulis sejak awal: bila waktu tunggu tidak turun setidaknya 30% "
          "dalam delapan minggu, percontohan dihentikan dan sumber daya dialihkan."),
         ("HASIL",
          "Dalam delapan minggu, waktu tunggu rata-rata turun 41%. Perluasan ke sebelas kantor "
          "lain dilakukan tanpa penambahan anggaran berarti."),
         ("PELAJARAN",
          "Kriteria yang ditetapkan sebelum menilai membuat keputusan berani bisa dibela dengan "
          "alasan, bukan dengan kekuasaan."),
        ]))

    st += t("""
## Rangkuman bab

- Keputusan berat biasanya masalah kriteria, bukan masalah informasi.
- Tetapkan kriteria dan bobot sebelum menilai opsi.
- Pilih jalur yang paling mudah dikoreksi ketika dua opsi hampir sama kuat.
- Catat keputusan di Kartu Keputusan, termasuk alasan dan rencana cadangan.
""")
    from content import extras
    st += extras.build("D5")
    from content import case2
    st += case2.build("D5")
    st.append(QRPanel("https://tuntas7d.id/toolkit/d5", "Toolkit D5: Decide",
                      "Matriks keputusan, Kartu Keputusan, daftar kriteria siap pakai",
                      "QR-D5"))
    st.append(worksheet_block(
        "WS-D5", "Kartu Keputusan", "Putuskan dengan kriteria, bukan suara terbanyak",
        [{"label": "Keputusan yang harus diambil (satu kalimat)", "lines": 2},
         {"label": "Pemilik keputusan & pihak terdampak", "lines": 2},
         ("table", ["Kriteria", "Bobot", "Opsi A", "Opsi B", "Opsi C"],
          [["", "", "", "", ""],
           ["", "", "", "", ""],
           ["", "", "", "", ""],
           ["", "", "", "", ""],
           ["Total", "100%", "", "", ""]],
          [0.40, 0.14, 0.15, 0.15, 0.16]),
         {"label": "Pilihan & tiga alasan teratas", "lines": 3},
         {"label": "Uji balik: kapan dinilai, dengan ukuran apa", "lines": 2},
         {"label": "Rencana cadangan bila menyimpang", "lines": 2}],
    ))
    return st
