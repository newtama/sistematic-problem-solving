"""Additional depth for BAGIAN 1 - mindset."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (tool_table, caption, callout, keyline, case_study,
                        worksheet_block, StatRow, rule)

S = styles()


def bab1_extra():
    st = [PageBreak()]
    st.append(H("Anatomi sebuah jebakan: bagaimana satu kesimpulan lahir", S["h3"],
                level=3, register=False))
    st += render("""
Agar mudah diingat, mari kita bedah bagaimana satu kesimpulan yang salah lahir, langkah demi langkah. Kisah ini adalah pola yang berulang di hampir semua organisasi.
""")
    st.append(tool_table(
        ["Tahap", "Apa yang terjadi", "Apa yang terlihat dari luar"],
        [["1. Isyarat", "Satu orang mengeluh tentang sesuatu", "Keluhan diterima"],
         ["2. Pola dini", "Keluhan serupa muncul dua kali lagi", "Terasa seperti pola"],
         ["3. Cerita", "Otak menyusun penjelasan yang masuk akal", "Semua merasa sudah paham"],
         ["4. Sepakat", "Yang ragu memilih diam agar tidak menyimpang", "Terlihat mufakat"],
         ["5. Solusi", "Solusi dibuat untuk cerita, bukan untuk fakta", "Terlihat produktif"],
         ["6. Kekecewaan", "Hasilnya tidak berubah", "Semua bingung"],
         ["7. Pengulangan", "Siklus dimulai lagi tanpa pemeriksaan", "Lelah dan sinis"]],
        [0.16, 0.46, 0.38]))
    st.append(callout("insight", "Cara memutus rantai di tahap ketiga", [
        para("Rantai ini paling mudah diputus di tahap ketiga, saat cerita baru mulai terbentuk. "
             "Yang dibutuhkan sederhana: satu orang bertanya, \"apa datanya?\" Pertanyaan itu "
             "menunda cerita selama satu menit, dan satu menit itu sering cukup untuk mengubah "
             "seluruh arah pembahasan."),
    ]))

    st.append(PageBreak())
    st.append(H("Tujuh jebakan lanjutan yang perlu kamu kenali", S["h3"], level=3,
                register=False))
    st += render("""
Enam jebakan di bab utama adalah yang paling sering. Tujuh berikutnya lebih halus, tetapi sama merugikannya.
""")
    st.append(tool_table(
        ["Jebakan", "Bentuknya", "Penawarnya"],
        [["Efek hasil", "Menilai keputusan dari hasilnya, bukan dari prosesnya",
          "Nilai prosesnya saat keputusan diambil"],
         ["Bias kelangsungan hidup", "Belajar hanya dari yang berhasil, bukan dari yang gagal",
          "Cari juga yang gagal dan tanyakan sebabnya"],
         ["Terlalu percaya diri", "Merasa yakin melebihi bukti yang dimiliki",
          "Tanyakan: seberapa yakin, dan atas dasar apa?"],
         ["Nol risiko", "Memilih yang tidak ada risikonya, padahal risikonya menunda",
          "Hitung biaya menunda seperti biaya bertindak"],
         ["Efek bingkai", "Tergantung cara masalah disajikan",
          "Tulis ulang masalah dalam dua bentuk berbeda"],
         ["Jangkar diri", "Terpaku pada keputusan yang sudah diambil sebelumnya",
          "Tanyakan: kalau mulai dari nol, apakah saya memilih hal yang sama?"],
         ["Terlalu dekat", "Menilai dari contoh yang paling dekat dan mudah diingat",
          "Cari data dari luar lingkaran terdekat"]],
        [0.22, 0.40, 0.38]))

    st.append(PageBreak())
    st.append(H("Lembar periksa sebelum mengambil keputusan penting", S["h3"],
                level=3, register=False))
    st += render("""
