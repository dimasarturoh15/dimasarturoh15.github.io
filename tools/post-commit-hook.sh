#!/bin/sh
# Hook post-commit: sinkronkan riwayat commit proyek ini ke situs portofolio.
#
# Pasang dengan menyalin berkas ini ke <repo proyek>/.git/hooks/post-commit,
# lalu sesuaikan SLUG dan NAME. Yang diperbarui: tabel log di halaman proyek,
# halaman jurnal harian, indeks jurnal, navigasi, dan daftar jurnal di beranda.

DOCS_DIR="D:/Dokumenku/docs-github"
SLUG="choralestudio"
NAME="ChoraleStudio"

[ -d "$DOCS_DIR/.git" ] || exit 0
REPO=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
HASH=$(git rev-parse --short HEAD 2>/dev/null) || exit 0
PY=$(command -v python || command -v py) || exit 0

# Variabel milik commit proyek ini tidak boleh terbawa ke perintah git untuk repo situs.
unset GIT_DIR GIT_INDEX_FILE GIT_WORK_TREE GIT_PREFIX GIT_EDITOR

LOG="$DOCS_DIR/.git/sync-commit.log"
LOCK="$DOCS_DIR/.git/sync-commit.lock"

# Satu sinkronisasi pada satu waktu (commit beruntun); kunci basi dilepas setelah 60 detik.
i=0
while ! mkdir "$LOCK" 2>/dev/null; do
  i=$((i + 1))
  if [ "$i" -gt 60 ]; then rm -rf "$LOCK"; fi
  sleep 1
done

{
  echo "== $(date '+%Y-%m-%d %H:%M:%S') $NAME $HASH"
  FILES=$("$PY" "$DOCS_DIR/tools/sync_commit.py" --repo "$REPO" --slug "$SLUG" --name "$NAME")
  if [ -n "$FILES" ]; then
    (cd "$DOCS_DIR" && echo "$FILES" | xargs git add --)
    if ! git -C "$DOCS_DIR" diff --cached --quiet; then
      git -C "$DOCS_DIR" commit -q -m "docs: sync $NAME commit $HASH"
    fi
  fi
} >>"$LOG" 2>&1
rmdir "$LOCK" 2>/dev/null

# Unggah di latar agar commit tidak menunggu jaringan.
(git -C "$DOCS_DIR" pull -q --rebase --autostash origin main >>"$LOG" 2>&1 &&
  git -C "$DOCS_DIR" push -q origin main >>"$LOG" 2>&1 &)

exit 0
