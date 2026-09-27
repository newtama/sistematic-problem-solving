"""One problem carried through all seven steps, shown in full detail."""
from reportlab.platypus import PageBreak, NextPageTemplate

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (tool_table, caption, callout, keyline, case_study,
                        worksheet_block, StatRow, rule, WriteLines)

S = styles()


def build():
    st = []
    st.append(NextPageTemplate("opener"))
    st.append(PageBreak())
    from frontmatter import StatementPage
    st.append(StatementPage(
        "Contoh Lengkap",
        "Satu Masalah, Tujuh Langkah",
        "Sebuah masalah kecil dikerjakan dari awal sampai akhir, apa adanya, termasuk kesalahan "
        "dan perbaikannya. Cara paling cepat memahami kerangka ini adalah melihatnya bekerja.",
        color=NAVY))
    st.append(NextPageTemplate("body"))

    st.append(PageBreak())
    st.append(H("Situasi awal: kedai kopi di sudut jalan", S["h2"], level=2,
                key="worked"))
    st += render("""
Seorang pemilik kedai kopi kecil menyampaikan satu keluhan yang sudah ia rasakan lama: "pelanggan pagi saya makin sedikit". Ia sudah mencoba dua hal: menambah pilihan menu, dan memberi potongan harga pagi. Keduanya tidak banyak mengubah keadaan.

Mari kita kerjakan bersama dengan tujuh langkah. Semua angka di bawah ini adalah contoh, tetapi bentuk pekerjaannya sama dengan yang akan kamu alami.

## Langkah 1 \u00b7 Detect: mengenali masalah yang sebenarnya

Hal pertama yang perlu diperiksa adalah apakah keluhannya sesuai dengan kenyataan. Pemilik kedai biasanya menghitung total penjualan harian. Mari kita lihat lebih rinci.
""")
    st.append(tool_table(
        ["Ukuran", "Angka", "Catatan"],
        [["Total transaksi per hari", "148", "turun dari 165 tiga bulan lalu"],
         ["Transaksi pukul 06.00\u201310.00", "51", "turun dari 78 \u2014 penurunan terbesar"],
         ["Transaksi pukul 10.00\u201314.00", "62", "naik sedikit"],
         ["Transaksi pukul 14.00\u201321.00", "35", "stabil"],
         ["Nilai belanja rata-rata pagi", "Rp 18.000", "stabil"],
         ["Nilai belanja rata-rata siang", "Rp 24.000", "naik"]],
        [0.36, 0.20, 0.44]))
    st += render("""
Perhatikan bagaimana rata-rata harian menyembunyikan cerita yang sebenarnya. Total transaksi turun 10%, tetapi penurunan itu seluruhnya berasal dari jam pagi. Sore dan siang justru sehat.

Ini contoh pertama dari pola yang berulang sepanjang buku: rata-rata menipu. Kalau pemilik kedai hanya melihat total, ia akan mencari solusi untuk seluruh hari, padahal masalahnya hanya satu blok waktu.

#### Apa yang seharusnya lebih dulu diperiksa

Sebelum menyimpulkan, ada tiga hal lain yang perlu dipastikan. Apakah penurunan terjadi tiba-tiba atau bertahap? Apakah ada kedai baru di sekitar? Dan apakah ada perubahan pada jam buka atau staf?
""")
    st.append(tool_table(
        ["Pertanyaan", "Jawaban", "Sumber"],
        [["Bertahap atau tiba-tiba?", "Bertahap, sekitar tiga bulan",
          "Buku kas harian"],
         ["Ada pesaing baru?", "Satu kedai buka 200 meter dari sini, dua bulan lalu",
          "Pengamatan langsung"],
         ["Ada perubahan staf atau jam?", "Tidak ada", "Jadwal kerja"]],
        [0.34, 0.40, 0.26]))
    st += render("""
Dengan tiga jawaban itu, kita bisa merumuskan deteksi yang lebih tajam. Penurunan bertahap pada satu blok waktu, bertepatan dengan munculnya pesaing baru, membuka pertanyaan yang lebih menarik: apa yang ditawarkan pesaing itu pada jam pagi?

## Langkah 2 \u00b7 Define: merumuskan dengan tajam

Sekarang kita ubah keluhan menjadi kalimat masalah berangka.
""")
    st.append(callout("tool", "Kalimat masalah kedai kopi", [
        para("Pada <b>jam 06.00\u201310.00</b>, jumlah transaksi turun dari <b>78</b> menjadi "
             "<b>51</b> dalam <b>tiga bulan terakhir</b>. Target kami <b>70 transaksi per pagi</b> "
             "dalam <b>dua bulan</b>, karena angka itu tingkat yang sehat sebelum penurunan. "
             "Bila dibiarkan, kami kehilangan sekitar <b>Rp 13,5 juta omzet per bulan</b>. "
             "Pemilik masalah: <b>pemilik kedai</b>."),
    ]))
    st += render("""
Perhatikan apa yang berubah setelah kalimat ini ditulis. Usulan seperti "menambah menu" dan "memberi potongan harga" tidak lagi otomatis masuk. Menu baru tidak akan menolong kalau masalahnya hanya di jam pagi, dan potongan harga justru menekan margin. Pertanyaan yang lebih tajam muncul: apa yang terjadi pada pelanggan pagi kita?

## Langkah 3 \u00b7 Dig: mencari akar

Kita mulai dengan mengumpulkan dugaan, lalu mengujinya.
""")
    st.append(tool_table(
        ["Dugaan", "Cara memeriksa", "Hasil"],
        [["Harga kita naik", "Bandingkan harga menu utama", "Tidak naik, sama seperti enam bulan lalu"],
         ["Kualitas menurun", "Tanya sepuluh pelanggan lama", "Tidak ada keluhan kualitas"],
         ["Pelanggan pindah ke pesaing", "Amati arus pelanggan pagi", "Benar, 19 dari 27 pelanggan "
          "hilang pergi ke arah pesaing"],
         ["Waktu tunggu bertambah", "Catat waktu penyajian pagi", "11 menit, naik dari 4 menit"],
         ["Jam buka terlalu siang", "Bandingkan jam buka", "Pesaing buka 06.00, kita 06.30"]],
        [0.26, 0.40, 0.34]))
    st += render("""
Dua dugaan terakhir menarik. Mari kita jalankan 5 Whys pada waktu tunggu, karena angka 11 menit itu mencurigakan.
""")
    st.append(tool_table(
        ["Lapis", "Pertanyaan", "Jawaban"],
        [["Whys 1", "Kenapa penyajian pagi butuh 11 menit?", "Ada penumpukan pesanan"],
         ["Whys 2", "Kenapa menumpuk?", "Hanya satu orang bertugas sebelum pukul 08.00"],
         ["Whys 3", "Kenapa hanya satu?", "Jadwal staf dimulai pukul 08.00"],
         ["Whys 4", "Kenapa jadwal mulai pukul 08.00?", "Jadwal dibuat dua tahun lalu ketika "
          "puncak pelanggan pukul 11.00"],
         ["Whys 5", "Kenapa tidak pernah diubah?", "Tidak ada tinjauan jadwal berkala"]],
        [0.14, 0.40, 0.46]))
    st += render("""
Akar yang muncul kuat: jadwal staf tidak lagi cocok dengan pola pelanggan. Pesaing baru mengeksploitasi celah yang sudah ada selama ini, hanya belum terasa akibatnya.

#### Verifikasi akar

Sebelum menerima akar ini, kita uji dengan cara paling kuat yang tersedia untuk kedai kecil: uji matikan. Selama satu minggu, satu orang ditambahkan untuk bertugas pukul 06.00, sementara minggu lain tetap seperti biasa.
""")
    st.append(tool_table(
        ["Minggu", "Penugasan pagi", "Waktu penyajian", "Transaksi pagi"],
        [["Minggu 1", "Satu orang", "11 menit", "49"],
         ["Minggu 2", "Dua orang", "5 menit", "63"],
         ["Minggu 3", "Satu orang", "10 menit", "52"],
         ["Minggu 4", "Dua orang", "5 menit", "66"]],
        [0.18, 0.24, 0.28, 0.30]))
    st += render("""
Polanya jelas. Ketika ada dua orang, transaksi pagi melonjak sekitar dua puluh lima persen. Akar terverifikasi dengan cara yang tidak bisa dibantah.

## Langkah 4 \u00b7 Design: merancang beberapa jalan

Sekarang kita rancang beberapa opsi. Perhatikan bahwa kita tidak langsung memilih menambah orang, karena menambah orang memiliki biaya tetap.
""")
    st.append(tool_table(
        ["Opsi", "Bentuknya", "Dampak", "Kesulitan"],
        [["A", "Tambah satu orang tetap untuk pagi", "Tinggi", "Sedang \u2014 biaya tetap naik"],
         ["B", "Ubah jam kerja staf yang ada, geser dari sore", "Tinggi", "Rendah \u2014 hanya jadwal"],
         ["C", "Siapkan pesanan sebelum buka untuk menu terlaris", "Sedang", "Rendah"],
         ["D", "Pesan lewat aplikasi agar siap saat tiba", "Sedang", "Sedang"],
         ["E", "Buka 30 menit lebih awal", "Rendah", "Rendah"]],
        [0.08, 0.44, 0.20, 0.28]))
    st += render("""
Opsi B menarik: menggeser satu staf dari sore, saat jumlah pelanggan sudah stabil dan menurun. Ini menyentuh akar tanpa menambah biaya tetap. Opsi C melengkapi dengan mengurangi waktu penyajian pada menu yang paling sering dipesan pagi.

## Langkah 5 \u00b7 Decide: memilih dengan kriteria

Sebelum menilai, kita tetapkan kriteria dan bobotnya.
""")
    st.append(tool_table(
        ["Kriteria", "Bobot", "A", "B", "C", "D", "E"],
        [["Dampak pada akar", "35%", "5", "5", "3", "3", "2"],
         ["Biaya operasional", "25%", "2", "5", "5", "4", "5"],
         ["Kecepatan hasil", "20%", "3", "5", "4", "2", "5"],
         ["Keberlanjutan", "20%", "4", "3", "4", "3", "2"],
         ["Skor berbobot", "100%", "3,55", "4,60", "3,85", "3,05", "3,20"]],
        [0.32, 0.14, 0.11, 0.11, 0.11, 0.11, 0.10]))
    st += render("""
Opsi B menang jelas. Opsi C menjadi pelengkap yang murah. Opsi A ditunda karena biaya tetapnya, meski dampaknya bagus. Keputusan: jalankan B sekarang, tambahkan C setelah B stabil, tinjau A bila hasilnya belum cukup.

## Langkah 6 \u00b7 Do: menjalankan tiga puluh hari

Keputusan diubah menjadi rancangan yang bisa dimulai besok pagi.
""")
    st.append(tool_table(
        ["Bagian", "Isi"],
        [["Hasil 30 hari", "Transaksi pagi rata-rata 68 per hari"],
         ["Angka tunggal", "Jumlah transaksi per pagi, dicatat setiap hari"],
         ["Langkah kecil harian", "Buka catatan sebelum buka, pastikan dua orang sudah siap (2 menit)"],
         ["Pemicu", "Setelah menyalakan mesin kopi, sebelum membuka pintu"],
         ["Pemilik", "Pemilik kedai; pengganti: kepala shift pagi"],
         ["Kendala utama", "Staf sore keberatan jamnya digeser"],
         ["Rencana pemulihan", "Bila staf tidak bisa, gunakan satu orang paruh waktu selama masa uji"]],
        [0.26, 0.74]))
    st += render("""
#### Catatan tinjauan mingguan

| Minggu | Transaksi pagi | Hambatan | Perubahan kecil |
|---|---|---|---|
| 1 | 61 | Staf baru belum terbiasa | Didampingi tiga hari pertama |
| 2 | 66 | Pesanan menu rumit menumpuk | Menu rumit tidak dijual sebelum 07.30 |
| 3 | 69 | Tidak ada | Menambah penyiapan awal untuk dua menu |
| 4 | 71 | Tidak ada | Tidak ada perubahan |

Perhatikan bahwa angka tidak langsung melonjak. Pada minggu pertama justru baru 61, karena staf baru perlu menyesuaikan diri. Inilah sebabnya tinjauan mingguan penting: tanpa itu, perbaikan ini mungkin dihentikan terlalu cepat pada hari kelima.

## Langkah 7 \u00b7 Drive: mengunci hasil

Hasil empat minggu tidak boleh hilang ketika pemilik kedai pergi berlibur atau ada staf baru.
""")
    st.append(tool_table(
        ["Penggerak", "Isi"],
        [["Standar kerja", "Satu kartu di dapur: \"Sebelum 08.00, dua orang bertugas. Menu rumit "
          "dibuka 07.30.\""],
         ["Pemilik standar", "Kepala shift pagi"],
         ["Pelatihan", "Kartu standar dibahas di hari pertama setiap staf baru"],
         ["Pengukuran lanjutan", "Transaksi pagi dicatat harian, dibahas setiap Senin"],
         ["Tinjauan", "Jadwal dan standar ditinjau setiap kuartal, karena pola pelanggan berubah"],
         ["Batas peringatan", "Bila transaksi pagi turun di bawah 60 selama seminggu, tinjauan "
          "dipercepat"]],
        [0.26, 0.74]))
    st += render("""
## Hasil akhir dan pelajaran

Dalam dua bulan, transaksi pagi kembali ke 72 per hari, bahkan melampaui tingkat sebelum penurunan. Omzet bulanan pulih, dan yang lebih penting, kedai sekarang punya cara memeriksa masalah, bukan hanya menebak.

#### Tujuh pelajaran dari satu kasus kecil

- **Detect.** Rata-rata harian menyembunyikan penurunan yang hanya terjadi di satu blok waktu.
- **Define.** Kalimat masalah berangka menghapus dua usulan yang tidak relevan.
- **Dig.** Tabel pengujian dugaan menyelamatkan waktu, karena dugaan pertama salah.
- **Design.** Lima opsi menemukan pilihan yang tidak terpikirkan pada awalnya.
- **Decide.** Kriteria membuat keputusan bisa dijelaskan, bahkan kepada staf yang keberatan.
- **Do.** Tinjauan mingguan menjaga perbaikan tidak dihentikan terlalu cepat.
- **Drive.** Standar membuat hasil bertahan meski orangnya berganti.

Perhatikan bahwa seluruh proses ini bisa dikerjakan dalam dua lembar kertas. Tidak ada perangkat lunak, tidak ada konsultan, dan tidak ada anggaran besar. Yang ada hanya urutan, data, dan disiplin.
""")
    st.append(keyline("Tujuh langkah bukan upacara. Ia cara paling murah untuk memastikan tenaga tidak terbuang."))
    st.append(callout("practice", "Kerjakan versimu sendiri", [
        para("Ambil satu masalah kecil di sekitarmu \u2014 bisa masalah kerja, masalah rumah, "
             "atau kebiasaanmu sendiri. Kerjakan tujuh langkah ini dalam dua lembar kertas. "
             "Batas waktunya: tujuh puluh menit. Kamu akan terkejut betapa banyak yang bisa "
             "diselesaikan dalam waktu sesingkat itu."),
    ]))
    st.append(worksheet_block(
        "WS-CONTOH", "Lembar Ringkas Tujuh Langkah", "Untuk masalah kecil apa pun",
        [{"label": "D1 \u00b7 Ukuran sekarang, ukuran tujuan, sebaran", "lines": 3},
         {"label": "D2 \u00b7 Kalimat masalah satu baris", "lines": 2},
         {"label": "D3 \u00b7 Akar & cara verifikasinya", "lines": 3},
         {"label": "D4 \u00b7 Tiga opsi", "lines": 3},
         {"label": "D5 \u00b7 Kriteria & pilihan", "lines": 3},
         {"label": "D6 \u00b7 Angka tunggal, langkah harian, pemicu", "lines": 3},
         {"label": "D7 \u00b7 Standar & pemilik", "lines": 3}],
    ))
    return st
