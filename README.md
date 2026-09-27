# TUNTAS 7D — Solusi Sistematis

Buku ajar dan panduan praktik **Pemecahan Masalah Sistematis** (*Systematic Problem Solving*).

Rahasia berpikir jernih, mengambil keputusan tepat, dan menyelesaikan masalah nyata.
Pendekatan praktis untuk mahasiswa, profesional, manajer, dan wirausaha, berbasis metode
yang terbukti berhasil dari Toyota, NASA, Kepner-Tregoe, McKinsey, PMI, Deming, serta Lean & Six Sigma.

## Unduh buku

| Format | Berkas | Keterangan |
|---|---|---|
| PDF (edisi cetak) | [dist/TUNTAS-7D.pdf](dist/TUNTAS-7D.pdf) | 201 halaman, B5 (176 × 250 mm), diagram vektor penuh |
| Word | [dist/TUNTAS-7D.docx](dist/TUNTAS-7D.docx) | ± 207 halaman, 20 diagram tertanam, QR toolkit, daftar isi otomatis |

Di halaman repo, klik berkas lalu tombol **Download**. Untuk unduhan langsung:

```
https://raw.githubusercontent.com/newtama/sistematic-problem-solving/main/dist/TUNTAS-7D.pdf
https://raw.githubusercontent.com/newtama/sistematic-problem-solving/main/dist/TUNTAS-7D.docx
```

## Isi

- **Bagian 0 — Pembuka.** Prolog, tes diagnostik tipe problem solver, cara membaca buku.
- **Bagian 1 — Mindset.** Jebakan bias kognitif; tiga mindset problem solver
  (Curiosity, Clarity, Courage).
- **Bagian 2 — TUNTAS 7D (inti).** Detect · Define · Dig · Design · Decide · Do · Drive.
  Tiap bab berformat sama: cerita pembuka, konsep inti, alat langkah-demi-langkah,
  ringkasan, pendalaman, dan worksheet.
- **Bagian 3 — Scale-Up & Workshop.** Problem solving untuk tim/bisnis dan untuk hidup,
  plus panduan fasilitator workshop satu hari (agenda, role play, kunci jawaban).
- **Penutup.** Bank 12 studi kasus nyata, program 30 hari, glosarium, indeks alat,
  template inti, daftar pustaka ilmiah, dan akses toolkit digital.

Fondasi ilmiahnya kuat: bias kognitif, 5 Whys, diagram tulang ikan, Pareto, SCAMPER,
matriks keputusan berbobot, dan siklus pembakuan standar kerja.

## Struktur repositori

```
src/                 kode pembangun buku
  theme.py           palet warna, font, geometri halaman
  engine.py          template halaman, heading, worksheet, tabel
  dsl.py             perender mini-markdown
  figures.py         diagram vektor
  content/           naskah buku
  build.py           -> output/TUNTAS-7D.pdf   (ReportLab)
  docxbuild.py       -> output/TUNTAS-7D.docx  (python-docx)
  docxkit.py         pembantu OOXML tingkat rendah
  docxstyles.py      gaya paragraf bernama
dist/                berkas siap unduh (PDF + DOCX)
assets/fonts/        Lora (serif isi) dan Inter (sans judul)
```

## Membangun ulang

```bash
pip install reportlab pypdf pypdfium2 python-docx segno pillow
python3 src/build.py        # output/TUNTAS-7D.pdf
python3 src/docxbuild.py    # output/TUNTAS-7D.docx
```

Untuk memeriksa hasil DOCX, konversi ke PDF:

```bash
LD_LIBRARY_PATH=/usr/lib/libreoffice/program \
  soffice --headless --norestore --convert-to pdf --outdir .qa/docx output/TUNTAS-7D.docx
```

## Berkas edisi sebelumnya

- `Pemecahan_Masalah_Sistematis.docx` — dokumen buku ajar versi awal.

## Lisensi

Hak cipta milik penyusun. Silakan hubungi pemilik repositori untuk penggunaan lebih lanjut.
