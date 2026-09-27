"""D1 - Detect: salah diagnosis, salah obat."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (h2, h3, h4, rule, caption, callout, keyline, StatRow,
                        QRPanel, tool_table, worksheet_block, case_study, WriteLines)
from stepchapter import Step, t

S = styles()

STEP = Step(
    "D1", "3", "Detect",
    "Langkah 1 dari 7 \u00b7 Mengenali masalah yang sebenarnya",
    "Setiap solusi yang gagal dimulai dari masalah yang tidak pernah benar-benar dikenali.",
    ["Kenapa kita sering salah membaca masalah",
     "Tiga lapis: gejala, masalah, akar",
     "Tool: Kanvas Deteksi Sinyal",
     "Studi kasus: komplain operasional",
     "Worksheet TUNTAS D1 + QR toolkit"],
    ACCENT)


def build():
    st = []
    st += STEP.opener()
    st += t("""
## Cerita pembuka: tiga jam yang sebenarnya empat puluh menit

Kepala sebuah rumah sakit daerah mengumpulkan seluruh kepala unit karena satu keluhan yang sudah terdengar setiap hari selama berbulan-bulan. "Antrean pendaftaran terlalu lama." Keluhan itu selalu muncul dalam survei kepuasan, selalu dibahas di rapat mingguan, dan selalu dijawab dengan cara yang sama: menambah kursi tunggu.

Pagi itu, seorang petugas rekam medis mengeluarkan kertas berisi catatan yang tidak pernah dibuka siapa pun: catatan jam kedatangan dan jam selesai pendaftaran, per menit, selama tiga puluh hari.

Angka rata-ratanya empat puluh tujuh menit. Bukan tiga jam. Tetapi ada dua hal yang membuat rata-rata itu menipu: puncak kedatangan antara pukul tujuh dan sembilan selalu melonjak sampai lebih dari dua jam, dan satu pos pendaftaran tertentu memerlukan waktu dua kali lebih lama karena satu kolom formulir yang harus diisi ulang.

Selama enam bulan, seluruh organisasi memperbaiki "antrean tiga jam" yang sebenarnya hanya gejala dari dua masalah berbeda. Ketika kedua hal itu diperbaiki secara terpisah, waktu tunggu rata-rata turun menjadi dua puluh delapan menit dan puncaknya tidak lagi melewati satu jam.
""")
    st.append(keyline("Selama enam bulan seluruh organisasi memperbaiki gejala, bukan masalah."))
    st += t("""
## Kenapa D1 menentukan segalanya

Bayangkan kamu ingin memotong pohon yang salah. Seberapa tajam kapakmu tidak lagi penting. Seberapa kuat tenagamu tidak lagi penting. Seberapa cepat kamu mengayun juga tidak lagi penting. Semua usaha yang kamu keluarkan justru memperbesar kerugian, karena energinya habis pada tempat yang salah.

Itulah langkah D1. Detect berarti mengenali masalah dengan benar sebelum satu sen pun energi dikeluarkan. Ini langkah yang paling sering dilewati karena terasa tidak seperti bekerja. Tidak ada yang bisa dilaporkan ke atasan. Tidak ada progres yang terlihat. Padahal di sinilah separuh hasil ditentukan.
""")
    st.append(StatRow([("50%", "hasil ditentukan di D1\u2013D2"), ("6 bln", "waktu terbuang karena salah arah"),
                       ("47\u219228", "menit waktu tunggu")]))
    st += t("""
## Tiga lapis yang harus kamu pisahkan

Setiap masalah datang dalam tiga lapis. Masalahnya, lapisan paling atas adalah yang paling berisik, jadi kita hampir selalu berhenti di sana.
""")
    st += t("!fig iceberg")
    st.append(tool_table(
        ["Lapis", "Apa itu", "Contoh", "Cara memeriksa"],
        [["Gejala", "Yang dilaporkan & dirasakan", "\"Antrenya lama\"", "Catat kata persisnya, jangan tafsirkan"],
         ["Masalah", "Pola yang terukur & berulang", "Puncak tunggu 2 jam pada 07.00\u201309.00", "Ukur frekuensi, durasi, dan sebarannya"],
         ["Akar", "Struktur, proses, atau kebijakan", "Satu kolom formulir wajib diisi ulang", "Tanya 'kenapa' 3\u20135 kali, lihat prosesnya"]],
        [0.14, 0.24, 0.30, 0.32]))
    st.append(callout("insight", "Uji tiga lapis dalam sepuluh detik", [
        para("Ambil satu keluhan yang kamu dengar hari ini. Tulis tiga baris. Kalau baris kedua "
             "berisi kata sifat seperti 'lama', 'buruk', atau 'sering', berarti kamu masih di "
             "lapis gejala. Ubah sampai muncul angka dan pola."),
    ]))

    st += t("""
