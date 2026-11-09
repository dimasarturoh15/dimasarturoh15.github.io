# 9 November 2026: Catatan commit Paroki Minomartani (5 commit)

Halaman ini dibuat otomatis dari riwayat Git [Paroki Minomartani](../projects/paroki-minomartani.md) setiap kali ada commit. Isinya adalah pesan commit apa adanya.

## Ringkasan

- Jumlah commit: 5
- Perubahan: 139 berkas, +26854 / -54 baris
- Rentang waktu: 17:39 sampai 18:09

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
