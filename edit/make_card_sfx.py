#!/usr/bin/env python3
"""Sanfte Sound-Varianten für das Einblenden der zwei Kunden-Videos auf den Händen.

A  soft-pop    Pop aus der HyperFrames-Bibliothek, tiefpassgefiltert und weich eingeblendet
B  swish       sanfter Luft-Swish (bandpassgefiltertes Rauschen, glatte Hüllkurve, ~0,26 s)
C  swish-tap   leiser Swish, der in einen weichen, tiefen „Tap“ beim Aufsetzen der Karte mündet

Jede Variante wird mono erzeugt; die Stereo-Position (rechte/linke Hand) setzt die Komposition.
Aufruf: python3 edit/make_card_sfx.py <pop.mp3> <zielordner>
"""
import subprocess
import sys

import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt, sosfiltfilt

pop_src, out_dir = sys.argv[1], sys.argv[2]
SR = 48000
rng = np.random.default_rng(11)


def save(name, x):
    x = x / np.abs(x).max() * 10 ** (-6 / 20)
    sf.write(f"{out_dir}/{name}.wav", x.astype(np.float32), SR, subtype="PCM_24")
    print(f"{name}.wav  {len(x) / SR:.2f} s")


def raised(n):
    return 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, n))


# A — Bibliotheks-Pop, entschärft (Tiefpass 4,5 kHz, 4-ms-Fade-in gegen den Klick)
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", pop_src, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                     capture_output=True, check=True).stdout
pop = np.frombuffer(raw, dtype=np.float32).copy()
pop = sosfilt(butter(2, 4500, "lp", fs=SR, output="sos"), pop)
pop[: int(0.004 * SR)] *= raised(int(0.004 * SR))
pop = pop[: int(0.45 * SR)]
pop[-int(0.08 * SR):] *= raised(int(0.08 * SR))[::-1]
save("card-a-softpop", pop)


# B — Luft-Swish: Rauschen durch einen langsam wandernden Bandpass, glatte Hüllkurve
def swish(dur=0.26, f_lo=900, f_hi=2600, peak=0.62):
    n = int(dur * SR)
    t = np.linspace(0, 1, n)
    noise = rng.standard_normal(n)
    out = np.zeros(n)
    blocks = 24  # Bandmitte gleitet nach oben -> „Heranfliegen“
    edges = np.linspace(0, n, blocks + 1).astype(int)
    for k in range(blocks):
        fc = f_lo * (f_hi / f_lo) ** (k / (blocks - 1))
        sos = butter(2, [fc / 1.6, fc * 1.6], "bp", fs=SR, output="sos")
        seg = sosfilt(sos, noise)
        a, b = edges[k], edges[k + 1]
        out[a:b] = seg[a:b]
    env = np.where(t < peak, np.sin(np.pi / 2 * t / peak) ** 2, np.cos(np.pi / 2 * (t - peak) / (1 - peak)) ** 2)
    out *= env
    return sosfiltfilt(butter(2, 6000, "lp", fs=SR, output="sos"), out)


save("card-b-swish", swish())


# C — leiser Swish + weicher Tap (Sinus 190 Hz -> 150 Hz, 8 ms Anschlag, 90 ms Abklingen)
sw = swish(dur=0.2, peak=0.85) * 0.55
n_tap = int(0.22 * SR)
tt = np.arange(n_tap) / SR
f = 150 + 40 * np.exp(-tt / 0.03)
tap = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.09)
tap[: int(0.008 * SR)] *= raised(int(0.008 * SR))
tap += 0.25 * np.sin(2 * np.pi * 2 * np.cumsum(f) / SR) * np.exp(-tt / 0.04)
c = np.zeros(len(sw) + n_tap)
c[: len(sw)] += sw
c[len(sw) - int(0.02 * SR): len(sw) - int(0.02 * SR) + n_tap] += tap
save("card-c-swishtap", c)


# ---------- Freigegeben: Variante A (Nutzer-Go) — finale Stereo-Dateien ----------
# Zwei klar getrennte Pops: rechts (erstes Video), links (zweites Video, einen Ganzton höher),
# Nachklang auf 0,3 s gekürzt, damit der zweite Einsatz nicht verwischt.
def pan_stereo(x, pan):
    th = (pan + 1) * np.pi / 4
    return np.stack([x * np.cos(th), x * np.sin(th)], axis=1)


def tail(x, keep=0.30, fade=0.12):
    x = x[: int(keep * SR)].copy()
    f = int(fade * SR)
    x[-f:] *= raised(f)[::-1]
    return x


def pitch_up(x, semitones):
    r = 2 ** (semitones / 12)  # schneller abspielen = höher und kürzer
    idx = np.arange(0, len(x) - 1, r)
    return np.interp(idx, np.arange(len(x)), x)


for name, sig, pan in [("card-pop-r", tail(pop), +0.4), ("card-pop-l", tail(pitch_up(pop, 2)), -0.4)]:
    y = pan_stereo(sig / np.abs(sig).max() * 10 ** (-6 / 20), pan)
    sf.write(f"{out_dir}/{name}.wav", y.astype(np.float32), SR, subtype="PCM_24")
    print(f"{name}.wav  {len(y) / SR:.2f} s  Pan {pan:+.1f}")
