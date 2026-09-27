"""Deep-dive supplements that thicken each TUNTAS 7D step chapter.

Each block adds: pertanyaan pemandu, kesalahan umum, contoh pengisian lengkap,
latihan drill, cheat sheet, dan satu mini case. Inserted before the worksheet.
"""
from reportlab.platypus import PageBreak, KeepTogether, Spacer

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (tool_table, caption, callout, keyline, case_study,
                        worksheet_block, WriteLines, rule, StatRow)

S = styles()


def _q(title, items):
    """A checklist of guiding questions."""
    out = [H(title, S["h3"], level=3, register=False)]
    stl = S["bullet"]
    for it in items:
        out.append(para(it, "bullet"))
    return out


def _mini(num, org, title, meta, sections, color=NAVY):
    return case_study(num, org, title, meta, sections, color=color, tag="MINI KASUS")


def build(code):
    fn = _BUILDERS.get(code)
    return fn() if fn else []


# =====================================================================
#  D1
# =====================================================================
def _d1():
    st = [PageBreak()]
    st.append(H("Pendalaman D1: Peta Pertanyaan Deteksi", S["h3"], level=3,
                register=False))
    st += render("""
Gunakan daftar pertanyaan berikut ketika kamu memeriksa sebuah laporan. Tujuannya bukan menghabiskan pertanyaan, tetapi memastikan tidak ada sudut yang terlewat.
""")
    st += _q("Pertanyaan tentang ukuran", [
        "Angka berapa yang mewakili masalah ini hari ini, dan siapa yang mengukurnya?",
        "Apakah angka itu rata-rata, total, atau puncak? Ketiganya bercerita berbeda.",
        "Seberapa besar variasi antar hari, antar lokasi, atau antar orang?",
        "Apakah ada periode di mana masalah ini tidak terjadi sama sekali? Kenapa?",
        "Kalau masalah ini hilang besok, angka mana yang paling pertama berubah?",
    ])
    st += _q("Pertanyaan tentang manusia", [
        "Siapa yang paling dulu merasakan masalah ini?",
        "Siapa yang paling terdampak, dan siapa yang paling tidak menyadarinya?",
        "Apakah keluhan datang dari satu kelompok saja, atau merata?",
        "Apa yang orang lakukan untuk mengakali masalah ini setiap hari?",
    ])
    st += _q("Pertanyaan tentang waktu", [
        "Sejak kapan masalah ini ada? Apa yang berubah saat itu?",
        "Apakah masalah ini memburuk, stabil, atau berulang?",
        "Apakah ada pola harian, mingguan, atau musiman?",
    ])
    st += _q("Pertanyaan tentang batas", [
        "Bagian mana dari masalah ini yang berada dalam kendali kita?",
        "Apa yang sengaja tidak kita masukkan, dan mengapa?",
        "Kapan kita akan menyatakan masalah ini selesai?",
    ])

    st.append(PageBreak())
    st.append(H("Empat pola sebaran yang paling sering menipu", S["h3"], level=3,
                register=False))
    st += render("""
Rata-rata tunggal menyembunyikan empat bentuk sebaran berikut. Kenali bentuknya, dan diagnosismu akan langsung lebih tajam.
""")
    st.append(tool_table(
        ["Pola", "Ciri", "Apa artinya", "Cara memeriksa"],
        [["Menumpuk di waktu", "Puncak tajam pada jam tertentu", "Masalah kapasitas, bukan kecepatan",
          "Pecah data per jam"],
         ["Menumpuk di tempat", "Satu lokasi jauh lebih buruk", "Masalah lokal, bukan sistemik",
          "Pecah data per lokasi"],
         ["Dua puncak", "Ada dua kelompok, bukan satu", "Mungkin ada dua akar berbeda",
          "Pecah data per jenis atau per segmen"],
         ["Ekor panjang", "Sebagian kecil kasus sangat ekstrem", "Beban terbesar dari sedikit kasus",
          "Urutkan dan lihat 10% terburuk"]],
        [0.18, 0.24, 0.28, 0.30]))
    st.append(callout("insight", "Aturan pecah data", [
        para("Sebelum menganalisis lebih dalam, pecah data paling tidak berdasarkan tiga hal: "
             "waktu, tempat, dan jenis. Tiga pemecahan ini menyelesaikan lebih banyak teka-teki "
             "daripada teknik statistik yang rumit."),
    ]))

    st.append(PageBreak())
    st.append(H("Contoh pengisian lengkap: layanan pelanggan", S["h3"], level=3,
                register=False))
    st.append(tool_table(
        ["Kotak kanvas", "Pengisian nyata"],
        [["1. Sinyal awal", "Tiga pelanggan besar mengeluh tentang respons lambat dalam dua minggu"],
         ["2. Sumber sinyal", "Pelanggan besar, disampaikan lewat telepon ke tim penjualan"],
         ["3. Ukuran sekarang", "Rata-rata waktu balasan pertama: 14 jam 20 menit"],
         ["4. Ukuran tujuan", "Rata-rata di bawah 4 jam, puncak di bawah 8 jam"],
         ["5. Sebaran", "Puncak pada Senin pagi (rata-rata 31 jam) dan pada akhir bulan (18 jam). "
                        "Pada hari lain hanya 6 jam. Terkonsentrasi pada tiket berlabel teknis."],
         ["6. Bukti yang hilang", "Distribusi beban tiket per jam, keterampilan tiap petugas, "
                                  "alokasi jam kerja per label"]],
        [0.24, 0.76]))
    st += render("""
Perhatikan bagaimana pengisian kotak kelima langsung menyempitkan ruang pencarian. Setelah sebarannya terlihat, pertanyaannya berubah dari "bagaimana mempercepat balasan" menjadi "apa yang istimewa pada Senin pagi dan akhir bulan". Pertanyaan kedua jauh lebih mungkin dijawab.

#### Empat kesalahan umum di D1 dan cara memperbaikinya

| Kesalahan | Gejalanya | Perbaikan |
|---|---|---|
| Menamai masalah terlalu dini | Semua orang sudah sepakat sebelum data ada | Tulis sinyal apa adanya, jangan beri nama |
| Puas pada satu rata-rata | Tidak ada angka minimum, puncak, atau sebaran | Hitung rata-rata, puncak, dan sebaran |
| Sumber tunggal | Semua informasi dari satu orang atau satu rapat | Cari minimal tiga sumber berbeda |
| Menunggu data lengkap | Pekerjaan tertunda berminggu-minggu | Mulai dengan 70% data yang relevan |
""")

    st.append(PageBreak())
    st.append(H("Latihan drill D1: tiga menit per laporan", S["h3"], level=3,
                register=False))
    st += render("""
Latihan ini bisa dilakukan sendiri setiap hari. Ambil satu laporan atau keluhan yang kamu dengar hari ini, lalu kerjakan tiga langkah ini dalam tiga menit.
""")
    st.append(tool_table(
        ["Menit", "Tindakan", "Contoh"],
        [["1", "Tulis keluhan apa adanya, tanpa memperbaiki bahasa", "\"Laporan sering telat\""],
         ["2", "Ubah menjadi angka, walau perkiraan kasar", "\"7 dari 20 laporan lewat tenggat, 3 hari rata-rata\""],
         ["3", "Sebutkan satu tempat, waktu, atau kelompok", "\"Terjadi pada laporan cabang timur, akhir bulan\""]],
        [0.12, 0.50, 0.38]))
    st.append(callout("practice", "Kerjakan sekarang", [
        para("Pilih satu keluhan yang kamu dengar dalam dua puluh empat jam terakhir. "
             "Jalankan tiga langkah di atas. Bandingkan hasilnya dengan cara kamu biasanya "
             "menanggapi keluhan. Perhatikan bedanya."),
        WriteLines(4),
    ]))
    return st


