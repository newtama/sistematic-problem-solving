"""Sector playbooks: cara menerapkan 7D di berbagai bidang."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para
from dsl import render
from components import (tool_table, caption, callout, keyline, case_study,
                        worksheet_block, StatRow, rule)

S = styles()


def build():
    st = [PageBreak()]
    st.append(H("Bab Tambahan: Playbook per Bidang", S["h2"], level=2,
                key="playbook"))
    st += render("""
Tujuh langkah TUNTAS 7D berlaku universal. Namun setiap bidang memiliki jenis data, kendala, dan sumber hambatan yang khas. Bab ini merangkum penyesuaian yang paling sering diperlukan, supaya kamu tidak perlu memulai dari nol.

Setiap playbook berisi empat hal: masalah yang paling sering muncul, data yang paling berguna, jebakan khas bidang itu, dan langkah pertama yang biasanya tepat.
""")

    _pb(st, "Manufaktur & Produksi",
        "Cacat, downtime, efisiensi, keselamatan kerja, pemborosan bahan",
        "Data cacat per stasiun dan per shift; waktu henti mesin; waktu siklus per unit; "
        "jumlah insiden keselamatan",
        "Fokus berlebihan pada inspeksi akhir. Ingat bahwa memeriksa lebih banyak tidak "
        "memperbaiki apa pun. Cacat harus dicegah di sumbernya.",
        "Hitung Pareto cacat per jenis dan per stasiun. Cari stasiun yang menyumbang 80% "
        "cacat, lalu jalankan 5 Whys di sana.")

    _pb(st, "Layanan Kesehatan",
        "Waktu tunggu, kepatuhan pasien, keselamatan, beban kerja staf, kesalahan administrasi",
        "Waktu tunggu per tahap; tingkat pasien tidak kembali; insiden keselamatan; waktu "
        "pengisian berkas",
        "Menyalahkan pasien atas kepatuhan rendah. Hampir selalu masalahnya ada pada kejelasan "
        "informasi atau kemudahan proses.",
        "Petakan perjalanan pasien dari pintu masuk sampai keluar, catat waktu setiap tahap. "
        "Tahap terlama hampir selalu bukan tahap yang dianggap paling penting.")

    _pb(st, "Pendidikan & Pelatihan",
        "Partisipasi siswa, hasil belajar, kehadiran, keterlibatan orang tua, disiplin",
        "Tingkat partisipasi per sesi; tingkat ketuntasan tugas; pola kehadiran; hasil asesmen "
        "per keterampilan",
        "Menyalahkan motivasi siswa. Periksa dulu rancangan kegiatan: apakah memberi ruang untuk "
        "mencoba, gagal, dan memperbaiki.",
        "Amati satu sesi secara diam-diam. Catat siapa yang berbicara, berapa lama, dan kapan. "
        "Pola interaksi biasanya langsung menunjukkan hambatan.")

    _pb(st, "Bisnis & UMKM",
        "Penjualan mandek, margin tipis, stok, kas, pelanggan tidak kembali, biaya operasional",
        "Margin per produk; nilai belanja rata-rata; frekuensi kunjungan; perputaran stok; "
        "waktu pembayaran",
        "Menambah promosi ketika masalahnya margin. Promosi yang salah hanya mempercepat "
        "kerugian, bukan menambah laba.",
        "Hitung laba per produk atau per transaksi, bukan hanya penjualan. Produk dengan "
        "penjualan besar sering menjadi penyumbang kerugian terbesar.")

    _pb(st, "Teknologi & Produk Digital",
        "Fitur tidak dipakai, keluhan pengguna, performa lambat, bug berulang, onboarding kurang",
        "Tingkat penggunaan fitur; tingkat penyelesaian tugas; waktu muat; jumlah keluhan per "
        "rilis",
        "Merancang dari daftar keinginan internal. Bukti masalah dari pengguna nyata hampir "
        "selalu mengubah arah.",
        "Amati lima pengguna menyelesaikan pekerjaan nyata. Hitung berapa yang berhasil tanpa "
        "bantuan. Ini angka paling jujur untuk dijadikan titik awal.")

    _pb(st, "Pemerintahan & Layanan Publik",
        "Antrean, pengaduan, kepatuhan, waktu proses, koordinasi antarunit, kepercayaan",
        "Waktu proses per tahap; jumlah pengaduan per jenis; tingkat pengulangan layanan; "
        "tingkat penyelesaian pada percobaan pertama",
        "Menyalahkan keterbatasan anggaran sebelum memeriksa proses. Banyak penundaan berasal "
        "dari langkah yang bisa dihapus tanpa biaya.",
        "Coba layani satu orang dari awal sampai akhir sambil mencatat setiap langkah. Berapa "
        "banyak langkah yang tidak menambah nilai bagi orang itu? Itu titik mulai yang paling kuat.")

    _pb(st, "Nirlaba & Organisasi Sosial",
        "Jangkauan penerima manfaat, keberlanjutan program, keterlibatan relawan, dampak",
        "Jumlah penerima manfaat per program; tingkat kelanjutan setelah program selesai; biaya "
        "per penerima; retensi relawan",
        "Mengukur kegiatan, bukan hasil. Menghitung jumlah pelatihan tidak sama dengan menghitung "
        "perubahan yang terjadi pada orang.",
        "Tentukan satu perubahan nyata yang ingin dicapai, lalu cari cara mengukurnya walau "
        "sederhana. Satu angka jujur lebih berguna daripada sepuluh laporan kegiatan.")

    _pb(st, "Keluarga & Pribadi",
        "Komunikasi, keuangan, kebiasaan, pendidikan anak, kesehatan, pembagian waktu",
        "Pengeluaran per kategori; waktu yang benar-benar dipakai; frekuensi konflik; kebiasaan "
        "harian; jam tidur",
        "Menyalahkan orang. Dalam masalah keluarga, hampir selalu ada kebutuhan yang tidak "
        "terpenuhi di balik perilaku yang mengganggu.",
        "Catat selama satu minggu tanpa mengubah apa pun. Pencatatan saja sudah mengubah "
        "kesadaran, dan biasanya langsung memperlihatkan di mana letak masalahnya.")

    st.append(PageBreak())
    st.append(H("Cara memilih playbook yang tepat", S["h3"], level=3, register=False))
    st += render("""
