# 10 November 2026: Catatan commit Paroki Minomartani (3 commit)

Halaman ini dibuat otomatis dari riwayat Git [Paroki Minomartani](../projects/paroki-minomartani.md) setiap kali ada commit. Isinya adalah pesan commit apa adanya.

## Ringkasan

- Jumlah commit: 3
- Perubahan: 47 berkas, +11050 / -15 baris
- Rentang waktu: 02:09 sampai 02:43

## Yang dikerjakan

### 02:09 · docs: backup retention 7/4/3, backups by Worker to R2, kolekte amounts allowed

Commit [`ce4b280`](https://github.com/dimasarturoh15/paroki-minomartani/commit/ce4b280685b0be1efc4601513eac9df1caff3ad0) · 4 berkas, +8 / -8 baris

### 02:27 · feat: activity posts with post-publish moderation and undo (week 7-8 package M)

Commit [`da5a91e`](https://github.com/dimasarturoh15/paroki-minomartani/commit/da5a91efc841d49494856b35500d9a8ac5e7182e) · 25 berkas, +5715 / -3 baris

POST-01..13: units post 1-2 photos (limit in settings posts_max_photos) with title,
date, location, description; unit taken from the account; consent checkbox required;
published at once with Super Users notified. Same-unit edit/delete with wrong-unit
tests; soft delete with one-hour undo, purged with photos after 7 days. Super Users
hide with a reason (unit notified), show again, and pin. Public Kegiatan page with
kind/month/text filters and load more, detail with WhatsApp share and Open Graph,
more from the unit, and Kegiatan terkini on the home page.

### 02:43 · feat: unit directory, unit profile pages, Cari Lingkungan Saya (week 7-8 package N)

Commit [`3be0f1e`](https://github.com/dimasarturoh15/paroki-minomartani/commit/3be0f1e7d43fc0747ecb768018178ba0c6efd7d6) · 18 berkas, +5327 / -4 baris

ORG-06: Direktori Unit under Profil, lingkungan grouped by church and wilayah,
kategorial separate. ORG-07: unit page with cover (or flat accent block), identity,
patron feast, about, meeting schedule, officers, upcoming agenda, gallery from posts,
and posts this year; edited by the unit itself (units.profile.write, own unit) with
wrong-unit tests. ORG-02/08: lingkungan keep their coverage areas; suggestions while
typing, active once any coverage exists, with a Hubungi Sekretariat fallback.
