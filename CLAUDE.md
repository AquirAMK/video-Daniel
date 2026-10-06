# Projekt: Welcomer-Video für die Social-Media-Agentur

Ziel: Die eigene Rohdatei (Talking Head) gemeinsam im Premium-Stil à la Iman Gadzhi schneiden.
Kommunikation mit dem Nutzer auf Deutsch.

- **Verbindliches Regelwerk:** `docs/styleguide.md` (Rhythmus, Farbe, Typo, Captions, Bausteine A–J,
  Übergänge, Sound, Workflow). Jeder Schnitt folgt diesem Dokument.
- Hintergrund und Tutorial-Rezepte: `docs/iman-gadzhi-stil-recherche.md`
- Referenzen dienen nur dem Stil. Inhalte, Motive und Layouts nicht kopieren.
- Vor dem Bauen immer erst den Edit-Plan (Satz → Baustein → Wort-Timestamp) vom Nutzer abnehmen lassen.
- Skills liegen unter `.claude/skills/` (Versionen in `skills-lock.json`). Einstieg für Grafiken:
  `hyperframes`, für den Rohschnitt: `video-use`, für Captions hinter dem Sprecher: `embedded-captions`.
- Transkription: `video-use` nutzt standardmäßig ElevenLabs Scribe (API-Key nötig). Ohne Key das
  Wort-Transkript lokal mit faster-whisper erzeugen (Audio per ffmpeg als 16-kHz-Array übergeben;
  PyAV-Version im Container passt nicht zum direkten Dateipfad).
