#!/usr/bin/env python3
"""Weicher „Ding“ für die Kunden-Karten auf den Händen (ersetzt den Sparkle).

Glockenartiger Ton mit weichem Anschlag (8 ms), wenigen, schnell abklingenden Obertönen,
Tiefpass gegen Härte und kurzem synthetischem Raumhall. Tonhöhen aus der Tonart des Songs
(Cis-Moll): Gis5 für die rechte Karte, Cis6 für die linke (Quarte aufwärts).

Aufruf: python3 edit/make_ding.py <zielordner>
"""
import sys

import numpy as np
import soundfile as sf
from scipy.signal import butter, fftconvolve, sosfilt

out_dir = sys.argv[1]
SR = 48000
DUR = 1.6
rng = np.random.default_rng(7)  # fester Seed: reproduzierbar

# Raumhall-Impulsantwort (Stereo, exponentiell abklingendes, tiefpassgefiltertes Rauschen, RT60 ~1,1 s)
n_ir = int(1.2 * SR)
t_ir = np.arange(n_ir) / SR
decay = np.exp(-6.9 * t_ir / 1.1)
lp = butter(2, 5200, "lp", fs=SR, output="sos")
ir = np.stack([sosfilt(lp, rng.standard_normal(n_ir)) * decay for _ in range(2)], axis=1)
ir[: int(0.012 * SR)] = 0  # 12 ms Pre-Delay
ir /= np.sqrt((ir ** 2).sum(axis=0, keepdims=True))


def ding(f0):
    n = int(DUR * SR)
    t = np.arange(n) / SR
    partials = [  # (Frequenzverhältnis, Amplitude, Abklingzeit in s)
        (1.0, 1.00, 0.85),
        (2.0, 0.10, 0.30),
        (2.76, 0.05, 0.16),  # leichter Glockencharakter
        (3.0, 0.03, 0.12),
    ]
    x = sum(a * np.sin(2 * np.pi * f0 * r * t) * np.exp(-t / tau) for r, a, tau in partials)
    att = int(0.008 * SR)
    x[:att] *= 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, att))  # weicher Anschlag, kein Klick
    x = sosfilt(butter(2, 4500, "lp", fs=SR, output="sos"), x)
    dry = np.stack([x, x], axis=1)
    wet = np.stack([fftconvolve(x, ir[:, c])[:n] for c in range(2)], axis=1)
    y = 0.8 * dry + 0.35 * wet
    fade = int(0.25 * SR)
    y[-fade:] *= np.cos(np.linspace(0, np.pi / 2, fade))[:, None] ** 2
    return y / np.abs(y).max() * 10 ** (-6 / 20)  # Spitze −6 dBFS


for name, f0 in [("ding-soft-gis", 830.61), ("ding-soft-cis", 1108.73)]:
    sf.write(f"{out_dir}/{name}.wav", ding(f0).astype(np.float32), SR, subtype="PCM_24")
    print(f"{name}.wav  {f0:.2f} Hz  {DUR} s")
