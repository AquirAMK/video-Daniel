#!/bin/bash
# Nachbearbeitung nach dem HyperFrames-Render:
#  1. Sprecher-Freisteller (Matte) über den Hook legen → „Willkommen“ steht HINTER dem Sprecher
#  2. Mastering: Limiter mit 4× Oversampling (True Peak, Decke −2,3 dBFS). Die Verstärkung wird
#     iterativ eingemessen, bis das Ergebnis −14 LUFS integriert bei ≤ −1,5 dBTP liegt.
#     (Bus-Kompression getestet: drückt die Dynamik auf ~1,5 LU, daher nur Limiter.)
#     30-ms-Fade-in: Der Ton setzt bei t = 0 schlagartig ein (Kick + Stimme); ohne Fade schwingt
#     der AAC-Encoder im ersten Block auf +2,8 dBTP über.
#     (loudnorm allein kippt bei der nötigen Verstärkung in den dynamischen Modus und
#      begrenzt die Spitzen nicht zuverlässig.)
# Aufruf: edit/finish.sh <render.mp4> <ausgabe.mp4>
set -euo pipefail
IN="${1:?render.mp4}"
OUT="${2:?ausgabe.mp4}"
HERE="$(cd "$(dirname "$0")" && pwd)"
FG="${FG:-$HERE/matte/hook_fg.mov}"   # RGBA, ab t=0 (Sprecher A); 4K60-Master: FG=edit/matte/hook_fg_4k.mov
# Video-Encoder (überschreibbar, z. B. für das 4K60-Master)
VENC="${VENC:--c:v libx264 -preset slow -crf 16}"
HOOK_END=1.12                  # Hook-Text ist bis ~1,08 s sichtbar
TARGET_I=-14
CEIL=0.767                     # Limiter-Decke −2,3 dBFS (linear), Reserve für AAC-Überschwinger (~0,3 dB)
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

measure() { # gibt "I TP" (LUFS, dBTP) aus
  ffmpeg -hide_banner -nostats -i "$1" -af ebur128=peak=true -f null - 2>&1 \
    | awk '/^ *I:/{i=$2} /^ *Peak:/{p=$2} END{print i, p}'
}
master() { # $1 = Verstärkung in dB, $2 = Ausgabe-WAV
  ffmpeg -hide_banner -v error -y -i "$TMP/in.wav" \
    -af "volume=${1}dB,aresample=192000,alimiter=limit=${CEIL}:attack=1.5:release=60:level=0,aresample=48000,afade=t=in:st=0:d=0.03:curve=qsin" \
    -c:a pcm_f32le "$2"
}

ffmpeg -hide_banner -v error -y -i "$IN" -vn -ac 2 -ar 48000 -c:a pcm_f32le "$TMP/in.wav"
read -r I0 TP0 < <(measure "$TMP/in.wav")
G=$(python3 -c "print(round($TARGET_I - ($I0), 2))")
for k in 1 2 3 4; do
  master "$G" "$TMP/m.wav"
  read -r I1 TP1 < <(measure "$TMP/m.wav")
  echo "  Durchlauf $k: Verstärkung ${G} dB → ${I1} LUFS, ${TP1} dBTP"
  D=$(python3 -c "print(round($TARGET_I - ($I1), 2))")
  python3 -c "import sys; sys.exit(0 if abs($D) <= 0.1 else 1)" && break
  G=$(python3 -c "print(round($G + $D, 2))")
done

ffmpeg -hide_banner -v error -y -i "$IN" -i "$FG" -i "$TMP/m.wav" \
  -filter_complex "[1:v]format=yuva444p,setpts=PTS-STARTPTS[fg];[0:v][fg]overlay=x=0:y=0:eof_action=pass:enable='lt(t,$HOOK_END)':format=auto,format=yuv420p[v]" \
  -map "[v]" -map 2:a \
  $VENC -pix_fmt yuv420p -color_primaries bt709 -color_trc bt709 -colorspace bt709 \
  -c:a aac -b:a 256k -movflags +faststart "$OUT"

echo "Eingang: ${I0} LUFS, ${TP0} dBTP"
ffmpeg -hide_banner -nostats -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I:|Peak:|LRA:)" | head -3
