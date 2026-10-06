#!/usr/bin/env python3
"""Beat-/Takt-Analyse für die Hintergrundmusik.

Aufruf: python3 edit/music_analyze.py <musik.wav|m4a|mp4> <ausgabe.json>

Ermittelt Tempo, Beat-Zeiten, die Taktphase (welcher Beat die „1“ ist) und
eine grobe Struktur (Energie pro Takt, Wechsel zwischen Abschnitten).
"""
import json
import sys

import librosa
import numpy as np

src, out = sys.argv[1], sys.argv[2]
SR = 22050
HOP = 256

y, _ = librosa.load(src, sr=SR, mono=True)
dur = len(y) / SR

# Beats auf dem Onset-Envelope (perkussiver Anteil, damit Pads/Strings nicht stören)
y_h, y_p = librosa.effects.hpss(y)
onset = librosa.onset.onset_strength(y=y_p, sr=SR, hop_length=HOP)
# Tempo mit Prior um 95 BPM schätzen; Halb-/Doppeltempo korrigieren (Hip-Hop/R&B: 70–140 BPM)
tempo = float(np.atleast_1d(librosa.feature.tempo(onset_envelope=onset, sr=SR, hop_length=HOP, start_bpm=95))[0])
while tempo < 70:
    tempo *= 2
while tempo > 140:
    tempo /= 2
_, beats = librosa.beat.beat_track(onset_envelope=onset, sr=SR, hop_length=HOP, bpm=tempo, tightness=400, units="frames")
bt = librosa.frames_to_time(beats, sr=SR, hop_length=HOP) - 0.015  # Onset-Latenz des Spektralfluss-Envelopes (~15–20 ms) ausgleichen

# Gleichmäßiges Raster aus den Beats schätzen (lineare Regression Index -> Zeit)
idx = np.arange(len(bt))
period, phase0 = np.polyfit(idx, bt, 1)
grid_err = bt - (phase0 + period * idx)

# Taktphase: Bass-/Kick-Energie und Harmoniewechsel pro Beat, über 4er-Zyklen gemittelt
S = np.abs(librosa.stft(y, n_fft=2048, hop_length=HOP))
freqs = librosa.fft_frequencies(sr=SR, n_fft=2048)
low = S[(freqs >= 30) & (freqs <= 120)].sum(axis=0)
low_on = np.maximum(0, np.diff(low, prepend=low[0]))
chroma = librosa.feature.chroma_cqt(y=y_h, sr=SR, hop_length=HOP)
chroma_sync = librosa.util.sync(chroma, beats, aggregate=np.median)
# sync() legt ein Segment vor den ersten Beat -> Element j = Wechsel in das Intervall ab Beat j
chroma_nov = np.linalg.norm(np.diff(chroma_sync, axis=1), axis=0)
beat_frames = beats
kick = np.array([low_on[max(0, f - 2): f + 3].max() for f in beat_frames])
scores = []
for ph in range(4):
    k = kick[ph::4].mean()
    c = chroma_nov[ph::4][: len(kick[ph::4])].mean() if len(chroma_nov) > ph else 0
    scores.append((ph, float(k), float(c)))
kn = np.array([s[1] for s in scores]); kn = kn / (kn.max() or 1)
cn = np.array([s[2] for s in scores]); cn = cn / (cn.max() or 1)
downbeat_phase = int(np.argmax(0.6 * kn + 0.4 * cn))
downbeats = bt[downbeat_phase::4]

# Struktur: RMS und Brillanz pro Takt
rms = librosa.feature.rms(y=y, hop_length=HOP)[0]
cent = librosa.feature.spectral_centroid(y=y, sr=SR, hop_length=HOP)[0]
bars = []
for i in range(len(downbeats) - 1):
    a, b = librosa.time_to_frames([downbeats[i], downbeats[i + 1]], sr=SR, hop_length=HOP)
    bars.append({
        "bar": i,
        "t": round(float(downbeats[i]), 3),
        "rms_db": round(float(20 * np.log10(rms[a:b].mean() + 1e-9)), 1),
        "low_db": round(float(20 * np.log10(low[a:b].mean() + 1e-9)), 1),
        "centroid": round(float(cent[a:b].mean())),
    })
# Abschnittswechsel: große Sprünge der Bar-Merkmale
feat = np.array([[b["rms_db"], b["low_db"], b["centroid"] / 200.0] for b in bars])
jumps = np.r_[0, np.linalg.norm(np.diff(feat, axis=0), axis=1)]
for b, j in zip(bars, jumps):
    b["change"] = round(float(j), 2)

res = {
    "file": src,
    "duration": round(dur, 3),
    "tempo_bpm": round(tempo, 3),
    "grid_bpm": round(60.0 / period, 3),
    "beat_period": round(float(period), 5),
    "grid_phase0": round(float(phase0), 4),
    "grid_err_ms_p95": round(float(np.percentile(np.abs(grid_err), 95) * 1000), 1),
    "downbeat_phase": downbeat_phase,
    "phase_scores": [{"phase": s[0], "kick": round(s[1], 3), "chroma": round(s[2], 3)} for s in scores],
    "beats": [round(float(t), 4) for t in bt],
    "downbeats": [round(float(t), 4) for t in downbeats],
    "bars": bars,
}
json.dump(res, open(out, "w"), indent=1)
print(f"Dauer {dur:.1f} s · Tempo {tempo:.2f} BPM (Raster {60/period:.3f} BPM, p95-Abweichung {res['grid_err_ms_p95']} ms)")
print(f"Taktphase {downbeat_phase} · Scores {res['phase_scores']}")
print("Takt  Zeit    RMS   Bass  Zentroid  Wechsel")
for b in bars:
    print(f"{b['bar']:4d} {b['t']:7.2f} {b['rms_db']:6.1f} {b['low_db']:6.1f} {b['centroid']:8d} {b['change']:7.2f}")