Tempel lembar ini di dekat tempat kerjamu. Pakai setiap kali kamu akan mengambil keputusan yang sulit dibatalkan.
""")
    st.append(tool_table(
        ["Periksa", "Pertanyaan", "Sudah?"],
        [["Sumber", "Apakah informasi saya berasal dari minimal tiga sumber berbeda?", ""],
         ["Pembanding", "Apakah ada unit atau orang yang tidak bermasalah untuk dibandingkan?", ""],
         ["Pembantah", "Apakah ada yang berani membantah, dan apakah saya mendengarkannya?", ""],
         ["Alternatif", "Apakah saya punya minimal dua penjelasan alternatif?", ""],
         ["Biaya menunda", "Berapa biaya menunggu, dibandingkan biaya salah?", ""],
         ["Titik ubah", "Bukti apa yang akan membuat saya mengganti keputusan?", ""],
         ["Catatan", "Apakah saya menuliskan alasan keputusan ini?", ""]],
        [0.18, 0.66, 0.16]))

    st.append(PageBreak())
    st.append(H("Latihan tujuh hari: melatih otak yang lebih jernih", S["h3"],
                level=3, register=False))
    st += render("""
Kebiasaan berpikir dibentuk oleh pengulangan kecil, bukan oleh seminar. Berikut program tujuh hari yang bisa dijalankan tanpa tambahan waktu berarti.
""")
    st.append(tool_table(
        ["Hari", "Latihan", "Waktu"],
        [["Senin", "Ubah satu keluhan hari ini menjadi satu angka", "3 menit"],
         ["Selasa", "Tanyakan \"apa datanya?\" sekali dalam rapat", "10 detik"],
         ["Rabu", "Tulis satu masalahmu dalam satu kalimat berangka", "5 menit"],
         ["Kamis", "Tanyakan \"kenapa\" tiga kali pada satu kejadian", "5 menit"],
         ["Jumat", "Cari satu pembanding untuk masalahmu", "10 menit"],
         ["Sabtu", "Tinjau apa yang kamu pikir benar minggu ini dan ternyata salah", "10 menit"],
         ["Minggu", "Tulis satu keputusan kecil dan alasan-alasannya", "10 menit"]],
        [0.14, 0.70, 0.16]))
    st.append(keyline("Berpikir jernih bukan bakat, tetapi kebiasaan yang bisa dilatih seperti otot."))
    st.append(callout("practice", "Jurnal berpikir mingguan", [
        para("Setiap akhir minggu, jawab empat pertanyaan ini di buku catatan. Setelah satu "
             "kuartal, kamu akan punya rekam jejak caramu berpikir, dan itu lebih berguna "
             "daripada catatan prestasi apa pun."),
        para("1. Keputusan apa yang saya ambil minggu ini, dan atas dasar apa?"),
        para("2. Di mana saya menebak padahal saya bisa mencari data?"),
        para("3. Apa yang saya hindari karena tidak nyaman?"),
        para("4. Satu hal apa yang akan saya lakukan berbeda minggu depan?"),
    ]))
    st.append(_ws("WS-1B", "Jurnal Berpikir Mingguan", "Salin dan pakai setiap minggu",
                  [{"label": "Keputusan minggu ini & alasannya", "lines": 3},
                   {"label": "Di mana aku menebak padahal bisa mencari data", "lines": 3},
                   {"label": "Apa yang kuhindari karena tidak nyaman", "lines": 2},
                   {"label": "Satu hal yang akan kulakukan berbeda", "lines": 2}]))

    st.append(PageBreak())
    st.append(H("Ketika jebakan kognitif menelan biaya nyata", S["h3"], level=3,
                register=False))
    st.append(case_study(
        "B1", "Perusahaan Distribusi", "Keputusan besar yang dibangun di atas bias",
        "Bab 1 \u00b7 keputusan yang tidak bisa dibatalkan",
        [("SITUASI", "Manajemen memutuskan membangun gudang baru di kota yang jauh, setelah "
          "mendengar dua pelanggan besar akan memperluas usaha di sana."),
         ("BIAS 1 \u00b7 EFEK KEDEKATAN", "Dua pelanggan itu adalah yang terdekat dan paling "
          "sering mengeluh. Kesan mereka sangat kuat, padahal keduanya hanya mewakili 8% volume."),
         ["BIAS 2 \u00b7 KONFIRMASI", "Tim hanya mencari data yang mendukung rencana. Data "
          "pertumbuhan wilayah lain tidak pernah dibuka."],
         ["BIAS 3 \u00b7 TERLALU PERCAYA DIRI", "Proyeksi dibuat dengan satu skenario, tanpa "
          "skenario buruk."],
         ["BIAS 4 \u00b7 EFEK BIAYA TENGGELAM", "Setelah gudang dibangun dan hasilnya jauh di "
          "bawah proyeksi, keputusan ditambah: membeli kendaraan baru untuk \"memanfaatkan\" "
          "gudang itu, padahal masalahnya gudang itu sendiri."],
         ["HASIL", "Dua tahun kemudian, gudang dijual dengan kerugian. Perusahaan kehilangan "
          "modal dan waktu yang seharusnya dipakai memperkuat rute yang sudah kuat."],
         ["PELAJARAN", "Semua keputusan buruk ini tidak diambil oleh orang bodoh. Semua diambil "
          "oleh orang cerdas yang tidak memasang rem kognitif. Rem itu sederhana: cari data "
          "yang membantah, cari pembanding, dan tulis asumsi di atas kertas sebelum memutuskan."],
        ]))
    st.append(callout("insight", "Rem paling murah: satu orang penantang", [
        para("Cara termurah memasang rem kognitif di rapat apa pun adalah menunjuk satu orang "
             "yang tugasnya secara resmi mencari kelemahan rencana. Selama perannya jelas, orang "
             "itu tidak dianggap mengganggu. Tanpa peran resmi, orang yang mencari kelemahan "
             "selalu terdengar seperti penghambat."),
    ]))
    return st


def bab2_extra():
    st = [PageBreak()]
    st.append(H("Dua manajer, satu masalah, dua akhir yang berbeda", S["h3"],
                level=3, register=False))
    st += render("""
