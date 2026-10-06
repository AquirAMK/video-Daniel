# Recherche: Welcomer-Video im Iman-Gadzhi-Stil

Quelle: „The Complete Guide to Editing like Iman Gadzhi in 2026! (Masterclass)“ von Joseph | Video Editing
(https://www.youtube.com/watch?v=O6HOYu_ZEnw, ca. 23 Min.)

Analysiert wurden das komplette Transkript, ca. 150 Storyboard-Frames und das Thumbnail. Den Videostream
selbst hat YouTube blockiert (Bot-Check), deshalb sind Feinheiten wie exakte Easing-Kurven aus dem
gesprochenen Text abgeleitet und nicht Frame für Frame nachgemessen. Werbeblöcke für den Kurs des
Creators („Ultimate Editors“) sind hier weggelassen.

---

## 1. Die drei Design-Prinzipien

### Farbe: die 60-30-10-Regel
- Gedreht wird vor einem **farbigen Hintergrundlicht** (rot, blau usw.). Diese Farbe bestimmt die
  Hauptfarbe des ganzen Videos.
- Aus ihr werden drei Varianten abgeleitet:
  - **60 %:** dunkle Variante als Hauptfarbe (Hintergründe, Flächen)
  - **30 %:** hellere Variante als Sekundärfarbe
  - **10 %:** knallige Variante als Akzentfarbe (Schlüsselwörter, Glows, Linien)
- Aus den Storyboards: fast schwarze Hintergründe, Akzente glühen (gelb-orange, rot, blau).

### Schrift: zwei Fonts
- **Sans-Font** für normalen Text (im Tutorial: *Creator Display Medium*), weiß.
- **Spezial-Font** nur für hervorgehobene Wörter: Serif, fett oder Script (im Tutorial: *Apple Garamond*,
  kursiv) in Akzentfarbe plus **Deep Glow**.
- Freie Alternativen: Sans → *Inter*, *Manrope*, *Satoshi*; Spezial → *Instrument Serif Italic*,
  *Cormorant Garamond Italic*, *Playfair Display Italic*.

### Formen: abgerundete Rechtecke
- UI-Elemente bestehen fast nur aus **Quadraten/Rechtecken**.
- **Eckenradius 30–70 px**, je nach Größe der Form (nicht zu rund, nicht zu eckig).
- Oft mit **leuchtender Kante (Glow-Edge)**, damit sie sich vom dunklen Hintergrund abheben.

---

## 2. Die vier Animationstypen

| # | Typ | Wann einsetzen |
|---|-----|----------------|
| 1 | **3D-Text-Sequenzen** (Wörter ploppen auf, teils *hinter* dem Sprecher) | Hook/Intro, Kernaussagen auf A-Roll oder B-Roll |
| 2 | **Abstrakte Story-Szenen** (KI-Bilder, Kamera fliegt durch) | eine Geschichte oder Emotion bebildern |
| 3 | **Cartoon-Szenen** (Figur vor Hintergrund, Zoom z. B. ins Gehirn) | Konzepte, Eigenschaften, „was in jemandem vorgeht“ |
| 4 | **UI-Animationen** (abgerundete Glow-Karten, on-screen oder Vollbild) | Listen, Schritte, Zahlen, Leistungen |

---

## 3. Technische Rezepte (aus After Effects übersetzt)

### Typ 1: Text-Pop-up (A-Roll mit Text hinter dem Sprecher)
1. **Sprecher freistellen** (AE: Roto Brush auf einem Duplikat). Ergebnis: Hintergrund-Layer und
   freigestellter Sprecher-Layer obendrauf. Text liegt dazwischen, dadurch wirkt er 3D.
2. **Buchstaben-Animation** (AE Text-Animator, Werte aus dem Tutorial):
   - Position: Buchstaben starten weiter unten
   - Blur: 10
   - Füllfarbe: Gelb (Startfarbe)
   - Opazität: 0
   - Range Selector: Shape *Ramp Up*, Units *Index*, End 0, Start in 1 s von 0 auf 5 animieren.
   - Ergebnis: Buchstaben „laufen“ gestaffelt von unscharf/unsichtbar ins Bild.
3. **Layout:** Wörter einzeln setzen („Work like new money“). Spezialwörter in Serif + hellem
   Orange + Deep Glow. Zweite Zeile leicht **im Bogen** angeordnet und in Z-Tiefe *vor* dem Sprecher.
4. **Tiefe:** Einstellungsebene zwischen Hintergrund und Sprecher mit Gaussian Blur, Helligkeit runter
   und invertierter, weicher Ellipsenmaske. So entsteht eine unscharfe Vignette.
5. **Kamerafahrt:** Start nah und hoch, dann Zoom-out und Absenken, Ease-in und Ease-out.
6. **Kino-Look:** *Posterize Time* auf **15 fps** für die Text-Pop-ups (bewusst ruckeliger Text).

### Typ 1b: Text auf B-Roll
- Eine Bildhälfte (z. B. links) mit Maske unscharf und dunkel machen, Text dort platzieren.
- Sans-Zeile plus Serif-Zeile in Orange („Both have their / *Competitive Advantages*“).
- **Unterstreichung, die sich zeichnet:** Pfad-Linie mit Trim Paths (End 0 → 100 %), Speed-Graph geglättet.

### Typ 2: Abstrakte Story-Szenen
1. Satz in 2–3 Phrasen zerlegen („When you come from **nothing** / **hardship** / you have a **hunger**“).
2. Pro Phrase ein **KI-Bild im selben Stil** (Referenzbilder mitgeben): monochrom blau, cineastisch,
   volumetrisches Licht, gleiche Figur und gleiche Umgebung. **2× upscalen.**
3. Bilder als 3D-Ebenen **nebeneinander bzw. hintereinander im Raum** anordnen. Kanten mit Linear Wipe
   und Feather weich auslaufen lassen.
4. Pro Szene: Sans-Text + Spezialwort (Akzentfarbe) + gezeichnete Unterstreichung.
5. **Kamera mit „Null-Stacking“:** Kamera → Null 1 → Null 2. Jede Bewegung erreicht ihr
   **Geschwindigkeitsmaximum genau am Szenenwechsel**. Die nächste Bewegung startet, bevor die vorige
   endet, die Kamera **steht also nie still**.
   Bewegungsfolge im Tutorial: schneller Schwenk von links → Schwenk rechts → Zoom-out → Schwenk rechts.

### Typ 3: Cartoon-Szene
- KI-Cartoonfigur **auf Greenscreen** generieren (Weiß lässt sich schlecht keyen, wenn die Augen weiß sind).
- Passender Cartoon-Hintergrund (z. B. Skyline) plus Vignette.
- Text in Z-Tiefe zwischen Figur und Hintergrund. Übergang: Text faded aus, Figur wird per Wipe
  schwarz, Vignette wird stärker.
- Detail (Gehirn) ploppt mit Rotation, Position und Opazität rein: **schnell rein, langsam aus**.
- Callout-Linien (Trim Paths) mit Labels („Infinite energy“, „Hard to replicate“).
- Kamera zoomt ins Detail, Speed-Peak am Übergang.

### Typ 4: UI-Karten (z. B. „Slow down / Be patient / Think long term“)
- **Hintergrund:** dunkler Verlauf (grau → schwarz) plus **Grid-Overlay** (1 px, 25 % Deckkraft).
- **Karte:** Rechteck mit **70 px Radius**, Verlaufsfüllung grau → schwarz.
- **Glow-Kante:** Light-Sweep-Effekt plus Deep Glow (0,5), Blend-Modus *Screen*.
- **Text:** weißer Sans-Text zentriert.
- **Icons:** dezent an den Kartenrändern, auf die Karte begrenzt (Track Matte), mit weichem Wipe
  ausgeblendet und niedriger Deckkraft. Quelle im Tutorial: Flaticon.
- Alles an einen **Platzhalter** parenten, dann wird nur dieser animiert: Skalierung und Position von
  klein/unten nach final in ca. 2 s, **schnell rein, langsam aus**.
- Für mehrere Karten duplizieren und **gestaffelt untereinander** einblenden.

### Weitere Muster aus den Storyboard-Frames
- „Later in this video“-Vorschau im Intro: kleine Clips in Glow-Rahmen mit Handschrift-Labels und Linien.
- Nummerierte Kapitel im Raum (1 Color / 2 Fonts / 3 Shapes) mit Glow, hinter bzw. neben dem Sprecher.
- B-Roll in **glühenden, abgerundeten Rahmen** auf dunklem Hintergrund statt Vollbild.
- Zahlen-Counter („$1,764“) über Karten.
- Dezentes CTA-Banner unten mit Farbverlauf („Join … below“).
- Sprecher-Setup: dunkle Lamellenwand, Pflanze, warmes Seitenlicht, farbiges Akzentlicht.

---

## 4. Übertragung auf das Welcomer-Video der Agentur

Vorschlag für ca. 60–90 s, 16:9 (Website-Hero). Für Social zusätzlich 9:16.

| Zeit | Abschnitt | Animationstyp |
|------|-----------|---------------|
| 0–5 s | Hook: „Wir machen deine Marke **unübersehbar**.“ | Typ 1: Text hinter dem Sprecher, Kamera-Zoom-out |
| 5–20 s | Problem: Unternehmer posten ins Leere, keine Zeit, keine Reichweite | Typ 2: 2–3 abstrakte Szenen in Markenfarbe |
| 20–40 s | Leistungen: Strategie, Content-Produktion, Community, Ads | Typ 4: gestaffelte UI-Karten mit Icons |
| 40–55 s | Beweis: Zahlen und Ergebnisse (Reichweite, Follower, Leads) | Typ 4: Counter auf Glow-Karte, B-Roll in Rahmen |
| 55–70 s | Ablauf: Erstgespräch → Strategie → Wachstum | Typ 4: 3-teilige Karten-Sequenz |
| 70–80 s | CTA: „Buch dir jetzt dein kostenloses Erstgespräch“ | Typ 1 + CTA-Button-Karte |

**Markenfarbe:** Beim Dreh ein farbiges Hintergrundlicht in der Agenturfarbe setzen und daraus die
60-30-10-Palette ableiten.

---

## 5. Umsetzung ohne After Effects (programmatisch)

| AE-Technik | Programmatische Entsprechung |
|------------|------------------------------|
| Schnitt, Füllwörter, Pausen | Transkript-basierter Schnitt mit ffmpeg (Skill `video-use`) |
| Roto Brush (Text hinter Sprecher) | Personen-Segmentierung pro Frame (z. B. MediaPipe/rembg) als Alpha-Maske |
| Text-Animator, Trim Paths, Glow | HTML/CSS/SVG + GSAP (HyperFrames) oder React (Remotion): `stroke-dashoffset`, `filter: blur()/drop-shadow()` |
| 3D-Kamera + Null-Stacking | CSS-3D-Transforms bzw. verschachtelte Gruppen mit getrennten Animationen |
| Posterize Time 15 fps | Zeit der Text-Animation auf 1/15 s quantisieren |
| KI-Bilder (Envato) | Bildgenerierung, z. B. über den in dieser Session verbundenen Higgsfield-Connector |
| Color Grading | ffmpeg-Filter (`eq`, `curves`, `colorbalance`) oder LUT |

---

## 6. Gefundene Skills (`npx skills find`)

Geprüft nach Installs, GitHub-Stars und Security-Audits auf skills.sh.

### Kern-Workflow (empfohlen)

| Skill | Wofür | Installs | Repo-Stars | Audits |
|-------|-------|----------|-----------|--------|
| `heygen-com/hyperframes@talking-head-recut` | **Passt am besten:** legt getimte, gestaltete Karten (Titel, Lower-Thirds, Callouts, Seitenpanels) passend zum Transkript über ein Talking-Head-Video und rendert MP4 | 278K | 57,3K | alle Pass |
| `heygen-com/hyperframes@hyperframes` | Einstieg/Router für HyperFrames (Video aus HTML), wird von den anderen vorausgesetzt | 786K | 57,3K | Snyk: Warn |
| `heygen-com/hyperframes@motion-graphics` | einzelne Motion-Elemente: Logo-Sting, Intro, Lower-Third | 358K | 57,3K | Snyk: Warn |
| `browser-use/video-use@video-use` | **Rohschnitt** aus dem Transkript: Versprecher, Pausen, Takes. Wichtig, weil `talking-head-recut` den Clip selbst nicht schneidet | 4,3K | 28,1K | Snyk: Warn |

### Alternativ: Remotion statt HyperFrames (React-basiert)

| Skill | Wofür | Installs | Repo-Stars |
|-------|-------|----------|-----------|
| `remotion-dev/skills@remotion-best-practices` | offizielle Remotion-Regeln | 577K | 4,8K |
| `remotion-dev/skills@remotion-captions` | animierte Untertitel aus Transkript | 127K | 4,8K |

### Ergänzend

| Skill | Wofür | Installs | Repo-Stars |
|-------|-------|----------|-----------|
| `affaan-m/ecc@video-editing` | allgemeiner Schnitt-Workflow für echtes Footage (Struktur, Overlays, Reframing 16:9 → 9:16) | 4,5K | 273,7K |
| `coreyhaines31/marketingskills@video` | Marketing-Video-Konzept, Ziel, Plattform, Länge | 77K | 53,4K |
| `coreyhaines31/marketingskills@copywriting` | Skript, Hook und CTA für das Welcomer-Video | 216K | 53,4K |
| `elevenlabs/skills@sound-effects` | Whooshes und Pops für die Animationen (braucht ElevenLabs-API-Key) | 8,6K | 472 |

### Bewusst nicht empfohlen
- `101-skills/superpowers@ai-video-generation` und Klone (qu-skills, magentosh …): sehr hohe Installzahl
  (680K), aber nur **5 GitHub-Stars**. Wirkt aufgebläht. Außerdem reine KI-Videogenerierung, kein Schnitt.

### Installation (Vorschlag)
```bash
npx skills add https://github.com/heygen-com/hyperframes --skill hyperframes
npx skills add https://github.com/heygen-com/hyperframes --skill talking-head-recut
npx skills add https://github.com/heygen-com/hyperframes --skill motion-graphics
npx skills add https://github.com/browser-use/video-use --skill video-use
npx skills add https://github.com/coreyhaines31/marketingskills --skill copywriting
```

---

## 7. Was noch gebraucht wird
1. **Rohmaterial:** Talking-Head-Aufnahme (ideal: 4K/1080p, farbiges Hintergrundlicht in Markenfarbe,
   externes Mikro) plus B-Roll (Team, Arbeitsplatz, Kunden-Posts, Screen-Recordings von Insights).
2. **Brand:** Logo (SVG/PNG), Markenfarbe(n), ggf. Fonts.
3. **Skript** bzw. Kernaussagen, oder Skript gemeinsam schreiben.
4. **Format:** 16:9 (Website), 9:16 (Reels/TikTok) oder beides; Ziellänge.
5. **Zahlen/Referenzen** für die Beweis-Karten.
