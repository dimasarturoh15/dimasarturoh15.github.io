# 7 November 2026: Catatan commit ChoraleStudio (5 commit)

Halaman ini dibuat otomatis dari riwayat Git [ChoraleStudio](../projects/choralestudio.md) setiap kali ada commit. Isinya adalah pesan commit apa adanya.

## Ringkasan

- Jumlah commit: 5
- Perubahan: 76 berkas, +957 / -73 baris
- Rentang waktu: 18:51 sampai 23:31

## Yang dikerjakan

### 18:51 · Uji hardware SC202HD: kalibrasi dan sinkronisasi

Commit [`2a0a9d5`](https://github.com/dimasarturoh15/ChoraleStudio/commit/2a0a9d5034b46d121eb55a3887baf82c8905f1f5) · 2 berkas, +29 / -2 baris

- Catat hasil uji SC202HD di PROGRESS: WASAPI Exclusive 0 dropout, latensi
  tidak konsisten antar-stream (2-3 ms, kadang ~10 ms) dan lompatan diam-diam
  di dalam stream; uji sinkron 1,33-1,49 ms (batas PRD 1 ms)
- sync_test.py menolak take berisi derau (puncak &lt; -50 dBFS atau keyakinan
  &lt; 1000) agar tidak menghasilkan angka selisih palsu

### 19:12 · Pilihan 1 SC202HD: target sinkron 3 ms, pemanasan, deteksi lompatan

Commit [`8f2e19c`](https://github.com/dimasarturoh15/ChoraleStudio/commit/8f2e19c935b21d4bc752b8c6983f1518149b1981) · 15 berkas, +266 / -30 baris

- PRD v1.1 rev. 1: target sinkronisasi antar-track &lt;= 3 ms (keputusan
  pengguna setelah uji SC202HD); CLI, uji lapangan, README, sync_test dan
  ambang kalibrasi disesuaikan
- Pemanasan sound card 5 detik sebelum hitungan awal saat merekam (layar
  rekam, CLI, sync_test); layar menampilkan "Menyiapkan sound card ..."
- stress_test.py --loopback: deteksi lompatan latensi yang tidak dilaporkan
  PortAudio sebagai dropout
- Panduan pengguna: persiapan laptop (charger, matikan FxSound dan sejenisnya,
  USB selective suspend mati)
- 5 tes baru; 246 tes lulus. Uji ulang SC202HD: 5,80 ms dan 2,26 ms, jadi
  target 3 ms belum terpenuhi secara andal (dicatat di PROGRESS)

### 19:37 · Kanal acuan sinkronisasi untuk take vokal

Commit [`ac46829`](https://github.com/dimasarturoh15/ChoraleStudio/commit/ac46829b712e8c72311d6257b825b4799d9b8069) · 31 berkas, +505 / -14 baris

- Modul chorale.audio.alignment: ukur latensi sebenarnya tiap take dari
  kanal acuan (kabel Output -> input lain) dan sejajarkan take per segmen,
  termasuk lompatan latensi di tengah lagu; tulis ulang atomik
- AudioSession merekam kanal acuan lewat ring buffer kedua; fallback ke
  kalibrasi dengan peringatan bila acuan tidak terdeteksi
- Opsi "Kanal acuan sinkronisasi" di Pengaturan, pengingat di Persiapan
  Rekam Vokal, sync_test.py --acuan
- PRD v1.1 rev. 2, ARCHITECTURE, panduan, uji lapangan, CLI, CHANGELOG
- 8 tes baru; 254 tes lulus. Uji hardware menyusul.

### 20:25 · Uji hardware kanal acuan di SC202HD dan perbaikan ambang lompatan

Commit [`8f58c09`](https://github.com/dimasarturoh15/ChoraleStudio/commit/8f58c090f36dc0e612c01e213aac08228bbf19f6) · 5 berkas, +65 / -5 baris

- Stress test 60 menit SC202HD: 0 dropout, tetapi 51 lompatan latensi
  diam-diam per jam (terdeteksi --loopback)
- sync_test.py --acuan-satu-kabel: kanal acuan diuji dengan satu kabel;
  hasil 0,43-0,73 ms (tanpa acuan 0,09-5,8 ms)
- JUMP_TOLERANCE 8 -> 24 sampel: klik bernada beda terukur selisih 11
  sampel di hardware dan memicu lompatan palsu; tes regresi ditambah
- PROGRESS dan README diperbarui

### 23:31 · Rilis 1.2.0: tampilan kalibrasi untuk SC202HD dan installer baru

Commit [`8a0f888`](https://github.com/dimasarturoh15/ChoraleStudio/commit/8a0f888d6fec6d332b7ca64c1ab10a85e942e857) · 23 berkas, +92 / -22 baris

- Kalibrasi Latensi: teks tidak lagi menempel; hasil berubah-ubah tampil
  "Berubah-ubah" dengan penjelasan bila kanal acuan aktif, atau
  "Tidak konsisten" (kuning) dengan saran mengaktifkan kanal acuan
- Versi 1.2.0 di aplikasi, pyproject, skrip Inno Setup, README, panduan
- build_installer.py melaporkan Setup.exe sesuai versi
- CHANGELOG 1.2.0; 256 tes lulus; Setup.exe 1.2.0 dipasang dan diuji
