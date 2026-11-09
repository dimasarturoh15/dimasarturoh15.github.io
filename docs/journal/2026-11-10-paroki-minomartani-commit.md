# 10 November 2026: Catatan commit Paroki Minomartani (6 commit)

Halaman ini dibuat otomatis dari riwayat Git [Paroki Minomartani](../projects/paroki-minomartani.md) setiap kali ada commit. Isinya adalah pesan commit apa adanya.

## Ringkasan

- Jumlah commit: 6
- Perubahan: 119 berkas, +21297 / -72 baris
- Rentang waktu: 02:09 sampai 03:39

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

### 03:02 · feat: structure, accounts, handover, Super User approvals, audit log (week 7-8 package O)

Commit [`a43358d`](https://github.com/dimasarturoh15/paroki-minomartani/commit/a43358d62269292cf5eb80ad48cf4fa1d772700a) · 17 berkas, +2667 / -25 baris

ORG-01..03: manage the unit tree (create, rename, move without cycles, church, order),
positions and holders; units, positions and accounts are deactivated, never deleted
(AUTH-10), and refused while active children or accounts remain. AUTH-06: create an
account with role, position, holder and start date; it can log in at once; roles must
fit the unit type. AUTH-07: handover requires typing SERAH TERIMA, closes the old term,
revokes every session of the position's accounts, and shows plus audits the email
password reminder. AUTH-09: adding or removing a Super User goes through
approval_requests decided by another Super User, re-validated on apply; the last Super
User can never be removed. ADM-05: audit log screen filtered by account, module and WIB
date with paging.

### 03:19 · feat: intention types, settings, dashboard summary, security headers (package P)

Commit [`3fa003a`](https://github.com/dimasarturoh15/paroki-minomartani/commit/3fa003ac233e73651a239d356831b98cd40f3235) · 21 berkas, +1300 / -25 baris

INT-28: Sekretariat and Super User add, edit, reorder and deactivate intention types
(at least one stays active). ADM-06: settings page for photos per post, slide duration,
lector opening/closing text, minimum app version (served at /public/app-config for
APP-11) and the daily manual push limit (PRD suggestion 3); Sekretariat sets the
liturgical label from the schedule page. ADM-02: Ringkasan cards per role (nearest
masses with intention counts and time left, new registrations, waiting approvals,
recent posts, unit posts this month). NFR-06: CSP, HSTS, X-Frame-Options, nosniff,
Referrer-Policy and Permissions-Policy on every web response.

### 03:39 · feat: weekly warta with autosave, Saturday 15.00 WIB publishing, PDF and WhatsApp text (package Q)

Commit [`4d8980a`](https://github.com/dimasarturoh15/paroki-minomartani/commit/4d8980a763f8183f960cc1e534d15d1a874e5238) · 34 berkas, +6280 / -7 baris

WRT-01..10: one edition per Sunday, Draf -> Siap terbit -> Terbit. Flexible sections
(free text, marriage banns, upcoming agenda, kolekte with public amounts) added,
edited and reordered, autosaved every 3 seconds with a stale-editor guard. Banns come
from SKR-17 and appear in three consecutive editions; agenda comes from the published
agenda of that week; both are frozen at publish. The dispatcher publishes ready
editions from Saturday 15.00 WIB (staging cron 0 8 * * 6, caught up by any later
trigger) and reminds Sekretariat once when the edition is still Draf. Reading page
with table of contents, A4 print to PDF, copy-to-WhatsApp text, Baru label for 48
hours, searchable archive per month, Warta minggu ini on the home page, and the warta
status card on Ringkasan. Push (WRT-11) follows with FCM.