Dua manajer di perusahaan yang sama menghadapi masalah identik: tim mereka kehilangan tenggat terlalu sering. Mari kita bandingkan cara mereka berpikir, langkah demi langkah.
""")
    st.append(tool_table(
        ["Tahap", "Manajer A", "Manajer B"],
        [["Respons pertama", "Mengumpulkan tim, menekankan pentingnya tenggat",
          "Menanyakan satu hal: tenggat mana yang paling sering terlewat?"],
         ["Data", "Tidak ada; hanya kesan bahwa tim kurang serius",
          "Menghitung: 7 dari 20 tenggat terlewat, semuanya pada pekerjaan yang menunggu "
          "dokumen dari pihak lain"],
         ["Pertanyaan", "\"Kenapa tim tidak disiplin?\"",
          "\"Apa yang membuat pekerjaan ini menunggu?\" (curiosity)"],
         ["Kesimpulan", "Masalah kemauan tim", "Masalah alur kerja yang tidak punya langkah "
          "paralel (clarity)"],
         ["Tindakan", "Rapat disiplin mingguan", "Mengubah alur: pekerjaan yang tidak "
          "bergantung dokumen dimulai lebih dulu"],
         ["Hasil", "Tenggat terlewat turun sedikit, lalu kembali lagi",
          "Tenggat terlewat turun dari 7 menjadi 2, dan bertahan"],
         ["Suasana tim", "Tertekan, saling menyalahkan", "Lebih tenang, karena masalahnya "
          "bukan mereka"]],
        [0.16, 0.42, 0.42]))
    st += render("""
Perhatikan perbedaannya bukan pada kecepatan bertindak. Manajer A bertindak lebih cepat. Perbedaannya ada pada dua hal: Manajer B bertanya sebelum menjawab, dan ia berani menyimpulkan bahwa masalahnya ada pada alur, bukan pada orang. Dua hal itulah inti dari curiosity dan courage.

#### Rencana dua puluh satu hari membangun tiga sikap

