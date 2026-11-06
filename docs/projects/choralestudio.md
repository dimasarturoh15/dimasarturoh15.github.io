# ChoraleStudio

> Aplikasi desktop Windows untuk merekam paduan suara SATB (Sopran, Alto, Tenor, Bass) dan piano secara bergiliran, lalu membuat master audio siap YouTube dengan satu klik. Dibuat untuk anggota paduan suara yang bukan teknisi audio.

## Dampak

| | Tanpa aplikasi ini | Dengan ChoraleStudio |
|---|---|---|
| Menyiapkan master siap YouTube | Perlu pengetahuan mixing dan mastering di aplikasi audio umum | Satu klik, lagu 4 menit selesai dalam 34 detik (target maksimal 60 detik) |
| Pemasangan | Python dan pustaka dipasang satu per satu | Satu berkas Setup.exe (87 MB), tanpa Python |

## Masalah yang diselesaikan

Merekam paduan suara empat suara biasanya butuh studio dan tenaga ahli. Aplikasi ini memungkinkan satu kelompok merekam tiap suara bergiliran (overdub) dengan satu sound card, mendengar suara yang sudah direkam lewat headphone, lalu mengolah semuanya menjadi master yang memenuhi standar YouTube tanpa mengatur satu pun parameter audio.

## Hasil di aplikasi

<figure markdown="span">
  ![Layar utama perekaman dengan lima track: Piano, Bass, Tenor, Alto, Sopran](../assets/img/chorale-layar-rekam.png){ loading=lazy }
  <figcaption>Layar perekaman: lima track, metronom, dan pengatur ruang di satu jendela.</figcaption>
</figure>

<figure markdown="span">
  ![Dialog Persiapan Rekam Vokal langkah 2: pemantauan level mikrofon](../assets/img/chorale-persiapan-vokal.png){ loading=lazy }
  <figcaption>Persiapan Rekam Vokal: panduan tiga langkah dengan meter level yang menyatakan "Level sudah pas".</figcaption>
</figure>

<figure markdown="span">
  ![Dialog Memproses Produksi dengan tujuh tahap](../assets/img/chorale-memproses.png){ loading=lazy }
  <figcaption>Proses produksi dalam tujuh tahap yang dapat dibatalkan kapan saja.</figcaption>
</figure>

<figure markdown="span">
  ![Layar Hasil Produksi berisi hasil pengukuran dan pembanding mentah dengan master](../assets/img/chorale-hasil.png){ loading=lazy }
  <figcaption>Hasil Produksi: ukuran kelantangan dan puncak, serta perbandingan mentah dengan master.</figcaption>
</figure>

## Alur kerja

```text title="Dari rekaman sampai master"
Rekam per suara (overdub) ─► pilih take terbaik
   ─► 1 peredam derau (opsional) ─► 2 saring frekuensi rendah ─► 3 rapikan karakter suara
   ─► 4 seimbangkan volume antar-suara ─► 5 atur posisi stereo ─► 6 reverb ruangan
   ─► 7 mastering (kompresor bus + limiter) ─► WAV 24-bit, MP3 320 kbps, laporan
```

## Fitur utama

