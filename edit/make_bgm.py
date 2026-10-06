#!/usr/bin/env python3
"""Musikbett für das Welcomer-Video schneiden (Family Affair, Instrumental).

Aufbau (Takte relativ zum ersten Downbeat des Songs bei 0,33 s):
  Video 0,000 – 46,503 s  =  Song-Takte  6 – 23  (Abschnitt A, Video startet auf einer „1“)
  Video 46,503 – 60,5 s   =  Song-Takte 96 – 101 (Outro, phrasengenauer Sprung auf die „1“)
  Schlussschlag (Takt 101) landet bei 59,42 s, direkt nach dem letzten Wort „euch“.

Beide Schnittpunkte liegen auf dem Beginn einer 8-Takt-Phrase, damit Bass-Zyklus und Phrasen
durchlaufen. Transienten werden sample-genau gesucht, der Übergang ist ein 6-ms-Crossfade
direkt vor dem Kick.

Aufruf: python3 edit/make_bgm.py work/music_full.wav work/music_beats.json <ausgabe.wav> <grid.json>
"""
import json
import sys

import numpy as np
import soundfile as sf

src, beats_json, out_wav, out_grid = sys.argv[1:5]
VIDEO_LEN = 60.5
FADE_OUT = 0.30

y, sr = sf.read(src, always_2d=True)
r = json.load(open(beats_json))
P = r["beat_period"]
BAR = 4 * P
D1 = r["downbeats"][0]  # = Takt 1 (relativ); Takt 0 liegt einen Takt davor


def bar_time(rel):
    return D1 + (rel - 1) * BAR


def onset_near(t, win=0.015):
    """Anschlag nahe t: erster Punkt, an dem die 1-ms-Hüllkurve (breitbandig) 25 % des
    Spitzenwerts der folgenden 30 ms erreicht. Das Beat-Raster liegt bereits auf ±5 ms."""
    a, b = int((t - win) * sr), int((t + win + 0.03) * sr)
    x = y[a:b].mean(axis=1)
    n = int(0.001 * sr)
    env = np.sqrt(np.convolve(x * x, np.ones(n) / n, mode="same"))
    pk = env.max()
    j = int(np.argmax(env > 0.25 * pk))
    return (a + j) / sr


A0, A1 = onset_near(bar_time(6)), onset_near(bar_time(24))
B0, HIT = onset_near(bar_time(96)), onset_near(bar_time(101))
PRE = 0.003  # 3 ms vor dem Transienten schneiden
print(f"Takt 6  {bar_time(6):.4f} -> Onset {A0:.4f}")
print(f"Takt 24 {bar_time(24):.4f} -> Onset {A1:.4f}")
print(f"Takt 96 {bar_time(96):.4f} -> Onset {B0:.4f}")
print(f"Takt 101 {bar_time(101):.4f} -> Onset {HIT:.4f}")

segA = y[int((A0 - PRE) * sr): int((A1 - PRE) * sr)]
segB = y[int((B0 - PRE) * sr):]
xf = int(0.006 * sr)
# Crossfade: Ende von A (inkl. der 6 ms nach dem Schnitt) gegen Anfang von B
tailA = y[int((A1 - PRE) * sr): int((A1 - PRE) * sr) + xf]
w = np.linspace(0, np.pi / 2, xf)[:, None]
joint = tailA * np.cos(w) + segB[:xf] * np.sin(w)
bed = np.concatenate([segA, joint, segB[xf:]])

# Video-Zeitachse: Downbeat von Takt 6 liegt bei t = PRE (3 ms) -> um PRE nach vorn ziehen,
# damit der Kick exakt auf t = 0 liegt; die ersten 3 ms werden zu einem 3-ms-Fade-in.
bed = bed[int(PRE * sr):]
fi = int(0.003 * sr)
bed[:fi] *= np.linspace(0, 1, fi)[:, None]
n = int(VIDEO_LEN * sr)
bed = bed[:n]
fo = int(FADE_OUT * sr)
bed[-fo:] *= np.cos(np.linspace(0, np.pi / 2, fo))[:, None] ** 2

splice_t = (A1 - A0)
hit_t = splice_t + (HIT - B0)
sf.write(out_wav, bed.astype(np.float32), sr, subtype="PCM_24")

# Beat-Raster in Video-Zeit (für das Timing der Übergänge)
grid = {
    "beat_period": P,
    "bar": BAR,
    "splice_t": round(splice_t, 4),
    "final_hit_t": round(hit_t, 4),
    "song_start": round(A0, 4),
    "downbeats": [round(k * BAR, 4) for k in range(int(VIDEO_LEN / BAR) + 1)],
    "beats": [round(k * P, 4) for k in range(int(VIDEO_LEN / P) + 1)],
}
json.dump(grid, open(out_grid, "w"), indent=1)
print(f"Sprung ins Outro bei {splice_t:.3f} s (Soll {18 * BAR:.3f}), Schlussschlag bei {hit_t:.3f} s (Soll {23 * BAR:.3f})")
print(f"Bett: {len(bed) / sr:.3f} s, {sr} Hz -> {out_wav}")