Sikap tidak dibangun dengan membaca. Ia dibangun dengan pengulangan kecil selama tiga minggu.
""")
    st.append(tool_table(
        ["Minggu", "Fokus", "Latihan harian (5 menit)"],
        [["1", "Curiosity", "Ajukan satu pertanyaan yang lebih baik daripada yang biasanya "
          "kamu ajukan, dan tuliskan jawabannya"],
         ["2", "Clarity", "Ubah satu pernyataan menjadi fakta terukur. Pisahkan cerita dari "
          "kenyataan"],
         ["3", "Courage", "Ambil satu langkah kecil pada hal yang biasanya kamu hindari karena "
          "tidak nyaman"]],
        [0.12, 0.22, 0.66]))
    st.append(keyline("Tiga minggu, tiga kebiasaan. Setelah itu, cara berpikirmu tidak akan kembali seperti semula."))
    st.append(_ws("WS-2C", "Lembar Tiga Sikap", "Catatan dua puluh satu hari",
                  [{"label": "Minggu 1 \u2014 pertanyaan terbaik yang aku ajukan", "lines": 4},
                   {"label": "Minggu 2 \u2014 cerita yang aku ubah menjadi fakta", "lines": 4},
                   {"label": "Minggu 3 \u2014 langkah berani yang aku ambil", "lines": 4}]))

    st.append(PageBreak())
    st.append(H("Curiosity: naikkan mutu pertanyaanmu", S["h3"], level=3,
                register=False))
    st += render("""
Mutu jawaban tidak pernah melebihi mutu pertanyaan. Latihan berikut mengajarkan cara mengubah pertanyaan dangkal menjadi pertanyaan yang membuka.
""")
    st.append(tool_table(
        ["Pertanyaan dangkal", "Kenapa dangkal", "Pertanyaan yang membuka"],
        [["\"Bagaimana cara memperbaikinya?\"", "Melompat ke solusi",
          "\"Sebenarnya apa yang sedang terjadi?\""],
         ["\"Siapa yang salah?\"", "Mencari orang, bukan sebab",
          "\"Proses mana yang membuat ini mungkin terjadi?\""],
         ["\"Apakah ini masalah besar?\"", "Jawabannya hanya ya atau tidak",
          "\"Seberapa besar, dan bagi siapa paling besar?\""],
         ["\"Kapan selesai?\"", "Fokus pada tenggat, bukan pada hasil",
          "\"Apa yang harus benar supaya bisa selesai?\""],
         ["\"Apakah kita punya anggaran?\"", "Menutup pintu sebelum mencari",
          "\"Versi paling murah yang masih menyentuh akar itu seperti apa?\""]],
        [0.28, 0.30, 0.42]))
    st.append(callout("story", "Kisah: satu pertanyaan yang membuka sepuluh pintu", [
        para("Di sebuah kantor layanan, tim terjebak bertahun-tahun pada pertanyaan "
             "\"bagaimana mempercepat pelayanan\". Berbagai cara dicoba: pelatihan, alat baru, "
             "petugas tambahan. Hasilnya selalu kembali ke titik semula."),
        para("Seorang staf baru mengubah pertanyaannya menjadi: \"Layanan apa yang sebenarnya "
             "paling sering pelanggan butuhkan, dan apakah semua orang memang perlu datang?\" "
             "Pertanyaan itu membuka pintu yang selama ini terkunci: ternyata 38% kunjungan "
             "adalah keperluan yang bisa diselesaikan tanpa kehadiran."),
        para("Perbaikan terbesar tidak datang dari mempercepat layanan, tetapi dari menghapus "
             "kebutuhan separuh kunjungan. Semua itu berasal dari satu pertanyaan yang lebih "
             "baik."),
    ]))

    st.append(PageBreak())
    st.append(H("Tiga puluh pertanyaan pengasah rasa ingin tahu", S["h3"], level=3,
                register=False))
    st += render("""
Simpan daftar ini. Ketika sebuah masalah terasa membosankan atau sudah terlalu lama, pilih lima pertanyaan dan jawab. Kebosanan biasanya tanda bahwa pertanyaannya belum cukup tajam.
""")
    st.append(tool_table(
        ["Tentang apa", "Pertanyaan"],
        [["Kenyataan", "Apa yang benar-benar terjadi, berbeda dari apa yang dilaporkan? Apa "
          "yang akan terlihat kalau saya berdiri di tempat kejadian?"],
         ["Angka", "Angka apa yang tidak saya periksa? Apakah rata-rata menyembunyikan sesuatu?"],
         ["Pembanding", "Siapa yang tidak bermasalah? Apa yang mereka lakukan berbeda?"],
         ["Waktu", "Sejak kapan ini terjadi? Apa yang berubah saat itu?"],
         ["Orang", "Siapa yang paling dulu tahu? Kenapa suaranya tidak sampai ke sini?"],
         ["Proses", "Langkah mana yang ada hanya karena kebiasaan? Siapa yang memutuskan "
          "bahwa langkah itu perlu?"],
         ["Aturan", "Aturan mana yang dibuat untuk kenyataan yang sudah berubah?"],
         ["Batas", "Bagian mana yang benar-benar ada dalam kendali saya?"],
         ["Biaya", "Berapa biaya membiarkan ini berlanjut satu tahun lagi?"],
         ["Perbaikan", "Kalau masalah ini selesai, apa yang menjadi lebih baik secara terukur?"]],
        [0.18, 0.82]))

    st.append(PageBreak())
    st.append(H("Clarity: latihan memisahkan fakta dari cerita", S["h3"], level=3,
                register=False))
    st += render("""
