#!/bin/bash
# Pro Segment: 4K HEVC -> 1080p30 H.264 (gegradet) + PCM-Audio mit 30-ms-Fades
set -e
cd "$(dirname "$0")"
G="eq=contrast=1.08:saturation=1.0,curves=master='0/0 0.25/0.23 0.75/0.77 1/1',colorbalance=rs=-0.03:bs=0.04,vignette=angle=PI/5"
python3 -I -c "
import json;d=json.load(open('edl.json'))
for i,s in enumerate(d['segments']): print(i, s['src_start'], round(s['src_end']-s['src_start'],4), round((s['src_end']-s['src_start'])*30))" |
while read i ss dur fr; do
  fo=$(python3 -c "print(round($dur-0.03,4))")
  echo "ffmpeg -v error -y -ss $ss -i ../raw/rohdatei.mov -t $dur -vf \"scale=1920:1080:flags=lanczos,fps=30,$G,format=yuv420p\" -frames:v $fr -c:v libx264 -preset medium -crf 13 -g 30 -bf 2 -color_primaries bt709 -color_trc bt709 -colorspace bt709 -af \"aresample=48000,afade=t=in:st=0:d=0.03,afade=t=out:st=$fo:d=0.03\" -c:a pcm_s16le -ar 48000 segs/s$(printf %02d $i).mov"
done > segs/jobs.txt
xargs -P 4 -I{} sh -c '{}' < segs/jobs.txt
ls segs/*.mov | sed "s/^segs\//file '/;s/$/'/" > segs/list.txt
ffmpeg -v error -y -f concat -safe 0 -i segs/list.txt -c copy aroll_cut.mov
