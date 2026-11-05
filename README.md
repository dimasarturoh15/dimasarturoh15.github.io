# dimasarturoh15

Situs dokumentasi berbasis **MkDocs (tema Material)**, dipublikasikan otomatis ke **GitHub Pages** lewat GitHub Actions.

## Struktur

```
.
├── mkdocs.yml                  # konfigurasi situs dan navigasi
├── requirements.txt            # dependensi Python
├── docs/
│   ├── index.md                # beranda
│   ├── projects/               # halaman proyek
│   ├── journal/                # jurnal belajar
└── .github/workflows/deploy.yml  # publikasi otomatis
```

## Langkah pertama kali

1. **Edit `mkdocs.yml`**: ganti `USERNAME` dan `REPO` di `site_url`, `repo_url`, dan `repo_name`, serta `site_author`.
2. **Edit `docs/index.md`**: isi data diri dan tautan Anda.
3. **Buat repo baru** di GitHub (misalnya `dokumentasi-github`), lalu unggah semua file di folder ini.
4. **Beri izin Actions menulis**: buka *Settings > Actions > General > Workflow permissions*, pilih **Read and write permissions**, lalu simpan.
5. **Jalankan workflow**: buka tab *Actions*, pilih workflow "Deploy dokumentasi", klik *Run workflow* (atau cukup push ke branch `main`).
6. **Aktifkan Pages**: setelah workflow selesai, buka *Settings > Pages*, pada *Source* pilih **Deploy from a branch**, branch `gh-pages`, folder `/ (root)`, lalu simpan.
7. Situs aktif di `https://USERNAME.github.io/REPO/`.

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

## Masalah umum

- **Workflow gagal dengan error izin**: pastikan langkah 4 sudah dilakukan.
- **Halaman 404 setelah publikasi**: pastikan Pages memakai branch `gh-pages`, dan tunggu beberapa menit.
- **Tampilan berantakan**: periksa `site_url` di `mkdocs.yml`, harus persis sama dengan alamat situs.