# =====================================================================
#  D2
# =====================================================================
def _d2():
    st = [PageBreak()]
    st.append(H("Pendalaman D2: Bank Kalimat Masalah", S["h3"], level=3,
                register=False))
    st += render("""
Salah satu cara tercepat belajar merumuskan masalah adalah melihat contoh. Perhatikan bagaimana kalimat kabur di kolom kiri diubah menjadi kalimat yang bisa diuji di kolom kanan.
""")
    st.append(tool_table(
        ["Kalimat kabur", "Kalimat tajam"],
        [["\"Kualitas produk menurun\"",
          "\"Tingkat keluhan cacat naik dari 1,2% ke 3,4% pada produk seri B dalam lima bulan. "
          "Target: di bawah 1,5%.\""],
         ["\"Karyawan kurang termotivasi\"",
          "\"Pengunduran diri sukarela naik dari 8% ke 19% per tahun pada divisi operasi, "
          "sebagian besar pada karyawan dengan masa kerja 6\u201312 bulan. Target: di bawah 12%.\""],
         ["\"Sistem sering lambat\"",
          "\"Waktu buka halaman transaksi melewati 5 detik pada 12% transaksi, dengan puncak "
          "pada pukul 11.00\u201313.00. Target: di bawah 2% di atas 3 detik.\""],
         ["\"Komunikasi tim buruk\"",
          "\"Dari 30 serah terima pekerjaan antartim dalam sebulan, 11 mengalami perbaikan ulang "
          "karena ketentuan yang tidak jelas. Target: di bawah 3.\""],
         ["\"Pengeluaran terlalu besar\"",
          "\"Biaya operasional per unit naik 17% dua kuartal berturut-turut, terutama pada "
          "biaya pengiriman. Target: kembali ke tingkat enam bulan lalu.\""]],
        [0.34, 0.66]))

    st.append(PageBreak())
    st.append(H("Kalimat masalah kosong: isi sendiri", S["h3"], level=3,
                register=False))
    st += render("""
Gunakan kerangka berikut. Isi bagian dalam tanda kurung dengan masalahmu, lalu baca ulang. Kalau ada satu bagian yang terasa mengambang, itu tanda kamu masih perlu kembali ke D1.
""")
    st.append(callout("tool", "Kerangka kalimat masalah", [
        para("Pada <b>(bagian mana persisnya)</b>, <b>(ukuran)</b> saat ini sebesar "
             "<b>(angka)</b>, sementara <b>(sejak kapan)</b>. Target kami <b>(angka target)</b> "
             "karena <b>(pembanding atau alasan)</b>. Bila dibiarkan, akibatnya "
             "<b>(konsekuensi berangka)</b>. Pemilik masalah: <b>(satu nama)</b>."),
    ]))
    st += render("""
#### Contoh mengisi kerangka
""")
    st.append(tool_table(
        ["Kolom", "Contoh 1 \u2014 layanan", "Contoh 2 \u2014 produksi"],
        [["Bagian persisnya", "Pendaftaran pasien baru", "Lini pengemasan malam"],
         ["Ukuran & angka", "Waktu proses 22 menit", "Downtime 6,4% dari jam kerja"],
         ["Sejak kapan", "tiga bulan terakhir", "sejak mesin diganti"],
         ["Target", "12 menit", "di bawah 2%"],
         ["Alasan target", "tingkat cabang pembanding", "standar pabrik lama"],
         ["Konsekuensi", "antrean menumpuk 40 orang", "kehilangan 180 unit per malam"],
         ["Pemilik", "Kepala pendaftaran", "Kepala produksi malam"]],
        [0.24, 0.38, 0.38]))

    st.append(PageBreak())
    st.append(H("Empat kesalahan umum di D2", S["h3"], level=3, register=False))
    st.append(tool_table(
        ["Kesalahan", "Gejala", "Perbaikan"],
        [["Kata sifat lolos", "Ada kata \"lambat\", \"buruk\", \"kurang\"",
          "Ganti setiap kata sifat dengan angka"],
         ["Cakupan terlalu luas", "\"Semua pengguna\", \"seluruh proses\"",
          "Persempit sampai satu kelompok atau satu tahap"],
         ["Ada kata \"dan\" berlebihan", "Satu kalimat memuat tiga masalah",
          "Pecah menjadi masalah terpisah, urutkan"],
         ["Tidak ada target", "Tidak tahu kapan selesai",
          "Tetapkan angka target dan alasannya"]],
        [0.22, 0.36, 0.42]))
    st.append(callout("insight", "Uji ulang di depan orang lain", [
        para("Tunjukkan kalimat masalahmu kepada satu orang yang tidak tahu konteksnya. Kalau "
             "ia bisa menebak dengan benar apa yang akan kamu perbaiki dan bagaimana caranya "
             "mengukur keberhasilan, kalimatmu tajam. Kalau ia bertanya balik, kalimatmu masih "
             "kabur."),
    ]))
    st.append(_mini(
        "M1", "Divisi Penjualan", "Satu kalimat yang mengubah arah seluruh kuartal",
        "Pendalaman D2",
        [("PERUMUSAN AWAL", "\"Angka penjualan harus dinaikkan.\""),
         ("MENGAPA GAGAL", "Tidak ada ukuran, tidak ada cakupan, tidak ada batas. Setiap "
          "orang menafsirkan target dengan caranya sendiri."),
         ("PERUMUSAN BARU", "\"Penjualan produk langganan, yang berulang tiap bulan, stagnan "
          "di 210 unit per bulan selama lima bulan. Target: 260 unit dalam dua kuartal.\""),
         ("AKIBAT PERUBAHAN", "Tim berhenti berdebat soal target umum dan mulai memeriksa "
          "kenapa pelanggan lama berhenti berlangganan."),
         ("HASIL", "Ditemukan bahwa 40% pelanggan berhenti pada bulan ketiga karena tidak "
          "mendapat penjelasan penggunaan. Satu panduan singkat dan satu panggilan lanjutan "
          "mengangkat penjualan berulang ke 268 unit."),
         ("PELAJARAN", "Kata 'penjualan' kabur. Kata 'penjualan produk langganan per bulan' "
          "langsung menunjuk ke tempat yang harus diperiksa."),
        ]))
    return st


