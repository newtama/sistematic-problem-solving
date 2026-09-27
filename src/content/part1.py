"""BAGIAN 1 - Mindset: jebakan kognitif & tiga sikap dasar."""
from reportlab.platypus import PageBreak, NextPageTemplate

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (h2, h3, h4, rule, caption, callout, keyline, StatRow,
                        QRPanel, tool_table, worksheet_block, case_study, gap,
                        PartDivider)

S = styles()


def _t(text):
    return render(text)


def build():
    st = []
    # =================================================================
    #  PART DIVIDER
    # =================================================================
    st.append(NextPageTemplate("opener"))
    st.append(PageBreak())
    st.append(PartDivider(
        "Bagian 1",
        "Mindset Sebelum Metode",
        "Sebelum tujuh langkah, ada tiga sikap. Alat terbaik tidak berguna kalau cara berpikirnya masih penuh jebakan.",
        color=NAVY))
    st.append(NextPageTemplate("body"))

    # =================================================================
    #  BAB 1
    # =================================================================
    st.append(PageBreak())
    st.append(H("Bab 1: Otakmu Bukan Dirancang untuk Solusi", S["h2"], level=2,
                key="bab1"))
    st += _t("""
Setiap pagi, seorang manajer gudang menelusuri lorong-lorongnya dengan kekhawatiran yang sama. Barang-barang salah tempat. Stok yang seharusnya tersedia ternyata kosong. Pekerja bolak-balik mencari. Ia sudah dua kali memarahi tim. Ia sudah memasang papan pengumuman. Ia sudah menambah satu orang khusus untuk merapikan. Setiap kali, rak-rak rapi selama dua minggu, lalu kembali berantakan.

Suatu hari, seorang kolega bertanya satu hal yang tidak pernah ditanyakan siapa pun: "Barang yang jumlahnya paling sering salah, apakah jenisnya selalu sama?" Manajer itu terdiam. Ia tidak tahu. Ia baru menyadari bahwa selama dua tahun ia menyelesaikan kekacauan, bukan mencari sumbernya.

Ternyata, hampir semua masalah berasal dari satu jenis barang yang hanya memakai satu rak tetapi dipesan dalam satuan berbeda dari satuan penyimpanannya. Satu perubahan label menyelesaikan apa yang dua tahun penertiban tidak bisa. Mantan manajer itu bukan orang bodoh. Ia hanya berpikir dengan cara yang paling wajar bagi manusia: melihat yang paling terlihat, dan memperbaiki yang paling mudah disentuh.
""")
    st.append(keyline("Otak kita hebat untuk bertahan hidup, belum tentu hebat untuk mendiagnosis masalah."))
    st += _t("""
## Kenapa otak bekerja begitu

Otak manusia berkembang untuk mengambil keputusan cepat dengan informasi yang tidak lengkap. Ribuan tahun lalu, yang cepat bertindak bertahan hidup, yang lama berpikir tidak. Warisan itu masih ada: kita cenderung menutup pertanyaan lebih cepat daripada membukanya, dan memilih penjelasan yang paling mudah diingat, bukan yang paling benar.

Masalahnya, dunia modern jarang menuntut kecepatan refleks. Dunia modern menuntut ketelitian diagnosis. Dan justru di situ otak kita paling rentan.

#### Prinsip kerja otak yang perlu kamu tahu

- **Hemat energi.** Berpikir keras itu mahal. Otak memilih jalan pintas, yaitu dugaan pertama yang muncul, lalu cenderung mempertahankannya.
- **Cari pola.** Kita melihat pola bahkan ketika tidak ada pola. Dua kejadian berdekatan dianggap punya hubungan sebab-akibat.
- **Hindari disonansi.** Kita tidak nyaman ketika fakta bertentangan dengan keyakinan. Cara termudah mengurangi ketidaknyamanan adalah menolak fakta, bukan mengubah keyakinan.
- **Butuh rasa aman sosial.** Kita cenderung mengikuti suara mayoritas agar tidak dianggap berbeda, terutama di ruang rapat.
- **Ingat yang dramatis.** Kejadian yang paling berkesan terasa paling sering, meski datanya tidak mendukung.
""")
    st += _t("!fig bias")
    st += _t("""
## Enam jebakan yang paling sering menggagalkan diagnosis

### 1. Bias konfirmasi

Kamu menduga masalahnya ada di pelayanan lambat. Lalu kamu mencari data yang membenarkan dugaan itu, dan tanpa sadar melewatkan data yang membantahnya. Bias konfirmasi membuat kita menjadi pengacara bagi kesimpulan sendiri, bukan hakim yang mencari kebenaran.
""")
    st.append(callout("warning", "Tanda kamu sedang terjebak", [
        para("Kamu merasa lega ketika menemukan satu bukti yang mendukung dugaanmu. "
             "Kamu kesal ketika ada yang menyodorkan bukti sebaliknya. Kalau itu terjadi, "
             "berhentilah sejenak. Kamu sedang mengumpulkan dukungan, bukan informasi."),
    ]))
    st += _t("""
### 2. Efek jangkar

Angka pertama yang kamu dengar menjadi patokan, bahkan ketika angka itu sembarangan. Pelanggan bilang "antreannya tiga jam". Kamu mencari cara memotong tiga jam itu. Padahal data menunjukkan rata-ratanya empat puluh menit, sementara puncaknya di jam tertentu mencapai tiga jam. Kamu berjuang melawan jangkar, bukan melawan masalah.

### 3. Bias ketersediaan

Yang paling mudah diingat terasa paling penting. Karena kamu baru membaca artikel tentang otomatisasi, semua masalah terlihat butuh otomatisasi. Karena kamu baru menyelesaikan masalah stok, semua masalah terlihat seperti masalah stok. Pikiran menyukai alat yang baru saja diasah.

### 4. Kausalitas palsu

Dua hal terjadi bersamaan, kita langsung menyimpulkan yang satu menyebabkan yang lain. Promo dimulai, penjualan naik. Berarti promo berhasil? Belum tentu. Bisa jadi pada periode yang sama ada musim liburan, atau kompetitor menaikkan harga. Tanpa pembanding, kita hanya punya cerita, bukan bukti.

### 5. Bias ahli

Semakin kamu menguasai sebuah bidang, semakin besar godaan untuk menjawab dari ingatan. Dokter yang sudah menangani ribuan pasien paling rentan melewatkan gejala yang tidak biasa, justru karena ia punya banyak pola siap pakai di kepalanya. Keahlian mempercepat, tetapi juga membutakan.

### 6. Tekanan kelompok

Dalam rapat, orang cenderung tidak menyuarakan keraguan ketika atasan sudah menyampaikan pendapat. Gejala ini punya nama: kesunyian kelompok. Semua mengangguk, tidak ada yang menguji. Keputusan terlihat mufakat, padahal hanya satu suara yang benar-benar dibahas.
""")
    st.append(callout("research", "Kesunyian kelompok itu nyata dan terukur", [
        para("Percobaan klasik tentang konformitas menunjukkan bahwa ketika beberapa orang "
             "dengan sengaja memberi jawaban yang jelas salah, peserta berikutnya cenderung "
             "ikut menjawab salah demi tidak tampak menyimpang. Temuan ini menjelaskan kenapa "
             "rapat bisa menyepakati keputusan yang buruk tanpa satu pun orang benar-benar "
             "mempercayainya."),
    ]))
    st.append(callout("insight", "Bagaimana jebakan ini dijinakkan", [
        para("Kamu tidak bisa menghapus cara kerja otak. Yang bisa kamu lakukan adalah memasang "
             "rem: <b>mulai dari data</b> sebelum opini, <b>tuliskan masalahnya</b> sebelum "
             "membahas solusi, <b>minta satu orang berperan sebagai penantang</b> di setiap "
             "rapat, dan <b>tunda kesimpulan</b> sampai paling tidak tiga penjelasan diuji."),
    ]))
    st += _t("""
## Cara melatih diri keluar dari jebakan

Kamu tidak perlu menjadi bebas bias. Kamu hanya perlu lambat satu detik pada saat yang tepat.
""")
    st.append(callout("practice", "Tiga pertanyaan penawar bias", [
        para("<b>Apa yang bisa membuktikan bahwa saya salah?</b> Kalau kamu tidak bisa "
             "membayangkan bukti yang akan mengubah pikiranmu, kamu sedang memegang keyakinan, "
             "bukan kesimpulan."),
        para("<b>Siapa yang akan tidak setuju, dan apa alasannya?</b> Bayangkan satu orang "
             "spesifik yang paling mungkin menentang. Tuliskan argumen terbaiknya sebelum ia "
             "mengucapkannya."),
        para("<b>Kalau bukan sebab ini, apa sebab lain yang masuk akal?</b> Paksa dirimu "
             "menuliskan paling tidak dua penjelasan alternatif."),
    ]))
    st.append(sp(4))
    st.append(case_study(
        "1", "Ritel Minimarket", "Promo tidak menaikkan laba",
        "Pola nyata \u00b7 42 gerai \u00b7 tiga bulan",
        [("MASALAH",
          "Manajemen meluncurkan diskon besar pada kategori minuman. Penjualan kategori itu "
          "naik 22%, tetapi laba gerai turun 6%. Kesimpulan awal: promonya kurang agresif, "
          "perlu diskon lebih besar lagi."),
         ("APA YANG TERJADI PADA PEMIKIRAN",
          "Semua orang melihat satu sebab yang paling mudah: harga. Tidak ada yang memeriksa "
          "tahap berikutnya dalam rantai, yaitu apa yang dibeli pelanggan setelah masuk toko. "
          "Ini contoh klasik efek jangkar pada angka penjualan."),
         ("YANG DITEMUKAN SAAT DATA DIPERIKSA",
          "Pelanggan memang membeli lebih banyak minuman diskon, tetapi belanjaan lain "
          "menurun. Margin minuman sangat tipis, sementara margin makanan ringan dan kebutuhan "
          "harian tinggi. Promo memindahkan keranjang belanja ke barang bermargin kecil."),
         ("PELAJARAN",
          "Sebelum menambah dosis, periksa dulu apakah obatnya bekerja pada penyakit yang "
          "benar. Kenaikan penjualan bukan bukti keberhasilan kalau laba yang jadi tujuan."),
         ("HASIL SETELAH ARAH DIUBAH",
          "Promo dipindahkan ke paket bundling makanan ringan. Laba gerai naik 9% dalam dua "
          "bulan tanpa menambah anggaran diskon."),
         ("TOOLS YANG DIPAKAI",
          "Pemisahan gejala dan tujuan, uji sebab alternatif, dan pembanding sebelum-sesudah "
          "pada metrik utama, bukan metrik antara."),
        ]))
    st += _t("""
## Rangkuman bab

- Otak dirancang untuk kecepatan, bukan untuk diagnosis yang teliti.
- Enam jebakan yang paling sering: konfirmasi, jangkar, ketersediaan, kausalitas palsu, bias ahli, dan tekanan kelompok.
- Kamu tidak menghapus bias, kamu memasang rem: mulai dari data, tulis masalahnya, tunjuk penantang, tunda kesimpulan.
""")
    st.append(worksheet_block(
        "WS-1", "Audit Bias Diriku", "Periksa cara berpikirmu sendiri",
        [{"label": "Masalah yang sedang kamu tangani", "lines": 2},
         {"label": "Dugaan awalku tentang penyebabnya", "lines": 3},
         {"label": "Bukti yang akan mengubah dugaanku", "lines": 3,
          "hint": "Kalau kamu tidak menemukan bukti apa pun, dugaanku masih keyakinan."},
         ("table", ["Bias", "Contoh nyata di masalahku", "Penawarnya"],
          [["Konfirmasi", "", "Cari data yang membantah"],
           ["Jangkar", "", "Cek angka rata-rata"],
           ["Ketersediaan", "", "Uji dua alat berbeda"],
           ["Kausalitas palsu", "", "Cari pembanding"],
           ["Bias ahli", "", "Minta orang baru memeriksa"],
           ["Tekanan kelompok", "", "Tunjuk satu penantang"]],
          [0.26, 0.44, 0.30]),
         ]))

    from content import part1_extra
    st += part1_extra.bab1_extra()

    # =================================================================
    #  BAB 2
    # =================================================================
    st.append(PageBreak())
    st.append(H("Bab 2: Tiga Mindset Problem Solver Kelas Dunia", S["h2"],
                level=2, key="bab2"))
    st += _t("""
Kalau kamu memerhatikan orang-orang yang tampak selalu berhasil menuntaskan masalah, kamu akan menemukan pola yang mengejutkan. Bukan pola alat. Bukan pola kecerdasan. Pola sikap.

Ada tiga sikap yang berulang pada hampir semua problem solver yang saya temui, baik di ruang pabrik, di ruang operasi rumah sakit, maupun di ruang keluarga. Saya menyebutnya Curiosity, Clarity, dan Courage.
""")
    st += _t("!fig mindset")
    st += _t("""
## 1. Curiosity: bertanya sebelum menjawab

Curiosity bukan rasa ingin tahu yang santai. Ia adalah disiplin untuk menahan jawaban sampai pertanyaannya cukup. Problem solver pemula merasa pintar ketika punya jawaban. Problem solver kelas dunia merasa pintar ketika punya pertanyaan yang lebih tajam.

Perhatikan perbedaannya. Ketika diberi laporan "produk sering dikembalikan", orang pemula langsung bertanya "bagaimana cara mengurangi pengembalian". Orang yang terlatih bertanya lebih dulu: "dikembalikan karena apa, oleh siapa, kapan, dan sejak kapan". Pertanyaan kedua membuka seluruh peta masalah. Pertanyaan pertama menutupnya.

#### Latihan rasa ingin tahu

- Ganti satu kalimat jawabanmu setiap kali rapat dengan satu pertanyaan.
- Sebelum mengusulkan solusi, ajukan tiga pertanyaan yang jawabannya belum kamu ketahui.
- Tulis di kertas "Saya mungkin salah tentang apa?" lalu tempel di meja kerja.

## 2. Clarity: memisahkan fakta dari cerita

Otak manusia menceritakan kisah, bukan melaporkan fakta. "Tim ini malas" adalah cerita. "Tiga dari lima tugas terlambat empat hari dalam dua minggu terakhir" adalah fakta. Cerita menutup diskusi. Fakta membukanya.

Clarity berarti satu hal yang terdengar sederhana tetapi sulit: memisahkan apa yang kamu ketahui dari apa yang kamu simpulkan. Tanpa pemisahan ini, setiap analisis akan berisi asumsi yang menyamar sebagai data. Dan asumsi yang tidak diperiksa adalah cara paling umum sebuah organisasi menipu dirinya sendiri.
""")
    st.append(callout("insight", "Aturan satu kalimat", [
        para("Setiap masalah harus bisa ditulis dalam satu kalimat yang memuat <b>apa</b>, "
             "<b>siapa</b>, <b>seberapa besar</b>, dan <b>sejak kapan</b>. Kalau kamu tidak "
             "bisa, masalahnya belum kamu pahami, dan solusinya belum layak dibuat."),
    ]))
    st.append(tool_table(
        ["Fakta (terukur)", "Laporan (kata orang)", "Simpulan (cerita)"],
        [["Rata-rata waktu tunggu 47 menit", "\"Antrenya lama sekali\"", "\"Petugasnya kurang niat\""],
         ["Error bayar 1 dari 60 transaksi", "\"Sistem sering gagal\"", "\"Sistemnya jelek, ganti\""],
         ["Angkat tangan 0,4 kali per jam", "\"Anak-anak pasif\"", "\"Anak-anak malas belajar\""]],
        [0.34, 0.33, 0.33]))
    st.append(caption("Tabel. Latih memindahkan pernyataan dari kolom kanan ke kolom kiri. Hampir selalu, "
                      "fakta di kolom kiri membuka lebih banyak kemungkinan daripada cerita di kolom kanan."))
    st += _t("""
## 3. Courage: berani mengubah, bukan hanya menambal

Courage dalam problem solving bukan keberanian menghadapi bahaya. Ia adalah keberanian menghadapi tiga hal yang lebih sering menghalangi: kebenaran yang tidak nyaman, keputusan yang tidak populer, dan perubahan yang mengganggu.

Menambal gejala selalu lebih mudah daripada memperbaiki akar. Menambah satu orang di pos pelayanan lebih mudah daripada mengubah cara kerja. Memarahi tim lebih mudah daripada mengubah jadwal. Membeli perangkat baru lebih mudah daripada mengubah kebiasaan. Setiap kemudahan itu berharga: masalah akan kembali, dan kali ini lebih kuat karena sudah terbukti bisa bertahan.
""")
    st.append(PullQuote("Menambal gejala memang lebih mudah. Itulah sebabnya biayanya lebih mahal."))
    st.append(callout("practice", "Tiga pertanyaan keberanian", [
        para("<b>Kalau saya memperbaiki akarnya, siapa yang akan keberatan?</b> Semakin jelas "
             "jawabannya, semakin penting masalah itu bagi organisasi."),
        para("<b>Apa hal terburuk yang terjadi kalau saya mengubah cara kerja ini?</b> Biasanya "
             "jauh lebih kecil daripada biaya membiarkan masalah kembali."),
        para("<b>Apa yang sedang saya hindari karena tidak nyaman?</b> Jawaban atas pertanyaan "
             "ini hampir selalu merupakan akar masalah."),
    ]))
    st += _t("""
## Ketiganya bekerja bersamaan

Ketiga sikap ini bukan pilihan. Mereka bekerja sebagai satu rangkaian. Curiosity mengumpulkan bahan mentah yang jujur. Clarity mengubah bahan itu menjadi masalah yang tajam. Courage mengubah masalah tajam menjadi tindakan yang mengganggu namun perlu. Matikan satu, seluruh rangkaian melemah.
""")
    st.append(tool_table(
        ["Situasi", "Sikap yang dibutuhkan", "Kalau sikap ini hilang"],
        [["Seseorang melaporkan masalah", "Curiosity", "Kita melompat ke solusi dan salah sasaran"],
         ["Rapat mulai berputar", "Clarity", "Kita berdebat tentang cerita, bukan fakta"],
         ["Sudah jelas akarnya", "Courage", "Kita memilih tambalan yang lebih aman"]],
        [0.34, 0.30, 0.36]))
    st.append(callout("story", "Kisah: perubahan yang menunggu sepuluh tahun", [
        para("Sebuah klinik gigi punya masalah yang sudah berlangsung sepuluh tahun: banyak "
             "pasien tidak kembali untuk kontrol lanjutan. Sudah banyak upaya: pesan pengingat, "
             "diskon kontrol, kartu loyalitas. Hasilnya naik sedikit lalu turun lagi."),
        para("Seorang dokter baru bergabung dan bertanya dengan cara yang berbeda. Ia menghubungi "
             "dua puluh pasien yang tidak kembali dan bertanya satu hal: apa yang terjadi setelah "
             "perawatan pertama. Ternyata enam belas dari dua puluh mengalami sensitivitas yang "
             "tidak dijelaskan sebelumnya, dan mereka mengira itu tanda perawatannya gagal."),
        para("Akar masalahnya bukan ingatan, bukan harga, bukan loyalitas. Akarnya informasi. Satu "
             "lembar penjelasan yang dibagikan saat pasien selesai perawatan mengubah tingkat "
             "kembali dari tiga puluh persen menjadi lebih dari tujuh puluh persen dalam tiga "
             "bulan. Perbaikannya murah. Yang mahal adalah sepuluh tahun pertanyaan yang tidak "
             "pernah diajukan."),
    ]))
    st += _t("""
## Rangkuman bab

- **Curiosity** membuat kita mengumpulkan bahan yang jujur sebelum menyimpulkan.
- **Clarity** memisahkan fakta dari cerita dan merumuskan masalah dalam satu kalimat.
- **Courage** membuat kita memperbaiki akar meski lebih sulit dan tidak populer.
- Ketiganya bekerja sebagai rangkaian. Kurang satu, seluruhnya melemah.
""")
    st.append(worksheet_block(
        "WS-2", "Cek Tiga Sikap Dasar", "Nilai dirimu dengan jujur",
        [{"label": "CERITA, bukan fakta: satu pernyataan yang belum aku periksa",
          "lines": 2,
          "hint": "Contoh: \"Tim malas.\" Ubah menjadi ukuran yang bisa diperiksa."},
         {"label": "Ubah menjadi fakta yang terukur", "lines": 2},
         {"label": "Pertanyaan yang belum aku ajukan (curiosity)", "lines": 3},
         {"label": "Akar yang aku hindari karena tidak nyaman (courage)", "lines": 3},
         {"label": "Satu keputusan tidak populer yang sebenarnya perlu aku ambil", "lines": 3}],
    ))
    st += part1_extra.bab2_extra()
    return st
