# Edit-Plan: Welcomer-Video (Entwurf v1, zur Abnahme)

Regelwerk: `docs/styleguide.md`. Format 16:9, 1920 × 1080, 60 fps → Export 1080p.
Alle Zeiten = **Wort-Timestamps in der Rohdatei** (`raw/rohdatei.mov`, Whisper).

## Vorgaben des Nutzers
- Kunden-Clips nur **kurz**, je ein Clip „auf“ einer Hand des Sprechers, **Ton aus**
- **Keine Namen** (keine Lower Thirds)
- Kontakt-Elemente mit **Platzhalter-Daten**
- **Straffer Schnitt**

## Kürzungen (Rohschnitt)
| Raus | Zeit | Grund |
|---|---|---|
| alle Pausen > 0,2 s | – | Rhythmus |
| „quasi“ | 17,54–17,96 | Füllwort |
| „natürlich auch gewissermaßen bedingt durch unser Alter“ | 40,38–43,24 | Länge, schwächt die Aussage |
| „auch“ (in „Kunden auch erfolgreich“) | 50,48–50,92 | Füllwort |

Ergebnis: ca. **58–60 s** statt 1:09.

## Ablauf
| # | Satz (Rohdatei) | Baustein | Start auf Wort |
|---|---|---|---|
| 1 | „Herzlich willkommen!“ | **Hook:** „Willkommen“ groß in Serif kursiv **hinter dem Sprecher** (freigestellt) | „Herzlich“ 0,56 (= Frame 0 nach Schnitt) |
| 2 | „Jetzt bist du auf unserem One-Pager … Erfolg auf Social Media.“ | Captions (1–3 Wörter, Blur-in), **Punch-in 115 %** | „Erfolg“ 5,38 → Gold |
| 3 | „Dieses Video ist ganz oben auf unserem One-Pager …“ | **E/H:** stilisierter One-Pager im Browser-Rahmen, oberster Video-Slot leuchtet in Gold auf | „ganz oben“ 7,50 |
| 4 | „… dass es das Allerwichtigste ist, was du hier zu sehen bekommst.“ | **A:** Vollbild-Typo auf hellem Papier: klein „das“ + riesig *Allerwichtigste* | „Allerwichtigste“ 10,32 |
| 5 | „Hier stellen wir uns vor, was wir machen und was du von uns erwarten kannst …“ | Licht-Flash zurück in A-Roll, Captions, **Punch-in 130 %** | Flash 13,00 · Punch „machen“ 15,64 |
| 6 | „… für eine potenzielle Zusammenarbeit.“ | Caption, „Zusammenarbeit“ Serif kursiv | 20,20 |
| 7 | Sprecherwechsel B: „Bei unseren Leistungen … breit gefächertes Spektrum.“ | **Licht-Flash** auf dem Schnitt, Caption „Leistungen“ groß | Flash 21,26 · „Leistungen“ 21,66 |
| 8 | „Neben Produktvideos und Bildern machen wir Konzepte und … personalisierte Social-Media-Strategien“ | **G: Icon-Flow** (dunkler Verlauf), 4 Icons auf den Wörtern, verbunden durch sich zeichnende Linien | „Produktvideos“ 24,52 · „Bildern“ 25,50 · „Konzepte“ 27,02 · „Strategien“ 30,16 |
| 9 | „… damit euer Business so weit wie möglich wachsen kann.“ | Icons treten zurück, *wachsen* Serif kursiv mit steigender Gold-Linie | „wachsen“ 32,48 |
| 10 | „Sprich, vom Blueprint bis zur letztendlichen Umsetzung wird von uns alles übernommen.“ | **A:** „Blueprint“ (Sans) → Gold-Linie zeichnet sich → *Umsetzung* (Serif kursiv) | „Blueprint“ 33,84 · „Umsetzung“ 35,12 |
| 11 | Sprecher A: „Wir sind ein sehr junges Team mit viel Social-Media-Know-how“ | **Invert-Flash** auf dem Schnitt, Captions „junges Team“, „Know-how“ Gold, Punch-in 115 % | Flash 37,18 · „Know-how“ 39,64 |
| 12 | „und haben mit diversen Kunden in verschiedensten Bereichen,“ | Captions, Punch-in 100 % (weit, damit die Hände frei sind) | „Kunden“ 45,22 |
| 13 | „**wie man hier eben sieht**, auch zusammengearbeitet“ | **Kunden-Clips auf den Händen** (siehe unten) | Erscheinen 46,50 · weg 48,60 |
| 14 | „und haben schon mehrere Kunden erfolgreich an ihre Ziele gebracht.“ | Captions, „erfolgreich“ Gold, *Ziele* Serif kursiv | 50,92 / 51,82 |
| 15 | „Wenn du auch Teil dieses Erfolgs sein möchtest, kannst du … nach ganz unten scrollen.“ | One-Pager aus #3 kehrt zurück und **scrollt nach unten** (Callback), Pfeil zeichnet sich | „scrollen“ 56,92 |
| 16 | „Da findest du unsere E-Mail und auch unsere Telefonnummer, … telefonisch, aber auch per WhatsApp erreichbar sind.“ | **H: Glas-Karten** neben dem Sprecher, gestaffelt: ✉ `hallo@deine-agentur.de` · ☎ `+49 000 0000000` · 💬 „WhatsApp“ (neutrales Chat-Icon) | „E-Mail“ 58,48 · „Telefonnummer“ 59,86 · „WhatsApp“ 62,64 |
| 17 | „Wir freuen uns auf eure Kontaktaufnahme und … auf eine potenzielle Zusammenarbeit mit euch.“ | Captions, am Ende Blur-out in **Endkarte** auf hellem Papier: *Zusammenarbeit* + Kontakt-Platzhalter, 1 s Standbild | „Zusammenarbeit“ 68,10 |

