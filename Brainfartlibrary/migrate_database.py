#!/usr/bin/env python3
"""
Datenbank-Migrations-Script für Brainfart Library
Fügt neue Felder hinzu und migriert bestehende Daten
"""

import json
import os
import shutil
from datetime import datetime

def migrate_database(db_path="data/prompts.json"):
    """Migriert die Datenbank auf die neue Struktur"""

    print("🔄 Starte Datenbank-Migration...")

    # Backup erstellen
    backup_path = f"{db_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    if os.path.exists(db_path):
        shutil.copy2(db_path, backup_path)
        print(f"✅ Backup erstellt: {backup_path}")

    # Datenbank laden
    try:
        with open(db_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ Datenbank-Datei nicht gefunden!")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON-Fehler beim Laden: {e}")
        return False

    print(f"📊 Gefundene Prompts: {len(data.get('prompts', {}))}")

    # Migration durchführen
    changes_made = False

    # 1. Tag-Management-Struktur hinzufügen
    if "tag_management" not in data:
        print("➕ Füge tag_management-Struktur hinzu...")

        # Alle verwendeten Tags sammeln
        all_tags = set()
        for prompt in data.get("prompts", {}).values():
            all_tags.update(prompt.get("tags", []))

        data["tag_management"] = {
            "available_tags": sorted(list(all_tags))
        }

        print(f"   ✅ {len(all_tags)} Tags zur Verwaltungsliste hinzugefügt")
        changes_made = True
    else:
        print("✓ tag_management bereits vorhanden")

    # 2. Color-Feld zu jedem Prompt hinzufügen
    prompts_updated = 0
    for prompt_id, prompt in data.get("prompts", {}).items():
        if "color" not in prompt:
            prompt["color"] = "none"
            prompts_updated += 1

    if prompts_updated > 0:
        print(f"➕ Füge color-Feld zu {prompts_updated} Prompt(s) hinzu...")
        print("   ✅ Alle Prompts auf Standard-Farbe 'none' gesetzt")
        changes_made = True
    else:
        print("✓ Alle Prompts haben bereits ein color-Feld")

    # 3. Metadaten aktualisieren
    if "metadata" in data and changes_made:
        data["metadata"]["last_modified"] = datetime.now().isoformat()
        print("✅ Metadaten aktualisiert")

    # Geänderte Datenbank speichern
    if changes_made:
        try:
            with open(db_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"💾 Datenbank erfolgreich migriert und gespeichert")
            print(f"\n📋 Zusammenfassung:")
            print(f"   - Prompts gesamt: {len(data.get('prompts', {}))}")
            print(f"   - Verwaltete Tags: {len(data.get('tag_management', {}).get('available_tags', []))}")
            print(f"   - Backup unter: {backup_path}")
            return True
        except Exception as e:
            print(f"❌ Fehler beim Speichern: {e}")
            print(f"   Backup wiederherstellen: {backup_path} -> {db_path}")
            return False
    else:
        print("\n✅ Keine Migration erforderlich - Datenbank ist bereits aktuell")
        # Backup löschen wenn keine Änderungen
        if os.path.exists(backup_path):
            os.remove(backup_path)
            print("   (Backup wurde entfernt)")
        return True

def verify_migration(db_path="data/prompts.json"):
    """Verifiziert die Migration"""
    print("\n🔍 Verifiziere Migration...")

    try:
        with open(db_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Checks
        checks = {
            "tag_management vorhanden": "tag_management" in data,
            "available_tags ist Liste": isinstance(data.get("tag_management", {}).get("available_tags"), list),
            "Alle Prompts haben color": all("color" in p for p in data.get("prompts", {}).values()),
            "Alle color-Werte gültig": all(
                p.get("color") in ["none", "red", "orange", "yellow", "green", "teal",
                                   "blue", "indigo", "purple", "pink", "brown", "gray", "black"]
                for p in data.get("prompts", {}).values()
            )
        }

        all_passed = all(checks.values())

        for check, passed in checks.items():
            status = "✅" if passed else "❌"
            print(f"   {status} {check}")

        if all_passed:
            print("\n🎉 Migration erfolgreich abgeschlossen!")
        else:
            print("\n⚠️  Einige Checks sind fehlgeschlagen")

        return all_passed

    except Exception as e:
        print(f"❌ Fehler bei der Verifikation: {e}")
        return False

if __name__ == "__main__":
    # Zum Brainfartlibrary-Verzeichnis wechseln
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print("=" * 60)
    print("  Brainfart Library - Datenbank-Migration v1.1.0")
    print("=" * 60)
    print()

    db_path = os.path.join("data", "prompts.json")

    # Migration durchführen
    success = migrate_database(db_path)

    if success:
        # Verifikation durchführen
        verify_migration(db_path)
    else:
        print("\n❌ Migration fehlgeschlagen!")
        print("   Bitte Backup manuell wiederherstellen.")

    print("\n" + "=" * 60)
