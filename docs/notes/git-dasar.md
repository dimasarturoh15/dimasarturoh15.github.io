# Git dasar

Perintah yang paling sering dipakai dalam alur kerja harian.

## Alur kerja inti

```bash
git status                  # lihat perubahan saat ini
git add .                   # tandai semua perubahan untuk di-commit
git commit -m "pesan jelas" # simpan perubahan dengan pesan
git push                    # kirim ke GitHub
git pull                    # ambil perubahan terbaru dari GitHub
```

## Memulai dari repo yang sudah ada

```bash
git clone https://github.com/USERNAME/REPO.git
```

## Menulis pesan commit yang baik

!!! tip
    Tulis apa yang berubah dan kenapa, dalam satu kalimat singkat. Contoh: `Tambah halaman jurnal hari pertama`.

## Perintah untuk melihat riwayat

```bash
git log --oneline           # riwayat ringkas
git diff                    # perubahan yang belum di-add
```
