# 6 November 2026: ChoraleStudio dari PRD ke installer

## Yang dikerjakan

- Mengerjakan [ChoraleStudio](../projects/choralestudio.md) per segmen, dari fondasi proyek (Segmen 0) sampai Setup.exe (Segmen 9). Hari ini mencakup layar perekaman, proses produksi, dan pemaketan.
- Memakai pola yang sama di setiap segmen: baca spesifikasi (PRD), tulis rencana maksimal 10 poin, kerjakan, jalankan tes, catat hasilnya di `PROGRESS.md`, lalu commit dan push.
- Menutup Segmen 9: 241 tes lulus, benchmark 34,4 detik untuk lagu 4 menit, stress test 60 menit tanpa dropout, dan Setup.exe 87 MB yang berjalan di laptop tanpa Python.
- Mendokumentasikan dua hal untuk orang awam: panduan pengguna bergambar dan daftar uji lapangan.

## Catatan

- Membagi pekerjaan besar menjadi segmen kecil membuat setiap langkah punya bukti selesai yang jelas: ada tes, ada angka, ada commit.
- Aturan proyek yang ditulis di awal (misalnya "suara penyanyi tidak diputar ulang oleh aplikasi") terbukti berguna saat ada informasi baru. Ketika ternyata sound card hanya punya tombol direct monitor ON/OFF dan bukan kenop, aturannya tetap berlaku dan hanya teks petunjuk yang perlu diganti.
- Hasil yang belum teruji harus dicatat sebagai "belum diuji", bukan "lulus". Tabel kriteria penerimaan di `PROGRESS.md` memakai tiga status: lulus, gagal, belum diuji.

## Berikutnya

- [ ] Menyambungkan sound card SPL Audio SC202HD, lalu kalibrasi dan uji sinkronisasi
- [ ] Rekam nyanyian asli dan menilai kualitas vokalnya dengan telinga
- [ ] Uji kegunaan: anggota baru menyelesaikan satu lagu dengan panduan di layar