## Alat: Kanvas Deteksi Sinyal

Kanvas ini terdiri dari enam kotak. Isinya sengaja dibuat sederhana supaya bisa dikerjakan dalam lima belas menit, sendirian atau bersama tim.
""")
    st.append(tool_table(
        ["Kotak", "Pertanyaan pemandu", "Contoh pengisian"],
        [["1. Sinyal awal", "Apa yang pertama kali membuat kita sadar ada masalah?", "Survei turun dua bulan berturut-turut"],
         ["2. Sumber sinyal", "Siapa yang merasakan paling dulu? Pelanggan, tim, atau angka?", "Petugas loket, lalu pelanggan"],
         ["3. Ukuran sekarang", "Angka berapa yang mewakili masalah ini saat ini?", "Rata-rata tunggu 47 menit"],
         ["4. Ukuran tujuan", "Angka berapa yang kita anggap selesai?", "Rata-rata 25 menit, puncak 45 menit"],
         ["5. Sebaran", "Apakah masalahnya merata atau menumpuk di bagian tertentu?", "Menumpuk 07.00\u201309.00 di loket 2"],
         ["6. Bukti yang hilang", "Data apa yang belum kita punya dan perlu dicari?", "Waktu per langkah pendaftaran"]],
        [0.20, 0.44, 0.36]))
    st.append(caption("Tabel. Enam kotak Kanvas Deteksi Sinyal. Kotak keenam paling sering dilewati, "
                      "padahal ia yang menentukan apakah analisismu akan kuat atau rapuh."))

    st += t("""
## Langkah demi langkah menjalankan D1

### Langkah 1: Kumpulkan sinyal, bukan kesimpulan

Kumpulkan kalimat apa adanya. Jangan perbaiki bahasa orang, jangan tafsirkan. Tuliskan siapa yang bilang dan kapan. Ini penting karena tafsiran dini akan mengarahkan seluruh analisis ke satu arah.

### Langkah 2: Ubah sinyal menjadi ukuran

Untuk setiap sinyal, cari satu angka yang mewakilinya. Kalau tidak ada angkanya, buat cara mengukurnya. Satu angka sederhana jauh lebih berguna daripada lima kalimat keluhan.

### Langkah 3: Periksa sebaran, bukan hanya rata-rata

Rata-rata menyembunyikan cerita. Empat puluh tujuh menit terasa wajar, tetapi kalau puncaknya dua jam, pelangganmu merasakan dua jam, bukan empat puluh tujuh menit. Selalu periksa: per jam berapa, per lokasi mana, per jenis apa, per orang siapa.

### Langkah 4: Tentukan batas masalah

Tuliskan dengan tegas apa yang termasuk dan apa yang tidak. Kalau kamu menyelesaikan keluhan pendaftaran, jangan sekaligus mengubah seluruh alur rumah sakit. Batas yang jelas menjaga energimu.

### Langkah 5: Cari bukti yang hilang

Daftarkan data yang belum kamu punya. Ini daftar belanja untuk D3, bukan hambatan untuk berhenti. Kamu boleh lanjut ke D2 sambil mengumpulkan data itu.

### Langkah 6: Rumuskan pernyataan deteksi

