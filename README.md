# 🧠 Brainfart Library

Eine lokale, web-basierte Prompt-Bibliothek für die Verwaltung deiner LLM-Prompts mit Cross-Platform-Synchronisation.

## ✨ Features

- **🌐 Web-Interface**: Modernes, responsives GUI über den Browser
- **💾 Lokale Speicherung**: Alle Daten bleiben auf deinem Computer
- **☁️ Cloud-Sync Ready**: Maximal 2 Dateien für einfache OneDrive/Cloud-Synchronisation
- **🏷️ Tag-System**: Organisiere Prompts mit Tags und Kategorien
- **📝 Draft-Modus**: Speichere Entwürfe ohne sie zu aktivieren
- **🔄 Versionierung**: Automatische Historie aller Prompt-Änderungen
- **🔍 Such-Funktionen**: Durchsuche Titel und Tags
- **📊 Statistiken**: Überblick über deine Prompt-Sammlung
- **⚡ Cross-Platform**: Läuft auf Windows und Linux

## 📁 Projektstruktur

```
Brainfartlibrary/
├── app/                    # Backend-Code
│   ├── main.py            # FastAPI-Anwendung
│   ├── models.py          # Datenmodelle
│   └── database.py        # JSON-Datenbank-Service
├── data/                  # Deine Prompt-Daten (für Cloud-Sync)
│   └── prompts.json       # Hauptdatenbank
├── static/                # Frontend-Assets
│   ├── app.js            # JavaScript-Logik
│   └── style.css         # Styling
├── templates/             # HTML-Templates
│   └── index.html        # Hauptseite
├── requirements.txt       # Python-Dependencies
└── run.py                # Start-Script
```

## 🚀 Installation & Start

### 1. Dependencies installieren
```bash
pip install -r requirements.txt
```

### 2. Anwendung starten
```bash
python run.py
```

### 3. Browser öffnen
Gehe zu: **http://127.0.0.1:8000**

## 💡 Verwendung

### Neuen Prompt erstellen
1. Klicke auf **"Neuer Prompt"**
2. Fülle Titel und Inhalt aus
3. Füge Tags hinzu (kommagetrennt)
4. Wähle Status: **Aktiv** oder **Entwurf**
5. Speichern

### Prompts verwalten
- **Bearbeiten**: Klicke auf eine Prompt-Karte
- **Suchen**: Nutze die Suchleiste in der Sidebar
- **Filtern**: Verwende die Filter-Buttons (Alle/Aktiv/Entwürfe)
- **Tags**: Klicke auf Tags in der Sidebar zum Filtern

### Versionierung
- Jede Änderung am Prompt-Inhalt erstellt automatisch eine neue Version
- Alte Versionen werden in der Historie gespeichert
- Die aktuelle Versionsnummer wird angezeigt

## ☁️ Cloud-Synchronisation

### Für OneDrive/Google Drive/Dropbox:
1. Verschiebe den `data/`-Ordner in deinen Cloud-Ordner
2. Erstelle einen symbolischen Link:
   - **Windows**: `mklink /D data "C:\\Users\\YourName\\OneDrive\\BrainfartLibrary\\data"`
   - **Linux**: `ln -s /home/yourname/OneDrive/BrainfartLibrary/data data`

### Manuelle Synchronisation:
- Kopiere einfach die Datei `data/prompts.json` zwischen deinen Geräten

## 🔧 Konfiguration

### Port ändern
Ändere in `run.py` die Zeile:
```python
port=8000  # Ändere zu gewünschtem Port
```

### Datenbank-Pfad ändern
Ändere in `app/main.py`:
```python
db = PromptDatabase("pfad/zu/deiner/datenbank.json")
```

## 🏗️ Technische Details

- **Backend**: Python 3.x + FastAPI
- **Frontend**: HTML5 + Bootstrap 5 + Vanilla JavaScript
- **Datenbank**: JSON-Files (human-readable, git-friendly)
- **API**: RESTful endpoints für alle Operationen

## 📡 API-Endpoints

- `GET /` - Web-Interface
- `GET /api/prompts` - Alle Prompts
- `POST /api/prompts` - Neuer Prompt
- `PUT /api/prompts/{id}` - Prompt bearbeiten
- `DELETE /api/prompts/{id}` - Prompt löschen
- `GET /api/search?q=query` - Suche
- `GET /api/tags` - Alle Tags
- `GET /api/stats` - Statistiken

## 🔄 Updates & Erweiterungen

Das System ist erweiterbar für:
- **Volltext-Suche** im Prompt-Inhalt
- **Export-Funktionen** (Markdown, HTML, PDF)
- **Import-Features** aus anderen Tools
- **Backup-Automatisierung**
- **CLI-Interface** für Power-User

## ⚠️ Wichtige Hinweise

- **Backup**: Sichere regelmäßig deine `data/prompts.json`
- **Synchronisation**: Schließe die App vor Cloud-Sync zwischen Geräten
- **Ports**: Stelle sicher, dass Port 8000 verfügbar ist
- **Browser**: Moderne Browser (Chrome, Firefox, Edge) werden empfohlen

## 🐛 Problembehebung

### Server startet nicht
```bash
# Prüfe ob Port 8000 belegt ist
netstat -ano | findstr :8000

# Verwende anderen Port
python run.py --port 8001
```

### Datenbank-Fehler
- Prüfe Schreibberechtigung im `data/`-Verzeichnis
- Validiere `prompts.json` auf JSON-Syntax-Fehler

### Dependencies-Probleme
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

---

**Viel Spaß mit deiner Brainfart Library! 🧠✨**
