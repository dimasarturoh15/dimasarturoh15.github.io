# 6 November 2026: Catatan commit ChoraleStudio (8 commit)

Halaman ini dibuat otomatis dari riwayat Git [ChoraleStudio](../projects/choralestudio.md) setiap kali ada commit. Isinya adalah pesan commit apa adanya.

## Ringkasan

- Jumlah commit: 8
- Perubahan: 234 berkas, +19322 / -322 baris
- Rentang waktu: 14:11 sampai 22:07

## Yang dikerjakan

### 14:11 · Tambah PRD v1.1 dan desain UI

Commit [`d3fe60e`](https://github.com/dimasarturoh15/ChoraleStudio/commit/d3fe60e93fabb5e51f42ee4dda3a723aed86c4ee) · 22 berkas, +4093 / -0 baris

### 14:38 · Segmen 0: fondasi proyek

Commit [`e9c34ce`](https://github.com/dimasarturoh15/ChoraleStudio/commit/e9c34ce0c140867638d749a7bd317ad2aaca0d38) · 15 berkas, +482 / -1 baris

- CLAUDE.md berisi aturan proyek
- Struktur paket src/chorale/{audio,project,dsp,ui}, tools/, tests/
- requirements.txt dengan versi dikunci, pyproject.toml untuk pytest
- docs/PRD_v1.1.md (salinan Markdown dari PDF) dan docs/PROGRESS.md
- README.md dan .gitignore dilengkapi
- Tes asap import semua modul

### 16:29 · Segmen 5: mastering dan ekspor

Commit [`37d370f`](https://github.com/dimasarturoh15/ChoraleStudio/commit/37d370f3e464e2e6ba98b3f0eb0d740849fd0d8c) · 45 berkas, +6313 / -6 baris

Mastering standar YouTube (FR-7), pengukuran BS.1770-4/EBU R128, dan
ekspor WAV 24-bit + MP3 320 kbps + laporan (FR-8). Gerbang Sprint 2
lulus: Contoh SATB -14,1 LUFS / -1,15 dBTP (FFmpeg cocok), produce()
33,8 detik untuk lagu 4 menit 5 track.

Commit ini juga memuat pekerjaan Segmen 1-4 yang belum pernah di-commit:
- Segmen 1: skrip uji hardware (daftar perangkat, WASAPI, kalibrasi
  latensi, stress test)
- Segmen 2: model proyek & take, engine rekam/putar, level meter
- Segmen 3: metronom, kompensasi latensi, CLI 5 track, uji sinkron
- Segmen 4: rantai pascaproduksi FR-5/FR-6 (DeepFilterNet ditunda)

Uji di SC202HD (kalibrasi, uji sinkron loopback, stress test 60 menit,
demo rekam) masih tertunda karena perangkat belum terdeteksi Windows.
Stress test 60 menit lulus di sound card bawaan (Realtek). Lihat
docs/PROGRESS.md. 192 tes lulus.

### 16:53 · Segmen 6: kerangka UI, daftar proyek, pengaturan

Commit [`7a0fd9e`](https://github.com/dimasarturoh15/ChoraleStudio/commit/7a0fd9e4cc7428e91db26365d1b61dd529ee70de) · 38 berkas, +2757 / -129 baris

- Tema PySide6 sesuai mockup (token warna, Inter + JetBrains Mono OFL,
  teks minimal 13 px), ikon garis buatan sendiri, widget bersama
- Jendela utama 1440x900 (minimal 1280x800) dengan QStackedWidget
- Layar Daftar Proyek dari recent.json, titik status 5 track,
  Buka Proyek Lain dengan dialog folder
- Dialog Proyek Baru (validasi judul, tempo 40-240, folder
  Documents\HarmoniSATB\&lt;judul> yang bisa diganti)
- Layar Pengaturan dua kolom: sound card, mode driver, buffer,
  pemetaan input dengan meter live, kalibrasi latensi di QThread
- Logika kalibrasi dipindah ke chorale.audio.calibration
- Titik masuk python -m chorale; screenshot di docs/screenshots
- 206 tes lulus

### 18:26 · Segmen 7: layar utama perekaman

Commit [`7242174`](https://github.com/dimasarturoh15/ChoraleStudio/commit/72421746d5d64fab02552a4464feb292e6b64dad) · 28 berkas, +2803 / -44 baris

- Layar perekaman: bar atas dengan pil status, transport (Ke Awal,
  Putar, Stop, jam), Tempo/Birama/Hitungan Awal, metronom + volume
- 5 bilah track: tombol rekam 72 px tiga status, Solo/Mute, volume
  -12..+6 dB, panel Pilih Take (pratinjau, Tidak lengkap, Rekam Ulang),
  waveform dari audio asli (peak di-cache), meter vertikal + lampu clip
- Status merekam: banner, jam merah, playhead, kontrol lain diredupkan
- Bar produksi: Ruang, Jumlah Reverb, tombol Proses Produksi & Master
  aktif setelah 5 track terisi
- Wizard Persiapan Rekam Vokal 3 langkah dengan meter target
- Dialog Sound card terputus dengan Hubungkan Ulang sungguhan
- Engine dibaca lewat QTimer 30 fps, tanpa sinyal Qt dari callback
- Shortcut Spasi (Putar/Stop) dan R (rekam track terpilih)
- 222 tes lulus; screenshot 08-13 (audio disimulasikan)

Uji manual dengan SC202HD masih menunggu perangkat tersambung.

### 20:26 · Segmen 8: proses produksi dan hasil

Commit [`4574a16`](https://github.com/dimasarturoh15/ChoraleStudio/commit/4574a162a3b4b4805239c67d6bd6bc264f7c5d7a) · 35 berkas, +1588 / -55 baris

- Dialog Memproses Produksi: produce() di QThread, progress bar, persen,
  perkiraan sisa waktu, checklist 7 tahap (selesai/berjalan/menunggu/
  dilewati), Batalkan yang benar-benar menghentikan proses termasuk
  FFmpeg dan menghapus file setengah jadi
- Layar Hasil Produksi: waveform master, putar + posisi waktu, A/B
  Mentah/Master dengan kelantangan disamakan tanpa memutus posisi,
  Laporan Mastering (centang/peringatan, Siap YouTube), Ekspor 3 file,
  Buka Folder Hasil (Explorer), Kembali & Ubah Pengaturan, Proses Ulang
- Alur penuh di jendela utama: Rekam -> Proses -> Hasil -> Kembali
- tools/import_takes.py untuk mengisi 5 track dari file WAV
- Perbaikan: Stop saat sesi disiapkan, detik tersimpan saat sound card
  terputus, crash Qt saat proses keluar
- 235 tes lulus; screenshot 14-17

### 21:56 · Segmen 9: installer dan dokumen uji lapangan

Commit [`7fdccd7`](https://github.com/dimasarturoh15/ChoraleStudio/commit/7fdccd723cc12926b779ae12859002d6ba115368) · 50 berkas, +1276 / -83 baris

- Versi 1.1.0; build PyInstaller onedir tanpa konsol (font, ikon, FFmpeg,
  PortAudio ber-ASIO), skrip Inno Setup dan tools/build_installer.py
- Log berotasi di %APPDATA%\HarmoniSATB\logs, dialog error ramah, uji mandiri
  (--uji-mandiri)
- Halaman Tentang: versi dan lisensi pihak ketiga
- Waktu buka dipercepat (import DSP ditunda ke latar)
- docs/UJI_LAPANGAN.md dan docs/PANDUAN_PENGGUNA.md bergambar
- SC202HD memakai tombol direct monitor ON/OFF: teks UI, PRD, dokumen disesuaikan
- Hasil akhir: 241 tes lulus, benchmark 34,4 s, stress test 60 menit 0 dropout
- Setup.exe dan tag v1.1.0 menunggu Inno Setup terpasang

### 22:07 · Segmen 9: Setup.exe dibuat dan diuji di laptop

Commit [`3cc0519`](https://github.com/dimasarturoh15/ChoraleStudio/commit/3cc0519d200e02e8ba97056d83f69d99608d8f26) · 1 berkas, +10 / -4 baris
