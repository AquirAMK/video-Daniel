#!/bin/bash
# 4K60-Master (3840 × 2160, 60 fps) in voller Qualität.
# Voraussetzung: edit/cut_segments_4k.sh (→ assets/aroll_4k.mp4) und der 4K-Freisteller
#   npx --yes hyperframes@0.8.138 remove-background edit/matte/hook_src_4k.mp4 -o edit/matte/hook_fg_4k.mov
# FFMPEG_PROCESS_TIMEOUT_MS: Der Standard (300 s) reicht nicht, um die 4K60-Frames
# der A-Roll zu extrahieren (Fehler VIDEO_EXTRACTION_FAILED; ffmpeg_timeout).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/videos/welcomer-video"
FFMPEG_PROCESS_TIMEOUT_MS=3600000 npx --yes hyperframes@0.8.138 render \
  -o renders/master_4k60_raw.mp4 --fps 60 --resolution landscape-4k --quality delivery
FG="$ROOT/edit/matte/hook_fg_4k.mov" \
VENC="-c:v libx264 -preset medium -crf 15 -profile:v high -level 5.2" \
  "$ROOT/edit/finish.sh" renders/master_4k60_raw.mp4 renders/welcomer_final_4k60.mp4
