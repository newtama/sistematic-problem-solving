"""A second full-length case study per TUNTAS 7D step, plus sector deep dives."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para
from dsl import render
from components import (tool_table, caption, callout, keyline, case_study,
                        worksheet_block, StatRow, rule)

S = styles()


def _c(num, org, title, meta, sections, color=NAVY, tag="STUDI KASUS"):
    return case_study(num, org, title, meta, sections, color=color, tag=tag)


def build(code):
    fn = _B.get(code)
    return fn() if fn else []


# ---------------------------------------------------------------------
def _d1():
    st = [PageBreak()]
    st.append(H("Studi kasus kedua: masalah yang tersembunyi di balik rata-rata",
                S["h3"], level=3, register=False))
    st.append(_c(
        "S1", "Perusahaan Logistik", "Pengiriman terlambat yang bukan salah kurir",
        "Pendalaman D1 \u00b7 220 kurir \u00b7 enam wilayah",
        [("GEJALA", "Pengaduan keterlambatan naik 40% dalam satu kuartal. Tudingan pertama: "
          "kurir kurang rajin karena beban kerja naik."),
         ("DETEKSI (D1)", "Waktu tempuh kurir ternyata stabil. Yang berubah: jumlah paket per "
          "kurir naik 18%, sementara waktu pengurusan di pusat distribusi naik 12 menit per "
          "siklus. Rata-rata menutupi dua kenyataan berbeda."),
         ("SEBARAN", "Keterlambatan menumpuk di satu wilayah, dan hanya setelah pukul 15.00. "
          "Di wilayah lain, angkanya normal."),
         ("KESIMPULAN DETEKSI", "Rumusan: \"Keterlambatan pengiriman wilayah tengah setelah "
          "pukul 15.00 mencapai 34%, sementara wilayah lain 6%. Target: di bawah 12%.\""),
         ("PELAJARAN", "Tuduhan pertama selalu mengarah ke manusia. Data hampir selalu mengarah "
          "ke sistem. Wilayah dan waktu adalah dua pemecahan yang paling sering membuka teka-teki."),
        ]))
    st.append(callout("insight", "Kebiasaan satu menit sebelum menyimpulkan", [
        para("Sebelum menyimpulkan sebuah masalah dari satu angka, selalu tanyakan: bagaimana "
             "bentuk sebarannya, dan siapa yang paling merasakan? Dua pertanyaan itu menghabiskan "
             "waktu satu menit, tetapi sering menghemat berminggu-minggu pekerjaan yang salah."),
    ]))
    return st


# ---------------------------------------------------------------------
def _d2():
    st = [PageBreak()]
    st.append(H("Studi kasus kedua: satu kalimat yang memecah kebuntuan", S["h3"],
                level=3, register=False))
    st.append(_c(
        "S2", "Koperasi Simpan Pinjam", "Anggota berhenti menabung",
        "Pendalaman D2 \u00b7 4.100 anggota \u00b7 dua belas bulan",
        [("MASALAH KABUR", "\"Anggota kurang aktif menabung.\" Rapat menghasilkan usulan: "
          "tambah hadiah, tambah undian, tambah petugas sosialisasi."),
         ("KENAPA GAGAL", "Tidak ada ukuran, tidak ada kelompok sasaran, tidak ada target. "
          "Semua usulan punya peluang sama untuk benar."),
         ("RUMUSAN TAJAM", "\"Anggota dengan masa keanggotaan di bawah satu tahun menabung "
          "rata-rata 1,2 kali per bulan, sementara anggota lama 3,4 kali. Target: anggota baru "
          "mencapai 2,5 kali per bulan dalam enam bulan.\""),
         ("EFEK", "Pertanyaan berubah dari \"bagaimana menambah insentif\" menjadi \"apa yang "
          "berbeda pada anggota baru\"."),
         ("TEMUAN", "Anggota baru tidak tahu cara menabung tanpa datang ke kantor, sementara "
          "anggota lama sudah punya kebiasaan dan saluran yang jelas."),
         ("HASIL", "Satu panduan langkah dan satu saluran setor melalui agen membuat frekuensi "
          "menabung anggota baru naik ke 2,7 kali per bulan dalam lima bulan."),
         ("PELAJARAN", "Perhatikan bagaimana kata \"anggota baru\" langsung menyempitkan ruang "
          "pencarian solusi."),
        ]))
    return st


# ---------------------------------------------------------------------
def _d3():
    st = [PageBreak()]
    st.append(H("Studi kasus kedua: akar yang tersembunyi di prosedur", S["h3"],
                level=3, register=False))
    st.append(_c(
        "S3", "Klinik Kesehatan", "Pasien tidak kembali untuk kontrol",
        "Pendalaman D3 \u00b7 1.800 pasien \u00b7 empat bulan",
        [("GEJALA", "Tingkat kunjungan kontrol hanya 34%. Rencana awal: memperbanyak pengingat "
          "dan menambah diskon kontrol."),
         ("KENAPA GAGAL", "Masalahnya bukan ingatan. Diskusikan lebih lama: ternyata pengingat "
          "sudah dikirim tiga kali, dan diskon sudah cukup besar."),
         ("5 WHYS", "Kenapa tidak kembali? Merasa tidak perlu. Kenapa merasa tidak perlu? Tidak "
          "tahu apa yang harus dipantau. Kenapa tidak tahu? Tidak ada penjelasan setelah "
          "perawatan. Kenapa tidak ada penjelasan? Tidak ada bagian khusus dalam prosedur "
          "penutupan perawatan."),
         ("VERIFIKASI", "Dua kelompok pasien dibandingkan. Kelompok yang menerima satu lembar "
          "penjelasan singkat memiliki tingkat kembali 68%, sementara kelompok lain tetap 34%."),
         ("AKAR", "Prosedur penutupan perawatan tidak memuat langkah penjelasan lanjutan."),
         ("PERBAIKAN", "Satu lembar penjelasan ditambahkan ke prosedur, dan satu pertanyaan "
          "wajib diajukan petugas sebelum pasien pulang."),
         ("HASIL", "Tingkat kembali naik dari 34% menjadi 71% dalam empat bulan, tanpa biaya "
          "pengingat tambahan."),
         ("PELAJARAN", "Akar masalah paling sering ada di prosedur yang tidak lengkap, bukan "
          "pada kemauan pasien."),
        ]))
    return st


# ---------------------------------------------------------------------
def _d4():
    st = [PageBreak()]
    st.append(H("Studi kasus kedua: dari satu ide menjadi lima opsi", S["h3"],
                level=3, register=False))
    st.append(_c(
        "S4", "Perusahaan Manufaktur", "Biaya energi naik terus",
        "Pendalaman D4 \u00b7 dua pabrik \u00b7 sembilan bulan",
        [("MASALAH", "Biaya energi naik 24% dalam setahun, sementara produksi hanya naik 6%."),
         ("IDE PERTAMA", "Mengganti mesin utama dengan model yang lebih hemat. Biaya besar, "
          "waktu pemasangan lama, dan pemasok belum tentu bisa memenuhi tenggat."),
         ("OPSI YANG DIRANCANG", "Lima opsi: ganti mesin; perbaiki isolasi; ubah jadwal operasi "
          "ke jam tarif rendah; matikan peralatan menganggur secara otomatis; pelihara mesin "
          "secara berkala agar efisiensi tidak turun."),
         ("PETA RADAR", "Isolasi berdampak sedang, mudah, cepat. Ubah jadwal berdampak tinggi, "
          "mudah, cepat. Otomatisasi mati berdampak sedang, sedang. Pemeliharaan berdampak "
          "sedang, mudah. Ganti mesin berdampak tinggi, sangat sulit."),
         ("KEPUTUSAN", "Tiga opsi mudah dijalankan bersamaan, mesin baru ditunda sampai "
          "hasil ketiganya terukur."),
         ("HASIL", "Biaya energi turun 17% dalam sembilan bulan, tanpa satu pun mesin baru."),
         ("PELAJARAN", "Ide pertama yang paling mahal sering mengalahkan empat ide murah yang "
          "sebenarnya cukup untuk menyelesaikan sebagian besar masalah."),
        ]))
    return st


# ---------------------------------------------------------------------
def _d5():
    st = [PageBreak()]
    st.append(H("Studi kasus kedua: keputusan yang tidak populer", S["h3"],
                level=3, register=False))
    st.append(_c(
        "S5", "Yayasan Pendidikan", "Memilih antara menambah kelas atau menambah guru",
        "Pendalaman D5 \u00b7 900 siswa \u00b7 satu tahun ajaran",
        [("SITUASI", "Ruang kelas penuh. Tiga opsi: menambah kelas baru, membagi kelas menjadi "
          "lebih besar, atau memakai dua sesi belajar."),
         ("KRITERIA DITETAPKAN LEBIH DULU", "Mutu pembelajaran (40%), biaya (25%), kecepatan "
          "penerapan (20%), dan kesejahteraan guru (15%)."),
         ("PENILAIAN", "Menambah kelas unggul pada mutu tetapi lemah pada biaya dan kecepatan. "
          "Kelas lebih besar lemah pada mutu. Dua sesi cukup pada mutu dan biaya, lambat pada "
          "kecepatan karena butuh penyesuaian jadwal."),
         ("KEPUTUSAN", "Dua sesi dipilih, dimulai dengan satu tingkat sebagai percontohan, "
          "dengan kriteria keberhasilan yang jelas."),
         ("PENGAMANAN", "Bila mutu turun dalam dua bulan, percontohan dihentikan dan kelas baru "
          "dibangun bertahap."),
         ("HASIL", "Mutu tidak turun, biaya terjaga, dan kapasitas bertambah 22% pada tahun "
          "berikutnya."),
         ("PELAJARAN", "Kriteria yang ditetapkan sebelum penilaian membuat keputusan sulit bisa "
          "dijelaskan kepada semua pihak."),
        ]))
    return st


# ---------------------------------------------------------------------
def _d6():
    st = [PageBreak()]
    st.append(H("Studi kasus kedua: dari kebiasaan lama menjadi kebiasaan baru",
                S["h3"], level=3, register=False))
    st.append(_c(
        "S6", "Kantor Akuntan", "Laporan selalu lewat tenggat",
        "Pendalaman D6 \u00b7 24 staf \u00b7 tiga bulan",
        [("MASALAH", "Rata-rata 7 dari 20 laporan lewat tenggat, dengan keterlambatan 3 hari. "
          "Keluhan pelanggan meningkat."),
         ("AKAR", "Dokumen dari klien sering datang terlambat, dan pekerjaan baru dimulai "
          "setelah dokumen lengkap. Tidak ada langkah persiapan paralel."),
         ("KEPUTUSAN", "Mulai pekerjaan yang tidak bergantung dokumen lebih dulu, sambil "
          "mengejar kelengkapan secara paralel."),
         ("LANGKAH KECIL", "Setiap pagi, satu orang memeriksa daftar dokumen dan mengirim "
          "pengingat tunggal kepada klien. Sepuluh menit."),
         ("PEMICU", "Setelah kopi pagi, sebelum membuka surel masuk."),
         ("ANGKA TUNGGAL", "Jumlah laporan lewat tenggat per minggu."),
         ("HASIL", "Dalam dua belas minggu, laporan lewat tenggat turun dari 7 menjadi 1 per "
          "minggu, dan keterlambatan rata-rata turun menjadi 0,6 hari."),
         ("PELAJARAN", "Perbaikan besar sering dimulai dari satu kebiasaan sepuluh menit yang "
          "ditempelkan pada rutinitas yang sudah ada."),
        ]))
    return st


# ---------------------------------------------------------------------
def _d7():
    st = [PageBreak()]
    st.append(H("Studi kasus kedua: ketika perbaikan justru menunggu untuk hilang",
                S["h3"], level=3, register=False))
    st.append(_c(
        "S7", "Rumah Sakit Swasta", "Waktu tunggu kembali setelah enam bulan",
        "Pendalaman D7 \u00b7 tiga gedung \u00b7 dua tahun",
        [("SITUASI AWAL", "Waktu tunggu berhasil turun dari 90 menjadi 35 menit. Semua puas, "
          "proyek ditutup, tim dibubarkan."),
         ("ENAM BULAN KEMUDIAN", "Waktu tunggu kembali ke 70 menit. Penyebabnya bukan "
          "kesalahan, tetapi ketiadaan pembakuan. Dua kepala unit pindah, dan tidak ada standar "
          "tertulis untuk alur baru."),
         ("PEMBAKUAN YANG DILAKUKAN", "Standar kerja satu halaman untuk alur pendaftaran, "
          "pelatihan wajib bagi petugas baru, satu pemilik standar di tingkat rumah sakit, dan "
          "satu angka yang dipantau bulanan."),
         ("PENGUKURAN", "Angka rata-rata dan puncak dipantau bulanan, dengan batas peringatan "
          "60 menit yang memicu tindakan dalam tujuh hari."),
         ("RITME", "Rapat tinjauan tiga puluh menit setiap bulan, dengan agenda tetap: angka, "
          "penyimpangan, keputusan."),
         ("HASIL", "Waktu tunggu bertahan di bawah 40 menit selama dua tahun, melewati tiga "
          "kali pergantian petugas dan satu penggantian kepala unit."),
         ("PELAJARAN", "Selama perbaikannya hanya hidup di ingatan beberapa orang, ia menunggu "
          "waktu untuk hilang. Pembakuan membuatnya hidup lebih lama daripada orang-orangnya."),
        ]))
    st.append(callout("insight", "Tanda pembakuan belum selesai", [
        para("Kalau kamu harus menjelaskan cara baru itu secara lisan kepada setiap orang baru, "
             "pembakuannya belum selesai. Ukuran pembakuan yang berhasil sederhana: orang baru "
             "bisa menjalankannya dengan benar hanya dengan membaca satu halaman, tanpa bertanya "
             "kepada siapa pun."),
    ]))
    return st


_B = {"D1": _d1, "D2": _d2, "D3": _d3, "D4": _d4, "D5": _d5, "D6": _d6, "D7": _d7}