## Detail: Kunden-Clips auf den Händen (#13)
- Bei 46,5–47,3 s öffnet Sprecher A beide Hände mit den Handflächen nach oben. Diese Geste wird zur Bühne.
- Clip 1 links, Clip 2 rechts, je eine **hochkante Video-Karte** (abgerundet, weicher Schatten, ca. 30 % Bildhöhe).
  Beide wachsen per Blur-in + Scale aus der jeweiligen Handfläche, folgen der Hand kurz (Tracking) und schweben
  danach ruhig an ihrem Platz, bis sie bei ~48,6 s per Blur-out verschwinden. Sichtbar ca. **2 s**.
- Clip 1 startet bei 0:00, Clip 2 bei 0:16. **Ton aus.**
- Ein kurzer Gold-Glow an den Kartenkanten, leiser Pop-Sound beim Erscheinen.

## Look
- **Farben (Vorschlag, passend zur goldenen Lobby):** Dunkel Espresso `#17120E` (60 %), Hell Papier `#F3EEE6` (30 %),
  Akzent Champagner-Gold `#C9A35B` (10 %)
- **Fonts:** Inter (Sans) + Instrument Serif Italic
- **A-Roll-Grading:** mehr Kontrast, leichte Vignette, Hauttöne natürlich halten
- **Übergänge:** nur Licht-Flash (Gold) + Invert-Flash
- **Sound:** ruhiges Musikbett (−20 dB unter Stimme), Boom bei #3, Whoosh beim Scrollen, Pops bei Icons/Karten, −14 LUFS

## Offene Punkte
1. Markenfarbe: Gold-Vorschlag ok, oder habt ihr eine eigene Agenturfarbe/ein Logo?
2. Wasserzeichen/Handle unten mittig: weglassen (da „ohne Namen“)?

---

## Umsetzung (Stand v1, abgenommen mit: Gold ok, kein Wasserzeichen, kein Text bei den Kunden-Clips)