# =====================================================================
#  D3
# =====================================================================
def _d3():
    st = [PageBreak()]
    st.append(H("Pendalaman D3: Tiga Cara Memverifikasi Akar", S["h3"], level=3,
                register=False))
    st += render("""
Akar yang tidak diverifikasi hanyalah cerita yang lebih panjang. Ada tiga cara memeriksanya, dari yang paling lemah sampai paling kuat.
""")
    st.append(tool_table(
        ["Cara", "Bagaimana", "Kekuatan", "Catatan"],
        [["Pemeriksaan data", "Cari pola di data yang mendukung akar", "Sedang",
          "Cepat, tetapi bisa terkecoh korelasi"],
         ["Perbandingan", "Bandingkan unit yang bermasalah dengan yang tidak",
          "Kuat", "Sangat ampuh bila ada pembanding alami"],
         ["Uji matikan", "Hilangkan akar sementara, lihat apakah masalah berkurang",
          "Terkuat", "Butuh keberanian, tetapi paling yakinkan"],
         ["Uji nyalakan", "Perkenalkan akar pada unit yang sehat, lihat apakah muncul masalah",
          "Kuat", "Berguna bila mematikan akar berisiko"]],
        [0.18, 0.40, 0.16, 0.26]))
    st.append(callout("insight", "Aturan pembanding", [
        para("Selalu cari pembanding. Unit yang bermasalah hampir selalu punya kembaran yang "
             "sehat. Perbedaan antara keduanya sering langsung menunjukkan akar masalah, "
             "tanpa perlu analisis yang rumit."),
    ]))

    st.append(PageBreak())
    st.append(H("Bank 5 Whys: contoh untuk berbagai bidang", S["h3"], level=3,
                register=False))
    st.append(tool_table(
        ["Bidang", "Gejala", "Rantai kenapa", "Akar"],
        [["Layanan", "Komplain naik", "Balasan lambat \u2192 tiket menumpuk \u2192 tidak ada "
          "pembagian label \u2192 semua tiket masuk satu antrean", "Alur tiket tidak dipecah"],
         ["Produksi", "Cacat goresan", "Komponen bergesekan \u2192 baki lepas \u2192 klip aus "
          "\u2192 cara bersih lama \u2192 prosedur tak diperbarui", "Prosedur kedaluwarsa"],
         ["Kesehatan", "Pasien tidak kontrol", "Pasien tidak datang \u2192 mengira perawatan "
          "gagal \u2192 sensitivitas tak dijelaskan \u2192 tidak ada informasi pasca perawatan",
          "Informasi pasien tidak lengkap"],
         ["Pendidikan", "Kelas tidak aktif", "Siswa diam \u2192 takut salah \u2192 jawaban "
          "salah dikoreksi di depan \u2192 tidak ada ruang mencoba", "Cara umpan balik"],
         ["Rumah tangga", "Uang habis", "Pengeluaran tak terasa \u2192 langganan berulang "
          "\u2192 diputuskan seketika \u2192 tidak ada pagar anggaran", "Keputusan tanpa pagar"]],
        [0.14, 0.16, 0.46, 0.24]))

    st.append(PageBreak())
    st.append(H("Empat kesalahan umum di D3", S["h3"], level=3, register=False))
    st.append(tool_table(
        ["Kesalahan", "Gejala", "Perbaikan"],
        [["Akar berupa nama orang", "\"Kurang teliti\", \"kurang peduli\"",
          "Tanya: proses apa yang membuat ketelitian sulit?"],
         ["5 Whys tanpa data", "Jawaban berupa dugaan, bukan fakta",
          "Setiap jawaban harus bisa diperiksa"],
         ["Mencari satu akar tunggal", "Analisis berhenti setelah satu jawaban",
          "Cari dua sampai tiga akar, lalu urutkan"],
         ["Akar di luar kendali", "\"Pasar lesu\", \"kebijakan pusat\"",
          "Cari akar yang bisa kamu pengaruhi"]],
        [0.24, 0.34, 0.42]))
    st.append(_mini(
        "M2", "Sekolah Menengah", "Kelas yang tidak aktif",
        "Pendalaman D3",
        [("GEJALA", "Guru melaporkan siswa jarang bertanya dan jarang berpendapat. Rencana "
          "awal: menambah tugas agar siswa terbiasa."),
         ("AKAR (5 WHYS)", "Kenapa siswa diam? Takut salah. Kenapa takut? Kesalahan sering "
          "ditanggapi dengan koreksi di depan kelas. Kenapa begitu? Guru mengejar waktu agar "
          "semua materi tersampaikan. Kenapa? Tidak ada ruang mengeksplorasi dalam rencana "
          "pelajaran."),
         ("VERIFIKASI", "Dua kelas diberi perlakuan berbeda selama tiga minggu. Kelas yang "
          "menerima umpan balik tertulis dan kesempatan mencoba tanpa nilai mengalami kenaikan "
          "jumlah interaksi empat kali lipat."),
         ("PELAJARAN", "Akar masalah perilaku hampir selalu ada di rancangan kegiatan, bukan "
          "pada kemauan orang."),
        ]))
    return st


