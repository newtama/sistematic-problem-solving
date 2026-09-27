"""D3 - Dig: menemukan akar, bukan daunnya."""
from reportlab.platypus import PageBreak

from theme import *  # noqa
from engine import styles, H, sp, para, PullQuote
from dsl import render
from components import (h2, h3, h4, rule, caption, callout, keyline, StatRow,
                        QRPanel, tool_table, worksheet_block, case_study, WriteLines)
from stepchapter import Step, t

S = styles()

STEP = Step(
    "D3", "5", "Dig",
    "Langkah 3 dari 7 \u00b7 Menemukan akar, bukan daunnya",
    "Berhenti di sebab pertama hampir selalu berarti menambal gejala. Akar biasanya tiga sampai lima lapis lebih dalam.",
    ["Mengapa kita berhenti terlalu cepat",
     "5 Whys, diagram tulang ikan, dan Pareto",
     "Tool: Peta Akar + uji verifikasi",
     "Studi kasus: cacat produksi turun 60%",
     "Worksheet TUNTAS D3 + QR toolkit"],
    STEP_COLORS["D3"])


def build():
    st = []
    st += STEP.opener()
    st += t("""
## Cerita pembuka: mesin yang mogok setiap Senin

Sebuah pabrik pengemasan punya masalah yang membuat kepala produksi kehilangan rambutnya. Mesin utama di lini dua berhenti mendadak hampir setiap Senin pagi. Bukan setiap hari. Setiap Senin. Sudah dua orang teknisi dikerahkan penuh waktu untuk kasus ini.

Jawaban pertama: komponen cepat aus. Solusinya mengganti komponen lebih sering. Biayanya naik, masalahnya tidak hilang.

Jawaban kedua, setelah beberapa minggu: getaran berlebih pada pemanasan awal. Solusinya menambah penjadwalan pemanasan. Masih tidak hilang.

Jawaban ketiga datang dari seorang operator lama yang biasanya hanya diam. Ia bertanya satu hal yang tidak pernah ditanyakan: "Kenapa hanya Senin?" Semua orang terdiam. Pabrik berhenti Sabtu dan Minggu. Suhu ruangan turun selama akhir pekan. Pada Senin pagi, pelumas mengental jauh lebih tebal daripada hari kerja biasa. Ketika mesin dinyalakan, beban awalnya jauh lebih berat.

Perbaikannya bukan komponen baru, bukan jadwal baru, tetapi satu hal kecil: satu lampu pemanas di sekitar bantalan, dinyalakan sejak Minggu malam. Biaya perbaikan setara sekali makan tim. Masalah dua tahun selesai dalam satu minggu setelah pertanyaan yang benar diajukan.
""")
    st.append(keyline("Pertanyaan \"kenapa\" tiga lapis lebih dalam hampir selalu menemukan jawaban yang jauh lebih murah."))
    st += t("""
## Kenapa kita berhenti terlalu cepat

Ada alasan psikologis dan alasan sosial. Secara psikologis, kita merasa sudah selesai begitu menemukan penjelasan yang masuk akal, bukan penjelasan yang benar. Secara sosial, pertanyaan lanjutan terasa seperti menantang orang, terutama bila jawaban pertama datang dari atasan.

Akibatnya, sebagian besar perbaikan di dunia ini adalah perbaikan lapis pertama. Dan perbaikan lapis pertama punya ciri khas: mahal, berulang, dan melelahkan.
""")
    st.append(callout("research", "Mengapa mencari akar itu masuk akal secara ekonomi", [
        para("Prinsip perbaikan berkelanjutan yang berakar pada sistem produksi modern berdiri di "
             "atas satu ide: masalah yang sama tidak boleh diselesaikan dua kali. Setiap kali "
             "sebuah masalah kembali, organisasi membayar biaya perbaikan, biaya gangguan, dan "
             "biaya kepercayaan yang hilang. Mencari akar lebih mahal di depan, tetapi jauh "
             "lebih murah di keseluruhan."),
        para("Di sisi kognitif, penelitian tentang cara orang menjelaskan sebab menemukan bahwa "
             "penjelasan pertama yang muncul biasanya bersifat dangkal dan berpusat pada orang. "
             "Pertanyaan lanjutan yang dipandu struktur menggeser penjelasan ke arah proses dan "
             "sistem, dan di situlah perbaikan yang bertahan biasanya berada."),
    ]))
    st += t("!fig whys")

    st += t("""
## Alat 1: Lima Pertanyaan Kenapa (5 Whys)

Alat paling sederhana dan paling sering diremehkan. Caranya: tuliskan gejala, lalu tanyakan "kenapa" sampai tiga sampai lima kali. Setiap jawaban harus berdasarkan fakta yang bisa kamu periksa, bukan dugaan.
""")
    st.append(tool_table(
        ["Lapis", "Pertanyaan", "Jawaban (harus berbasis fakta)"],
        [["Gejala", "\u2014", "Mesin lini 2 berhenti setiap Senin pagi"],
         ["Whys 1", "Kenapa berhenti?", "Beban awal motor terlalu tinggi"],
         ["Whys 2", "Kenapa beban awal tinggi?", "Pelumas lebih kental dari biasanya"],
         ["Whys 3", "Kenapa pelumas lebih kental?", "Suhu ruangan turun selama akhir pekan"],
         ["Whys 4", "Kenapa suhu rendah jadi masalah?", "Tidak ada pemanasan sebelum start"],
         ["Whys 5", "Kenapa tidak ada pemanasan?", "Prosedur start tidak mempertimbangkan jeda akhir pekan"]],
        [0.14, 0.34, 0.52]))
    st.append(caption("Tabel. Contoh 5 Whys yang berakhir pada prosedur, bukan pada orang. "
                      "Perhatikan bahwa akarnya bisa diubah dengan biaya kecil."))

    st += t("""
## Alat 2: Diagram Tulang Ikan (sebab berlapis)

Ketika masalahnya besar dan banyak orang punya dugaan berbeda, diagram tulang ikan membantu menampung semua dugaan lalu mengujinya. Bagian tulang biasanya mengikuti kategori: manusia, mesin, metode, material, pengukuran, dan lingkungan.
""")
    st += t("!fig fishbone")
    st.append(tool_table(
        ["Kategori", "Pertanyaan pemandu"],
        [["Manusia", "Apakah ada keterampilan, kebiasaan, atau beban kerja yang berpengaruh?"],
         ["Mesin", "Apakah alat atau sistem berkontribusi, termasuk perawatannya?"],
         ["Metode", "Apakah prosedur dan urutan kerjanya masih cocok untuk kondisi sekarang?"],
         ["Material", "Apakah bahan, data, atau masukan yang dipakai bermutu cukup?"],
         ["Pengukuran", "Apakah cara kita mengukur bisa salah atau menyesatkan?"],
         ["Lingkungan", "Apakah kondisi sekitar, waktu, atau tempat berpengaruh?"]],
        [0.22, 0.78]))

    st += t("""
## Alat 3: Pareto 80/20 untuk memilih akar yang layak

Setelah semua dugaan dikumpulkan dan diuji, biasanya akan terlihat bahwa sebagian kecil sebab menyumbang sebagian besar masalah. Di sinilah Pareto bekerja: urutkan sebab berdasarkan besar kontribusinya, lalu pilih yang paling besar untuk dikerjakan lebih dulu.
""")
    st += t("!fig pareto")
    st.append(keyline("Selesaikan sebab yang paling besar lebih dulu. Sisa masalahnya akan menyusut sendiri."))

    st += t("""
## Langkah demi langkah menjalankan D3

### Langkah 1: Tuliskan masalah dari D2 sebagai titik mula
Gunakan kalimat masalah yang sudah tajam. Jangan mulai dari keluhan mentah.

### Langkah 2: Kumpulkan semua dugaan tanpa menghakimi
Gunakan tulang ikan. Tampung semua dugaan, termasuk yang terdengar aneh. Yang aneh sering jadi kunci.

### Langkah 3: Ubah dugaan menjadi pernyataan yang bisa diperiksa
Setiap tulang harus berubah menjadi pernyataan seperti: "Jika X benar, maka pada data akan terlihat Y." Kalau tidak bisa diubah, dugaan itu belum layak diperiksa.

### Langkah 4: Jalankan 5 Whys pada dugaan yang paling kuat
Jangan jalankan 5 Whys pada semua dugaan. Pilih dua atau tiga yang paling mungkin, lalu gali dalam.

### Langkah 5: Verifikasi akarnya dengan data
Ini langkah yang membedakan analisis dari cerita. Sebelum menerima sebuah akar, cari bukti bahwa akar itu memang berperan. Cara paling kuat: matikan sementara akarnya dan lihat apakah masalahnya berkurang.

### Langkah 6: Urutkan dengan Pareto
Setelah akar terverifikasi, urutkan berdasarkan kontribusinya. Kerjakan yang paling besar dulu.

### Langkah 7: Tulis rantai sebab secara utuh
Tuliskan dari gejala sampai akar sebagai rantai. Rantai yang jelas akan membuat solusi di D4 hampir menulis dirinya sendiri.
""")
    st.append(callout("warning", "Empat kesalahan paling umum di D3", [
        para("<b>1. Berhenti pada sebab yang berbunyi nama orang.</b> Kalau akarmu berakhir pada "
             "\"kurang teliti\" atau \"kurang peduli\", kamu belum sampai akar. Tanyakan: apa yang "
             "membuat ketelitian sulit dilakukan?"),
        para("<b>2. Menjalankan 5 Whys tanpa data.</b> Jawaban yang tidak diperiksa hanya "
             "memperpanjang cerita, bukan menambah pemahaman."),
        para("<b>3. Mencari satu akar tunggal.</b> Sebagian besar masalah punya beberapa akar "
             "yang saling memperkuat. Mencari satu akar bisa membuat analisis jadi sempit."),
        para("<b>4. Berhenti pada sebab yang di luar kendali.</b> \"Pasar sedang lesu\" mungkin "
             "benar, tetapi tidak membantu. Cari akar yang bisa kamu pengaruhi."),
    ]))

    st.append(sp(4))
    st.append(case_study(
        "4", "Pabrik Komponen", "Cacat produksi turun 60%",
        "Pola nyata \u00b7 dua lini produksi \u00b7 90 hari",
        [("GEJALA",
          "Tingkat cacat naik dari 2,1% menjadi 4,8% dalam empat bulan. Rencana awal: "
          "memperketat pemeriksaan akhir dan menambah inspektur mutu."),
         ("KENAPA RENCANA AWAL SALAH",
          "Menambah pemeriksaan akhir hanya akan menangkap cacat lebih banyak, tetapi "
          "tidak menghentikan penyebabnya. Ini sama dengan memasang jaring lebih banyak "
          "di bawah pohon yang buahnya berjatuhan."),
         ("D3 \u00b7 ANALISIS",
          "Tim mengumpulkan semua cacat dan mengelompokkannya. Ternyata 71% cacat berasal "
          "dari satu jenis: permukaan tergores, dan hampir seluruhnya terjadi di satu "
          "stasiun kerja pada pergantian shift."),
         ("5 WHYS PADA CACAT TERGORES",
          "Kenapa tergores? Karena komponen bersentuhan dengan jalur saat dipindahkan. "
          "Kenapa bersentuhan? Karena baki tidak terpasang sempurna. Kenapa tidak terpasang? "
          "Karena klip baki aus. Kenapa cepat aus? Karena saat pergantian shift, baki "
          "dibersihkan dengan cara yang mempercepat keausan. Kenapa cara itu dipakai? Karena "
          "prosedur kebersihan yang lama masih beredar dan tidak pernah diperbarui."),
         ("VERIFIKASI",
          "Tim menguji: satu shift memakai cara pembersihan lama, satu shift memakai cara baru. "
          "Pada shift dengan cara lama, cacat gores muncul kembali dalam tiga hari. "
          "Akar terverifikasi."),
         ("PERBAIKAN",
          "Prosedur kebersihan diperbarui, klip baki diganti dengan bahan lebih tahan, dan "
          "pemeriksaan hanya dipasang sebagai pengaman, bukan sebagai solusi."),
         ("HASIL 90 HARI",
          "Cacat turun dari 4,8% menjadi 1,9%, turun sekitar 60% dari puncaknya. Biaya "
          "perbaikan jauh lebih kecil daripada biaya satu bulan tambahan inspeksi."),
        ]))

    st += t("""
## Rangkuman bab

- Berhenti pada sebab pertama adalah penyebab utama perbaikan yang berulang.
- Tiga alat utama: 5 Whys, tulang ikan, dan Pareto.
- Setiap dugaan harus diubah menjadi pernyataan yang bisa diperiksa.
- Akar yang diterima wajib diverifikasi dengan data, bukan dengan kesepakatan.
""")
    from content import extras
    st += extras.build("D3")
    from content import case2
    st += case2.build("D3")
    st.append(QRPanel("https://tuntas7d.id/toolkit/d3", "Toolkit D3: Dig",
                      "Lembar 5 Whys, template tulang ikan, kalkulator Pareto",
                      "QR-D3"))
    st.append(worksheet_block(
        "WS-D3", "Peta Akar Masalah", "Dari gejala sampai akar yang terverifikasi",
        [{"label": "Masalah dari D2 (satu kalimat)", "lines": 2},
         ("table", ["Kategori tulang ikan", "Dugaan sebab", "Cara memeriksa"],
          [["Manusia", "", ""],
           ["Mesin / alat", "", ""],
           ["Metode / prosedur", "", ""],
           ["Material / data", "", ""],
           ["Pengukuran", "", ""],
           ["Lingkungan", "", ""]],
          [0.26, 0.40, 0.34]),
         {"label": "5 Whys untuk dugaan terkuat (gejala \u2192 1 \u2192 2 \u2192 3 \u2192 4 \u2192 5)",
          "lines": 6},
         {"label": "Verifikasi: bagaimana aku membuktikan akar ini benar?", "lines": 3},
         {"label": "Urutan Pareto: akar mana yang menyumbang paling besar?", "lines": 2}],
    ))
    return st
