# Analyse der alternativen Confiforms-Lösung

## URL: https://wiki.vertuna.com/spaces/TEST/pages/18186319/Create+Jira+issue+save+the+created+Jira+key+back+to+ConfiForms+and+create+a+page+with+Jira+macro

## Überblick
Diese alternative Lösung zeigt eine erweiterte Confiforms-Implementation, die folgende Funktionalitäten bietet:
1. Jira Issue erstellen
2. Jira Key zurück zu ConfiForms speichern
3. Automatische Erstellung einer Confluence-Seite mit Jira-Makro

## Erkannte Struktur

### Formular-Felder
1. **JIRAKey** (text) - Wird automatisch befüllt nach Issue-Erstellung
2. **pageTitle** (text) - Titel für die zu erstellende Confluence-Seite

### Field Definition Rules
- JIRAKey-Feld wird versteckt wenn ID leer ist (condition: id:[empty])

### IFTTT-Aktionen

#### 1. Jira Issue Creation
```
Event: onCreated
Action: Create JIRA Issue
ResultName: myjiracreator
```

**JSON-Payload:**
```json
{
    "fields": {
        "project": {
            "key": "TEST"
        },
        "summary": "TEST Issue - [entry.pageTitle]",
        "issuetype": {
            "name": "Bug"
        }
    }
}
```

#### 2. ConfiForms Entry Update
```
Event: onCreated
Action: Create ConfiForms Entry
Title: entryId=[entry.id]&amp;JIRAKey=${iftttResult_myjiracreator}
```
- Speichert den Jira Key zurück in das ursprüngliche ConfiForms-Entry

#### 3. Confluence Page Creation
```
Event: onCreated
Action: Create Page
Title: [entry.pageTitle]
```
- Erstellt eine neue Confluence-Seite
- Enthält Jira-Makro zur Anzeige des erstellten Issues

### Jira-Makro Integration
Die erstellte Seite enthält ein Jira-Makro:
```
server: JIRA
columns: key,summary,type,created,updated,due,assignee,reporter,priority,status,resolution
maximumIssues: 20
jqlQuery: key = [entry.JIRAKey] OR parent = [entry.JIRAKey]
serverId: e448067e-a16a-3ba7-893b-87a33aec6e05
```

## Unterschiede zu unserer Lösung

### Erweiterte Funktionalität
1. **Automatische Seiten-Erstellung**: Erstellt automatisch eine neue Confluence-Seite
2. **Jira-Makro Integration**: Zeigt das erstellte Issue direkt in der neuen Seite an
3. **Bidirektionale Datenverknüpfung**: Speichert Jira Key zurück in ConfiForms
4. **Erweiterte JQL-Queries**: Unterstützt Parent-Child-Beziehungen

### Technische Unterschiede
1. **Projekt**: Verwendet "TEST" statt "JIRAPRO24"
2. **Issue Type**: Verwendet "Bug" statt "Epic"
3. **Komplexere IFTTT-Kette**: Drei verkettete IFTTT-Aktionen
4. **Automatische Page-Generierung**: Zusätzliche Funktionalität

## Vorteile der alternativen Lösung
1. **Vollständige Workflow-Automatisierung**: Von Issue-Erstellung bis zur Dokumentation
2. **Bessere Nachverfolgung**: Jira Key wird in ConfiForms gespeichert
3. **Integrierte Dokumentation**: Automatische Seiten-Erstellung
4. **Erweiterte Jira-Integration**: Direkte Anzeige des Issues in Confluence

## Potenzielle Nachteile
1. **Höhere Komplexität**: Mehr bewegliche Teile
2. **Mehr Fehlerquellen**: Drei IFTTT-Aktionen können fehlschlagen
3. **Berechtigungsanforderungen**: Benötigt Rechte zur Seiten-Erstellung
4. **Wartungsaufwand**: Komplexere Konfiguration zu pflegen



## Vollständige Struktur der alternativen Lösung

### ConfiForms Table
```xml
<ac:structured-macro ac:name="confiform-table">
    <ac:parameter ac:name="messageToShowWhenEmpty">No records yet</ac:parameter>
    <ac:parameter ac:name="formName">f</ac:parameter>
</ac:structured-macro>
```
- Zeigt alle erstellten Einträge in einer Tabelle an
- Nachricht "No records yet" wenn keine Einträge vorhanden

### Field Displays
Die Lösung zeigt sowohl JIRAKey als auch pageTitle Felder in der Tabelle an:
```xml
<ac:structured-macro ac:name="confiform-field">
    <ac:parameter ac:name="fieldName">JIRAKey</ac:parameter>
</ac:structured-macro>

<ac:structured-macro ac:name="confiform-field">
    <ac:parameter ac:name="fieldName">pageTitle</ac:parameter>
</ac:structured-macro>
```

### Created Pages Section
```xml
<p>Created pages:</p>
<ac:structured-macro ac:name="children">
</ac:structured-macro>
```
- Zeigt automatisch alle erstellten Child-Pages an
- Nutzt das native Confluence Children-Makro

## Technische Details

### JQL Query Details
```
jqlQuery: key = [entry.JIRAKey] OR parent = [entry.JIRAKey]
```
- Zeigt sowohl das Haupt-Issue als auch alle Child-Issues an
- Ermöglicht hierarchische Issue-Darstellung

### Server-Konfiguration
```
serverId: e448067e-a16a-3ba7-893b-87a33aec6e05
```
- Spezifische Jira-Server-ID für die Integration
- Muss an die eigene Jira-Instanz angepasst werden

## Workflow-Ablauf der alternativen Lösung

1. **Benutzer-Eingabe**: pageTitle wird eingegeben
2. **Jira Issue Creation**: 
   - Issue wird mit Summary "TEST Issue - [pageTitle]" erstellt
   - Issue Type: Bug
   - Projekt: TEST
3. **ConfiForms Update**:
   - Jira Key wird zurück in das ursprüngliche Entry gespeichert
   - JIRAKey-Feld wird sichtbar gemacht
4. **Page Creation**:
   - Neue Confluence-Seite wird erstellt
   - Titel entspricht dem pageTitle
   - Seite enthält Jira-Makro mit dem erstellten Issue
5. **Anzeige**:
   - ConfiForms Table zeigt alle Einträge
   - Children-Makro zeigt alle erstellten Seiten
   - Jira-Makro zeigt Issue-Details

## Erweiterte Features

### Bidirektionale Verknüpfung
- Jira Issue → ConfiForms (via JIRAKey)
- ConfiForms → Confluence Page (via pageTitle)
- Confluence Page → Jira Issue (via Jira-Makro)

### Automatische Dokumentation
- Jede Issue-Erstellung führt zu einer dokumentierten Seite
- Hierarchische Struktur durch Children-Makro
- Direkte Issue-Anzeige in der Dokumentation

### Skalierbarkeit
- Table-View für Übersicht aller Einträge
- Children-Makro für Navigation zwischen Seiten
- JQL-Unterstützung für komplexe Abfragen