Bila masalahmu menyentuh dua bidang, gunakan playbook yang paling dekat dengan tempat masalah itu terjadi. Bila masih ragu, gunakan pertanyaan berikut.
""")
    st.append(tool_table(
        ["Kalau masalahmu tentang\u2026", "Playbook", "Data pertama yang dicari"],
        [["Tingkat gagal atau rusak", "Manufaktur", "Pareto cacat per jenis"],
         ["Waktu menunggu", "Layanan kesehatan / publik", "Waktu per tahap"],
         ["Partisipasi atau perubahan perilaku", "Pendidikan", "Pola interaksi per sesi"],
         ["Laba atau kas", "Bisnis & UMKM", "Margin per produk"],
         ["Pemakaian atau penyelesaian tugas", "Teknologi", "Tingkat penyelesaian tanpa bantuan"],
         ["Dampak atau keberlanjutan program", "Nirlaba", "Perubahan nyata penerima manfaat"],
         ["Hubungan atau kebiasaan", "Keluarga & pribadi", "Catatan harian sederhana"]],
        [0.38, 0.26, 0.36]))
    st.append(callout("insight", "Prinsip yang berlaku di semua bidang", [
        para("Terlepas dari bidangnya, tiga hal ini selalu benar. Pertama, masalah tanpa angka "
             "akan sulit diselesaikan. Kedua, rata-rata menyembunyikan tempat masalah sebenarnya. "
             "Ketiga, akar tersembunyi paling sering ada di dalam proses, bukan di dalam orang."),
    ]))
    return st


def _pb(st, title, problems, data, trap, first):
    st.append(PageBreak())
    st.append(H(title, S["h2"], level=3, register=False))
    st.append(tool_table(
        ["Bagian", "Isi"],
        [["Masalah yang paling sering", problems],
         ["Data yang paling berguna", data],
         ["Jebakan khas", trap],
         ["Langkah pertama yang biasanya tepat", first]],
        [0.26, 0.74]))
    for label, body in (("Catatan penting", None),):
        pass