# =====================================================================
#  D4
# =====================================================================
def _d4():
    st = [PageBreak()]
    st.append(H("Pendalaman D4: Tiga Puluh Pertanyaan Perancangan", S["h3"],
                level=3, register=False))
    st += render("""
Ketika ide mandek, jangan menunggu inspirasi. Baca daftar ini dan jawab satu per satu. Satu pertanyaan biasanya cukup untuk membuka jalan.
""")
    st.append(tool_table(
        ["Kategori", "Pertanyaan"],
        [["Menghilangkan", "Bagian mana yang bisa dihapus tanpa mengurangi hasil? Langkah mana "
          "yang ada hanya karena kebiasaan? Apakah semua persetujuan ini perlu?"],
         ["Menggabungkan", "Dua langkah mana yang bisa disatukan? Dua formulir mana yang "
          "menanyakan hal sama? Dua tim mana yang bisa berbagi alat?"],
         ["Mengubah urutan", "Apa yang terjadi kalau langkah terakhir dipindah ke depan? "
          "Kalau pemeriksaan dilakukan lebih awal, apakah cacat bisa dicegah?"],
         ["Memindahkan", "Siapa yang paling tepat mengerjakan bagian ini? Apakah orang yang "
          "mengerjakannya sekarang memang yang paling dekat dengan masalah?"],
         ["Mengubah aturan", "Aturan mana yang dibuat untuk kondisi yang sudah berubah? Batas "
          "mana yang dulu masuk akal tetapi sekarang menghambat?"],
         ["Memakai ulang", "Sumber daya menganggur apa yang bisa dipakai? Bagian mana yang "
          "sudah pernah diselesaikan tim lain?"],
         ["Menyederhanakan", "Bagaimana bentuknya kalau harus selesai dalam seperempat sumber "
          "daya? Apa versi paling sederhana yang masih menyentuh akar?"]],
        [0.20, 0.80]))

    st.append(PageBreak())
    st.append(H("Cara menjalankan sesi perancangan 45 menit", S["h3"], level=3,
                register=False))
    st.append(tool_table(
        ["Menit", "Tahap", "Aturan"],
        [["0\u20135", "Tulis akar masalah di papan", "Semua melihat akar yang sama"],
         ["5\u201325", "Hasilkan ide tanpa menilai", "Tidak boleh ada \"tidak mungkin\""],
         ["25\u201335", "Kelompokkan ide", "Cari kesamaan, bukan perbedaan"],
         ["35\u201342", "Uji kematian tiap opsi", "Sebutkan penyebab gagal di depan"],
         ["42\u201345", "Pilih tiga opsi terkuat", "Belum memutuskan, baru menyaring"]],
        [0.16, 0.36, 0.48]))
    st.append(keyline("Delapan opsi kasar lebih berharga daripada satu ide rapi yang belum diuji."))
    st.append(callout("warning", "Tanda sesi perancangan sedang mati", [
        para("Kalau semua ide mulai berbunyi mirip, atau kalau satu orang mendominasi, hentikan "
             "dan ganti rute. Minta setiap orang menulis tiga ide di kertas secara diam-diam "
             "selama tiga menit, baru dibacakan. Cara ini hampir selalu menghidupkan kembali "
             "sesi yang mati."),
    ]))
    st.append(_mini(
        "M3", "Distribusi", "Satu perubahan urutan menggantikan sistem mahal",
        "Pendalaman D4",
        [("MASALAH", "Pesanan salah kirim karena barang disiapkan sebelum alamat diverifikasi."),
         ("OPSI YANG DIRANCANG", "Empat opsi: sistem pemindaian baru; menambah pemeriksa "
          "ganda; mengubah urutan kerja; mengganti label."),
         ("UJI KEMATIAN", "Sistem baru butuh enam bulan. Pemeriksa ganda menambah biaya tetap. "
          "Mengubah urutan kerja hampir tanpa biaya, tetapi butuh kedisiplinan."),
         ("KEPUTUSAN", "Urutan kerja diubah: alamat diverifikasi lebih dulu, baru barang "
          "disiapkan. Diuji di satu shift selama dua minggu."),
         ("HASIL", "Salah kirim turun 71% dalam sebulan. Sistem pemindaian ditunda, dan "
          "dananya dialihkan ke kebutuhan lain."),
         ("PELAJARAN", "Perubahan urutan hampir selalu lebih murah daripada perubahan alat."),
        ]))
    return st