- **Rekam bergiliran dengan metronom dan hitungan awal.** Setiap suara direkam sebagai take sendiri, dan beberapa take dapat dipilih ulang. Latensi sound card dikompensasi otomatis lewat kalibrasi.
- **Rekaman aman dari listrik padam.** Audio ditulis ke disk terus-menerus lewat ring buffer dan thread penulis terpisah, dengan header WAV diperbarui setiap detik, sehingga paling banyak 1 detik hilang.
- **Callback audio yang bersih.** Di jalur real-time hanya ada penyalinan ke buffer: tanpa alokasi besar, tanpa akses disk, tanpa logging, dan tanpa menyentuh objek antarmuka.
- **Driver sesuai prioritas.** ASIO bila ada, lalu WASAPI Exclusive, lalu WASAPI Shared.
- **Panduan persiapan rekam vokal.** Posisi penyanyi, gain mikrofon dengan meter berwarna, dan pengaturan headphone dituntun langkah demi langkah. Suara penyanyi sendiri tidak diputar ulang oleh aplikasi, tetapi lewat tombol direct monitor di sound card.
- **Mastering untuk YouTube dengan prioritas jelas.** True Peak di bawah -1,0 dBTP (mutlak), lalu kelantangan -14 LUFS ±1, lalu rentang dinamika (LRA) yang hanya dilaporkan. Hasilnya diukur ulang secara independen dengan FFmpeg (ebur128).
- **Pembanding mentah dan master (A/B).** Level keduanya disamakan sehingga yang terdengar adalah perbedaan pengolahan, bukan perbedaan keras.
- **Tiga ruang dan tiga takaran reverb.** Gereja Kecil, Aula, dan Katedral, masing-masing dengan jumlah Sedikit, Normal, atau Banyak.
- **Mesin pengolah bisa dijalankan dari baris perintah** tanpa antarmuka, dan seluruh fitur bekerja tanpa internet.
- **Log berotasi dan pesan kesalahan ramah.** Detail teknis hanya masuk ke berkas log, pengguna melihat pesan sederhana dengan tombol "Buka Folder Log".

## Pengujian

| Uji | Hasil |
|---|---|
| Tes otomatis (pytest) | 241 tes lulus |
| Kecepatan proses lagu 4 menit, 5 track | 34,4 detik (target ≤ 60 detik) |
| Stabilitas rekam dan putar, buffer 5,3 ms | 3 kali 60 menit tanpa satu pun dropout (sound card Realtek) |
| Standar YouTube pada sinyal uji ekstrem | True Peak ≤ -1,0 dBTP pada semua berkas uji |
| Rekaman paduan suara asli (dataset terbuka Universitat Pompeu Fabra, lisensi CC BY-NC) | -14,0 LUFS, -1,2 dBTP, selisih dengan FFmpeg 0,04 LU, diproses 15 detik |
| Pemasangan | Setup.exe terpasang dan berjalan di laptop tanpa Python di PATH |

## Status dan batasan

- Uji dengan sound card utama proyek, SPL Audio SC202HD, belum dilakukan: kalibrasi latensi, selisih sinkronisasi antar-track, stress test di perangkat itu, dan rekaman nyanyian asli. Jadwalnya menyusul setelah perangkat tersambung.
- Penilaian kualitas vokal oleh pendengar dan uji kegunaan oleh anggota baru juga belum dilakukan. Panduan ujinya sudah tersedia.
- Peredam derau DeepFilterNet sengaja ditunda sampai rekaman asli bisa didengar, karena peredam derau untuk suara bicara berisiko meninggalkan artefak pada vokal panjang.
- Aplikasi memuat pedalboard dan FFmpeg yang berlisensi GPL v3. Bila pemasangnya dibagikan ke pihak lain, ketentuan GPL v3 berlaku. Daftar lisensi lengkap ada di halaman Tentang Aplikasi.
- Repositori kode belum dibuka untuk umum.

## Teknologi

Python 3.12, PySide6, sounddevice (PortAudio), soundfile, NumPy, SciPy, pedalboard, pyloudnorm, FFmpeg, pytest, PyInstaller, dan Inno Setup.

## Log Pengerjaan

| Waktu | Hash | Ringkasan Perubahan |
|---|---|---|
| 2026-11-06 16:53 | `7a0fd9e` | Segmen 6: kerangka UI, daftar proyek, pengaturan |
| 2026-11-06 18:26 | `7242174` | Segmen 7: layar utama perekaman |
| 2026-11-06 20:26 | `4574a16` | Segmen 8: proses produksi dan hasil |
| 2026-11-06 21:56 | `7fdccd7` | Segmen 9: installer dan dokumen uji lapangan |
| 2026-11-06 22:07 | `3cc0519` | Segmen 9: Setup.exe dibuat dan diuji di laptop |
