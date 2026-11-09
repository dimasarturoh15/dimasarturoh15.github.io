# 9 November 2026: Catatan commit Paroki Minomartani (11 commit)

Halaman ini dibuat otomatis dari riwayat Git [Paroki Minomartani](../projects/paroki-minomartani.md) setiap kali ada commit. Isinya adalah pesan commit apa adanya.

## Ringkasan

- Jumlah commit: 11
- Perubahan: 258 berkas, +33821 / -117 baris
- Rentang waktu: 17:39 sampai 18:56

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
