#!/usr/bin/env python3
"""
Brainfart Library - Lokale Prompt-Bibliothek
Startet den lokalen Web-Server für die Prompt-Verwaltung
"""

import os
import sys
import uvicorn

# Projekt-Pfad zum Python-Path hinzufügen
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

if __name__ == "__main__":
    print("🧠 Brainfart Library startet...")
    print("📍 Lokale Adresse: http://127.0.0.1:8000")
    print("⏹️  Zum Beenden: Strg+C")
    print("-" * 50)

    try:
        uvicorn.run(
            "app.main:app",
            host="127.0.0.1",
            port=8000,
            reload=True,
            reload_dirs=[current_dir]
        )
    except KeyboardInterrupt:
        print("\n👋 Brainfart Library beendet. Bis bald!")
    except Exception as e:
        print(f"❌ Fehler beim Starten: {e}")
        sys.exit(1)
