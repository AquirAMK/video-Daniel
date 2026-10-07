#!/usr/bin/env python3
"""Ton-Retusche am Füllwort-Schnitt „quasi“ (Ausgabe 14,833 s).

Der Schnitt endet in der Rohdatei bei 17,533 s, das „K“ von „quasi“ beginnt aber schon bei
17,465 s (Verschlusslaut + Behauchung bis 17,53 s). Den Schnitt selbst zu verlängern würde
alles danach um zwei Frames verschieben (Captions, Grafiken, Beat-Sync). Darum wird nur der
Ton dort stummgeschaltet: 20-ms-Blende direkt nach „du“ (Ausgabe 14,735–14,755 s), danach
Stille bis zum Segmentwechsel 14,833 s. Bild und Länge bleiben identisch.

Aufruf: python3 edit/fix_quasi_k.py edit/aroll_cut.mov videos/welcomer-video/assets/aroll.mp4
"""
import os
import subprocess
import sys
import tempfile

import numpy as np
import soundfile as sf

src_mov, aroll_mp4 = sys.argv[1], sys.argv[2]
FADE_START, FADE_END, MUTE_END = 14.735, 14.755, 14.833

with tempfile.TemporaryDirectory() as tmp:
    wav = os.path.join(tmp, "a.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src_mov, "-vn", "-c:a", "pcm_f32le", wav], check=True)
    x, sr = sf.read(wav, always_2d=True)
    a, b, c = (int(t * sr) for t in (FADE_START, FADE_END, MUTE_END))
    x[a:b] *= (0.5 + 0.5 * np.cos(np.linspace(0, np.pi, b - a)))[:, None]
    x[b:c] = 0.0
    sf.write(wav, x.astype(np.float32), sr, subtype="FLOAT")
    out = os.path.join(tmp, "aroll.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", aroll_mp4, "-i", wav, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", out], check=True)
    os.replace(out, aroll_mp4)
print(f"{aroll_mp4}: Ton {FADE_START}–{MUTE_END} s ausgeblendet (Bild unverändert)")
