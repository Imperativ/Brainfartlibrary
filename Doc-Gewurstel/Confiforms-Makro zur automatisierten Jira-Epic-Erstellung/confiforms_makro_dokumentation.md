# Confiforms-Makro für automatisierte Jira-Epic-Erstellung

## Übersicht

Dieses Dokument beschreibt die vollständige Konfiguration eines Confiforms-Makros für Confluence, das es Benutzern ermöglicht, über eine einfache Eingabemaske automatisch Jira-Epics im Projekt JIRAPRO24 zu erstellen. Das Makro nutzt die Confiforms IFTTT-Integration, um über die Jira REST API v3 neue Epics zu erstellen und dem Benutzer nach erfolgreicher Erstellung einen interaktiven Link zum neuen Epic anzuzeigen.

## Technische Grundlagen

### Confiforms-Architektur

Confiforms ist ein leistungsstarkes Plugin für Atlassian Confluence, das es ermöglicht, datengesteuerte Formulare und Workflows direkt in Confluence-Seiten zu erstellen [1]. Die Architektur basiert auf mehreren Kernkomponenten:

**Confiforms Form Definition**: Das Hauptmakro, das die Struktur und Eigenschaften des Formulars definiert. Es fungiert als Container für alle anderen Confiforms-Komponenten und legt die grundlegenden Parameter wie Formularname, Speicheroptionen und Berechtigungen fest [1].

**Confiforms Field Definition**: Diese Makros definieren die einzelnen Eingabefelder des Formulars. Jedes Feld hat einen spezifischen Typ (Text, Textarea, Dropdown, etc.) und kann mit Validierungsregeln und Abhängigkeiten konfiguriert werden [1].

**Confiforms Registration Control**: Dieses Makro stellt die eigentliche Benutzeroberfläche für die Dateneingabe bereit. Es kann entweder mit einer Standardlayout oder mit einem benutzerdefinierten Layout verwendet werden [1].

**Confiforms IFTTT Integration Rules**: Das Herzstück für externe Integrationen. IFTTT (If This Then That) ermöglicht es, auf Ereignisse wie das Erstellen, Bearbeiten oder Löschen von Datensätzen zu reagieren und entsprechende Aktionen auszuführen [1].

### Jira REST API Integration

Die Integration mit Jira erfolgt über die REST API v3, die eine standardisierte Schnittstelle für die programmatische Interaktion mit Jira bietet [2]. Für die Epic-Erstellung sind folgende Aspekte relevant:

**Authentifizierung**: Die API unterstützt verschiedene Authentifizierungsmethoden, wobei für Confiforms-Integrationen typischerweise Basic Authentication mit API-Token verwendet wird [2].

**Epic-spezifische Felder**: Epics sind ein spezieller Issue-Type in Jira mit besonderen Eigenschaften. Das Epic Name-Feld ist ein Custom Field, das nur für Epic Issue Types verfügbar ist und als Pflichtfeld konfiguriert werden kann [3].

**JSON-Struktur**: Die API erwartet Daten im JSON-Format, wobei die Struktur spezifische Felder für Projekt, Issue-Type, Summary und Custom Fields enthält [2].

## Makro-Konfiguration

### Schritt 1: Confiforms Form Definition

Die Basis des Makros bildet das Confiforms Form Definition Makro mit folgender Konfiguration:


```
Makro: ConfiForms Form
Parameter:
- ConfiForms Form name: epicCreator
- Registration form title: Neues Jira Epic erstellen
- Save button label: Epic erstellen
- Close button label: Schließen
- Lock form: false
- Secure storage: false
```

Diese Konfiguration erstellt ein Formular mit dem Namen "epicCreator", das als eindeutige Identifikation innerhalb der Confluence-Seite dient. Der Titel "Neues Jira Epic erstellen" wird dem Benutzer im Registrierungsdialog angezeigt, während der angepasste Button-Text "Epic erstellen" die Aktion klarer beschreibt als der Standard-Text "Speichern".

### Schritt 2: Field Definition für Epic-Name