Ini latihan yang paling cepat memberi hasil, karena hampir semua diskusi yang berputar berasal dari pencampuran fakta dan cerita.
""")
    st.append(tool_table(
        ["Pernyataan", "Jenisnya", "Ubah menjadi fakta"],
        [["\"Prosesnya membingungkan\"", "Cerita",
          "\"Tiga dari lima petugas baru meminta bantuan pada langkah keempat\""],
         ["\"Pelanggan tidak sabar\"", "Cerita",
          "\"Tingkat pembatalan pesanan naik setelah menunggu lebih dari 8 menit\""],
         ["\"Mesinnya sering rusak\"", "Cerita",
          "\"Downtime 6,4% dari jam kerja, 70% terjadi pada shift malam\""],
         ["\"Tim kurang koordinasi\"", "Cerita",
          "\"11 dari 30 serah terima butuh perbaikan ulang\""],
         ["\"Produknya kurang menarik\"", "Cerita",
          "\"Konversi halaman produk 1,2%, sementara kategori sejenis 3,1%\""]],
        [0.30, 0.16, 0.54]))
    st.append(callout("practice", "Latihan cermin", [
        para("Tuliskan tiga kalimat yang paling sering kamu ucapkan tentang masalahmu. Untuk "
             "setiap kalimat, tuliskan fakta yang mendasarinya. Kalau kamu tidak bisa menuliskan "
             "faktanya, kamu sudah menemukan asumsi terbesarmu."),
    ]))

    st.append(PageBreak())
    st.append(H("Courage: percakapan sulit yang tidak bisa dihindari", S["h3"], level=3,
                register=False))
    st += render("""
Sebagian besar akar masalah berujung pada percakapan yang dihindari. Bukan percakapan tentang orang, tetapi percakapan tentang kenyataan yang tidak nyaman. Berikut kerangka yang membuat percakapan itu mungkin.
""")
    st.append(tool_table(
        ["Langkah", "Kalimat pembuka", "Tujuan"],
        [["Fakta", "\"Saya melihat angka ini\u2026\"", "Menyepakati kenyataan"],
         ["Dampak", "\"Akibatnya ini terjadi\u2026\"", "Menunjukkan mengapa penting"],
         ["Pertanyaan", "\"Menurutmu apa yang membuat ini terjadi?\"", "Mengundang sudut pandang lain"],
         ["Kepemilikan", "\"Apa yang bisa kita ubah bersama?\"", "Menghindari menyalahkan"],
         ["Kesepakatan", "\"Apa satu langkah pertama, dan siapa?\"", "Mengubah menjadi tindakan"]],
        [0.18, 0.42, 0.40]))
    st.append(keyline("Keberanian bukan berbicara keras, tapi bersedia menghadapi kenyataan yang tidak nyaman."))
    st.append(_ws("WS-2B", "Rencana Percakapan Sulit", "Siapkan sebelum berbicara",
                  [{"label": "Kenyataan yang perlu disepakati (angka/fakta)", "lines": 3},
                   {"label": "Dampaknya bila dibiarkan", "lines": 2},
                   {"label": "Sudut pandang yang mungkin berbeda", "lines": 3},
                   {"label": "Satu langkah pertama yang bisa disepakati", "lines": 2},
                   {"label": "Siapa & kapan", "lines": 1}]))
    return st


def _ws(code, title, subtitle, fields):
    return worksheet_block(code, title, subtitle, fields)
