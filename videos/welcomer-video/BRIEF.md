---
workflow: general-video
flow: automation
storyboard: no
message: "Wir sind ein junges Social-Media-Team, das vom Blueprint bis zur Umsetzung alles übernimmt – melde dich bei uns."
destination: website
aspect: 1920x1080
language: de
audience: "Besucher des Agentur-One-Pagers (potenzielle Kunden)"
length: 60s
---

## Intent

Welcomer-Video ganz oben auf dem One-Pager einer jungen Social-Media-Agentur. Zwei Sprecher in einer
warm beleuchteten Hotel-Lobby. Premium-Look à la Iman Gadzhi: ruhig, edel, eine Akzentfarbe
(Champagner-Gold), Editorial-Typografie, wortgenau getimte Animationen. Verbindliches Regelwerk:
`docs/styleguide.md`. Abgenommener Ablauf: `docs/edit-plan.md`.

## Assets

- assets/aroll.mp4 — Rohschnitt der Rohdatei (Pausen/Füllwörter entfernt, gegradet, 1080p30, 59,67 s), Basis-Spur mit Ton
- assets/clip1.mp4 — Kunden-Clip 1 (Sushi-Laden), ab 0:00, 4:5 zugeschnitten (eingebrannte Untertitel weggeschnitten), stumm
- assets/clip2.mp4 — Kunden-Clip 2 (Restaurant), ab 0:16, 4:5 zugeschnitten, stumm
- assets/fonts/ — Archivo (variabel: Gewicht 100–900, Breite 62–125 %, normal + kursiv), eine Familie für alle Texte
- assets/music/bgm_edit.wav — Musikbett „Family Affair“ (Mary J. Blige, Instrumental), vom Nutzer geliefert, takt-genau geschnitten mit `edit/make_bgm.py` (nicht im Git)

## Customizations

- Kunden-Clips erscheinen nur kurz (~2 s) auf den Handflächen des Sprechers (Hand-Tracking), Ton aus, **kein Text** dazu
- Keine Namen / Lower Thirds, **kein Wasserzeichen**
- Kontakt-Elemente (E-Mail, Telefon, WhatsApp) mit den echten Daten: bremen.bites@gmail.com · 0160 7913817
- Hook „Willkommen“ hinter dem freigestellten Sprecher (Matte-Composite nach dem Render)
- Straffer Schnitt (~60 s)

## Notes

- Alle Bildschirmtexte deutsch, echte Umlaute und ß, deutsche Typografie
- Format bleibt 16:9 (1920 × 1080), kein 9:16-Export
- Musik: „Family Affair“ (Instrumental, 92,9 BPM), Nutzerwunsch. Video startet auf einer „1“, Sprung ins Song-Outro bei 46,503 s,
  Schlussschlag bei 59,421 s direkt nach dem letzten Wort. Voiceover-Carve gegen die Stimme, Bett ca. 20 LU unter der Stimme
  (Nutzer: zweimal „etwas leiser“).
  Hinweis an den Nutzer: kommerzieller Song, für die Website ist eine Lizenz nötig.
- SFX sehr dezent (insgesamt ca. −10,5 dB ggü. v1), keine Bass-Booms, kein Schluss-Chime; bei den Kunden-Karten ein weicher
  Pop (Variante A, vom Nutzer per Hörprobe freigegeben), zweimal: rechts auf der Achtel 38,43 s, links auf der „1“ 38,75 s
- Leistungen-Graph: „Personalisierte Social-Media-Strategien“ („Personalisierte“ in Gold, das Alleinstellungsmerkmal)
