

# Recherche-Ergebnisse: Confiforms IFTTT und Jira-Integration

## Wichtige Erkenntnisse aus der Dokumentation

### Confiforms IFTTT-Grundlagen
- IFTTT-Makros sind Teil der Confiforms Form Definition und müssen im Confiforms Form Makro-Body platziert werden
- Es gibt 4 Event-Typen: onCreated, onModified, onDeleted, onError
- IFTTT-Operationen sind NICHT TRANSAKTIONAL
- 38 verschiedene Aktionstypen verfügbar, einschließlich Jira-Issue-Erstellung

### Jira-Integration Spezifika
- Jira-Issues können über Application Link oder WebService Connection erstellt werden
- JSON-Format wird für die Jira REST API verwendet
- Feldwerte können über [entry.FIELD_NAME] referenziert werden
- Für Felder mit Zeilenumbrüchen muss escapeJSON verwendet werden
- IFTTT-Ergebnisse können über ${iftttResult_0} oder [iftttResult_0] abgerufen werden

### Beispiel JSON für Jira-Issue-Erstellung:
```json
{
    "fields": {
       "project": { 
          "key": "TEST"
       },
       "summary": "[entry.summary]",
       "description": "[entry.details.escapeJSON]",
       "issuetype": {
          "name": "Bug"
       }
   }
}
```

### Für Epic-Erstellung relevante Punkte:
- Epic ist ein spezieller Issue-Type in Jira
- customfield_10103 kann als zusätzliches Feld gesetzt werden
- Projekt-Key JIRAPRO24 muss verwendet werden



## Epic-spezifische Erkenntnisse

### Epic Name vs Epic Link
- **Epic Name**: Nur für Epic Issue Type verfügbar, kurzer Name zur Identifikation des Epics
- **Epic Link**: Relationales Feld für alle Issue Types (außer Sub-tasks), verknüpft Issues mit ihrem Parent Epic
- Epic Name ist standardmäßig ein Pflichtfeld beim Erstellen von Epics

### Wichtige Punkte für die Implementierung:
1. Epic ist ein spezieller Issue Type in Jira
2. Epic Name ist ein Custom Field, das nur für Epic Issue Type verfügbar ist
3. customfield_10103 kann als zusätzliches Feld für spätere Modifikationen verwendet werden
4. Projekt-Key JIRAPRO24 muss in der JSON-Struktur verwendet werden

### Nächste Schritte:
- Entwicklung der Confiforms-Makro-Konfiguration
- Erstellung der JSON-Struktur für Epic-Erstellung
- Implementation der IFTTT-Integration