- **Rohschnitt:** 59,7 s (`edit/make_edl.py` → `edit/cut_segments.sh`), Zeitachse unten = Ausgabe-Zeit.
  „quasi“-Schnitt (v7): Das „K“ setzt schon bei 17,465 s ein. Das Segment davor ist um 2 Frames in der Quelle verschoben
  (Slip in `make_edl.py`: 16,400–17,4667 statt 16,4667–17,5333): gleiche Länge, nur 13,767–14,833 s ändert sich,
  alle Zeiten davor und danach bleiben. Ton des Segments auf exakt 32 Frames aufgefüllt (AAC-Blockgrenze der Rohdatei).
- **Projekt:** `videos/welcomer-video/` (HyperFrames), Nachbearbeitung `edit/finish.sh`.
- **Kunden-Clips:** Karten sitzen auf den Handflächen (Hand-Tracking per MediaPipe), rechts Clip 1 ab 0:00,
  links Clip 2 ab 0:16, sichtbar ca. 38,4–40,6 s, stumm, Clip 1 auf 4:5 beschnitten (eingebrannte
  Untertitel entfernt), keinerlei Text.
- **Captions:** zweistufig (kleine Einleitung + großes Schlüsselwort), Zonen links/rechts neben dem Kopf,
  pro Satz genau ein Akzentwort in Serif kursiv.
- **Kontaktdaten:** `bremen.bites@gmail.com`, `0160 7913817` (in `index.html` an je 3 Stellen: One-Pager, Glas-Karten, Endkarte).
- **Musik:** „Family Affair“ (Instrumental), vom Nutzer nachgeliefert. Tempo 92,9 BPM (Takt 2,5835 s), 8-Takt-Phrasen.
  Schnitt (`edit/make_bgm.py`): Video 0–46,503 s = Song-Takte 6–23, danach Song-Outro (Takte 96–101), Schlussschlag 59,421 s.
  Mix: Voiceover-Carve (Stärke 0,8) gegen die Stimme, Bett-Pegel 0,16 (v4/v5: je −3 dB auf Wunsch), Hand-Stufe „Akzente Start/Schluss“.
- **Übergänge auf dem Beat-Raster:** One-Pager 5,167 (Downbeat) · Allerwichtigste 8,396–10,98 (genau ein Takt) ·
  Leistungen 20,668 (Phrasenbeginn) · Blueprint 29,065 · One-Pager 2 46,503 (Downbeat = Musik-Sprung) ·
  Endkarte 56,838 (Downbeat) · Goldlinie 59,41 mit dem Schlussschlag. Sprecherschnitte 17,767 und 32,533 liegen auf Achteln.
- **SFX:** v3 −7 dB, v4 nochmals −3,5 dB; Bass-Booms und Schluss-Chime entfernt.
- **Kunden-Karten (v5):** weicher Pop (Variante A aus der Hörprobe, `edit/make_card_sfx.py`), zweimal und klar getrennt:
  rechte Karte 38,39 s / Pop 38,43 (Achtel, rechts), linke Karte 38,71 s / Pop 38,75 (Downbeat, links, einen Ganzton höher).
- **Leistungen-Graph (v5):** „Personalisierte Social-Media-Strategien“, „Personalisierte“ in Gold kursiv auf dem Wort (24,64 s).
- **Typografie (v4):** eine Familie für alles: Archivo. Schlüsselwörter Black (900), Akzentwörter Black kursiv in Gold/Bronze
  (ersetzt Instrument Serif), Kleintexte SemiBold. Laufweite −0,035 em bei großen Wörtern.
- **Endkarte:** dunkel (Espresso) mit *Zusammenarbeit* in Gold-Serif und den Kontakt-Platzhaltern, abweichend vom
  Plan (helles Papier); auf Wunsch umstellbar.
- **Vorschau v1:** 60,5 s, −14,6 LUFS, Spitzenpegel −1,4 dBTP. Master `renders/welcomer_vorschau_v1.mp4`,
  komprimierte Kopie `_web.mp4` (< 30 MB) für den Versand.
