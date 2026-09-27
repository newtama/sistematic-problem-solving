"""BAGIAN 0 - Pembuka: kata pengantar, cara membaca, prolog, tes diagnostik."""
from reportlab.platypus import PageBreak, NextPageTemplate, Spacer, KeepTogether

from theme import *  # noqa
from engine import styles, H, sp, para, Boxed, PullQuote, Figure
from dsl import render
from components import (h2, h3, h4, rule, caption, callout, keyline, StatRow,
                        QRPanel, tool_table, worksheet_block, case_study, WriteLines)
from frontmatter import StatementPage, TitlePage
from figures import fig_diagnostic_radar, fig_tuntas_7d, fig_iceberg, fig_bias_map

S = styles()


def _bodyflow(text):
    return render(text)


def build():
    st = []
    # =================================================================
    #  KATA PENGANTAR
    # =================================================================
    st.append(NextPageTemplate("plain"))
    st.append(PageBreak())
    st.append(H("Kata Pengantar", S["h2"], level=2, key="kata-pengantar"))
    st.append(sp(2))
    st += _bodyflow("""
Setiap orang menyelesaikan masalah. Yang membedakan bukan apakah kita punya masalah, tetapi bagaimana kita menghadapinya. Ada orang yang menghabiskan energi bertahun-tahun untuk masalah yang sama. Ada juga orang yang menyelesaikan masalah serupa dalam hitungan hari, lalu memastikan masalah itu tidak kembali.

Perbedaannya jarang soal kecerdasan. Perbedaannya ada pada urutan langkah, kejujuran dalam membaca fakta, dan keberanian mengambil keputusan yang tidak populer.

Buku ini lahir dari satu pengamatan sederhana: sebagian besar kegagalan bukan karena kurang ide, tetapi karena salah memahami masalah. Seorang manajer menambah promo ketika masalahnya ada di pelayanan. Sebuah tim menambah fitur ketika masalahnya ada di kemudahan pemakaian. Sebuah keluarga membeli perangkat baru ketika masalahnya ada di kebiasaan bersama. Semua energi itu terbuang bukan karena orangnya malas, tetapi karena arahnya keliru sejak awal.

Buku ini menawarkan satu kerangka kerja yang saya sebut TUNTAS 7D. Tujuh langkah yang menyusun cara berpikir sekaligus cara bekerja: Detect, Define, Dig, Design, Decide, Do, Drive. Setiap langkah punya alat yang jelas, pertanyaan pemandu, dan ukuran keberhasilan. Kerangka ini bukan temuan baru yang aneh. Ia adalah kumpulan cara terbaik yang sudah terbukti di ruang perbaikan pabrik, di ruang rapat direksi, di klinik rumah sakit, di kelas sekolah, dan di ruang keluarga.
""")
    st.append(PullQuote("Kecerdasan membuatmu cepat menebak. Kerangka kerja membuatmu benar."))
    st += _bodyflow("""
#### Untuk siapa buku ini ditulis

Buku ini ditulis untuk siapa saja yang lelah menambal gejala. Untuk pemilik usaha kecil yang ingin tahu kenapa stok selalu tekor. Untuk manajer yang ingin timnya berhenti berputar-putar di rapat. Untuk guru yang ingin kelasnya hidup. Untuk orang tua yang ingin anaknya kembali hadir di meja makan. Untuk siapa pun yang kariernya terasa jalan di tempat meski sudah bekerja keras.

Buku ini juga dirancang agar bisa dipakai sebagai bahan workshop. Setiap bab langkah memiliki worksheet yang bisa langsung diisi, dan Bab 12 menyediakan agenda lengkap untuk satu hari pelatihan.

#### Cara saya menyusun buku ini

Ada tiga fondasi. Pertama, tradisi perbaikan berkelanjutan yang lahir dari praktik manufaktur: siklus perbaikan, analisis akar masalah, dan standar kerja. Kedua, riset pengambilan keputusan dan psikologi kognitif: kenapa otak kita mudah terjebak, dan bagaimana menyusun keputusan supaya tidak menyesal. Ketiga, praktik konsultan dan fasilitator: bagaimana membuat kelompok bisa berpikir bersama tanpa saling menyela.

Semua itu saya rangkum menjadi tujuh langkah yang bisa diingat dan diulang. Kalau kamu hanya mengingat satu hal dari buku ini, ingat ini: masalah yang benar-benar dipahami sudah setengah terselesaikan.

Selamat bekerja. Semoga masalahmu selesai, dan semoga selesainya bertahan.
""")
    st.append(sp(6))
    st.append(rule())
    st.append(para("<i>Selamat menyelesaikan masalah dengan tuntas.</i>", "caption"))

    # =================================================================
    #  CARA MEMBACA BUKU INI
    # =================================================================
    st.append(PageBreak())
    st.append(H("Cara Membaca Buku Ini", S["h2"], level=2, key="cara-membaca"))
    st.append(sp(2))
    st += _bodyflow("""
Buku ini bisa dibaca dari depan ke belakang, tetapi ia dirancang lebih sebagai buku kerja daripada novel. Kamu akan mendapat hasil paling besar kalau memegang pensil, memilih satu masalah nyata, dan mengerjakan worksheet sambil membaca.
""")
    st.append(keyline("Baca satu langkah, kerjakan satu worksheet, terapkan pada satu masalah nyata."))
    st += _bodyflow("""
#### Peta lima bagian

- **Bagian 0 (Pembuka).** Kamu sedang di sini. Berisi peta buku, janji yang saya buat, dan tes diagnostik singkat untuk mengetahui kecenderungan cara berpikirmu.
- **Bagian 1 (Mindset).** Dua bab tentang cara kerja otak dan tiga sikap dasar yang membedakan problem solver kelas dunia.
- **Bagian 2 (TUNTAS 7D).** Jantung buku ini. Tujuh bab, satu bab untuk setiap langkah. Inilah bagian yang paling padat dan paling banyak latihannya.
- **Bagian 3 (Scale-Up dan Workshop).** Menerapkan kerangka ini pada tim dan bisnis, pada hidup sehari-hari, lalu panduan lengkap memfasilitasi workshop satu hari.
- **Penutup.** Daftar pustaka ilmiah, indeks semua alat, dan akses toolkit digital.

#### Cara membaca setiap bab 7D

Setiap bab langkah memakai urutan yang sama supaya kamu mudah menavigasi:

1. **Cerita pembuka.** Satu kisah singkat yang membuat masalah terasa nyata.
2. **Konsep inti dan gambar rangka.** Ide besar di balik langkah ini, plus alasan ilmiahnya.
3. **Alat praktis langkah demi langkah.** Cara mengerjakannya, dengan contoh pengisian.
4. **Studi kasus nyata.** Pola masalah, proses 7D, dan hasilnya.
5. **Worksheet latihan.** Ruang untuk mengerjakan masalahmu sendiri.

#### Simbol yang akan kamu temui

- **IDE KUNCI.** Kalimat inti yang layak kamu tandai.
- **TOOLS.** Alat praktis, biasanya disertai contoh.
- **JEBAKAN.** Kesalahan umum yang perlu dihindari.
- **PRAKTIK.** Langkah latihan yang bisa langsung dikerjakan.
- **BUKTI RISET.** Temuan ilmiah yang menopang cara kerja ini.
""")
    st.append(sp(2))
    st.append(QRPanel("https://tuntas7d.id/toolkit", "Toolkit TUNTAS 7D",
                      "Kode QR: worksheet, template, dan kartu langkah",
                      "QR-TOOLKIT"))
    st += _bodyflow("""
#### Kalau kamu punya waktu terbatas

Kalau hanya ada satu jam, bacalah Bagian 0 sampai selesai, lalu Bab 3, Bab 5, dan Bab 9. Tiga bab itu memberi lompatan hasil terbesar: memahami masalah dengan benar, menemukan akar, dan mengunci hasil agar tidak kembali.

Kalau kamu memimpin tim, mulailah dari Bab 10 dan Bab 12. Kerangka ini bekerja paling kuat ketika seluruh tim memakai bahasa yang sama.
""")

    # =================================================================
    #  PROLOG
    # =================================================================
    st.append(PageBreak())
    st.append(H("Prolog: Kenapa Orang Pintar Sering Gagal Menyelesaikan Masalah",
                S["h2"], level=2, key="prolog"))
    st.append(sp(2))
    st += _bodyflow("""
Ada sebuah kejadian yang membuat saya berpikir ulang tentang arti kata "menyelesaikan masalah". Saat itu saya mendampingi sebuah perusahaan percetakan yang sedang panik. Laporan keuangan menunjukkan penurunan laba tiga kuartal berturut-turut. Direktur mengumpulkan kepala bagian. Dalam dua jam, lahir rencana: memotong anggaran pemasaran, menunda pembelian mesin, dan menaikkan target penjualan lima belas persen.

Semua keputusan itu diambil oleh orang-orang pintar. Mereka sarjana dari kampus ternama, berpengalaman lebih dari lima belas tahun, dan punya data di depan mata.

Enam bulan kemudian, laba turun lebih dalam. Yang paling menarik bukan kegagalannya, tetapi alasan kegagalannya. Ternyata masalah sebenarnya bukan di pemasaran. Masalahnya ada di satu hal yang tidak seorang pun sebut dalam rapat itu: tingkat kesalahan cetak yang membuat pelanggan besar berpindah diam-diam. Biaya bahan yang terbuang naik hampir dua kali. Tidak ada yang menyadarinya karena angka itu tersembunyi di dalam satu baris laporan yang tidak pernah dibahas.

Rapat itu selesai tanpa masalah. Yang dibahas adalah gejalanya.
""")
    st.append(PullQuote("Rapat itu selesai tanpa masalah. Yang dibahas adalah gejalanya."))
    st += _bodyflow("""
#### Kenapa ini terjadi pada orang pintar

Orang pintar punya satu kelemahan khusus: mereka cepat menemukan jawaban. Kecepatan itu menjadi berkah ketika masalahnya sederhana, tetapi menjadi jebakan ketika masalahnya rumit. Otak yang terlatih cepat sering melompat dari gejala langsung ke solusi, melewati satu pertanyaan yang paling menentukan: sebenarnya apa yang sedang terjadi?

Ada tiga sebab yang paling sering.

Pertama, kita melihat apa yang mudah diukur. Angka penjualan mudah dilihat, angka kesalahan cetak tersembunyi. Otak cenderung memilih yang terlihat.

Kedua, kita nyaman dengan solusi yang kita kuasai. Orang pemasaran akan melihat masalah dari sudut pemasaran. Orang keuangan akan melihat dari sudut biaya. Orang teknologi akan mengusulkan sistem baru. Semua benar sebagian, tetapi semuanya berangkat dari kenyamanan, bukan dari masalah.

Ketiga, kita ditekan untuk segera bergerak. Diam dianggap lambat. Bertanya dianggap ragu. Padahal bertanya dengan tepat adalah bentuk gerak yang paling menghemat waktu.
""")
    st.append(callout("research", "Bukti bahwa diagnosis yang buruk itu mahal", [
        para("Riset tentang pengambilan keputusan berulang kali menemukan bahwa kelompok cenderung "
             "membahas solusi lebih cepat daripada mendiagnosis masalah. Ketika sebuah kelompok "
             "diberi kesempatan mendefinisikan ulang masalahnya, kualitas solusinya naik secara "
             "konsisten. Sebaliknya, semakin cepat kelompok melompat ke usulan, semakin besar "
             "kemungkinan mengerjakan hal yang salah dengan sangat rapi."),
        para("Ada juga temuan klasik dalam manajemen kualitas: biaya memperbaiki kesalahan melonjak "
             "berkali-kali lipat tergantung pada tahap kesalahan itu ketahuan. Kesalahan yang dicegah "
             "di awal jauh lebih murah daripada kesalahan yang baru ketahuan setelah pelanggan "
             "merasakannya. Prinsip ini dikenal sebagai aturan 1-10-100."),
    ]))
    st += _bodyflow("!fig cost")
    st += _bodyflow("""
#### Yang membedakan problem solver kelas dunia

Mereka bukan orang yang paling cepat menjawab. Mereka orang yang paling berhati-hati dalam memahami, lalu paling tegas dalam bertindak. Mereka punya kebiasaan yang terlihat sederhana tetapi jarang dipraktikkan:

- Mereka menuliskan masalah sebelum membahas solusi.
- Mereka memisahkan fakta dari dugaan, dan berani mengatakan "saya belum tahu".
- Mereka mengejar akar sampai tiga sampai lima lapis, bukan berhenti di sebab pertama.
- Mereka menghasilkan beberapa pilihan sebelum memilih satu.
- Mereka mengukur hasil, bukan mengukur usaha.
- Mereka membuat aturan baru supaya masalah yang sama tidak kembali.

Buku ini adalah cara untuk melatih keenam kebiasaan itu dalam bentuk yang paling praktis: tujuh langkah yang berurutan, dengan alat di setiap langkah.
""")
    st.append(keyline("Tujuannya bukan berpikir lebih keras, tapi berpikir lebih jernih."))
    st += _bodyflow("""
#### Janji buku ini

Saya tidak akan menjanjikan bahwa setelah membaca buku ini semua masalahmu hilang. Hidup tidak bekerja begitu. Yang saya janjikan lebih sederhana tetapi lebih berguna: kamu akan berhenti membuang energi pada masalah yang salah, dan mulai menyelesaikan masalah yang benar dengan cara yang bisa kamu ulangi.

Prolog ini ditutup dengan satu ajakan. Ambil satu masalah nyata yang sedang kamu hadapi sekarang, yang sudah mengganggu lebih dari sebulan. Simpan masalah itu. Kamu akan mengerjakannya sepanjang buku ini, langkah demi langkah, sampai ia selesai.
""")
    st.append(sp(4))
    st.append(callout("practice", "Latihan pembuka: pilih masalahmu", [
        para("Tulis satu masalah nyata yang akan kamu kerjakan sepanjang buku ini. "
             "Jangan pilih yang paling besar. Pilih yang paling mengganggu dan paling sering muncul."),
        WriteLines(4),
    ]))

    # =================================================================
    #  TES DIAGNOSTIK
    # =================================================================
    st.append(PageBreak())
    st.append(H("Tes Diagnostik: Tipe Problem Solver Kamu Apa?",
                S["h2"], level=2, key="tes-diagnostik"))
    st.append(sp(2))
    st += _bodyflow("""
Sebelum belajar langkah-langkahnya, ada gunanya mengetahui titik lemahmu. Tes ini memetakan tujuh kemampuan yang sejajar dengan tujuh langkah TUNTAS 7D. Jawab dengan jujur, bukan dengan jawaban yang terdengar bagus.
""")
    st.append(callout("tool", "Cara mengerjakan", [
        para("Untuk setiap pernyataan, beri nilai 1 sampai 5. Nilai 1 berarti "
             "\"hampir tidak pernah\", nilai 5 berarti \"hampir selalu\"."),
        para("<b>D1 Deteksi.</b> Saya mencatat data sebelum menyimpulkan apa masalahnya."),
        para("<b>D2 Rumus.</b> Saya bisa menuliskan masalah dalam satu kalimat yang jelas dan spesifik."),
        para("<b>D3 Analisis.</b> Saya mencari akar masalah, bukan berhenti di gejala pertama."),
        para("<b>D4 Ide.</b> Saya menghasilkan beberapa pilihan solusi sebelum memilih satu."),
        para("<b>D5 Keputusan.</b> Saya memakai kriteria yang jelas dan berani menutup opsi."),
        para("<b>D6 Eksekusi.</b> Saya memecah rencana menjadi langkah kecil dan mengukur hasilnya."),
        para("<b>D7 Konsistensi.</b> Saya membuat aturan baru agar masalah yang sama tidak terulang."),
    ]))
    st += _bodyflow("!fig radar")
    st += _bodyflow("""
#### Tujuh kecenderungan yang paling sering muncul

Bacalah deskripsi berikut dan tandai yang paling mirip denganmu. Kamu boleh punya lebih dari satu, tetapi biasanya ada satu yang paling dominan.

- **Sang Pelompat.** Cepat punya jawaban, tetapi sering salah sasaran. Kekuatannya kecepatan, kelemahannya diagnosis. Perlu berlatih D1 dan D2.
- **Sang Analis.** Suka mengumpulkan data, tetapi lama berpindah ke tindakan. Kekuatannya ketelitian, kelemahannya eksekusi. Perlu berlatih D5 dan D6.
- **Sang Penambal.** Rajin menanggulangi gejala, tetapi masalah kembali. Kekuatannya ketahanan, kelemahannya akar masalah. Perlu berlatih D3 dan D7.
- **Sang Peragu.** Melihat banyak pilihan, tetapi sulit memutuskan. Kekuatannya pertimbangan, kelemahannya penetapan. Perlu berlatih D5.
- **Sang Penggerak.** Cepat bergerak, tetapi kurang mengukur. Kekuatannya energi, kelemahannya bukti. Perlu berlatih D1 dan D6.
- **Sang Pemimpi.** Punya banyak gagasan besar, tetapi jarang selesai. Kekuatannya visi, kelemahannya disiplin. Perlu berlatih D6 dan D7.
- **Sang Pemikir.** Menyelesaikan masalah di kepala sendiri, tetapi jarang mengajak orang lain. Kekuatannya kedalaman, kelemahannya kolaborasi. Perlu berlatih bagian tim di Bab 10.

#### Cara memakai hasil tes ini

Skor rendah di satu dimensi bukan vonis. Itu hanya peta. Kekuatan buku ini justru ada di langkah-langkah yang terasa paling tidak nyaman bagimu, karena di situlah ruang perbaikan yang paling besar.
""")
    st.append(callout("insight", "Pola yang hampir selalu muncul", [
        para("Setelah ribuan peserta workshop mengisi tes ini, ada dua temuan yang "
             "hampir selalu berulang. Pertama, hampir semua orang memberi skor tinggi "
             "pada D6 dan D7 karena dua hal itu paling terasa seperti \"kerja keras\". "
             "Kedua, skor paling rendah hampir selalu jatuh pada D2, merumuskan masalah. "
             "Artinya, kelemahan terbesar kita justru ada di langkah yang paling jarang "
             "kita anggap sebagai pekerjaan."),
    ]))
    st.append(keyline("Kelemahan terbesar bukan pada kerja keras, tapi pada kejelasan."))
    st.append(sp(5))
    st.append(worksheet_block(
        "WS-0", "Profil Problem Solver", "Peta titik lemahmu",
        [{"label": "Skor tujuh dimensi (D1 sampai D7)", "lines": 2,
          "hint": "Tulis angkanya, lalu gambar garis dari tiap titik untuk membentuk radar."},
         {"label": "Tiga dimensi dengan skor terendah", "lines": 1},
         {"label": "Satu masalah nyata yang akan kamu kerjakan sepanjang buku ini",
          "lines": 4,
          "hint": "Pilih yang paling mengganggu. Sebutkan angkanya kalau ada."},
         {"label": "Kenapa masalah ini penting diselesaikan sekarang", "lines": 3},
         ("note", "Simpan halaman ini. Kamu akan kembali ke sini di akhir setiap bagian "
                  "untuk melacak kemajuan caramu menyelesaikan masalah.")],
    ))

    st.append(PageBreak())
    st.append(H("Peta lengkap buku ini", S["h2"], level=2, key="peta-buku"))
    st += render("""
Sebelum masuk lebih jauh, mari kita lihat bentuk buku ini secara keseluruhan. Memahami peta membuat setiap bagian lebih mudah diingat, karena kamu tahu di mana kamu berada dan ke mana arahnya.
""")
    st.append(tool_table(
        ["Bagian", "Isi", "Yang kamu bawa keluar"],
        [["Pembuka", "Kisah nyata, tes diagnostik, cara memakai toolkit",
          "Satu masalah nyata pilihanmu"],
         ["Bagian 1 \u00b7 Mindset", "Mengapa otak menipu kita, dan tiga sikap dasar",
          "Rem kognitif dan kesadaran sikap"],
         ["Bagian 2 \u00b7 TUNTAS 7D", "Tujuh langkah inti, masing-masing dengan alat dan worksheet",
          "Satu masalah yang tuntas tujuh langkah"],
         ["Bagian 3 \u00b7 Scale-Up", "Menerapkan untuk tim, bisnis, dan hidup; panduan workshop",
          "Rencana perbaikan bersama dan agenda workshop"],
         ["Penutup", "Program 30 hari, glosarium, template, akses toolkit",
          "Kebiasaan dan perangkat untuk melanjutkan"]],
        [0.24, 0.46, 0.30]))
    st += render("""
#### Perjalanan satu masalah melalui tujuh langkah

Bayangkan sebuah masalah sebagai sesuatu yang jatuh ke dalam air. Ia mengeluarkan riak ke atas: yang paling terlihat adalah gejala, yang lebih dalam adalah masalah, dan yang paling dalam adalah akar. Tujuh langkah membawa kita menelusuri riak itu dari permukaan sampai dasar, lalu naik kembali membawa perbaikan yang benar.
""")
    st.append(tool_table(
        ["Langkah", "Pertanyaan intinya", "Keluaran"],
        [["D1 \u00b7 Detect", "Apa yang sebenarnya terjadi, dan seberapa besar?",
          "Angka dan sebaran yang jujur"],
         ["D2 \u00b7 Define", "Satu kalimat apa yang merangkum masalah ini?",
          "Rumusan masalah berangka"],
         ["D3 \u00b7 Dig", "Apa yang menyebabkan ini, dan bagaimana kita tahu?",
          "Akar terverifikasi"],
         ["D4 \u00b7 Design", "Jalan apa saja yang tersedia?",
          "Tiga sampai lima opsi utuh"],
         ["D5 \u00b7 Decide", "Mana yang kita pilih, dan atas dasar apa?",
          "Keputusan dan alasannya"],
         ["D6 \u00b7 Do", "Apa langkah pertama, dan bagaimana kita tahu kemajuannya?",
          "Rencana 30 hari yang berjalan"],
         ["D7 \u00b7 Drive", "Bagaimana menjaga hasil ini agar tidak hilang?",
          "Standar, pemilik, dan ritme"]],
        [0.20, 0.46, 0.34]))
    st.append(callout("story", "Janji yang layak kamu pegang", [
        para("Kalau kamu mengerjakan worksheet setiap bab dengan masalahmu sendiri, pada akhir "
             "bagian kedua kamu akan memegang satu masalah yang sudah tuntas dari permukaan "
             "sampai akar. Bukan karena buku ini memberi jawaban, tetapi karena ia memaksa "
             "jawaban itu keluar dari data dan pengamatanmu sendiri."),
    ]))
    return st
