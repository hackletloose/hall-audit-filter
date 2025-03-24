# Audit Filter Bot

Ein Discord-Bot, der Nachrichten aus definierten Kanälen filtert und über einen Webhook weiterleitet.

## Features

- Filtert Nachrichten, die bestimmte Begriffe enthalten (z.B. "broadcast", "whitespace", "Camera")
- Leitet gefilterte Nachrichten an einen definierten Webhook weiter
- Führt periodische Aufgaben aus (z.B. regelmäßige Checks alle 30 Sekunden)

## Voraussetzungen

- Python 3.8+
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation

1. Repository klonen:
   ```bash
   git clone https://github.com/dein-benutzername/audit-filter.git
   cd audit-filter
2. (Optional) Virtuelle Umgebung erstellen und aktivieren:
   ```bash
   python -m venv venv
   source venv/bin/activate
3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
4. `.env` Datei erstellen
   ```bash
   cp.env.dist .env
   ```
   die Variablen in der ´.env´ Datei anpassen.
