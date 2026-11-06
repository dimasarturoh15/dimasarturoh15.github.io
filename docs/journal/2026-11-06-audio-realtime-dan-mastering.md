# 6 November 2026: Belajar audio real-time dan standar YouTube

## Yang dipelajari

- **Callback audio tidak boleh menunggu.** Fungsi yang dipanggil sound card ratusan kali per detik hanya boleh menyalin data ke sebuah buffer. Menulis ke disk, mencatat log, atau menyentuh antarmuka di dalamnya membuat suara putus-putus (dropout). Penulisan ke disk dikerjakan thread lain lewat ring buffer.
- **Rekaman harus tahan listrik padam.** Header berkas WAV diperbarui setiap detik, sehingga rekaman yang terputus masih bisa dibuka dan paling banyak 1 detik hilang.
- **Tiga ukuran yang berbeda.** LUFS menyatakan kelantangan yang terdengar, True Peak menyatakan puncak sinyal setelah diubah ke analog, dan LRA menyatakan rentang dinamika. Untuk YouTube, urutan prioritasnya True Peak di bawah -1,0 dBTP (mutlak), lalu -14 LUFS ±1, lalu LRA yang hanya dilaporkan.
- **Limiter yang jujur memakai oversampling.** Puncak di antara dua sampel bisa lebih tinggi daripada puncak sampel itu sendiri. Limiter dengan oversampling 4 kali menangkap puncak itu, sehingga angka True Peak yang dilaporkan benar.
- **Mengukur ulang dengan alat lain.** Hasil pengukuran aplikasi dicek dengan filter ebur128 di FFmpeg. Selisihnya 0,04 LU pada lagu uji, sehingga angkanya bisa dipercaya.
- **Menyamakan kelantangan, bukan puncak.** Volume tiap suara diseimbangkan dengan LUFS karena telinga menilai keras berdasarkan energi, bukan puncak sesaat.

## Kendala

- Pengodean ke MP3 bisa menaikkan puncak sinyal sedikit. Karena itu aplikasi mengukur ulang MP3 hasil encoding, dan bila puncaknya lewat -1,0 dBTP, MP3 dikecilkan sedikit dan hal itu dicatat sebagai peringatan di laporan.

## Catatan

- Rekaman paduan suara asli dari dataset terbuka (Universitat Pompeu Fabra, lisensi CC BY-NC) dipakai sebagai bahan uji. Hasilnya -14,0 LUFS dan -1,2 dBTP, dan berkasnya hanya dipakai untuk uji, tidak diunggah.

## Berikutnya

- [ ] Menilai hasil dengan telinga pada rekaman nyanyian dari ruang latihan yang sebenarnya