Innerhalb des Confiforms Form Makros wird ein Field Definition Makro für das Epic-Name-Eingabefeld platziert:

```
Makro: ConfiForms Field Definition
Parameter:
- Field Name: epicName
- Field Type: text
- Field Label: Epic Name
- Required: true
- Max Length: 255
```

Das Feld "epicName" ist als Pflichtfeld konfiguriert, da sowohl Jira als auch die Geschäftslogik einen Epic-Namen erfordern. Die maximale Länge von 255 Zeichen entspricht den typischen Jira-Feldlimitierungen und verhindert übermäßig lange Namen, die die Benutzerfreundlichkeit beeinträchtigen könnten.

### Schritt 3: Registration Control

Das Registration Control Makro stellt die Benutzeroberfläche bereit:

```
Makro: ConfiForms Registration Control
Parameter:
- Form name: epicCreator
- Show as: dialog
- Button label: Neues Epic erstellen
```

Die Dialog-Darstellung bietet eine saubere, modale Benutzeroberfläche, die den Benutzer nicht von der aktuellen Seite wegführt. Der Button-Text "Neues Epic erstellen" macht die Funktion sofort erkennbar.

### Schritt 4: IFTTT Integration für Jira-Epic-Erstellung

Das Kernstück der Integration ist das IFTTT-Makro, das auf das "onCreated"-Ereignis reagiert:

```
Makro: ConfiForms IFTTT
Parameter:
- Event: onCreated
- Action to perform: Create Jira Issue
- Custom name for the action result: jiraEpicResult
- Do not report error: false
```

**Makro-Body (JSON für Jira REST API):**

```json
{
    "fields": {
        "project": {
            "key": "JIRAPRO24"
        },
        "summary": "[entry.epicName]",
        "issuetype": {
            "name": "Epic"
        },
        "customfield_10103": "[entry.epicName]"
    }
}
```

Diese JSON-Struktur definiert die Daten, die an die Jira REST API gesendet werden. Der Projekt-Key "JIRAPRO24" ist fest kodiert, wie in den Anforderungen spezifiziert. Das Summary-Feld erhält den vom Benutzer eingegebenen Epic-Namen über die Referenz `[entry.epicName]`. Der Issue-Type wird explizit als "Epic" gesetzt, und das Custom Field "customfield_10103" wird ebenfalls mit dem Epic-Namen befüllt, um spätere Modifikationen zu ermöglichen.

### Schritt 5: Erfolgsanzeige und Link-Generierung

Ein zweites IFTTT-Makro wird für die Rückmeldung an den Benutzer konfiguriert:

```
Makro: ConfiForms IFTTT
Parameter:
- Event: onCreated
- Action to perform: Update Entry
- Condition: [iftttResult_jiraEpicResult] IS NOT EMPTY
- Custom name for the action result: updateResult
```

**Makro-Body:**

```json
{
    "jiraKey": "[iftttResult_jiraEpicResult.key]",
    "jiraUrl": "https://your-jira-instance.com/browse/[iftttResult_jiraEpicResult.key]",
    "status": "Epic erfolgreich erstellt"
}
```

Dieses IFTTT nutzt das Ergebnis des ersten IFTTT-Aufrufs, um zusätzliche Felder im Confiforms-Datensatz zu aktualisieren. Die Jira-Ticket-Nummer und URL werden aus der API-Antwort extrahiert und für die Anzeige vorbereitet.

### Schritt 6: Zusätzliche Field Definitions für Ergebnisanzeige

Um die Ergebnisse anzuzeigen, werden weitere Felder definiert:

```
Makro: ConfiForms Field Definition (für jiraKey)
Parameter:
- Field Name: jiraKey
- Field Type: text
- Field Label: Jira Ticket
- Required: false

Makro: ConfiForms Field Definition (für jiraUrl)
Parameter:
- Field Name: jiraUrl
- Field Type: text
- Field Label: Jira Link
- Required: false

Makro: ConfiForms Field Definition (für status)
Parameter:
- Field Name: status
- Field Type: text
- Field Label: Status
- Required: false
```

### Schritt 7: ListView für Ergebnisanzeige

