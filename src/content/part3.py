"""BAGIAN 3 - Scale-up & Workshop."""
from reportlab.platypus import PageBreak, NextPageTemplate

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (PartDivider, keyline, tool_table, caption, callout,
                        case_study, worksheet_block, QRPanel, WriteLines, rule)

S = styles()


def build():
    st = []
    st.append(NextPageTemplate("opener"))
    st.append(PageBreak())
    st.append(PartDivider(
        "Bagian 3",
        "Scale-Up & Workshop",
        "Tujuh langkah yang sama, dipakai untuk tim, bisnis, keluarga, dan karier. Ditutup panduan memfasilitasi workshop satu hari.",
        color=TEAL))
    st.append(NextPageTemplate("body"))

    # =================================================================
    #  BAB 10
    # =================================================================
    st.append(PageBreak())
    st.append(H("Bab 10: Problem Solving untuk Tim & Bisnis", S["h2"], level=2,
                key="bab10"))
    st += render("""
Sampai di sini, kerangka TUNTAS 7D dipakai pada satu masalah. Di dalam tim, ada satu lapisan tambahan: tujuh orang yang melihat masalah dengan tujuh cara berbeda. Lapisan itu bisa menjadi kekuatan terbesar, atau sumber kekacauan terbesar.

Bab ini menunjukkan cara menjalankan 7D bersama orang lain tanpa rapat yang berputar-putar.
""")
    st += render("!fig meeting")

    st += render("""
## Tiga aturan dasar kerja tim

Aturan pertama: satu masalah, satu lembar, satu pemilik. Kelompok yang membahas lima masalah dalam satu rapat akan membuat lima rencana setengah jadi.

Aturan kedua: pisahkan waktu menyelidiki dari waktu memutuskan. Dalam waktu menyelidiki, semua pertanyaan boleh diajukan. Dalam waktu memutuskan, semua jawaban harus dinilai.

Aturan ketiga: setiap orang punya peran yang jelas. Tanpa peran, rapat menjadi pidato bergiliran.
""")
    st.append(tool_table(
        ["Peran", "Tugas", "Kalau tidak ada"],
        [["Pemilik masalah", "Menjaga tujuan dan mengambil keputusan akhir", "Rapat tanpa ujung"],
         ["Fasilitator", "Menjaga urutan 7D dan waktu", "Pembicaraan melompat-lompat"],
         ["Pencatat", "Menulis fakta, bukan kesan", "Keputusan diingat berbeda-beda"],
         ["Penantang", "Wajib mencari kelemahan usulan", "Keputusan lemah lolos tanpa uji"],
         ["Pelaksana", "Menjalankan langkah harian", "Rencana tidak turun ke lapangan"]],
        [0.22, 0.42, 0.36]))

    st += render("""
## Menjalankan 7D dalam satu rapat dua jam

Rapat dua jam bisa menuntaskan D1 sampai D5 untuk masalah yang sedang. Ini susunan waktunya.
""")
    st.append(tool_table(
        ["Waktu", "Langkah", "Kegiatan", "Keluaran"],
        [["0\u201310 menit", "Pembuka", "Tulis masalah apa adanya, tanpa solusi", "Kata-kata asli"],
         ["10\u201325", "D1", "Kumpulkan sinyal & ukuran sebaran", "Kanvas Deteksi Sinyal"],
         ["25\u201345", "D2", "Tajamkan kalimat masalah", "Satu kalimat berangka"],
         ["45\u201375", "D3", "5 Whys / tulang ikan, cari akar", "Dua-tiga akar kandidat"],
         ["75\u2013105", "D4", "SCAMPER, hasilkan 8 opsi", "Opsi kasar"],
         ["105\u2013115", "Istirahat", "Jangan dilewati", "Energi kembali"],
         ["115\u2013125", "D5", "Kriteria & matriks keputusan", "Pilihan & alasan"]],
        [0.16, 0.14, 0.42, 0.28]))
    st.append(keyline("Rapat yang baik punya keluaran di setiap segmen, bukan hanya kesan."))
    st.append(callout("insight", "Tanda rapat sedang berputar dan cara menghentikannya", [
        para("Kalau dua orang berdebat lebih dari tiga menit tentang hal yang tidak berasal dari "
             "data, hentikan. Tuliskan kedua pendapat di kolom dugaan, lalu minta data untuk "
             "mengujinya. Perdebatan tanpa data tidak akan selesai, hanya berganti pelaku."),
    ]))

    st.append(sp(4))
    st.append(case_study(
        "9", "Tim Startup", "Meluncurkan fitur yang gagal dipakai",
        "Pola nyata \u00b7 8 orang \u00b7 peluncuran tiga fitur",
        [("SITUASI",
          "Sebuah startup meluncurkan tiga fitur dalam enam bulan. Ketiganya kurang dipakai. "
          "Tim mulai saling menuding: produk bilang engineering lambat, engineering bilang "
          "nilai bisnisnya tidak jelas, pemasaran bilang produknya sulit dijelaskan."),
         ("PEMBUATAN MASALAH (D2, DIKERJAKAN BERSAMA)",
          "Kalimat masalah yang disepakati: \"Dari tiga fitur terakhir, hanya 6% pengguna aktif "
          "memakainya lebih dari sekali pada 30 hari pertama. Target minimal 20%, sesuai fitur "
          "paling berhasil tahun lalu.\""),
         ("AKAR (D3)",
          "Akar terverifikasi: fitur dirancang dari daftar keinginan internal, bukan dari "
          "pekerjaan yang benar-benar dilakukan pengguna. Tidak ada satu pun anggota tim yang "
          "pernah menonton pengguna menyelesaikan pekerjaannya."),
         ("OPSI (D4)",
          "Empat opsi: menambah onboarding, menghapus fitur yang gagal, membuat riset pengguna "
          "rutin, dan mengubah proses perencanaan agar setiap fitur wajib punya bukti masalah."),
         ("KEPUTUSAN (D5) & PELAKSANAAN (D6)",
          "Dua opsi dipilih: riset pengguna rutin dua minggu sekali, dan aturan bahwa setiap "
          "usulan fitur harus menyertakan satu kalimat masalah yang berangka beserta buktinya. "
          "Percobaan 30 hari dengan satu fitur."),
         ("PEMBAKUAN (D7)",
          "Aturan itu masuk ke dokumen proses produk. Setiap usulan fitur baru wajib memuat "
          "bagian rumusan masalah. Tinjauan penggunaan dilakukan setiap bulan."),
         ("HASIL",
          "Enam bulan kemudian, tingkat penggunaan fitur baru naik dari 6% menjadi 31%, dan "
          "jumlah fitur yang dibatalkan sebelum dibangun naik. Tim berhenti berdebat soal "
          "prioritas, karena buktinya ada di depan."),
         ("PELAJARAN",
          "Pada tim, tujuan utama 7D bukan menemukan solusi, tetapi menyamakan gambaran "
          "masalah. Ketika gambarnya sama, perdebatannya selesai dengan sendirinya."),
        ]))

    st.append(PageBreak())
    st += render("""
## Studi kasus bisnis: UMKM dengan stok yang selalu tekor

Masalah yang terdengar klasik tetapi nyata dialami ribuan usaha: bahan baku sering habis, "
sering menumpuk, dan selalu terasa mahal.
""")
    st.append(case_study(
        "10", "UMKM Kuliner", "Stok bahan baku selalu tekor",
        "Pola nyata \u00b7 tiga gerai \u00b7 enam bulan",
        [("GEJALA",
          "Bahan baku sering habis pada hari sibuk, tetapi di hari lain menumpuk dan terbuang. "
          "Pemilik merasa masalahnya adalah pemasok yang tidak bisa diandalkan."),
         ("D1 \u00b7 DETEKSI",
          "Ternyata pemasok datang tepat waktu. Yang bermasalah adalah pencatatan: pemakaian "
          "harian tidak dicatat, hanya diingat. Angka rata-rata pemborosan mencapai 14% dari "
          "biaya bahan per bulan."),
         ("D2 \u00b7 RUMUSAN",
          "\"Pemborosan bahan baku 14% per bulan pada tiga gerai, khusus pada bahan segar "
          "dengan masa simpan di bawah tiga hari. Target: di bawah 6% dalam tiga bulan.\""),
         ("D3 \u00b7 AKAR",
          "Dua akar: pemesanan dilakukan berdasarkan perkiraan tanpa data pemakaian; dan tiga "
          "gerai memesan secara terpisah, sehingga tidak bisa saling menutup kekurangan."),
         ("D4\u2013D5 \u00b7 OPSI & KEPUTUSAN",
          "Opsi yang dipilih bukan sistem mahal, tetapi satu buku catatan pemakaian bersama dan "
          "satu aturan pemesanan mingguan terpusat untuk bahan segar."),
         ("D6 \u00b7 EKSEKUSI",
          "Satu angka dipantau: persentase bahan terbuang per minggu. Langkah harian: mencatat "
          "pemakaian selama sepuluh menit setelah tutup. Pemicu: setelah kas ditutup."),
         ("D7 \u00b7 PEMBAKUAN",
          "Buku catatan menjadi standar. Pemilik gerai bertanggung jawab mengisi setiap hari, "
          "dan pemesanan mingguan dilakukan bersama setiap Senin pagi."),
         ("HASIL",
          "Pemborosan turun dari 14% menjadi 5,4% dalam empat bulan. Penghematan itu setara "
          "dengan laba satu gerai tambahan, tanpa menambah penjualan sama sekali."),
         ("PELAJARAN",
          "Masalah stok hampir selalu masalah catatan, bukan masalah pemasok."),
        ]))

    # =================================================================
    #  BAB 11
    # =================================================================
    st.append(PageBreak())
    st.append(H("Bab 11: Problem Solving untuk Hidup", S["h2"], level=2, key="bab11"))
    st += render("""
Tujuh langkah yang sama bekerja untuk hal-hal yang paling pribadi. Bahkan mungkin di sana ia paling berguna, karena masalah pribadi jarang dianalisis dengan jujur. Kita terlalu cepat menyimpulkan, terlalu cepat menyalahkan, dan terlalu cepat menyerah.

Bagian ini memakai tiga contoh yang paling sering muncul: konflik keluarga, keuangan pribadi, dan karier yang terasa buntu.
""")
    st += render("!fig family")

    st.append(case_study(
        "11", "Keluarga", "Anak kecanduan gawai",
        "Pola nyata \u00b7 satu keluarga \u00b7 empat bulan",
        color=TEAL,
        sections=[
         ("GEJALA",
          "Anak berusia tiga belas tahun menghabiskan lebih dari lima jam sehari di gawai. "
          "Nilai sekolah turun, tidur malam kurang, dan komunikasi di rumah menegang. Upaya "
          "yang sudah dilakukan: menyita perangkat, memarahi, dan membatasi kuota internet."),
         ("KENAPA CARA LAMA GAGAL",
          "Semua upaya berfokus pada gawai. Karena akarnya bukan gawai, setiap upaya hanya "
          "memindahkan konflik, bukan menyelesaikannya. Menyita perangkat berakhir dengan "
          "pertengkaran dan penggunaan diam-diam."),
         ("D1\u2013D2 \u00b7 DETEKSI DAN RUMUSAN",
          "Orang tua mencatat selama dua minggu: jam penggunaan, waktu, dan apa yang hilang. "
          "Rumusan: \"Rata-rata 5,4 jam per hari, dengan puncak setelah pulang sekolah sampai "
          "makan malam. Target: di bawah 2 jam pada jam tersebut, sambil menjaga kegiatan yang "
          "anak senangi.\""),
         ("D3 \u00b7 AKAR",
          "Setelah beberapa percakapan yang tidak menuduh, muncul dua akar. Pertama, anak tidak "
          "punya kegiatan yang membuatnya merasa mampu setelah pulang sekolah: ia merasa tidak "
          "bagus di apa pun yang coba ia lakukan. Kedua, gawai menjadi satu-satunya ruang di "
          "mana ia punya kendali dan diterima teman-temannya."),
         ("D4\u2013D5 \u00b7 OPSI DAN KEPUTUSAN",
          "Opsi: menambah kegiatan, mengatur jam gawai bersama, mengubah jam keluarga, dan "
          "mencari bantuan sekolah. Keputusan berbasis kriteria: mana yang menjaga hubungan, "
          "bukan merusaknya. Yang dipilih: satu kegiatan pilihan anak + satu aturan jam yang "
          "disepakati bersama, bukan diterapkan sepihak."),
         ("D6 \u00b7 EKSEKUSI",
          "Angka tunggal: jam penggunaan setelah pulang sekolah. Langkah harian: makan malam "
          "bersama tanpa gawai, tiga puluh menit. Pemicu: begitu makan malam disiapkan, semua "
          "perangkat masuk ke keranjang bersama, termasuk milik orang tua."),
         ("D7 \u00b7 PEMBAKUAN",
          "Aturan jam dan makan malam menjadi kesepakatan tertulis yang ditempel di dapur, "
          "ditinjau setiap bulan bersama anak."),
         ("HASIL",
          "Dalam empat bulan, penggunaan di jam tersebut turun menjadi 1,6 jam. Nilai sekolah "
          "berangsur membaik, tetapi hasil yang paling penting: anak kembali bercerita tanpa "
          "diminta."),
         ("PELAJARAN",
          "Menghadapi perilaku tanpa memahami kebutuhannya hanya memindahkan masalah. "
          "Perhatikan betapa pentingnya langkah D3 dalam masalah keluarga."),
        ]))

    st.append(PageBreak())
    st.append(case_study(
        "12", "Keuangan Pribadi", "Gaji besar tetapi selalu habis",
        "Pola nyata \u00b7 satu rumah tangga \u00b7 lima bulan",
        color=TEAL,
        sections=[
         ("GEJALA",
          "Pendapatan gabungan tergolong tinggi, tetapi tabungan hampir selalu nol di akhir "
          "bulan. Sudah beberapa kali mencoba mencatat pengeluaran, tetapi berhenti setelah "
          "satu-dua minggu."),
         ("KENAPA CATATAN GAGAL",
          "Catatan pengeluaran seringkali hanya sebuah daftar. Ia tidak dipakai untuk mengubah "
          "keputusan. Mencatat tanpa menganalisis hanya menambah rasa bersalah, bukan solusi."),
         ("D1\u2013D2 \u00b7 DETEKSI DAN RUMUSAN",
          "Rumusan: \"Rata-rata tabungan bulanan hanya 2% dari pendapatan, sementara tujuan "
          "minimal 15%. Pengeluaran tidak kekurangan, tetapi tidak punya urutan prioritas.\""),
         ("D3 \u00b7 AKAR",
          "Setelah tiga bulan mutasi diperiksa, ditemukan bahwa 31% pengeluaran berasal dari "
          "langganan dan pembelian kecil berulang yang tidak pernah dirasakan manfaatnya. Akar: "
          "keputusan pengeluaran diambil seketika, tanpa pagar anggaran."),
         ("D4\u2013D5 \u00b7 OPSI DAN KEPUTUSAN",
          "Opsi: memotong semua langganan, menyiapkan amplop anggaran, memindahkan tabungan "
          "otomatis di awal bulan, dan menetapkan jeda 24 jam untuk pembelian di atas batas "
          "tertentu. Yang dipilih: amplop anggaran + pemindahan otomatis + jeda 24 jam."),
         ("D6 \u00b7 EKSEKUSI",
          "Angka tunggal: persentase tabungan per bulan. Langkah harian: mencatat satu baris "
          "pengeluaran hari itu, tiga menit. Pemicu: setelah makan malam, di meja yang sama."),
         ("D7 \u00b7 PEMBAKUAN",
          "Pemindahan otomatis berjalan sendiri. Tinjauan anggaran dilakukan setiap tanggal 1, "
          "lima belas menit, bersama pasangan."),
         ("HASIL",
          "Dalam lima bulan, tabungan bulanan naik dari 2% menjadi 18%. Yang lebih penting, "
          "pertengkaran soal uang menurun drastis karena keduanya melihat anggaran yang sama."),
         ("PELAJARAN",
          "Uang jarang masalah jumlah. Ia hampir selalu masalah keputusan yang tidak punya "
          "pagar."),
        ]))

    st.append(PageBreak())
    st.append(case_study(
        "13", "Karier", "Sudah kerja keras tetapi tidak naik jabatan",
        "Pola nyata \u00b7 satu karyawan \u00b7 enam bulan",
        color=TEAL,
        sections=[
         ("GEJALA",
          "Seorang karyawan bekerja lebih lama dari rekan-rekannya, jarang menolak tugas, dan "
          "hampir selalu memenuhi tenggat. Namun tiga kali kesempatan promosi jatuh ke orang "
          "lain. Ia menyimpulkan bahwa kantornya tidak menghargai kerja keras."),
         ("D1 \u00b7 DETEKSI YANG JUJUR",
          "Alih-alih bertanya pada perasaan, ia bertanya pada data. Ia menuliskan seluruh "
          "pencapaiannya enam bulan terakhir dan membandingkannya dengan kriteria yang tertulis "
          "di penilaian kinerja."),
         ("D2 \u00b7 RUMUSAN",
          "\"Saya memenuhi kriteria output pada semua periode, tetapi tidak memenuhi kriteria "
          "dampak lintas tim: hanya satu dari tujuh proyek saya melibatkan tim lain. Target: "
          "tiga proyek lintas tim dalam dua kuartal.\""),
         ("D3 \u00b7 AKAR",
          "Akarnya bukan kurang kerja keras, tetapi terlalu banyak mengerjakan pekerjaan yang "
          "terlihat tetapi tidak terlihat penting. Ia menjadi orang yang menyelesaikan tugas "
          "semua orang, bukan orang yang mengangkat isu yang berdampak besar."),
         ("D4\u2013D5 \u00b7 OPSI DAN KEPUTUSAN",
          "Opsi: meminta proyek lintas tim, memimpin satu inisiatif perbaikan, meminta umpan "
          "balik dari dua pemimpin, dan mengurangi tugas yang tidak berdampak. Yang dipilih: "
          "memimpin satu inisiatif perbaikan lintas tim, sekaligus meminta umpan balik terarah."),
         ("D6 \u00b7 EKSEKUSI",
          "Angka tunggal: jumlah keterlibatan lintas tim per kuartal. Langkah harian: tiga puluh "
          "menit untuk proyek lintas tim sebelum pekerjaan rutin dimulai. Pemicu: setelah kopi "
          "pagi, sebelum membuka surel."),
         ("D7 \u00b7 PEMBAKUAN",
          "Ia menetapkan aturan pribadi: setiap kuartal harus ada satu inisiatif lintas tim. "
          "Setiap akhir kuartal, ia meninjau bersama atasannya."),
         ("HASIL",
          "Dalam dua kuartal, ia memimpin dua inisiatif lintas tim dengan hasil terukur. Pada "
          "kesempatan promosi berikutnya, ia dipilih, dan alasannya jelas bagi semua orang."),
         ("PELAJARAN",
          "Kerja keras tanpa arah adalah kerja keras yang tidak terlihat. Periksa kriteria "
          "sebelum menyalahkan keadaan."),
        ]))

    # =================================================================
    #  BAB 12 - WORKSHOP
    # =================================================================
    from content import playbooks
    st += playbooks.build()

    st.append(PageBreak())
    st.append(H("Bab 12: Panduan Fasilitator Workshop Satu Hari", S["h2"],
                level=2, key="bab12"))
    st += render("""
Bab ini adalah buku panduan terpisah di dalam buku. Ia berisi agenda satu hari, peran, "
perlengkapan, skrip pembuka, dan kunci jawaban worksheet. Ikuti urutannya apa adanya, atau "
sesuaikan sesuai kebutuhan.
""")
    st.append(keyline("Workshop yang berhasil bukan yang paling meriah, tetapi yang menghasilkan satu masalah yang benar-benar tuntas."))
    st += render("!fig agenda")

    st += render("""
## Tujuan dan janji workshop

**Tujuan:** setiap peserta menyelesaikan satu masalah nyata melalui tujuh langkah TUNTAS 7D, dan keluar dengan satu rencana 30 hari yang siap dijalankan.

**Janji:** pada akhir hari, setiap peserta memiliki satu masalah yang sudah dirumuskan dengan angka, satu akar terverifikasi, tiga opsi, satu keputusan beralasan, dan satu langkah kecil untuk besok pagi.
""")
    st.append(tool_table(
        ["Sasaran akhir", "Bentuk keluarannya"],
        [["Masalah terdeteksi", "Kanvas Deteksi Sinyal terisi"],
         ["Masalah terumus", "Satu kalimat masalah berangka"],
         ["Akar terverifikasi", "Peta akar dengan cara verifikasi"],
         ["Opsi dirancang", "Minimal tiga opsi utuh"],
         ["Keputusan diambil", "Kartu Keputusan terisi"],
         ["Rencana siap", "Kanvas Eksekusi 30 Hari"],
         ["Pembakuan", "Peta Pembakuan + pemilik"]],
        [0.42, 0.58]))

    st.append(PageBreak())
    st += render("""
## Agenda satu hari (08.30\u201316.30)

Perhatikan bahwa hari ini dirancang untuk bergerak cepat, tetapi tidak melompati langkah.
""")
    st.append(tool_table(
        ["Waktu", "Sesi", "Kegiatan inti", "Keluaran"],
        [["08.30\u201309.00", "Pembuka", "Perkenalan, janji, tes diagnostik", "Profil peserta"],
         ["09.00\u201309.30", "Mindset", "Bias kognitif & tiga sikap dasar", "Komitmen sikap"],
         ["09.30\u201310.15", "D1 Detect", "Mini kuliah 15 menit + latihan 30 menit", "Kanvas Deteksi"],
         ["10.15\u201310.30", "Istirahat", "Kopi & bergerak", "Energi"],
         ["10.30\u201311.15", "D2 Define", "Latihan tajamkan kalimat masalah", "Kalimat masalah"],
         ["11.15\u201312.15", "D3 Dig", "5 Whys berpasangan + tulang ikan", "Peta akar"],
         ["12.15\u201313.15", "Makan siang", "Jeda penuh, tanpa pekerjaan", "Segar"],
         ["13.15\u201314.00", "D4 Design", "Sesi SCAMPER tanpa menilai", "8\u201312 opsi"],
         ["14.00\u201314.45", "D5 Decide", "Matriks keputusan + Kartu Keputusan", "Keputusan"],
         ["14.45\u201315.00", "Istirahat", "Jeda singkat", "Fokus"],
         ["15.00\u201315.45", "D6 Do", "Kanvas 30 hari + uji kematian", "Rencana eksekusi"],
         ["15.45\u201316.15", "D7 Drive", "Peta pembakuan + pemilik", "Rencana pembakuan"],
         ["16.15\u201316.30", "Penutup", "Presentasi kilat & komitmen publik", "Komitmen"]],
        [0.16, 0.14, 0.44, 0.26]))

    st.append(PageBreak())
    st += render("""
## Perlengkapan dan persiapan ruangan

- Satu set worksheet TUNTAS 7D per peserta (unduh dari toolkit digital).
- Kertas plano, sticky notes empat warna, spidol tebal, dan selotip.
- Satu dinding khusus untuk "papan masalah" tempat semua orang menempel status.
- Meja bundar lebih baik daripada meja panjang, karena setiap orang harus bicara.
- Aturan ruangan ditempel di dinding: tidak menyalahkan orang, berbicara berbasis data, dan semua usulan dicatat.

## Peran dalam workshop

**Fasilitator.** Menjaga urutan dan waktu. Tidak memberi jawaban, hanya mengajukan pertanyaan pemandu. Ini peran yang paling sulit, karena godaan untuk memberi tahu sangat besar.

**Pencatat.** Menuliskan fakta dan keputusan di papan. Bukan menafsirkan.

**Penantang.** Setiap kelompok punya satu orang yang bertugas mencari kelemahan usulan. Peran ini dirotasi setiap sesi supaya setiap orang pernah merasakannya.

**Penjaga waktu.** Mengingatkan lima menit sebelum sesi berakhir.
""")
    st.append(callout("insight", "Skrip pembuka yang bisa dibacakan", [
        para("\"Hari ini kita tidak akan belajar teori. Kita akan menyelesaikan satu masalah "
             "nyata yang sudah mengganggu pekerjaan kalian lebih dari sebulan. Satu masalah, "
             "satu lembar, tujuh langkah. Aturannya hanya tiga: kita bicara dengan data, kita "
             "tidak menyalahkan orang, dan kita tidak melewatkan langkah. Kalau ada yang ingin "
             "melompat ke solusi, saya akan menahan sebentar. Bukan karena solusinya buruk, "
             "tetapi karena kita belum tahu masalahnya dengan cukup jelas.\""),
    ]))

    st.append(PageBreak())
    st += render("""
## Kunci jawaban worksheet (untuk fasilitator)

Bagian ini untuk fasilitator. Bagikan hanya setelah peserta selesai mengerjakan.
""")
    st.append(tool_table(
        ["Worksheet", "Kesalahan yang paling sering", "Cara memperbaiki di tempat"],
        [["WS-D1", "Peserta menulis keluhan, bukan ukuran", "Minta satu angka, sekecil apa pun"],
         ["WS-D1", "Hanya satu angka, tanpa sebaran", "Tanya: menumpuk di mana?"],
         ["WS-D2", "Kalimat masalah berisi kata sifat", "Minta ganti setiap kata sifat dengan angka"],
         ["WS-D2", "Cakupan terlalu luas", "Minta persempit sampai satu tempat/orang"],
         ["WS-D3", "Berhenti di sebab pertama", "Tanya \"kenapa\" satu kali lagi"],
         ["WS-D3", "Akar berupa nama orang", "Alihkan ke proses: apa yang membuatnya sulit?"],
         ["WS-D4", "Kurang dari tiga opsi", "Paksa jalankan SCAMPER huruf E dan R"],
         ["WS-D5", "Kriteria ditulis setelah menilai", "Minta bobot ditulis sebelum skor"],
         ["WS-D6", "Langkah harian terlalu besar", "Pecah sampai 30 menit"],
         ["WS-D6", "Tidak ada pemicu", "Tanyakan: setelah kebiasaan apa?"],
         ["WS-D7", "Standar tanpa pemilik", "Minta satu nama ditulis sekarang"],
         ["WS-D7", "Tidak ada ritme tinjauan", "Tetapkan tanggal di kalender"]],
        [0.16, 0.44, 0.40]))

    st += render("""
## Dua role play yang paling efektif

**Role play pertama: si pelompat solusi.** Dua peserta berperan. Satu orang memaparkan masalah, satu orang berperan sebagai orang yang selalu melompat ke solusi. Tugas kelompok menahan diskusi agar tetap di langkah yang sedang dikerjakan. Latihan ini melatih kesabaran diagnosis.

**Role play kedua: rapat yang berputar.** Kelompok dibagi dua dengan usulan berbeda, tanpa data. Kelompok harus menyadari bahwa perdebatan tanpa data tidak bisa selesai, lalu berhenti dan mencari fakta. Latihan ini melatih perpindahan dari opini ke bukti.
""")
    st.append(callout("practice", "Penutup workshop: komitmen publik", [
        para("Minta setiap peserta mengucapkan satu kalimat di depan semua orang: \"Besok pagi "
             "pukul [jam], saya akan melakukan [langkah kecil] untuk masalah [nama masalah].\" "
             "Komitmen yang diucapkan di depan orang lain jauh lebih sering dijalankan "
             "daripada komitmen yang ditulis di buku pribadi."),
    ]))

    st.append(PageBreak())
    st.append(worksheet_block(
        "WS-FAS", "Lembar Persiapan Fasilitator", "Rencanakan workshopmu",
        [{"label": "Masalah utama yang akan dibawa peserta (bila seragam)", "lines": 2},
         {"label": "Jumlah peserta & jumlah kelompok", "lines": 1},
         {"label": "Peran yang sudah ditetapkan (fasilitator, pencatat, penantang, penjaga waktu)",
          "lines": 3},
         {"label": "Perlengkapan yang perlu disiapkan", "lines": 3},
         {"label": "Tiga aturan ruangan yang akan ditempel", "lines": 3},
         {"label": "Cara mengukur keberhasilan workshop ini", "lines": 2},
         {"label": "Rencana tindak lanjut dua minggu setelah workshop", "lines": 2}],
    ))
    st.append(QRPanel("https://tuntas7d.id/toolkit/workshop", "Toolkit Workshop",
                      "Paket lengkap: agenda, worksheet, slide, kartu peran, sertifikat",
                      "QR-WS"))
    return st
