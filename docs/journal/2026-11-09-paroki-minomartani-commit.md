# 9 November 2026: Catatan commit Paroki Minomartani (23 commit)

Halaman ini dibuat otomatis dari riwayat Git [Paroki Minomartani](../projects/paroki-minomartani.md) setiap kali ada commit. Isinya adalah pesan commit apa adanya.

## Ringkasan

- Jumlah commit: 23
- Perubahan: 455 berkas, +61754 / -198 baris
- Rentang waktu: 17:39 sampai 22:54

## Yang dikerjakan

### 17:39 · chore: paket awal proyek

Commit [`af06ee4`](https://github.com/dimasarturoh15/paroki-minomartani/commit/af06ee4f61445d7c740a696eaa4244a15dcf4f8d) · 53 berkas, +14769 / -0 baris

### 17:39 · docs: catat keputusan orientasi (peran, sesi 90 hari, retensi)

Commit [`7420b14`](https://github.com/dimasarturoh15/paroki-minomartani/commit/7420b14252ca6e15b2d19318b03fdafc73a3e06f) · 4 berkas, +31 / -17 baris

Memindahkan keputusan Prompt 0 ke PRD (§4, AUTH-03, INT-29, PERM-05),
Blueprint, dan CLAUDE.md.

### 17:43 · docs: label 16px sesuai aturan teks minimal 16px

Commit [`c0eeb55`](https://github.com/dimasarturoh15/paroki-minomartani/commit/c0eeb5544765eccf71807cb3d10ac3e089905a4d) · 2 berkas, +2 / -1 baris

### 18:03 · chore: monorepo skeleton (api, web, shared) with lint, typecheck, test

Commit [`dcaa2ad`](https://github.com/dimasarturoh15/paroki-minomartani/commit/dcaa2adbdbf3e6246704d82197abc0879e2a1cb4) · 50 berkas, +8560 / -12 baris

- pnpm workspace: apps/api (Hono Worker), apps/web (Next.js 16.4.5 + OpenNext +
  Tailwind v4), packages/shared (roles, code alphabet, intention types, WIB time
  helpers with weekday tests)
- GET /health returns version and server time in UTC and WIB (NFR-10, NFR-11)
- Cron dispatcher stub; no cron triggers active yet
- Vitest in workerd via @cloudflare/vitest-plugin (renamed from vitest-pool-workers)
- OpenNext worker bundle: 834 KiB gzip (free plan limit 3 MiB)

### 18:09 · feat(api): schema modules A and B, official seed, mass occurrence generator

Commit [`28d02b3`](https://github.com/dimasarturoh15/paroki-minomartani/commit/28d02b33d8ba263fcf94f4fdadae2e16071a4e98) · 30 berkas, +3492 / -24 baris

FR-JDW JDW-01..03, FR-ORG ORG-01..03, FR-AUTH (tables only)
- Drizzle schema: units tree, coverage areas, positions, holders, accounts,
  device sessions, two-person approval check, audit logs; churches, mass
  rules, mass occurrences (special masses = source 'special'), confession
  schedules, office closures, liturgical days, settings
- seed/official.sql: both churches and the five regular masses exactly as in
  DESIGN.md, base units; seed/dev.sql: fake accounts for every role
- generateMassOccurrences: 30 days ahead, idempotent, never changes masses
  that have intentions (hook for Module C) or were cancelled
- Tests on local D1: weekday/time pairs Nov 2026-Jan 2027, UTC deadlines and
  15-minute lock, idempotence, rule changes, protected masses

### 18:16 · feat(api): OTP login, sessions, devices, new-device alert

Commit [`151d380`](https://github.com/dimasarturoh15/paroki-minomartani/commit/151d380df6c1279d25295cde9f2827e253cd4705) · 23 berkas, +3627 / -6 baris

FR-AUTH AUTH-01..05
- POST /auth/request-otp, /auth/verify-otp, /auth/logout, /auth/devices/revoke-all,
  /auth/not-me; GET /auth/me, /auth/devices
- OTP: 6 digits, 10 minutes, single use, HMAC-SHA-256 with OTP_PEPPER, 5 attempts
  reserved atomically, newest code only; identical response and work for
  unknown/inactive emails; 60 s resend wait; 5 requests/email/hour; per-IP limits
- Sessions: 32-byte tokens, SHA-256 stored, checked on every request, expire after
  90 days without activity; __Host- cookie (HttpOnly, Secure, SameSite=Lax) for web,
  bearer for the app
- New-device email with a single-use 'Ini bukan saya' link to a confirmation page;
  POST revokes all sessions and notifies Super Users
- Forwarded client IP/city trusted only with INTERNAL_SECRET
- Emails go to the log until RESEND_API_KEY exists; production fails closed

### 18:22 · feat(api): policy module can(), declared route permissions, audit logs

Commit [`e6831cf`](https://github.com/dimasarturoh15/paroki-minomartani/commit/e6831cf163403b8a9e02f1ac2a01d913a9e83aad) · 20 berkas, +833 / -22 baris

PERM-01..05, AUTH-04, AUTH-09, ADM-05
- packages/shared/src/permissions.ts: role x action matrix from the Blueprint
  (data shared with the dashboard menu); docs/PERMISSIONS.md generated from it
  and kept in sync by a test
- apps/api/src/policy: can(actor, action, resource) with own-unit scope,
  can_read_suggestions, approver != requester, last Super User guard;
  permit() declares and enforces each route's permission (401/403/404)
- Test fails if any route lacks permit(); hand-written role x action table;
  every role x endpoint incl. no session
- audit_logs for logout, sign-out everywhere, 'Ini bukan saya', and the new
  Super User endpoints GET/POST /admin/accounts/:id/devices[/revoke-all]

### 18:35 · feat(web): design tokens, local fonts, public layout, home skeleton, 404

Commit [`bd8c77e`](https://github.com/dimasarturoh15/paroki-minomartani/commit/bd8c77e9550ad6164dbf7763ea0e74cbf8787bf8) · 29 berkas, +1150 / -18 baris

FR-WEB WEB-01, WEB-04 (skeleton), WEB-05, WEB-07; FR-JDW JDW-11
- Tokens from DESIGN.md as CSS variables + Tailwind v4 theme; Tailwind default
  colors, text sizes and shadows removed (no blue, nothing below 16px)
- Dark palette proposal under prefers-color-scheme, contrast checked by
  scripts/contrast.mjs and documented in DESIGN.md (awaiting approval)
- Plus Jakarta Sans self-hosted via next/font/local; Material Symbols weight 300
  as inline SVG paths (only the icons used)
- Button, Input, Rule, PhotoPlaceholder, LivePill; header with logo slot (no
  monogram), liturgical label from settings, no-JS mobile menu; footer with
  Sekretariat facts only
- GET /public/home (edge-cached 60 s): next mass per church; web home reads it
  through the service binding with a friendly fallback
- Development cron trigger runs the daily jobs (mass occurrences)
- OpenNext bundle 899 KiB gzip

### 18:51 · feat(web): admin host routing, API proxy, OTP login, dashboard shell, my devices

Commit [`908bdfa`](https://github.com/dimasarturoh15/paroki-minomartani/commit/908bdfa8aa869c7a3fbfc53c7b6c025257fdb0c6) · 36 berkas, +1150 / -11 baris

FR-ADM ADM-01, ADM-08; FR-AUTH AUTH-01..05 (web)
- worker.ts routes by host before OpenNext: admin host -> /admin, /admin on the
  public host -> admin host when ADMIN_HOST is set, noindex for the dashboard
  (Next.js proxy.ts avoided: Node middleware is experimental on OpenNext/CF)
- /api/* proxied to the API Worker over the service binding: allowlisted
  headers, browser X-Internal-Secret/X-Client-* stripped, client IP/city added
  with INTERNAL_SECRET, cross-site writes refused
- Login: email -> 6-box code (paste, one-time-code, keyboard nav), resend after
  60 s, Indonesian errors; 'Ini bukan saya' confirmation page (token in URL
  fragment, POST only)
- Dashboard shell: sidebar from the shared permission matrix (menuFor), role
  badge, bell, sign out; Ringkasan; Perangkat saya with typed-keyword
  sign-out-everywhere; placeholder for sections built later
- Tests: menu per role, header forwarding, host routing; manual check of every
  fake account through the web proxy
- OpenNext bundle 1097 KiB gzip

### 18:53 · feat(api): POST /admin/mass-occurrences/generate for Sekretariat (JDW-03)

Commit [`d9ba6a0`](https://github.com/dimasarturoh15/paroki-minomartani/commit/d9ba6a0358b76a660f5459d6062b79fc797be933) · 3 berkas, +36 / -0 baris

Runs the idempotent generator on demand (after a schedule change, or to fill a
fresh environment); schedule.write only, audited, with role x endpoint tests.

### 18:56 · chore: staging configuration on workers.dev and GitHub Actions CI

Commit [`b461b1f`](https://github.com/dimasarturoh15/paroki-minomartani/commit/b461b1fe43c6c578dad179caf15365752069c772) · 8 berkas, +171 / -6 baris

- env.staging for both Workers (separate D1 paroki-db-staging, daily cron at
  01.00 WIB, service binding to paroki-api-staging, noindex everywhere)
- Staging D1 created (APAC), migrated and seeded with fake data
- robots.txt disallows everything outside production
- CI: format, lint, typecheck, test, OpenNext build on every push/PR; staging
  deploy on main only when CLOUDFLARE_API_TOKEN/ACCOUNT_ID exist
- README: one-time setup, secrets, manual deploy, reading OTP from logs
- Not deployed yet: the account has no workers.dev subdomain and R2 is not
  enabled (both need the Cloudflare dashboard)

### 20:13 · chore: staging deployed on parokiminomartani.workers.dev

Commit [`a8e6342`](https://github.com/dimasarturoh15/paroki-minomartani/commit/a8e6342727a03959e80072f371aafcb9984437a3) · 3 berkas, +7 / -9 baris

- R2 bucket paroki-files-staging bound as FILES; ADMIN_ORIGIN points to the
  staging dashboard
- Secrets OTP_PEPPER and INTERNAL_SECRET set with wrangler secret put
- Verified on staging: /health, home with next masses from D1, robots disallow,
  noindex, OTP login via the web proxy (code from wrangler tail), new-device
  alert link, role menu, POST /admin/mass-occurrences/generate (58 masses)
- Web bundle 1129 KiB gzip, API 186 KiB gzip (free plan limit 3 MiB)

### 20:40 · docs: Sekretariat hours (daily except Tuesday, 08.30-16.00), clergy names allowed

Commit [`0231527`](https://github.com/dimasarturoh15/paroki-minomartani/commit/02315274a9027ecdb099ce79797b36cd84232140) · 4 berkas, +9 / -8 baris

Decisions by Dimas for week 3-4: office hours replace the old 08.30-14.00 fact
(DESIGN.md, PRD SKR-12/PAGE-07, Blueprint); clergy names may be shown when
entered by Sekretariat; two image sizes at upload; in-house block editor.

### 20:41 · docs: tidy decision list in OPEN-QUESTIONS

Commit [`f341883`](https://github.com/dimasarturoh15/paroki-minomartani/commit/f3418839e9858d068f3b315bf3b68e3525657270) · 1 berkas, +2 / -2 baris

### 20:46 · feat: photo uploads to R2 in two sizes, public image serving (week 3-4 package A)

Commit [`8926cb1`](https://github.com/dimasarturoh15/paroki-minomartani/commit/8926cb19152973e215383dda4c878e50a71d5df2) · 18 berkas, +2895 / -0 baris

CLAUDE.md Files/Images, NFR-07, POST-04 groundwork
- media table; POST /media (organizers): two sizes re-encoded in the browser,
  checked by content (JPEG/PNG/WebP magic bytes, pixel size), EXIF/GPS refused,
  size limits, unguessable keys, unit and uploader recorded, audited
- GET /media/public/... immutable and edge-cached; private keys never served
- Web: prepareImage() (canvas re-encode, 1600/800 px, ~250 KB, WebP or JPEG),
  ImageUpload component for the editor and slider
- Actions media.upload / media.read in the matrix and role tests

### 21:06 · feat: static pages with block editor and revisions, Profil, Sejarah, Gereja Kami, Struktur, Kontak (week 3-4 package B)

Commit [`1505809`](https://github.com/dimasarturoh15/paroki-minomartani/commit/150580912436c643402d85069c826ef017560ef0) · 54 berkas, +5675 / -18 baris

FR-WEB PAGE-01..08, FR-ORG ORG-04, ORG-05, ORG-09
- pages + page_revisions (every save is a revision; restore = new save with the
  old content, audited); history_entries; church details; show_on_structure
- Shared block schema (heading, paragraph, quote, image, points, details,
  YouTube on Profil only) with a tiny safe inline syntax; images only from our
  media store; rendered without raw HTML; YouTube as a click-to-load facade
- Public pages: Profil (quick numbers from data), ARDAS, Sejarah timeline,
  Gereja Kami (schedule from the mass rules), Struktur (current holders, former
  pastors, no contact data), Kontak (open/closed status), Kebijakan Privasi,
  Pedoman Publikasi; empty states instead of invented text
- Dashboard: block editor, revision history, timeline, church details, office
  hours (settings.write)
- Sekretariat hours: every day except Tuesday, 08.30-16.00 (data migration)
- Role x endpoint tests for every new endpoint

### 21:29 · feat: schedule page (masses, confession, agenda), calendar export, schedule admin (week 3-4 package C)

Commit [`8354ef7`](https://github.com/dimasarturoh15/paroki-minomartani/commit/8354ef7c6cd0b12d0fa23533b3a0cb2ef114829f) · 31 berkas, +5722 / -12 baris

FR-JDW JDW-01..09, PERM-01
- Public /jadwal: masses for 7 days grouped per day with special masses first,
  church choice remembered by cookie (no client JS), Sakramen Tobat, agenda per
  WIB month as list or calendar with unit filter; agenda detail page
- .ics export (RFC 5545 escaping and folding, no invented durations) and Google
  Calendar links; proxy forwards Content-Disposition
- Dashboard: mass rules (each change regenerates 30 days and reports
  conflicts), special masses with their own intention deadline, confession
  times, Sekretariat closures, agenda
- agenda_events: unit roles only create/edit/delete their own unit's rows
  (first endpoint-level wrong-unit tests); parish-wide roles default to Paroki
- Fix: semicolons were not escaped in .ics text (caught by lint, now tested)

### 21:42 · feat: Persembahan Kasih with two-person approval, approvals screen (week 3-4 package D)

Commit [`fcffc4c`](https://github.com/dimasarturoh15/paroki-minomartani/commit/fcffc4cb0c7cf5ca9aac03a22cdabd9e31612b9b) · 19 berkas, +3885 / -4 baris

FR-WEB DON-01..05, PERM-04, ADM-04
- donation_accounts changed only by applying an approved approval_request;
  the requester can never decide (policy + DB CHECK); the decision is claimed
  atomically so a change is never applied twice; stale targets are refused
- Only PGPM accounts (holder must contain PGPM), numeric account numbers, QRIS
  only with an uploaded official image; nothing seeded
- All Super Users are notified of pending and decided requests
- Public page: approved accounts only, copy button, QRIS with 'Simpan ke
  galeri', anti-fraud notice, empty state until Bendahara confirms
- Dashboard: propose create/update/deactivate; Persetujuan with old vs new
  comparison, approve/reject with reason
- Design fix: amber is only for deadlines (removed from dashboard states)

### 22:01 · feat: home slider, site search, loading skeleton, notification bell (week 3-4 packages E and F)

Commit [`7c48036`](https://github.com/dimasarturoh15/paroki-minomartani/commit/7c48036258d343463e9e21e29576a4e144bbaf42) · 29 berkas, +4151 / -15 baris

FR-WEB WEB-02, WEB-03, WEB-06, WEB-08; FR-ADM ADM-03
- hero_slides with a display window (WIB) and at most 6 active; text below the
  photo, never on it; fade every 6 s, pauses on hover/focus/touch, no autoplay
  with reduced motion, dots, previous/next, swipe; slider manager for Super User
- /public/search over pages, history and agenda (LIKE with escaping, real text
  hits only); /cari works without JavaScript
- Grey skeleton while public pages load
- Bell: GET /auth/notifications, POST /auth/notifications/read (own only),
  unread count on /auth/me and as a badge in the top bar; /admin/notifikasi
- Roadmap week 3-4 ticked (home live banner, warta and activities wait for
  their modules)

### 22:14 · docs: dark palette approved; drafts of Kebijakan Privasi and Pedoman Publikasi

Commit [`293b5f1`](https://github.com/dimasarturoh15/paroki-minomartani/commit/293b5f19d7e9e335dcfd82ea7bb3f2ca423c7509) · 6 berkas, +163 / -8 baris

- DESIGN.md: dark mode approved by Dimas (9 Nov 2026)
- docs/drafts: privacy policy (UU PDP 27/2022) and publication guidelines for
  review by Pastor Paroki and DPP, written from what the system actually does,
  with reviewer notes on open points (backup retention, intentions on stream,
  response deadlines, contact person, effective date)
- Roadmap: daily purge also covers otp_codes, rate_limits, not_me_tokens and
  audit_logs older than 1 year (PAGE-08, NFR-07)

### 22:36 · docs: list of materials and decisions needed from the parish

Commit [`10f3f08`](https://github.com/dimasarturoh15/paroki-minomartani/commit/10f3f08804e1363a25d81d259aefd10fc7dd3596) · 1 berkas, +95 / -0 baris

Grouped by provider (Pastor/PGPM, Bendahara, Sekretariat, Komsos, content,
trial, phase 2) with deadlines; mirrors the shareable checklist page.

### 22:46 · docs: week 5-6 decisions (optional stipend proof, intention status model, Turnstile test keys)

Commit [`1ad5fae`](https://github.com/dimasarturoh15/paroki-minomartani/commit/1ad5fae5c66a2f4aeeac0b2ffe92f96b3bea13c4) · 4 berkas, +6 / -5 baris

### 22:54 · feat: public mass intention form, transfer proof upload, status lookup (week 5-6 package G)

Commit [`113ddd1`](https://github.com/dimasarturoh15/paroki-minomartani/commit/113ddd1184b62d1b243ccfc6b225d4defef54c44) · 27 berkas, +5323 / -0 baris

FR-INT INT-01..11; CLAUDE.md Codes
- intention_types (fixed order, fields_schema), intentions (one row per mass,
  shared code for repeats), proof_uploads; purge_after = mass + 3 months
- GET /public/intentions/form with a signed form-open token; submissions are
  accepted until the deadline, or within 15 minutes after it when the form was
  opened before it (decided by the server); closed masses return the next open
  ones of the same church
- Stipend voluntary: transfer needs an uploaded proof (private R2, single use,
  re-encoded image, EXIF refused), cash or none need nothing; amounts never stored
- INT- codes: 6 unbiased random characters from the unambiguous alphabet
- Turnstile verification (Cloudflare test keys until the real widget exists),
  per-IP rate limits, zod validation per type (names &lt;= 60, arwah &lt;= 20, text &lt;= 250)
- GET /public/status/:code: status and schedule only; Terkunci/Dibacakan
  computed from the mass times
- Web: /layanan, 4-step form with review, /cek-status with Riwayat Kode Saya
