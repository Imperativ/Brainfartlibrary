# ConfiForms-Makro Konzeption: Jira-Epic-Erstellung

## Technische Spezifikationen
- **Confluence**: Version 9.2.4
- **Jira**: Version 10.3.6 (Data Center)
- **ConfiForms**: Version 3.17.7
- **Jira-Projekt**: BWPTLS24
- **Jira-URL**: https://jira.franz.extraklaus.de/
- **Authentifizierung**: Application Link (für authentifizierte Benutzer)

## Formular-Struktur

### Benötigte Makros:
1. **ConfiForms Form Definition** (Container)
2. **ConfiForms Field Definition** (für jedes Formularfeld)
3. **ConfiForms Registration Control** (Submit-Button)
4. **ConfiForms IFTTT Integration Rules** (Jira-API-Integration)
5. **ConfiForms TableView** (für die 5 letzten Tickets)

### Formularfelder (in Reihenfolge):

1. **summary** (Text)
   - Beschriftung: "Zusammenfassung"
   - Typ: text
   - Pflichtfeld: Ja
   - Validierung: 5-255 Zeichen, keine Sonderzeichen

2. **epic_name** (Text)
   - Beschriftung: "Epic Name"
   - Typ: text
   - Pflichtfeld: Ja
   - Automatisch gleich summary

3. **anforderungskategorie** (Dropdown)
   - Beschriftung: "Anforderungskategorie"
   - Typ: dropdown
   - Optionen: "technische Anforderung", "fachliche Anforderung", "betriebliche Anforderung", "Qualitätsanforderung"
   - Pflichtfeld: Ja

4. **components** (Multi-Select)
   - Beschriftung: "Komponenten"
   - Typ: multiselect
   - Datenquelle: Dynamisch aus Jira-Projekt BWPTLS24
   - Pflichtfeld: Nein

5. **priority** (Dropdown)
   - Beschriftung: "Priorität"
   - Typ: dropdown
   - Optionen: "Sehr niedrig", "Niedrig", "Mittel", "Hoch", "Sehr hoch"
   - Standard: "Mittel"
   - Pflichtfeld: Ja

6. **assignee** (User-Select)
   - Beschriftung: "Bearbeiter"
   - Typ: user
   - Standard: Aktueller Benutzer
   - Pflichtfeld: Nein

7. **co_bearbeiter** (Multi-User-Select)
   - Beschriftung: "Co-Bearbeiter/-in"
   - Typ: multiuser
   - Pflichtfeld: Nein

8. **description** (Textarea)
   - Beschriftung: "Beschreibung"
   - Typ: textarea
   - Pflichtfeld: Nein

9. **fix_versions** (Multi-Select)
   - Beschriftung: "Lösungsversion"
   - Typ: multiselect
   - Datenquelle: Dynamisch aus Jira-Projekt BWPTLS24
   - Pflichtfeld: Nein

### Versteckte Felder:
- **duedate**: Automatisch aktuelles Datum
- **customfield_10524**: Automatisch aktuelles Datum

## JSON-Mapping für Jira-API

```json
{
    "fields": {
        "project": {
            "key": "BWPTLS24"
        },
        "issuetype": {
            "name": "Epic"
        },
        "summary": "Einführung von [entry.summary]",
        "customfield_10103": "[entry.epic_name]",
        "customfield_10403": {
            "id": "[entry.anforderungskategorie]"
        },
        "components": [
            {
                "name": "[entry.components]"
            }
        ],
        "priority": {
            "name": "[entry.priority]"
        },
        "duedate": "[entry._now.jiraDate]",
        "customfield_10524": "[entry._now.jiraDate]",
        "assignee": {
            "name": "[entry.assignee]"
        },
        "customfield_12500": {
            "name": "[entry.co_bearbeiter]"
        },
        "description": "[entry.description.escapeJSON]",
        "fixVersions": [
            {
                "name": "[entry.fix_versions]"
            }
        ]
    }
}
```

## Workflow-Ablauf

1. **Formular anzeigen**: Benutzer klickt auf Button
2. **Eingabe validieren**: Client-seitige Validierung
3. **Epic erstellen**: IFTTT-Regel sendet JSON an Jira-API
4. **Erfolg anzeigen**: Issue-Key wird zurückgegeben
5. **Tabelle aktualisieren**: 5 neueste Epics anzeigen
6. **Fehlerbehandlung**: Bei Fehlern Benutzer informieren

## Fehlerbehandlung

- **Validierungsfehler**: Felder rot markieren, Fehlermeldung anzeigen
- **API-Fehler**: Benutzerfreundliche Meldung mit Fehlerdetails
- **Netzwerkfehler**: Retry-Mechanismus vorschlagen
- **Berechtigungsfehler**: Auf fehlende Jira-Rechte hinweisen

## Benutzeroberfläche

- **Responsive Design**: Funktioniert auf Desktop und Mobile
- **Intuitive Bedienung**: Klare Beschriftungen und Hilfestellungen
- **Fortschrittsanzeige**: Loading-Spinner während API-Aufruf
- **Erfolgsmeldung**: Link zum erstellten Epic mit Ticket-Nummer