Tutup D1 dengan satu kalimat: "Kami mendeteksi [ukuran] pada [siapa/bagian mana] sebesar [angka] sejak [kapan], sementara tujuan kami [angka target]."
""")
    st.append(keyline("Deteksi yang baik selalu bisa ditulis dalam satu kalimat berangka."))
    st.append(callout("warning", "Empat jebakan paling umum di D1", [
        para("<b>1. Terlalu cepat menamai masalah.</b> Begitu kamu menyebutnya 'masalah "
             "pelayanan', seluruh analisis akan berkisar pada pelayanan."),
        para("<b>2. Puas pada rata-rata.</b> Rata-rata sering menyembunyikan puncak yang justru "
             "paling dirasakan orang."),
        para("<b>3. Mengandalkan satu sumber.</b> Kalau semua informasinya dari satu orang, kamu "
             "sedang mendeteksi masalah orang itu, bukan masalah sistem."),
        para("<b>4. Mencari data tanpa batas.</b> Menunggu data lengkap adalah cara paling halus "
             "untuk menunda pekerjaan. Cukup 70% data yang relevan untuk mulai bergerak."),
    ]))

    st.append(sp(4))
    st.append(case_study(
        "2", "Operator Transportasi", "Komplain terlambat yang bukan soal kecepatan",
        "Pola nyata \u00b7 1.200 pengemudi \u00b7 enam kota",
        [("GEJALA YANG DILAPORKAN",
          "Keluhan pengguna naik. Tudingan pertama selalu sama: pengemudi melambat, "
          "mungkin menurunkan semangat kerja. Muncul usulan menaikkan insentif."),
         ("D1 \u00b7 KENALI DENGAN BENAR",
          "Tim mengumpulkan tiga sumber sekaligus: waktu tunggu penumpang, waktu tempuh "
          "pengemudi, dan kepadatan permintaan per jam per wilayah. Hasilnya mengejutkan. "
          "Waktu tempuh pengemudi sebenarnya stabil dan bahkan sedikit membaik."),
         ("TEMUAN DARI SEBARAN",
          "Masalahnya menumpuk pada pukul 17.00\u201319.00 di wilayah pusat bisnis. Kenaikan "
          "waktu tunggu dua kali lipat terjadi hanya di sana. Insentif dinaikkan pun tidak "
          "akan menambah mobil pada jam itu, karena pengemudi jam itu memang sudah penuh."),
         ("MASALAH YANG SEBENARNYA",
          "Permintaan melonjak jauh lebih cepat daripada ketersediaan pada jam dan wilayah "
          "tertentu. Ini masalah pencocokan permintaan dan penawaran, bukan masalah semangat."),
         ("PELAJARAN",
          "Tuduhan pertama hampir selalu mengarah pada orang. Data hampir selalu mengarah "
          "pada sistem. Uji keduanya sebelum memutuskan."),
         ("HASIL D1",
          "Masalah dipersempit menjadi satu jam dan satu wilayah. Perbaikan yang benar bisa "
          "dirancang spesifik, dan alokasi armada pada jam itu menurunkan waktu tunggu 34% "
          "dalam delapan minggu."),
        ]))

    st += t("""
## Rangkuman bab

- D1 adalah tentang mengenali masalah yang benar sebelum mengeluarkan energi apa pun.
- Pisahkan tiga lapis: gejala, masalah terukur, dan akar.
- Gunakan Kanvas Deteksi Sinyal untuk memastikan deteksinya lengkap.
- Selalu periksa sebaran, bukan hanya rata-rata.
""")
    from content import extras
    st += extras.build("D1")
    from content import case2
    st += case2.build("D1")
    st.append(QRPanel("https://tuntas7d.id/toolkit/d1", "Toolkit D1: Detect",
                      "Kanvas deteksi, lembar pengumpulan data, contoh terisi",
                      "QR-D1"))
    st.append(worksheet_block(
        "WS-D1", "Kanvas Deteksi Sinyal", "Kerjakan untuk masalahmu sekarang",
        [{"label": "1. Sinyal awal (apa yang pertama membuatmu sadar)", "lines": 2},
         {"label": "2. Sumber sinyal (siapa yang merasakan paling dulu)", "lines": 2},
         {"label": "3. Ukuran sekarang (angka hari ini)", "lines": 2},
         {"label": "4. Ukuran tujuan (angka yang kamu anggap selesai)", "lines": 2},
         {"label": "5. Sebaran (per jam / lokasi / jenis / orang)", "lines": 3,
          "hint": "Kalau kamu hanya punya satu angka, curigai dirimu sedang menyembunyikan puncak."},
         {"label": "6. Bukti yang hilang (data yang perlu dicari di D3)", "lines": 2},
         {"label": "Rumuskan pernyataan deteksi dalam satu kalimat berangka", "lines": 3}],
    ))
    return st