# =====================================================================
#  D5
# =====================================================================
def _d5():
    st = [PageBreak()]
    st.append(H("Pendalaman D5: Bank Kriteria Siap Pakai", S["h3"], level=3,
                register=False))
    st += render("""
Pemilihan kriteria sering membuat rapat berputar. Gunakan bank berikut, pilih empat sampai lima, lalu beri bobot. Jangan memakai semua.
""")
    st.append(tool_table(
        ["Kelompok", "Kriteria", "Cocok untuk"],
        [["Dampak", "Kesesuaian dengan akar; besarnya pengaruh; banyaknya orang terbantu",
          "Semua keputusan"],
         ["Biaya", "Biaya langsung; biaya operasional lanjutan; kebutuhan orang tambahan",
          "Keputusan dengan anggaran terbatas"],
         ["Waktu", "Kecepatan hasil pertama; waktu penerapan penuh", "Masalah mendesak"],
         ["Risiko", "Kemungkinan gagal; akibat bila gagal; kemudahan dikembalikan",
          "Perubahan besar"],
         ["Keberlanjutan", "Kemudahan dirawat; ketergantungan pada satu orang",
          "Perbaikan jangka panjang"],
         ["Penerimaan", "Kesiapan tim; pengaruh pada pelanggan; keadilan bagi semua pihak",
          "Perubahan yang menyentuh orang"]],
        [0.16, 0.56, 0.28]))
    st.append(callout("insight", "Aturan lima kriteria", [
        para("Kalau kriteria lebih dari lima, penilaian menjadi lambat dan hasilnya tidak bisa "
             "dijelaskan. Kalau kurang dari tiga, keputusan cenderung mengikuti satu kepentingan "
             "saja. Lima adalah titik seimbangnya."),
    ]))

    st.append(PageBreak())
    st.append(H("Cara memutuskan ketika dua opsi hampir sama", S["h3"], level=3,
                register=False))
    st += render("""
Ini situasi yang paling sering membuat orang menunda berbulan-bulan. Ada empat jalan keluar yang bisa dipakai berurutan.
""")
    st.append(tool_table(
        ["Jalan keluar", "Pertanyaan pemandu", "Kapan dipakai"],
        [["Pilih yang mudah dikoreksi", "Opsi mana yang paling cepat diketahui salahnya?",
          "Ketika ketidakpastian tinggi"],
         ["Pilih yang bisa dimulai lebih cepat", "Opsi mana yang bisa jalan minggu ini?",
          "Ketika ada tekanan waktu"],
         ["Cari titik tengah", "Bisakah opsi A diuji kecil sambil opsi B disiapkan?",
          "Ketika keduanya saling melengkapi"],
         ["Uji pilihan", "Bisakah keduanya dicoba kecil selama dua minggu?",
          "Ketika datanya kurang dan biayanya rendah"]],
        [0.26, 0.44, 0.30]))
    st.append(callout("insight", "Keputusan yang bisa dibalik vs tidak bisa dibalik", [
        para("Bedakan dua jenis keputusan. Keputusan yang bisa dibatalkan tanpa biaya besar "
             "boleh diambil cepat dan diuji. Keputusan yang sulit dibatalkan harus dinilai "
             "dengan sangat hati-hati. Sebagian besar keputusan sebenarnya jenis pertama, "
             "tetapi diperlakukan seperti jenis kedua, dan itulah sumber kelambanan."),
    ]))
    st.append(_mini(
        "M4", "Koperasi", "Dua opsi setara, keputusan ditunda sebulan",
        "Pendalaman D5",
        [("SITUASI", "Dua opsi pengembangan layanan punya skor hampir sama: 3,72 dan 3,75."),
         ("KENAPA MACET", "Tim menunggu data tambahan yang ternyata tidak pernah mengubah "
          "skor lebih dari 0,05."),
         ("JALAN KELUAR", "Kedua opsi diuji kecil selama tiga minggu pada dua kelompok "
          "pelanggan berbeda, dengan biaya rendah."),
         ("HASIL", "Satu opsi jelas lebih unggul pada minggu kedua. Keputusan diambil "
          "berdasarkan hasil uji, bukan perdebatan."),
         ("PELAJARAN", "Ketika data tidak bisa memutuskan, uji kecil sering bisa. Ini jauh "
          "lebih cepat daripada menunggu kepastian."),
        ]))
    return st


