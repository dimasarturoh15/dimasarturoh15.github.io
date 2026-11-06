# Dimas Arturoh: portofolio

Situs dokumentasi berbasis **MkDocs (tema Material)**, dipublikasikan otomatis ke **GitHub Pages** lewat GitHub Actions.

## Struktur

```
.
├── mkdocs.yml                  # konfigurasi situs dan navigasi
├── requirements.txt            # dependensi Python
├── docs/
│   ├── index.md                # beranda
│   ├── projects/               # halaman proyek
│   ├── journal/                # jurnal belajar (sebagian dibuat otomatis dari commit)
├── tools/                      # sinkronisasi commit ke jurnal
└── .github/workflows/deploy.yml  # publikasi otomatis
```

## Langkah pertama kali

1. **Edit `mkdocs.yml`**: sesuaikan `site_name`, `site_author`, dan `site_url`.
2. **Edit `docs/index.md`**: isi data diri dan tautan Anda.
3. **Buat repo baru** di GitHub bernama `USERNAME.github.io`, lalu unggah semua file di folder ini.
4. **Beri izin Actions menulis**: buka *Settings > Actions > General > Workflow permissions*, pilih **Read and write permissions**, lalu simpan.
5. **Jalankan workflow**: buka tab *Actions*, pilih workflow "Deploy dokumentasi", klik *Run workflow* (atau cukup push ke branch `main`).
6. **Aktifkan Pages**: setelah workflow selesai, buka *Settings > Pages*, pada *Source* pilih **Deploy from a branch**, branch `gh-pages`, folder `/ (root)`, lalu simpan.
7. Situs aktif di `https://USERNAME.github.io/`.

## Mencoba di komputer sendiri (opsional)

```bash
pip install -r requirements.txt
mkdocs serve
```

Lalu buka `http://127.0.0.1:8000`. Setiap perubahan file langsung terlihat.

## Menambah halaman

1. Buat file `.md` baru di folder yang sesuai di `docs/`.
2. Daftarkan di bagian `nav` pada `mkdocs.yml`.
3. Commit dan push. Situs diperbarui otomatis dalam 1-2 menit.

## Jurnal otomatis dari commit

`tools/sync_commit.py` menyusun ulang dari riwayat Git: tabel "Log Pengerjaan" di halaman proyek, halaman jurnal harian `docs/journal/<tanggal>-<slug>-commit.md`, indeks jurnal, navigasi, dan daftar jurnal di beranda. Skrip aman dijalankan berulang kali.

Agar berjalan setiap commit, salin `tools/post-commit-hook.sh` ke `.git/hooks/post-commit` di repositori proyek, lalu sesuaikan `SLUG` dan `NAME`. Hook membuat commit `docs: sync <proyek> commit <hash>` di repo ini dan mengunggahnya di latar. Catatan proses ada di `.git/sync-commit.log`.

Menjalankan manual (misalnya untuk tanggal tertentu):

```bash
python tools/sync_commit.py --repo "D:/My Project/ChoraleStudio" --slug choralestudio --name ChoraleStudio --tanggal 2026-11-06
```

Hook hanya berjalan untuk commit yang dibuat di laptop ini. Commit lewat situs GitHub atau komputer lain baru tercatat pada commit lokal berikutnya.

## Masalah umum

- **Workflow gagal dengan error izin**: pastikan langkah 4 sudah dilakukan.
- **Halaman 404 setelah publikasi**: pastikan Pages memakai branch `gh-pages`, dan tunggu beberapa menit.
- **Tampilan berantakan**: periksa `site_url` di `mkdocs.yml`, harus persis sama dengan alamat situs.
