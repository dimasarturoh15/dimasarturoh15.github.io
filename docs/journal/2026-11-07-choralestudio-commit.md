# 7 November 2026: Catatan commit ChoraleStudio (1 commit)

Halaman ini dibuat otomatis dari riwayat Git [ChoraleStudio](../projects/choralestudio.md) setiap kali ada commit. Isinya adalah pesan commit apa adanya.

## Ringkasan

- Jumlah commit: 1
- Perubahan: 2 berkas, +29 / -2 baris
- Rentang waktu: 18:51 sampai 18:51

## Yang dikerjakan

### 18:51 · Uji hardware SC202HD: kalibrasi dan sinkronisasi

Commit [`2a0a9d5`](https://github.com/dimasarturoh15/ChoraleStudio/commit/2a0a9d5034b46d121eb55a3887baf82c8905f1f5) · 2 berkas, +29 / -2 baris

- Catat hasil uji SC202HD di PROGRESS: WASAPI Exclusive 0 dropout, latensi
  tidak konsisten antar-stream (2-3 ms, kadang ~10 ms) dan lompatan diam-diam
  di dalam stream; uji sinkron 1,33-1,49 ms (batas PRD 1 ms)
- sync_test.py menolak take berisi derau (puncak &lt; -50 dBFS atau keyakinan
  &lt; 1000) agar tidak menghasilkan angka selisih palsu
