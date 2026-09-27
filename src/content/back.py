"""PENUTUP - Epilog, kumpulan studi kasus, daftar pustaka, indeks tools."""
from reportlab.platypus import PageBreak, NextPageTemplate

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (PartDivider, keyline, tool_table, caption, callout,
                        case_study, worksheet_block, QRPanel, rule)
from frontmatter import StatementPage

S = styles()


def build():
    st = []
    st.append(NextPageTemplate("opener"))
    st.append(PageBreak())
    st.append(PartDivider(
        "Penutup",
        "Membawa Pulang Cara Berpikir Ini",
        "Dari tujuh langkah menjadi satu kebiasaan. Ditutup dengan daftar pustaka, indeks alat, dan akses toolkit digital.",
        color=NAVY))
    st.append(NextPageTemplate("body"))

    # =================================================================
    #  EPILOG
    # =================================================================
    st.append(PageBreak())
    st.append(H("Epilog: Tujuh Langkah yang Menjadi Kebiasaan", S["h2"],
                level=2, key="epilog"))
    st += render("""
Awal buku ini dibuka dengan sebuah rapat yang gagal karena membahas gejala. Akhir buku ini sebaiknya ditutup dengan pertanyaan: bagaimana supaya rapat seperti itu tidak terjadi lagi?

Jawabannya bukan pada alat. Alat sudah ada di tanganmu. Jawabannya ada pada kebiasaan. Tujuh langkah yang dipakai sekali hanya menghasilkan satu masalah yang selesai. Tujuh langkah yang menjadi kebiasaan menghasilkan organisasi yang berpikir lebih jernih.

Setiap kali kamu tergoda melompat ke solusi, ingat satu hal: kamu tidak sedang memperlambat diri, kamu sedang memastikan tenaga tidak terbuang. Pelompat solusi bekerja cepat dan sering salah. Penyelesai masalah yang baik bekerja dengan tempo yang tepat dan hampir selalu benar arahnya.

Ada satu tanda bahwa cara berpikir ini sudah menjadi milikmu. Kamu berhenti bertanya "apa yang harus kita lakukan" dan mulai bertanya "sebenarnya apa yang sedang terjadi". Begitu pertanyaan pertama itu berpindah, semua yang lain mengikutinya.
""")
    st.append(PullQuote("Bertanya lebih dulu bukan tanda ragu. Itu tanda kamu sudah pernah salah."))
    st += render("""
#### Tujuh kebiasaan untuk dibawa pulang

- **Detect.** Setiap keluhan dicatat apa adanya, lalu diubah menjadi angka.
- **Define.** Setiap masalah ditulis dalam satu kalimat berangka sebelum dibahas solusinya.
- **Dig.** Setiap akar digali paling tidak tiga lapis, dan diverifikasi dengan data.
- **Design.** Setiap keputusan punya paling tidak tiga opsi utuh.
- **Decide.** Setiap pilihan punya kriteria yang ditulis sebelum penilaian.
- **Do.** Setiap rencana punya satu angka, satu langkah kecil harian, dan satu pemicu.
- **Drive.** Setiap perbaikan punya standar, pemilik, dan ritme tinjauan.

#### Ajakan terakhir

Ambil masalahmu yang sebenarnya, bukan yang di worksheet. Kerjakan dengan tujuh langkah ini, tulis di satu lembar kertas, tempel di tempat yang kamu lihat setiap hari. Selesaikan dalam tiga puluh hari.

Setelah selesai, ajari satu orang lain. Mengajarkan adalah cara tercepat untuk memastikan kamu benar-benar memahaminya. Dan mungkin, orang itu akan menyelesaikan masalah yang sudah bertahun-tahun mengganggu hidupnya, karena kamu meluangkan waktu untuk berpikir lebih jernih.
""")
    st.append(sp(4))
    st.append(callout("insight", "Satu halaman yang layak kamu simpan", [
        para("<b>TUNTAS 7D dalam satu tarikan napas.</b> Kenali masalahnya dengan angka "
             "(Detect). Rumuskan satu kalimat berangka (Define). Gali sampai akar yang "
             "terverifikasi (Dig). Rancang minimal tiga opsi utuh (Design). Pilih dengan "
             "kriteria, bukan suara (Decide). Jalankan 30 hari dengan satu angka dan satu "
             "langkah kecil (Do). Bakukan dengan standar, pemilik, dan tinjauan (Drive)."),
    ]))

    # =================================================================
    #  BANK 12 STUDI KASUS
    # =================================================================
    st.append(PageBreak())
    st.append(H("Bank Studi Kasus: 12 Kasus Nyata", S["h2"], level=2, key="studi-kasus"))
    st += render("""
Dua belas kasus berikut adalah inti praktik buku ini. Beberapa di antaranya sudah kamu temui di bab-bab sebelumnya, dan sebagian sudah kamu baca dalam bentuk ringkas. Di sini semuanya dikumpulkan dalam format seragam supaya bisa dipakai untuk latihan dan diskusi kelompok.

Untuk setiap kasus, coba kerjakan dulu rumusannya sendiri sebelum membaca analisisnya. Cara belajar paling cepat adalah mencoba sebelum melihat jawabannya.
""")
    st.append(tool_table(
        ["No", "Konteks", "Masalah", "Hasil utama"],
        [["1", "Ritel minimarket", "Promo tidak menaikkan laba", "Laba naik 9%"],
         ["2", "Operator transportasi", "Komplain terlambat", "Tunggu turun 34%"],
         ["3", "Tim teknologi", "Fitur baru tidak dipakai", "Pemakaian 4%\u219214%"],
         ["4", "Pabrik komponen", "Cacat produksi naik", "Cacat turun 60%"],
         ["5", "Rumah sakit umum", "Antrean 3 jam", "Tunggu 30 menit"],
         ["6", "Layanan publik", "Kepuasan layanan turun", "Tunggu turun 41%"],
         ["7", "UMKM kuliner", "Omzet mandek", "Omzet naik 3x"],
         ["8", "Jaringan layanan", "Hasil tidak menyebar", "Bertahan di 60 cabang"],
         ["9", "Tim startup", "Fitur gagal dipakai", "Pemakaian 6%\u219231%"],
         ["10", "UMKM kuliner", "Stok selalu tekor", "Boros 14%\u21925,4%"],
         ["11", "Keluarga", "Anak kecanduan gawai", "5,4\u21921,6 jam"],
         ["12", "Keuangan pribadi", "Gaji besar selalu habis", "Tabungan 2%\u219218%"]],
        [0.06, 0.24, 0.40, 0.30]))

    st.append(PageBreak())
    st.append(case_study(
        "1", "Ritel Minimarket", "Promo yang tidak menaikkan laba",
        "Konteks \u00b7 42 gerai \u00b7 hasil: laba naik 9%",
        [("MASALAH (D2)", "Penjualan kategori minuman naik 22% setelah diskon, tetapi laba "
          "gerai turun 6%. Target: laba naik minimal 5% tanpa menambah anggaran diskon."),
         ("AKAR (D3)", "Promo memindahkan keranjang belanja pelanggan dari barang bermargin "
          "tinggi ke minuman bermargin tipis. Tidak ada satu pun insentif untuk menaikkan "
          "keranjang secara keseluruhan."),
         ("OPSI (D4)", "Diskon lebih besar pada minuman; bundling dengan makanan ringan; "
          "diskon bertingkat untuk total belanja; menghentikan promo."),
         ("KEPUTUSAN (D5)", "Bundling makanan ringan dipilih karena marginnya sehat dan "
          "menaikkan keranjang tanpa menurunkan persepsi nilai."),
         ("EKSEKUSI (D6)", "Satu angka: laba per gerai per minggu. Langkah harian: memastikan "
          "satu penawaran bundling terpasang dan terlihat. Pemicu: saat menyiapkan gerai pagi."),
         ("PEMBAKUAN (D7)", "Sepuluh gerai dengan kenaikan terbaik dijadikan standar bundling, "
          "dan tinjauan margin dilakukan bulanan."),
         ("HASIL", "Laba naik 9% dalam dua bulan, tanpa tambahan anggaran diskon, dengan "
          "penjualan minuman tetap tumbuh."),
         ("TOOLS UTAMA", "Pemisahan gejala-tujuan, uji sebab alternatif, pembanding sebelum-sesudah."),
        ]))

    st.append(case_study(
        "4", "Pabrik Komponen", "Cacat produksi turun 60% dengan pendekatan satu halaman",
        "Konteks \u00b7 dua lini \u00b7 hasil: cacat 4,8%\u21921,9%",
        [("MASALAH (D2)", "Cacat naik dari 2,1% menjadi 4,8% dalam empat bulan. Target: "
          "kembali ke bawah 2,5%."),
         ("RENCANA AWAL YANG SALAH", "Memperketat inspeksi akhir. Ini menangkap lebih banyak "
          "cacat tetapi tidak menghentikan sumbernya."),
         ("AKAR (D3)", "71% cacat adalah goresan, terkonsentrasi di satu stasiun pada pergantian "
          "shift, berasal dari prosedur pembersihan lama yang mempercepat keausan klip baki."),
         ("OPSI (D4)", "Menambah inspektur; mengganti klip; memperbarui prosedur; mengubah "
          "urutan pembersihan."),
         ("KEPUTUSAN (D5)", "Prosedur diperbarui dan klip diganti bahan lebih tahan, dimulai "
          "di satu stasiun sebagai uji kecil."),
         ("EKSEKUSI (D6)", "Satu angka: cacat goresan per shift. Langkah harian: pemeriksaan "
          "baki lima menit sebelum shift mulai. Pemicu: setelah briefing shift."),
         ("PEMBAKUAN (D7)", "Prosedur baru masuk dokumen kerja, pelatihan pembersihan diperbarui, "
          "dan prosedur lama ditarik dari peredaran."),
         ("HASIL", "Cacat turun menjadi 1,9% dalam 90 hari, turun sekitar 60% dari puncaknya."),
         ("TOOLS UTAMA", "Pareto, tulang ikan, 5 Whys, uji kecil berbasis shift."),
        ]))

    st.append(PageBreak())
    st.append(case_study(
        "5", "Rumah Sakit Umum", "Antrean tiga jam menjadi tiga puluh menit",
        "Konteks \u00b7 900 pasien/hari \u00b7 hasil: tunggu 100\u219230 menit",
        [("MASALAH (D2)", "Waktu tunggu rawat jalan mencapai tiga jam pada pagi hari, dengan "
          "kepuasan pasien di titik terendah lima tahun. Target: rata-rata di bawah 45 menit."),
         ("DETEKSI (D1)", "Rata-rata 100 menit, tetapi sebarannya menumpuk: puncak pagi "
          "melewati dua jam, sementara sore hanya sekitar 30 menit."),
         ("AKAR (D3)", "Dua akar: penjadwalan dokter tidak sinkron dengan kedatangan pasien, "
          "dan berkas asuransi tidak lengkap menyebabkan pengulangan administrasi."),
         ("OPSI (D4)", "Gedung tunggu baru; janji temu daring; pemisahan jalur berkas; "
          "penyebaran jam praktik; kombinasi ketiganya."),
         ("KEPUTUSAN (D5)", "Pemisahan jalur berkas dijalankan lebih dulu sebagai langkah "
          "cepat, diikuti janji temu daring sebagai arah jangka menengah."),
         ("EKSEKUSI (D6)", "Satu angka: waktu tunggu rata-rata per hari. Langkah harian: "
          "verifikasi kelengkapan berkas sebelum pasien masuk antrean. Pemicu: saat pasien "
          "mengambil nomor."),
         ("PEMBAKUAN (D7)", "Alur berkas masuk prosedur pendaftaran; tim janji temu dibentuk "
          "dengan pemilik tetap dan tinjauan bulanan."),
         ("HASIL", "Waktu tunggu rata-rata turun menjadi 30 menit dalam enam minggu; kepuasan "
          "pasien melampaui tingkat tertinggi sebelumnya."),
         ("TOOLS UTAMA", "Analisis sebaran, dua akar terpisah, Radar Opsi, langkah cepat + arah "
          "jangka menengah."),
        ]))

    st.append(case_study(
        "7", "UMKM Kuliner", "Omzet naik tiga kali",
        "Konteks \u00b7 satu gerai \u00b7 hasil: omzet 3x dalam setahun",
        [("MASALAH (D2)", "Rata-rata pembelian hanya 1,1 porsi per transaksi, sementara biaya "
          "pengiriman tetap membuat pesanan kecil hampir tidak berlaba. Target: 1,6 porsi."),
         ("AKAR (D3)", "Menu hanya dijual per porsi tunggal; bahan pendamping sering terbuang "
          "karena tidak ada paket yang menggabungkannya."),
         ("OPSI (D4)", "Menaikkan harga; paket bundling; minimum pembelian pengiriman."),
         ("KEPUTUSAN (D5)", "Bundling dipilih karena menyentuh akar tanpa menaikkan harga "
          "satuan yang berisiko mengusir pelanggan."),
         ("EKSEKUSI (D6)", "Satu angka: porsi per transaksi. Langkah harian: menyebutkan paket "
          "bundling dalam satu kalimat. Pemicu: setelah mencatat pesanan."),
         ("PEMBAKUAN (D7)", "Paket masuk daftar menu tetap dan pelatihan singkat untuk staf baru."),
         ("HASIL", "Porsi per transaksi naik dari 1,1 ke 1,9; omzet bulanan naik sekitar tiga "
          "kali tanpa menambah jam kerja."),
         ("TOOLS UTAMA", "Siklus 30 hari, satu angka tunggal, pemicu, tinjauan mingguan."),
        ]))

    st.append(PageBreak())
    st.append(case_study(
        "11", "Keluarga", "Anak kecanduan gawai",
        "Konteks \u00b7 satu keluarga \u00b7 hasil: 5,4\u21921,6 jam",
        color=TEAL,
        sections=[
         ("MASALAH (D2)", "Rata-rata 5,4 jam penggunaan gawai per hari, puncak setelah pulang "
          "sekolah. Target: di bawah 2 jam pada jam tersebut."),
         ("AKAR (D3)", "Dua akar: tidak ada kegiatan yang membuat anak merasa mampu, dan gawai "
          "menjadi satu-satunya ruang kendali dan penerimaan sosial."),
         ("OPSI (D4)", "Memperketat larangan; menambah kegiatan pilihan anak; aturan jam "
          "bersama; mengubah jam makan malam keluarga; bantuan sekolah."),
         ("KEPUTUSAN (D5)", "Kriteria: menjaga hubungan, bukan merusaknya. Yang dipilih: "
          "kegiatan pilihan anak + aturan jam yang disepakati bersama."),
         ("EKSEKUSI (D6)", "Satu angka: jam penggunaan setelah sekolah. Langkah harian: makan "
          "malam bersama tanpa gawai. Pemicu: saat makan malam disiapkan."),
         ("PEMBAKUAN (D7)", "Kesepakatan tertulis ditempel di dapur, ditinjau bulanan bersama anak."),
         ("HASIL", "Penggunaan turun ke 1,6 jam dalam empat bulan; komunikasi keluarga pulih."),
         ("TOOLS UTAMA", "Deteksi berbasis pencatatan, analisis kebutuhan (bukan perilaku), "
          "kriteria yang menjaga hubungan."),
        ]))

    st.append(case_study(
        "12", "Keuangan Pribadi", "Gaji besar tetapi selalu habis",
        "Konteks \u00b7 satu rumah tangga \u00b7 hasil: tabungan 2%\u219218%",
        color=TEAL,
        sections=[
         ("MASALAH (D2)", "Tabungan bulanan hanya 2% dari pendapatan; target minimal 15%."),
         ("AKAR (D3)", "31% pengeluaran berasal dari langganan dan pembelian kecil berulang "
          "yang tidak dirasakan manfaatnya. Keputusan diambil seketika tanpa pagar."),
         ("OPSI (D4)", "Memotong langganan; amplop anggaran; tabungan otomatis di awal bulan; "
          "jeda 24 jam untuk pembelian besar."),
         ("KEPUTUSAN (D5)", "Amplop anggaran + tabungan otomatis + jeda 24 jam dipilih karena "
          "bekerja tanpa menuntut kemauan setiap hari."),
         ("EKSEKUSI (D6)", "Satu angka: persentase tabungan. Langkah harian: catat satu baris, "
          "tiga menit. Pemicu: setelah makan malam."),
         ("PEMBAKUAN (D7)", "Tabungan otomatis berjalan sendiri; tinjauan anggaran setiap "
          "tanggal 1 selama lima belas menit."),
         ("HASIL", "Tabungan naik dari 2% ke 18% dalam lima bulan, dan konflik soal uang menurun."),
         ("TOOLS UTAMA", "Audit pengeluaran, opsi otomatis, pemicu kebiasaan, tinjauan bulanan."),
        ]))

    st.append(PageBreak())
    st.append(case_study(
        "9", "Tim Startup", "Fitur yang gagal dipakai",
        "Konteks \u00b7 8 orang \u00b7 hasil: 6%\u219231%",
        [("MASALAH (D2)", "Hanya 6% pengguna aktif memakai fitur baru lebih dari sekali pada "
          "30 hari pertama. Target: minimal 20%."),
         ("AKAR (D3)", "Fitur dirancang dari daftar keinginan internal, bukan dari pekerjaan "
          "nyata pengguna. Tidak ada anggota tim yang pernah mengamati pengguna."),
         ("OPSI (D4)", "Onboarding baru; menghapus fitur gagal; riset pengguna rutin; "
          "mewajibkan bukti masalah pada setiap usulan fitur."),
         ("KEPUTUSAN (D5)", "Riset pengguna rutin + aturan bukti masalah, diuji pada satu fitur "
          "selama 30 hari."),
         ("EKSEKUSI (D6)", "Satu angka: pemakaian fitur baru. Langkah harian: satu sesi "
          "pengamatan pengguna, 30 menit. Pemicu: setiap Selasa pagi."),
         ("PEMBAKUAN (D7)", "Aturan bukti masalah masuk dokumen proses produk; tinjauan "
          "pemakaian dilakukan bulanan."),
         ("HASIL", "Pemakaian fitur baru naik dari 6% ke 31% dalam enam bulan; jumlah fitur "
          "yang dibatalkan sebelum dibangun juga naik."),
         ("TOOLS UTAMA", "Perumusan bersama, analisis proses, aturan pembakuan."),
        ]))

    st.append(case_study(
        "8", "Jaringan Layanan", "Hasil yang bertahan di 60 cabang",
        "Konteks \u00b7 60 cabang \u00b7 hasil: bertahan dua tahun",
        [("MASALAH (D2)", "Perbaikan berhasil di lima cabang percontohan tetapi tidak menyebar; "
          "cabang lain kembali ke cara lama."),
         ("AKAR (D3)", "Perbaikan hanya hidup dalam pelatihan lisan; tidak ada standar tertulis, "
          "pemilik, dan pengukuran lanjutan."),
         ("OPSI (D4)", "Memperbanyak pelatihan; membuat standar tertulis; menunjuk pengelola "
          "standar; memantau satu angka bulanan."),
         ("KEPUTUSAN (D5)", "Kombinasi standar + pemilik + ritme dipilih karena kecepatan "
          "menyebar ditentukan oleh kekuatan sistem, bukan besarnya perubahan."),
         ("EKSEKUSI (D6)", "Standar satu halaman; setiap cabang punya pemilik; satu angka "
          "dipantau bulanan dengan batas peringatan."),
         ("PEMBAKUAN (D7)", "Rapat tinjauan bulanan tiga puluh menit; standar diperbarui tiap "
          "kuartal; cabang terbaik berbagi cara."),
         ("HASIL", "Perbaikan bertahan di seluruh 60 cabang selama dua tahun, dan muncul "
          "perbaikan lanjutan dari cabang sendiri."),
         ("TOOLS UTAMA", "Standar kerja, Diagram Penggerak, ritme pengukuran dan tinjauan."),
        ]))

    st.append(PageBreak())
    st.append(case_study(
        "2", "Operator Transportasi", "Komplain pengguna terlambat",
        "Konteks \u00b7 3.400 mitra \u00b7 hasil: tunggu turun 34%",
        [("MASALAH (D2)", "Pengaduan tentang waktu tunggu naik 52% dalam satu kuartal. Target: "
          "kembali ke tingkat kuartal sebelumnya."),
         ("AKAR (D3)", "Dua akar: penugasan pesanan tidak memperhitungkan kepadatan wilayah, "
          "dan aplikasi menampilkan estimasi waktu yang selalu sama tanpa memperbarui posisi "
          "mitra terdekat."),
         ("OPSI (D4)", "Menambah mitra; memperbaiki algoritma penugasan; memperbaiki estimasi "
          "waktu; memberi informasi kepada pengguna saat permintaan tinggi."),
         ("KEPUTUSAN (D5)", "Perbaikan estimasi dan informasi dipilih lebih dulu karena paling "
          "cepat dan langsung menyentuh persepsi pengguna; penugasan diperbaiki berikutnya."),
         ("EKSEKUSI (D6)", "Satu angka: selisih antara estimasi dan kedatangan nyata. Langkah "
          "harian: tinjauan cepat anomali tiap pagi. Pemicu: setelah laporan harian masuk."),
         ("PEMBAKUAN (D7)", "Pemantauan selisih estimasi menjadi indikator tetap dengan pemilik "
          "di tim operasi."),
         ("HASIL", "Waktu tunggu rata-rata turun 34%, dan pengaduan turun sampai di bawah "
          "tingkat awal. Pelajaran penting: sebagian keluhan datang dari ketidaksesuaian "
          "ekspektasi, bukan dari kecepatan semata."),
         ("TOOLS UTAMA", "Pemisahan persepsi dan kenyataan, perbaikan bertahap."),
        ]))

    st.append(case_study(
        "3", "Tim Teknologi", "Fitur baru tidak dipakai pengguna",
        "Konteks \u00b7 12 orang \u00b7 hasil: pemakaian 4%\u219214%",
        [("MASALAH (D2)", "Pemakaian fitur baru hanya 4% dari pengguna aktif. Target minimal 20%."),
         ("AKAR (D3)", "Fitur diletakkan tiga lapis di dalam menu, dan pengguna tidak tahu "
          "masalah apa yang ia selesaikan."),
         ("OPSI (D4)", "Memindahkan posisi fitur; menulis penjelasan manfaat; menampilkan "
          "petunjuk saat relevan; memanggil pengguna untuk riset."),
         ("KEPUTUSAN (D5)", "Memindahkan posisi dan menampilkan petunjuk saat relevan dipilih, "
          "diuji pada dua kelompok pengguna."),
         ("EKSEKUSI (D6)", "Satu angka: persentase pengguna yang menemukan fitur dalam 7 hari. "
          "Langkah harian: pantau jalur klik pertama pengguna baru."),
         ("PEMBAKUAN (D7)", "Aturan: setiap fitur baru diuji pada lima pengguna sebelum rilis, "
          "dan dipastikan dapat ditemukan dalam dua kali klik."),
         ("HASIL", "Pemakaian naik dari 4% menjadi 14% dalam delapan minggu, tanpa perubahan "
          "pada fitur itu sendiri."),
         ("TOOLS UTAMA", "Uji kecil, pengukuran perilaku, aturan pembakuan."),
        ]))

    st.append(PageBreak())
    st.append(case_study(
        "6", "Instansi Layanan Publik", "Waktu tunggu turun 41%",
        "Konteks \u00b7 14 kantor \u00b7 hasil: keputusan berani yang terbukti",
        [("MASALAH (D2)", "Waktu tunggu rata-rata 96 menit, dengan puncak di tiga kantor "
          "mencapai 140 menit. Target: di bawah 60 menit."),
         ("AKAR (D3)", "Pendaftaran dan penjadwalan tidak tersinkron; dan 38% kunjungan "
          "sebenarnya bisa diselesaikan tanpa kehadiran."),
         ("OPSI (D4)", "Menambah petugas; menambah loket; memindahkan sebagian layanan ke "
          "saluran tanpa tatap muka; janji temu."),
         ("KEPUTUSAN (D5)", "Kriteria ditetapkan lebih dulu: dampak, anggaran, kecepatan, "
          "risiko. Saluran tanpa tatap muka dan janji temu menang."),
         ("EKSEKUSI (D6)", "Satu angka: waktu tunggu rata-rata per hari per kantor. Langkah "
          "harian: memastikan saluran daring berjalan dan memantau permintaan tertunda."),
         ("PEMBAKUAN (D7)", "Standar layanan daring masuk prosedur resmi; angka dipantau "
          "bulanan; kantor terbaik berbagi praktik."),
         ("HASIL", "Waktu tunggu turun 41% dalam satu kuartal, dan jumlah kunjungan turun "
          "karena orang memakai saluran tanpa tatap muka."),
         ("TOOLS UTAMA", "Kriteria sebelum penilaian, penghapusan langkah tak bernilai."),
        ]))

    st.append(case_study(
        "10", "UMKM Retail", "Stok menumpuk dan kas tertekan",
        "Konteks \u00b7 dua toko \u00b7 hasil: perputaran stok naik 2,3x",
        [("MASALAH (D2)", "Perputaran stok 1,1 kali per tahun dengan 22% modal tertahan pada "
          "barang lambat terjual. Target: perputaran di atas 2,5 kali."),
         ("AKAR (D3)", "Pembelian berdasarkan diskon pemasok, bukan berdasarkan kecepatan "
          "terjual; tidak ada pencatatan barang lambat."),
         ("OPSI (D4)", "Menghentikan pembelian diskon besar-besaran; mencatat kecepatan "
          "terjual; memberi diskon untuk barang lambat; mengubah syarat pembelian."),
         ("KEPUTUSAN (D5)", "Pencatatan kecepatan terjual dan penghentian pembelian impulsif "
          "dipilih lebih dulu."),
         ("EKSEKUSI (D6)", "Satu angka: jumlah barang yang tidak bergerak lebih dari 60 hari. "
          "Langkah harian: menempel label tanggal pada barang baru. Pemicu: saat menerima "
          "barang kiriman."),
         ("PEMBAKUAN (D7)", "Aturan pembelian baru: tidak ada pembelian tanpa melihat kecepatan "
          "terjual enam bulan terakhir."),
         ("HASIL", "Perputaran stok naik menjadi 2,3 kali, dan modal yang tertahan turun dari "
          "22% menjadi 9% dalam lima bulan."),
         ("TOOLS UTAMA", "Analisis Pareto, aturan pembelian, pemicu harian."),
        ]))

    from content import program
    st += program.build()

    from content import appendix
    st += appendix.build()

    # =================================================================
    #  DAFTAR PUSTAKA
    # =================================================================
    st.append(PageBreak())
    st.append(H("Daftar Pustaka & Sumber Ilmiah", S["h2"], level=2, key="pustaka"))
    st += render("""
Buku ini berdiri di atas tradisi panjang. Daftar berikut dikelompokkan berdasarkan asal gagasan, supaya kamu bisa menelusuri lebih dalam bagian yang paling menarik bagimu.
""")
    st.append(tool_table(
        ["Tema", "Sumber & aliran pemikiran", "Yang diambil buku ini"],
        [["Perbaikan berkelanjutan",
          "Tradisi manajemen kualitas dan perbaikan proses yang berakar pada sistem produksi "
          "modern, termasuk gagasan standar kerja dan siklus perbaikan.",
          "Siklus perbaikan, standar kerja, gagasan bahwa tanpa standar tidak ada dasar "
          "memperbaiki."],
         ["Analisis akar masalah",
          "Metode pertanyaan berulang dan diagram sebab-akibat yang lazim dalam bidang mutu "
          "dan keselamatan kerja.",
          "5 Whys, diagram tulang ikan, dan disiplin verifikasi akar dengan data."],
         ["Pengambilan keputusan",
          "Riset tentang penilaian dan pilihan, termasuk gagasan kriteria berbobot dan "
          "penghindaran penetapan dini.",
          "Matriks keputusan, Kartu Keputusan, aturan menetapkan kriteria sebelum menilai."],
         ["Psikologi kognitif",
          "Kajian tentang bias penilaian dan pengaruh sosial pada penilaian, termasuk "
          "konformitas dan polarisasi kelompok.",
          "Peta enam jebakan kognitif dan cara memasang rem."],
         ["Psikologi kebiasaan & tujuan",
          "Riset penetapan tujuan dan pembentukan kebiasaan, termasuk peran umpan balik dan "
          "pemicu perilaku.",
          "Siklus 30 hari, satu angka tunggal, pemicu, aturan dua hari."],
         ["Desain & kreativitas",
          "Teknik berpikir kreatif dan pemisahan tahap menghasilkan ide dari tahap menilai.",
          "SCAMPER, Radar Opsi, aturan tiga opsi minimum."],
         ["Praktik konsultan & fasilitasi",
          "Pendekatan fasilitasi kelompok, peran penantang, dan kerja berbasis lembar kerja "
          "yang dirancang untuk dipakai di lapangan.",
          "Peran tim, agenda rapat 7D, panduan workshop satu hari."]],
        [0.22, 0.42, 0.36]))
    st.append(caption("Catatan. Buku ini menyajikan kerangka kerja yang dapat dipakai langsung. "
                      "Untuk penelusuran akademis, telusuri tema di kolom pertama dan gunakan istilah "
                      "kunci seperti continuous improvement, root cause analysis, decision analysis, "
                      "cognitive bias, habit formation, dan group facilitation."))

    # =================================================================
    #  INDEKS TOOLS
    # =================================================================
    st.append(PageBreak())
    st.append(H("Indeks Alat: TUNTAS 7D", S["h2"], level=2, key="indeks"))
    st += render("""
Semua alat dalam buku ini dikumpulkan di satu tempat untuk memudahkan pencarian ketika kamu sedang bekerja.
""")
    st.append(tool_table(
        ["Alat", "Langkah", "Kegunaan", "Halaman"],
        [["Kanvas Deteksi Sinyal", "D1", "Mengenali masalah dengan benar dan berangka", "WS-D1"],
         ["Uji tiga lapis", "D1", "Memisahkan gejala, masalah, dan akar", "Bab 3"],
         ["Kanvas Rumus Masalah", "D2", "Menajamkan kalimat masalah", "WS-D2"],
         ["Uji PROBLEM", "D2", "Memeriksa kelengkapan rumusan", "Bab 4"],
         ["Lima Pertanyaan Kenapa", "D3", "Menemukan akar secara berurutan", "Bab 5"],
         ["Diagram Tulang Ikan", "D3", "Menampung semua dugaan sebab", "Bab 5"],
         ["Analisis Pareto", "D3", "Memilih akar paling berdampak", "Bab 5"],
         ["Rute Empat Arah", "D4", "Membuka opsi dari kebuntuan", "Bab 6"],
         ["SCAMPER", "D4", "Memaksa ide baru muncul", "Bab 6"],
         ["Radar Opsi", "D4", "Memetakan dampak dan kesulitan", "Bab 6"],
         ["Matriks Keputusan", "D5", "Memilih dengan kriteria berbobot", "Bab 7"],
         ["Kartu Keputusan", "D5", "Menyimpan alasan dan rencana cadangan", "WS-D5"],
         ["Kanvas Eksekusi 30 Hari", "D6", "Mengubah rencana menjadi langkah harian", "WS-D6"],
         ["Uji Kecil", "D6", "Belajar tanpa mempertaruhkan seluruh sumber daya", "Bab 8"],
         ["Diagram Penggerak", "D7", "Memastikan hasil tidak terkikis", "Bab 9"],
         ["Standar Kerja Satu Halaman", "D7", "Membakukan cara baru", "WS-D7"],
         ["Peta Pembakuan", "D7", "Menetapkan pemilik dan ritme", "WS-D7"],
         ["Lembar Fasilitator", "Bab 12", "Menjalankan workshop satu hari", "WS-FAS"]],
        [0.34, 0.12, 0.42, 0.12]))

    # =================================================================
    #  TOOLKIT DIGITAL
    # =================================================================
    st.append(PageBreak())
    st.append(H("Akses Toolkit Digital", S["h2"], level=2, key="toolkit"))
    st += render("""
Semua worksheet, template, dan kartu langkah dalam buku ini tersedia dalam bentuk digital yang bisa dicetak, diisi di layar, atau dipakai di papan tulis digital. Gunakan kode QR atau tautan berikut.
""")
    st.append(QRPanel("https://tuntas7d.id/toolkit", "Toolkit Utama",
                      "Semua worksheet TUNTAS 7D, template, dan kartu langkah",
                      "QR-TOOLKIT"))
    st.append(sp(4))
    st.append(tool_table(
        ["Sumber daya", "Isi", "Tautan"],
        [["Toolkit D1\u2013D7", "Worksheet langkah, contoh terisi, lembar data", "tuntas7d.id/toolkit/d1 \u2026 d7"],
         ["Paket Workshop", "Agenda, slide, kartu peran, sertifikat", "tuntas7d.id/toolkit/workshop"],
         ["Papan Digital", "Versi papan tulis digital untuk kerja tim", "tuntas7d.id/papan"],
         ["Kartu Saku", "Ringkasan tujuh langkah, ukuran saku", "tuntas7d.id/kartu"],
         ["Studi Kasus Lengkap", "Dua belas kasus dengan data contoh", "tuntas7d.id/kasus"]],
        [0.26, 0.44, 0.30]))
    st.append(callout("practice", "Cara memulai dalam sepuluh menit", [
        para("Unduh Kanvas Deteksi Sinyal. Ambil satu masalah yang paling mengganggu minggu ini. "
             "Isi enam kotaknya. Simpan lembar itu di tempat yang kamu lihat setiap hari. "
             "Sisanya akan mengikuti."),
    ]))

    # =================================================================
    #  TENTANG PENULIS
    # =================================================================
    st.append(PageBreak())
    st.append(H("Tentang Penulis", S["h2"], level=2, key="penulis"))
    st += render("""
Buku ini disusun berdasarkan pola yang berulang di ruang perbaikan pabrik, ruang rapat manajemen, ruang layanan publik, ruang kelas, dan ruang keluarga. Ia lahir dari satu keyakinan sederhana: cara menyelesaikan masalah bisa dipelajari, dan cara terbaiknya bisa dipinjam dari siapa pun yang sudah membuktikannya.

Melalui TUNTAS Press, kerangka ini dikembangkan bersama praktisi perbaikan proses, fasilitator workshop, dan pelatih kepemimpinan di berbagai bidang. Fokusnya satu: membuat cara berpikir yang biasanya hanya dipakai konsultan menjadi alat sehari-hari yang bisa dipakai siapa saja, dengan kertas dan pensil.

Buku ini adalah bagian pertama dari rangkaian TUNTAS 7D. Versi lanjutan akan membahas penerapan pada skala organisasi besar, pengukuran dampak, dan pembentukan budaya perbaikan.
""")
    st.append(sp(4))
    st.append(rule())
    st.append(para("<b>TUNTAS PRESS</b> \u00b7 Buku kerja praktis untuk perbaikan yang tuntas.", "caption"))
    st += render("""
#### Ajakan untuk pembaca

Kalau buku ini berguna bagimu, ajarkan kepada satu orang. Tulisan yang paling hidup adalah tulisan yang dipakai. Kami akan senang mendengar bagaimana tujuh langkah ini bekerja di masalahmu, dan bagaimana ia bisa diperbaiki.

Kirimkan ceritamu, pertanyaanmu, atau usulan perbaikan untuk edisi berikutnya melalui portal yang sama dengan toolkit digital.
""")

    st.append(PageBreak())
    st.append(H("Catatan Perjalananmu", S["h2"], level=2, key="catatan"))
    st += render("""
Sebelum menutup buku ini, sisihkan sepuluh menit untuk menulis. Bukan ringkasan bab, melainkan janji pada dirimu sendiri.

#### Tiga hal yang berubah dalam cara saya menyelesaikan masalah

Satu kalimat untuk setiap hal. Tulis yang paling terasa, bukan yang paling terdengar pintar.
""")
    st.append(worksheet_block(
        "NOTES", "Catatan Perjalananmu", "Disimpan sebagai rujukan enam bulan dari sekarang",
        [{"label": "1. Hal yang paling mengubah cara saya berpikir", "lines": 3},
         {"label": "2. Langkah 7D yang paling sulit untuk saya, dan mengapa", "lines": 3},
         {"label": "3. Kebiasaan kecil yang akan saya pertahankan", "lines": 3},
         {"label": "Masalah berikutnya yang akan saya kerjakan dengan tujuh langkah",
          "lines": 3},
         {"label": "Satu orang yang akan saya ajarkan cara ini", "lines": 2},
         ("note", "Tulis tanggal hari ini di bawah, lalu simpan halaman ini. Enam bulan "
                  "dari sekarang, buka kembali dan lihat apa yang bertahan.")],
    ))

    st.append(PageBreak())
    st.append(H("Lembar Kerja Cepat: Satu Halaman untuk Satu Masalah", S["h2"],
                level=2, key="lembar-cepat"))
    st += render("""
Ketika kamu sudah terbiasa, seluruh tujuh langkah bisa dimuat dalam satu halaman. Pakai lembar ini untuk masalah sehari-hari yang tidak membutuhkan analisis panjang. Fotokopi halaman ini dan simpan beberapa lembar di meja kerjamu.
""")
    st.append(worksheet_block(
        "QUICK", "Satu Halaman untuk Satu Masalah", "Versi ringkas tujuh langkah",
        [{"label": "D1 \u00b7 Apa yang sebenarnya terjadi? Angka & sebarannya", "lines": 2},
         {"label": "D2 \u00b7 Satu kalimat masalah (bagian, angka, target)", "lines": 2},
         {"label": "D3 \u00b7 Dugaan akar & cara mengujinya", "lines": 3},
         {"label": "D4 \u00b7 Tiga opsi yang tersedia", "lines": 3},
         {"label": "D5 \u00b7 Pilihan & alasannya", "lines": 2},
         {"label": "D6 \u00b7 Langkah pertama besok & angka yang dipantau", "lines": 2},
         {"label": "D7 \u00b7 Cara menjaga hasilnya", "lines": 2}],
    ))
    st.append(keyline("Tujuh langkah, satu halaman, satu masalah. Mulai dari yang kecil, hari ini."))

    # The back cover starts a fresh page with the full-bleed opener template;
    # NextPageTemplate applies once the next page begins, so a single break is
    # enough (a second one would leave an empty body page in between).
    st.append(NextPageTemplate("opener"))
    st.append(PageBreak())
    from frontmatter import BackCoverPage
    st.append(BackCoverPage())
    return st
