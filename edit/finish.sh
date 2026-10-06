#!/bin/bash
# Nachbearbeitung nach dem HyperFrames-Render:
#  1. Sprecher-Freisteller (Matte) über den Hook legen → „Willkommen“ steht HINTER dem Sprecher
#  2. Lautheit auf −14 LUFS / −1 dBTP normalisieren (zweistufiges loudnorm)
# Aufruf: edit/finish.sh <render.mp4> <ausgabe.mp4>
set -euo pipefail
IN="${1:?render.mp4}"
OUT="${2:?ausgabe.mp4}"
HERE="$(cd "$(dirname "$0")" && pwd)"
FG="$HERE/matte/hook_fg.mov"   # RGBA, 30 fps, ab t=0 (Sprecher A)
HOOK_END=1.12                  # Hook-Text ist bis ~1,08 s sichtbar

# Messdurchlauf für loudnorm
STATS=$(ffmpeg -hide_banner -nostats -i "$IN" -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
mi=$(echo "$STATS" | python3 -c "import json,sys;print(json.load(sys.stdin)['input_i'])")
mtp=$(echo "$STATS" | python3 -c "import json,sys;print(json.load(sys.stdin)['input_tp'])")
mlra=$(echo "$STATS" | python3 -c "import json,sys;print(json.load(sys.stdin)['input_lra'])")
mth=$(echo "$STATS" | python3 -c "import json,sys;print(json.load(sys.stdin)['input_thresh'])")
moff=$(echo "$STATS" | python3 -c "import json,sys;print(json.load(sys.stdin)['target_offset'])")

ffmpeg -hide_banner -v error -y -i "$IN" -i "$FG" \
  -filter_complex "[1:v]format=yuva444p,setpts=PTS-STARTPTS[fg];[0:v][fg]overlay=x=0:y=0:eof_action=pass:enable='lt(t,$HOOK_END)':format=auto,format=yuv420p[v]" \
  -map "[v]" -map 0:a \
  -af "loudnorm=I=-14:TP=-1:LRA=11:measured_I=$mi:measured_TP=$mtp:measured_LRA=$mlra:measured_thresh=$mth:offset=$moff:linear=true,aresample=48000" \
  -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -color_primaries bt709 -color_trc bt709 -colorspace bt709 \
  -c:a aac -b:a 256k -movflags +faststart "$OUT"

ffmpeg -hide_banner -nostats -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I:|Peak:|LRA:)" | head -3
