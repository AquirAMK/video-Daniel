#!/bin/bash
# 4K60-Master der A-Roll: gleiche Schnittliste (edl.json) und gleiches Grading wie cut_segments.sh,
# aber 3840×2160 bei 60 fps direkt aus der Rohdatei. Nur Bild; der Ton kommt unverändert aus
# aroll_cut.mov (dort sind alle Ton-Korrekturen bereits enthalten).
set -e
cd "$(dirname "$0")"
mkdir -p segs4k
G="eq=contrast=1.08:saturation=1.0,curves=master='0/0 0.25/0.23 0.75/0.77 1/1',colorbalance=rs=-0.03:bs=0.04,vignette=angle=PI/5"
python3 -I -c "
import json;d=json.load(open('edl.json'))
for i,s in enumerate(d['segments']): print(i, s['src_start'], round(s['src_end']-s['src_start'],4), round((s['src_end']-s['src_start'])*60))" |
while read i ss dur fr; do
  echo "ffmpeg -v error -y -ss $ss -i ../raw/rohdatei.mov -t $dur -an -vf \"fps=60,$G,format=yuv420p\" -frames:v $fr -c:v libx264 -preset faster -crf 12 -g 60 -bf 2 -color_primaries bt709 -color_trc bt709 -colorspace bt709 segs4k/s$(printf %02d $i).mp4"
done > segs4k/jobs.txt
xargs -P 2 -I{} sh -c '{}' < segs4k/jobs.txt
ls segs4k/s*.mp4 | sed "s/^segs4k\//file '/;s/$/'/" > segs4k/list.txt
ffmpeg -v error -y -f concat -safe 0 -i segs4k/list.txt -i aroll_cut.mov -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -movflags +faststart ../videos/welcomer-video/assets/aroll_4k.mp4
