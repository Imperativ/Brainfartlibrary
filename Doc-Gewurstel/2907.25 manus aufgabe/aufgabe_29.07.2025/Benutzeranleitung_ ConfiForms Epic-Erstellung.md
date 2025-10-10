# Benutzeranleitung: ConfiForms Epic-Erstellung

**Version:** 1.0  
**Datum:** 29. Juli 2025  
**Zielgruppe:** Endbenutzer mit Jira-Berechtigung für Projekt BWPTLS24

## Schnellstart

Das ConfiForms-Makro ermöglicht es Ihnen, Epic-Tickets im Jira-Projekt BWPTLS24 direkt aus Confluence heraus zu erstellen, ohne manuell in Jira navigieren zu müssen.

### Voraussetzungen
- Anmeldung in Confluence erforderlich
- Berechtigung zur Epic-Erstellung in Jira-Projekt BWPTLS24
- Aktive Application Link-Verbindung zwischen Confluence und Jira

## Formular ausfüllen

### Pflichtfelder (müssen ausgefüllt werden):

**1. Zusammenfassung**
- Kurze, prägnante Beschreibung des Epics (5-255 Zeichen)
- Wird automatisch mit "Einführung von" ergänzt
- Beispiel: "Neue Benutzeroberfläche für Dashboard"

**2. Anforderungskategorie**
- Dropdown-Auswahl aus vier Optionen:
  - Technische Anforderung
  - Fachliche Anforderung
  - Betriebliche Anforderung
  - Qualitätsanforderung

**3. Priorität**
- Standard-Jira-Prioritäten verfügbar
- Standardwert: "Mittel"
- Optionen: Sehr niedrig, Niedrig, Mittel, Hoch, Sehr hoch

### Optionale Felder:

**4. Komponenten**
- Mehrfachauswahl möglich
- Werden dynamisch aus Jira-Projekt geladen
- Leer lassen, falls nicht zutreffend

**5. Bearbeiter**
- Standardmäßig auf Sie selbst gesetzt
- Kann auf anderen Benutzer geändert werden
- Leer lassen für automatische Zuweisung

**6. Co-Bearbeiter/-in**
- Mehrere Benutzer auswählbar
- Werden zusätzlich dem Epic zugewiesen

**7. Beschreibung**
- Detaillierte Beschreibung des Epics
- Unterstützt mehrzeiligen Text
- Optional, aber empfohlen

**8. Lösungsversion**
- Mehrfachauswahl möglich
- Werden dynamisch aus Jira-Projekt geladen

## Epic erstellen

1. Alle Pflichtfelder ausfüllen
2. Optionale Felder nach Bedarf ergänzen
3. Button "Epic erstellen" klicken
4. Auf Bestätigung warten

### Erfolgsmeldung
Bei erfolgreicher Erstellung erhalten Sie:
- Bestätigungsmeldung
- Epic-Nummer (z.B. BWPTLS24-123)
- Direktlink zum Epic in Jira
- Automatische Aktualisierung der Übersichtstabelle

## Übersichtstabelle

Die Tabelle unter dem Formular zeigt die 5 zuletzt erstellten Epics an:
- **Epic-Nummer**: Klickbarer Link zum Jira-Ticket
- **Epic-Name**: Klickbarer Link zum Jira-Ticket  
- **Ersteller**: Wer das Epic erstellt hat
- **Erstellt am**: Datum und Uhrzeit der Erstellung
- **Status**: Erfolgreich erstellt oder Fehler

## Häufige Probleme und Lösungen

### "Fehler bei der Epic-Erstellung"
**Mögliche Ursachen:**
- Fehlende Jira-Berechtigung
- Application Link-Problem
- Ungültige Eingabedaten

**Lösungsansätze:**
1. Alle Pflichtfelder prüfen
2. Sonderzeichen in Textfeldern vermeiden
3. Bei wiederholten Fehlern Administrator kontaktieren

### "Komponenten/Lösungsversionen werden nicht geladen"
**Lösungsansätze:**
1. Seite neu laden (F5)
2. Browser-Cache leeren
3. Prüfen, ob Jira erreichbar ist

### "Link zum Epic funktioniert nicht"
**Lösungsansätze:**
1. Prüfen, ob Sie in Jira angemeldet sind
2. Direkten Link aus Erfolgsmeldung verwenden
3. Epic-Nummer manuell in Jira suchen

## Tipps für optimale Nutzung

### Zusammenfassung formulieren
- Verwenden Sie klare, verständliche Begriffe
- Vermeiden Sie Abkürzungen ohne Erklärung
- Denken Sie daran: "Einführung von" wird automatisch vorangestellt

### Beschreibung strukturieren
- Nutzen Sie Absätze für bessere Lesbarkeit
- Beschreiben Sie das "Was" und "Warum"
- Fügen Sie Akzeptanzkriterien hinzu, wenn bekannt

### Bearbeiter zuweisen
- Lassen Sie das Feld leer für Selbstzuweisung
- Wählen Sie nur Personen aus, die tatsächlich verfügbar sind
- Co-Bearbeiter sparsam einsetzen

## Support und Kontakt

Bei technischen Problemen oder Fragen zur Nutzung wenden Sie sich an:
- **IT-Support**: [Ihre Support-Kontaktdaten]
- **Jira-Administration**: [Ihre Jira-Admin-Kontakte]
- **Confluence-Administration**: [Ihre Confluence-Admin-Kontakte]

Halten Sie bei Supportanfragen folgende Informationen bereit:
- Fehlermeldung (Screenshot)
- Verwendeter Browser und Version
- Zeitpunkt des Auftretens
- Eingabedaten (ohne sensible Informationen)

