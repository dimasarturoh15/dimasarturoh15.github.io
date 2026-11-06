# 6 November 2026: Pemaketan, lisensi, dan temuan saat uji

## Yang dikerjakan

- Membuat paket aplikasi dengan PyInstaller (folder 328 MB) dan installer Inno Setup (Setup.exe 87 MB) dengan shortcut Start Menu dan Desktop. Data pengguna di `%APPDATA%` tidak ikut terhapus saat uninstall.
- Menambah log berotasi dan pesan kesalahan ramah: traceback lengkap hanya ke berkas log, pengguna melihat pesan sederhana.
- Menambah halaman Tentang Aplikasi berisi versi dan daftar lisensi pihak ketiga.
- Menambah perintah `--uji-mandiri` yang memproses lima track sintetis sampai ekspor, supaya orang lain bisa memastikan aplikasinya sehat tanpa sound card.

## Kendala dan temuan

- **Aplikasi lambat dibuka.** Pengukuran menunjukkan `import scipy.signal` memakan sekitar 11 detik di laptop ini. Dengan menunda pemuatan modul pengolah audio ke thread latar setelah jendela tampil, waktu buka turun dari sekitar 26 detik menjadi sekitar 10 detik.
- **Peluncuran pertama setelah build lambat** (20 sampai 50 detik) karena Windows Defender memindai berkas baru. Setelah itu normal.
- **Lisensi.** Pedalboard dan build FFmpeg yang dibawa aplikasi berlisensi GPL v3. Selama dipakai sendiri tidak ada masalah, tetapi bila Setup.exe dibagikan, kode sumbernya harus bisa diperoleh penerima. Inno Setup juga menyatakan "Non-commercial use only".
- **Bug yang baru ketahuan saat uji.** Tombol Stop yang ditekan saat sesi masih disiapkan tidak membersihkan track yang sedang direkam, dan detik rekaman yang tersimpan saat sound card dicabut dihitung sebelum penulis disk selesai. Keduanya diperbaiki dan ditambah tes regresi.

## Catatan

- Mengukur lebih dulu sebelum mengoptimalkan menghemat waktu: sumber lambatnya ternyata satu import, bukan kode sendiri.
- Fitur yang belum bisa diuji karena perangkat belum tersedia dicatat terbuka di `PROGRESS.md`, bukan dianggap beres.

## Berikutnya

- [ ] Menguji instalasi di komputer lain yang belum pernah memasang Python
- [ ] Memutuskan cara membagikan aplikasi dengan mempertimbangkan GPL v3
