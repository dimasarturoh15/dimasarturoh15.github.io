# 8 November 2026: Catatan commit ChoraleStudio (2 commit)

Halaman ini dibuat otomatis dari riwayat Git [ChoraleStudio](../projects/choralestudio.md) setiap kali ada commit. Isinya adalah pesan commit apa adanya.

## Ringkasan

- Jumlah commit: 2
- Perubahan: 28 berkas, +109 / -28 baris
- Rentang waktu: 00:46 sampai 01:02

## Yang dikerjakan

### 00:46 · Cek gain untuk setiap kelompok suara vokal

Commit [`6df99f8`](https://github.com/dimasarturoh15/ChoraleStudio/commit/6df99f8a49b750966cba141ece7e1bb0fadf46a9) · 20 berkas, +88 / -16 baris

- Persiapan Rekam Vokal bisa dimulai di langkah "Atur Gain Mic"
  (start_step); dipakai saat pertama kali merekam kelompok suara vokal
  berikutnya. Panduan penuh tetap sekali per proyek; rekam ulang suara
  yang sama tidak ditanya
- ui_screenshots.py memperhitungkan pemanasan dan cek gain; screenshot
  "Sound card terputus" kembali menampilkan detik yang benar
- Panduan pengguna, CHANGELOG, PROGRESS; 257 tes lulus

### 01:02 · Rilis 1.3.0: cek gain per kelompok suara

Commit [`7b3f2be`](https://github.com/dimasarturoh15/ChoraleStudio/commit/7b3f2beda292c6378d33ae89ce03bbcb7031c543) · 8 berkas, +21 / -12 baris

- Versi 1.3.0 di aplikasi, pyproject, skrip Inno Setup, README, panduan
- CHANGELOG 1.3.0, PROGRESS
- Setup.exe 1.3.0 dibangun, dipasang di laptop, dan lulus uji tanpa Python
