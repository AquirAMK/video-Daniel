# Erzeugt edl.json für den Rohschnitt (Quellzeiten in Sekunden, auf 1/30 s gerastert).
import json, math
FPS = 30
silences = [(1.34,2.15),(6.31,6.73),(12.36,13.00),(14.48,14.97),(15.93,16.54),(20.87,21.24),
            (23.99,24.34),(25.79,26.15),(27.62,27.92),(30.65,30.89),(33.01,33.33),(35.67,35.97),
            (36.95,37.21),(52.42,52.93),(57.31,57.77),(58.89,59.15),(63.51,63.85),(65.89,66.32)]
# Gestrichene Wörter (Quelle): quasi, „natürlich … Alter“, „auch“
removals = [(17.55,18.01),(40.20,43.70),(50.40,50.62)]
START, END = 0.48, 69.30
cuts = []
for s, e in silences:
    if e - s < 0.22: continue
    a, b = s + 0.08, e - 0.06
    if (s, e) == (36.95, 37.21): a = 36.98   # vor dem Bildwechsel auf Sprecher A (37,000)
    if (s, e) == (20.87, 20.87): pass
    cuts.append((a, b))
cuts += removals
cuts.sort()
snap = lambda t: round(t * FPS) / FPS
segs, cur = [], START
for a, b in cuts:
    segs.append((snap(cur), snap(a))); cur = b
segs.append((snap(cur), snap(END)))
# Bildwechsel A→B liegt bei 20,967: Segmentgrenze muss davor enden / danach starten
out, t = [], 0.0
for s, e in segs:
    out.append({"src_start": round(s, 4), "src_end": round(e, 4), "out_start": round(t, 4)})
    t += e - s
json.dump({"fps": FPS, "segments": out, "duration": round(t, 4)}, open("/home/user/video-Daniel/edit/edl.json", "w"), indent=1)
for o in out: print(o)
print("Dauer", round(t, 2))