Ein ListView-Makro zeigt die erstellten Epics und ihre Links an:

```
Makro: ConfiForms ListView
Parameter:
- Form name: epicCreator
- Filter: status IS NOT EMPTY
- Number of items to show: 10
```

**ListView-Body:**

```html
<div class="epic-result">
    <h4>Epic erfolgreich erstellt!</h4>
    <p><strong>Epic Name:</strong> [entry.epicName]</p>
    <p><strong>Jira Ticket:</strong> <a href="[entry.jiraUrl]" target="_blank">[entry.jiraKey]</a></p>
    <p><strong>Status:</strong> [entry.status]</p>
</div>
```

## Erweiterte Konfiguration

### Fehlerbehandlung

Für eine robuste Lösung sollte ein zusätzliches IFTTT für Fehlerbehandlung implementiert werden:

```
Makro: ConfiForms IFTTT
Parameter:
- Event: onError
- Action to perform: Update Entry
- Custom name for the action result: errorResult
```

**Makro-Body:**

```json
{
    "status": "Fehler bei der Epic-Erstellung",
    "errorMessage": "Bitte versuchen Sie es erneut oder kontaktieren Sie den Administrator"
}
```

### Automatische Seitenaktualisierung

Um die automatische Seitenaktualisierung zu implementieren, kann JavaScript in einem HTML-Makro verwendet werden:

```html
<script>
// Überwacht Änderungen im Confiforms-Container
var observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        if (mutation.type === 'childList') {
            // Prüft auf neue Epic-Ergebnisse
            var epicResults = document.querySelectorAll('.epic-result');
            if (epicResults.length > 0) {
                // Aktualisiert die Seite nach 2 Sekunden
                setTimeout(function() {
                    location.reload();
                }, 2000);
            }
        }
    });
});

// Startet die Überwachung
var targetNode = document.querySelector('.confluenceTable');
if (targetNode) {
    observer.observe(targetNode, { childList: true, subtree: true });
}
</script>
```

## Authentifizierung und Sicherheit

### API-Token-Konfiguration

Die Authentifizierung erfolgt über die Confluence-Jira Application Link Konfiguration. Administratoren müssen sicherstellen, dass:

1. Eine Application Link zwischen Confluence und Jira konfiguriert ist
2. Die Benutzer über ausreichende Berechtigungen verfügen, um Epics im Projekt JIRAPRO24 zu erstellen
3. Die API-Verbindung ordnungsgemäß getestet wurde

### Berechtigungsmodell

Confiforms nutzt das Confluence-Berechtigungsmodell. Benutzer mit "Edit"-Berechtigung für die Seite haben administrative Rechte für das Formular. Durch Einschränkung der Edit-Rechte kann der Zugriff auf das Formular kontrolliert werden [1].

## Deployment und Testing

### Installation

1. Platzieren Sie alle Makros in der gewünschten Reihenfolge auf einer Confluence-Seite
2. Konfigurieren Sie die Parameter entsprechend der obigen Spezifikation
3. Testen Sie die Application Link-Verbindung zu Jira
4. Führen Sie einen Testlauf mit einem Dummy-Epic durch

### Validierung

Vor der Produktionsfreigabe sollten folgende Tests durchgeführt werden:

- **Funktionstest**: Erstellen eines Test-Epics und Überprüfung in Jira
- **Berechtigungstest**: Validierung mit verschiedenen Benutzerrollen
- **Fehlerbehandlung**: Test mit ungültigen Daten oder Verbindungsproblemen
- **Performance**: Überprüfung der Antwortzeiten bei mehreren gleichzeitigen Anfragen

## Referenzen

[1] Vertuna WIKI - ConfiForms Documentation: https://wiki.vertuna.com/spaces/CONFIFORMS/pages/1212428/Documentation

[2] Atlassian Developer - Jira REST API Examples: https://developer.atlassian.com/server/jira/platform/jira-rest-api-examples/

[3] Atlassian Support - Epic Name vs Epic Link: https://support.atlassian.com/jira/kb/epic-name-vs-epic-link/

