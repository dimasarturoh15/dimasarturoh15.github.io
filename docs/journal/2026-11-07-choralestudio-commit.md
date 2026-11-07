# 7 November 2026: Catatan commit ChoraleStudio (2 commit)

Halaman ini dibuat otomatis dari riwayat Git [ChoraleStudio](../projects/choralestudio.md) setiap kali ada commit. Isinya adalah pesan commit apa adanya.

## Ringkasan

- Jumlah commit: 2
- Perubahan: 17 berkas, +295 / -32 baris
- Rentang waktu: 18:51 sampai 19:12

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