# =====================================================================
#  D6
# =====================================================================
def _d6():
    st = [PageBreak()]
    st.append(H("Pendalaman D6: Papan Progres & Ritme Tinjauan", S["h3"], level=3,
                register=False))
    st += render("""
Eksekusi tidak ditentukan oleh besarnya tekad, tetapi oleh tampaknya kemajuan. Papan progres membuat kemajuan terlihat setiap hari.
""")
    st.append(tool_table(
        ["Isi papan", "Contoh", "Mengapa penting"],
        [["Angka utama hari ini", "Waktu tunggu rata-rata: 38 menit", "Membuat kemajuan terlihat"],
         ["Angka terbaik sejauh ini", "36 menit", "Memberi rasa mungkin"],
         ["Hambatan hari ini", "\"Dua petugas izin\"", "Hambatan yang terlihat cepat selesai"],
         ["Langkah kecil besok", "\"Catat waktu loket 2\"", "Menjaga momentum"],
         ["Satu kemenangan minggu ini", "\"Puncak turun di bawah 60 menit\"", "Menjaga semangat"]],
        [0.26, 0.38, 0.36]))
    st.append(callout("insight", "Aturan lima belas menit", [
        para("Tinjauan harian tidak perlu lama. Lima belas menit berdiri di depan papan, "
             "membaca tiga angka, menyebut satu hambatan, dan memilih satu langkah untuk "
             "besok. Rapat panjang justru menggerus waktu yang seharusnya dipakai bekerja."),
    ]))

    st.append(PageBreak())
    st.append(H("Cara merancang pemicu yang benar-benar bekerja", S["h3"], level=3,
                register=False))
    st += render("""
Pemicu adalah jembatan antara niat dan tindakan. Rumusnya sederhana: setelah [kebiasaan yang sudah ada], saya akan [langkah kecil baru], di [tempat].
""")
    st.append(tool_table(
        ["Pemicu lemah", "Kenapa gagal", "Pemicu kuat"],
        [["\"Nanti kalau sempat\"", "Tidak ada waktu yang jelas",
          "\"Setelah menutup kas, sebelum pulang\""],
         ["\"Setiap hari\"", "Tidak menempel pada rutinitas",
          "\"Setelah briefing pagi, di ruang loket\""],
         ["\"Kalau ingat\"", "Bergantung pada ingatan",
          "\"Begitu kopi pagi disiapkan, sebelum membuka surel\""],
         ["\"Kalau ada waktu luang\"", "Waktu luang tidak pernah datang",
          "\"Setelah makan siang, lima menit pertama\""]],
        [0.26, 0.30, 0.44]))

    st.append(PageBreak())
    st.append(H("Empat kesalahan umum di D6", S["h3"], level=3, register=False))
    st.append(tool_table(
        ["Kesalahan", "Gejala", "Perbaikan"],
        [["Terlalu banyak angka", "Lima indikator dipantau, tidak ada yang serius",
          "Pilih satu angka utama"],
         ["Langkah terlalu besar", "Langkah pertama butuh tiga hari",
          "Pecah sampai 15\u201330 menit"],
         ["Tanpa pemicu", "Langkah sering terlewat",
          "Tempelkan pada kebiasaan yang sudah ada"],
         ["Tanpa rencana pemulihan", "Satu hari terlewat menjadi berhenti total",
          "Siapkan versi minimal dan aturan dua hari"]],
        [0.22, 0.36, 0.42]))
    st.append(_mini(
        "M5", "Bengkel Servis", "Rencana besar yang dimulai dari satu langkah kecil",
        "Pendalaman D6",
        [("SITUASI", "Waktu penyelesaian servis rata-rata 4,2 hari, pelanggan mengeluh. "
          "Rencana awal terlalu besar: menambah dua teknisi dan membeli alat baru."),
         ("LANGKAH KECIL", "Satu perubahan: setiap motor yang masuk difoto dan diberi catatan "
          "diagnosis awal sebelum disimpan. Lima belas menit per unit."),
         ("ANGKA TUNGGAL", "Rata-rata hari penyelesaian per unit."),
         ("PEMICU", "Setelah motor diterima, sebelum masuk area penyimpanan."),
         ("HASIL", "Dalam tiga minggu, waktu turun dari 4,2 menjadi 3,1 hari, tanpa teknisi "
          "atau alat tambahan. Penambahan teknisi ditunda, dan dananya dipakai untuk hal lain."),
         ("PELAJARAN", "Sebagian besar rencana besar mengandung satu langkah kecil yang "
          "sebenarnya sudah cukup untuk sebagian besar hasil."),
        ]))
    return st


# =====================================================================
#  D7
# =====================================================================
def _d7():
    st = [PageBreak()]
    st.append(H("Pendalaman D7: Template Standar Kerja Satu Halaman", S["h3"],
                level=3, register=False))
    st += render("""
Standar yang baik muat dalam satu halaman dan bisa dibaca dalam lima menit. Gunakan kerangka berikut.
""")
    st.append(tool_table(
        ["Bagian", "Isi", "Contoh"],
        [["Nama standar", "Singkat dan jelas", "\"Verifikasi alamat sebelum penyiapan\""],
         ["Tujuan", "Satu kalimat", "\"Mencegah salah kirim pada pesanan pengiriman\""],
         ["Langkah", "Tiga sampai tujuh langkah berurutan", "Periksa alamat \u2192 cocokkan \u2192 siapkan"],
         ["Penanda benar", "Bagaimana tahu langkah sudah benar", "Ada tanda centang pada label"],
         ["Pengecualian", "Kondisi khusus & cara menanganinya", "Alamat tidak ditemukan \u2192 tahan pesanan"],
         ["Pemilik", "Satu nama", "Kepala gudang"],
         ["Tanggal tinjau", "Kapan diperbarui", "Setiap kuartal"]],
        [0.20, 0.42, 0.38]))
    st.append(callout("insight", "Standar bukan belenggu", [
        para("Ada kekhawatiran bahwa standar membuat orang kaku. Justru sebaliknya: standar "
             "yang jelas memberi titik mula yang sama bagi semua orang, sehingga perbaikan "
             "berikutnya bisa dibangun di atas dasar yang dikenal. Tanpa standar, setiap orang "
             "memulai dari tempat berbeda dan perbaikan sulit diukur."),
    ]))

    st.append(PageBreak())
    st.append(H("Ritme tinjauan: agenda tiga puluh menit", S["h3"], level=3,
                register=False))
    st.append(tool_table(
        ["Menit", "Agenda", "Pertanyaan kunci"],
        [["0\u20135", "Angka terbaru", "Apakah kita masih di jalur yang benar?"],
         ["5\u201315", "Satu penyimpangan", "Apa yang berubah dan mengapa?"],
         ["15\u201325", "Satu keputusan", "Apa yang akan kita sesuaikan?"],
         ["25\u201330", "Pemilik & tanggal", "Siapa, kapan, dan bagaimana kita tahu berhasil?"]],
        [0.14, 0.34, 0.52]))
    st.append(keyline("Rapat tinjauan memeriksa sistem, bukan menilai orang."))

    st.append(PageBreak())
    st.append(H("Empat kesalahan umum di D7", S["h3"], level=3, register=False))
    st.append(tool_table(
        ["Kesalahan", "Gejala", "Perbaikan"],
        [["Standar terlalu tebal", "Tidak ada yang membacanya",
          "Pangkas sampai satu halaman"],
         ["Dokumen lama dibiarkan", "Dua cara beredar bersamaan",
          "Tarik semua versi lama"],
         ["Tidak ada pemilik", "Tidak ada yang sadar saat menyimpang",
          "Tulis satu nama di lembar standar"],
         ["Berhenti mengukur", "Hasil terkikis tanpa terlihat",
          "Tetapkan ritme pemantauan dan batas peringatan"]],
        [0.22, 0.36, 0.42]))
    st.append(_mini(
        "M6", "Rantai Kafe", "Perbaikan yang hilang karena tidak dibakukan",
        "Pendalaman D7",
        [("SITUASI", "Waktu penyajian berhasil dipangkas dari 9 menit ke 5 menit di satu "
          "cabang percontohan."),
         ("TANPA PEMBAKUAN", "Enam bulan kemudian, waktu kembali ke 8,5 menit. Tiga barista "
          "lama pindah, dan barista baru menjalankan urutan lama."),
         ("PEMBAKUAN YANG DILAKUKAN", "Satu kartu standar di area penyajian, satu sesi pelatihan "
          "untuk semua barista, satu pemilik standar, dan pemeriksaan waktu setiap bulan."),
         ("HASIL", "Waktu bertahan di sekitar 5,2 menit selama dua tahun, termasuk setelah "
          "tiga kali pergantian staf."),
         ("PELAJARAN", "Perbaikan hidup selama orangnya masih ingat. Standar membuatnya hidup "
          "lebih lama daripada ingatan."),
        ]))
    st.append(callout("practice", "Uji kesiapan pembakuan", [
        para("Sebelum menutup sebuah perbaikan, jawab empat pertanyaan ini. Kalau ada satu "
             "yang belum bisa dijawab, pembakuannya belum siap."),
        para("1. Di mana standar itu bisa dibaca oleh siapa pun, kapan saja?"),
        para("2. Siapa namanya yang menjaga standar ini?"),
        para("3. Angka apa yang dipantau, dan setiap berapa lama?"),
        para("4. Kapan standar ini akan ditinjau ulang?"),
    ]))
    return st


_BUILDERS = {
    "D1": _d1, "D2": _d2, "D3": _d3, "D4": _d4,
    "D5": _d5, "D6": _d6, "D7": _d7,
}
