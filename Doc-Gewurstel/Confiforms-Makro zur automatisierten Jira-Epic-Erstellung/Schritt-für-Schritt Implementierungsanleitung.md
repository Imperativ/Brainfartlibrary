# Schritt-für-Schritt Implementierungsanleitung

## Confiforms-Makro für Jira-Epic-Erstellung

Diese Anleitung führt Sie durch die praktische Umsetzung des Confiforms-Makros in Confluence. Folgen Sie den Schritten in der angegebenen Reihenfolge, um ein funktionsfähiges Epic-Erstellungsformular zu implementieren.

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass:
- Confiforms Plugin in Confluence installiert und aktiviert ist
- Eine Application Link zwischen Confluence und Jira konfiguriert ist
- Sie über Edit-Berechtigung für die Ziel-Confluence-Seite verfügen
- Ihre Benutzer Berechtigung haben, Epics im Projekt JIRAPRO24 zu erstellen

## Schritt 1: Neue Confluence-Seite erstellen

1. Navigieren Sie zu dem Confluence-Space, in dem das Makro platziert werden soll
2. Erstellen Sie eine neue Seite mit einem aussagekräftigen Titel wie "Epic-Erstellung für JIRAPRO24"
3. Öffnen Sie die Seite im Bearbeitungsmodus

## Schritt 2: ConfiForms Form Definition hinzufügen

1. Klicken Sie auf das "+" Symbol, um ein neues Makro hinzuzufügen
2. Suchen Sie nach "ConfiForms Form" und wählen Sie es aus
3. Konfigurieren Sie die Parameter wie folgt:

```
ConfiForms Form name: epicCreator
Registration form title: Neues Jira Epic erstellen
Save button label: Epic erstellen
Close button label: Schließen
Lock form: (nicht aktiviert)
Secure storage: (nicht aktiviert)
```

4. Bestätigen Sie die Eingabe mit "Insert"

## Schritt 3: Field Definition für Epic-Name hinzufügen

1. Platzieren Sie den Cursor INNERHALB des ConfiForms Form Makros
2. Fügen Sie ein neues Makro hinzu: "ConfiForms Field Definition"
3. Konfigurieren Sie die Parameter:

```
Field Name: epicName
Field Type: text
Field Label: Epic Name
Required: true
Max Length: 255
```

4. Bestätigen Sie mit "Insert"

## Schritt 4: Zusätzliche Field Definitions für Ergebnisanzeige

Fügen Sie drei weitere Field Definition Makros hinzu (alle INNERHALB des Form Makros):

### Field Definition für Jira Key:
```
Field Name: jiraKey
Field Type: text
Field Label: Jira Ticket
Required: false
```

### Field Definition für Jira URL:
```
Field Name: jiraUrl
Field Type: text
Field Label: Jira Link
Required: false
```

### Field Definition für Status:
```
Field Name: status
Field Type: text
Field Label: Status
Required: false
```

## Schritt 5: IFTTT für Jira-Epic-Erstellung hinzufügen

1. Fügen Sie ein "ConfiForms IFTTT" Makro INNERHALB des Form Makros hinzu
2. Konfigurieren Sie die Parameter:

```
Event: onCreated
Action to perform: Create Jira Issue
Custom name for the action result: jiraEpicResult
Do not report error: (nicht aktiviert)
```

3. Im Makro-Body fügen Sie folgenden JSON-Code ein:

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

**Wichtiger Hinweis**: Verwenden Sie das "No Format" Makro um den JSON-Code, falls Confluence Formatierungsprobleme verursacht:

1. Platzieren Sie den Cursor im IFTTT-Makro-Body
2. Fügen Sie ein "No Format" Makro hinzu
3. Fügen Sie den JSON-Code in das No Format Makro ein

## Schritt 6: IFTTT für Ergebnis-Update hinzufügen

1. Fügen Sie ein zweites "ConfiForms IFTTT" Makro INNERHALB des Form Makros hinzu
2. Konfigurieren Sie die Parameter:

```
Event: onCreated
Action to perform: Update Entry
Condition: [iftttResult_jiraEpicResult] IS NOT EMPTY
Custom name for the action result: updateResult
```

3. Im Makro-Body fügen Sie folgenden JSON-Code ein:

```json
{
    "jiraKey": "[iftttResult_jiraEpicResult.key]",
    "jiraUrl": "https://IHRE-JIRA-INSTANZ.com/browse/[iftttResult_jiraEpicResult.key]",
    "status": "Epic erfolgreich erstellt"
}
```

**Wichtig**: Ersetzen Sie "IHRE-JIRA-INSTANZ.com" durch die tatsächliche URL Ihrer Jira-Instanz.

## Schritt 7: IFTTT für Fehlerbehandlung hinzufügen

1. Fügen Sie ein drittes "ConfiForms IFTTT" Makro INNERHALB des Form Makros hinzu
2. Konfigurieren Sie die Parameter:

```
Event: onError
Action to perform: Update Entry
Custom name for the action result: errorResult
```

3. Im Makro-Body:

```json
{
    "status": "Fehler bei der Epic-Erstellung",
    "errorMessage": "Bitte versuchen Sie es erneut oder kontaktieren Sie den Administrator"
}
```

## Schritt 8: Registration Control hinzufügen

1. Platzieren Sie den Cursor AUSSERHALB des ConfiForms Form Makros
2. Fügen Sie ein "ConfiForms Registration Control" Makro hinzu
3. Konfigurieren Sie die Parameter:

```
Form name: epicCreator
Show as: dialog
Button label: Neues Epic erstellen
```

## Schritt 9: ListView für Ergebnisanzeige hinzufügen

1. Fügen Sie ein "ConfiForms ListView" Makro AUSSERHALB des Form Makros hinzu
2. Konfigurieren Sie die Parameter:

```
Form name: epicCreator
Filter: status IS NOT EMPTY
Number of items to show: 10
```

3. Im ListView-Body fügen Sie folgenden HTML-Code ein:

```html
<div class="epic-result" style="border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; background-color: #f9f9f9;">
    <h4 style="color: #0052cc; margin-top: 0;">Epic erfolgreich erstellt!</h4>
    <p><strong>Epic Name:</strong> [entry.epicName]</p>
    <p><strong>Jira Ticket:</strong> <a href="[entry.jiraUrl]" target="_blank" style="color: #0052cc; text-decoration: none;">[entry.jiraKey]</a></p>
    <p><strong>Status:</strong> <span style="color: #36b37e;">[entry.status]</span></p>
    <p style="margin-bottom: 0;"><small>Erstellt am: [entry._created.formatDate('dd.MM.yyyy HH:mm')]</small></p>
</div>
```

## Schritt 10: Automatische Seitenaktualisierung (Optional)

Für die automatische Seitenaktualisierung fügen Sie ein HTML-Makro AUSSERHALB aller anderen Makros hinzu:

```html
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Überwacht Änderungen im Confiforms-Container
    var observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList') {
                // Prüft auf neue Epic-Ergebnisse
                var epicResults = document.querySelectorAll('.epic-result');
                if (epicResults.length > 0) {
                    // Aktualisiert die Seite nach 3 Sekunden
                    setTimeout(function() {
                        location.reload();
                    }, 3000);
                }
            }
        });
    });

    // Startet die Überwachung
    var targetNode = document.querySelector('body');
    if (targetNode) {
        observer.observe(targetNode, { childList: true, subtree: true });
    }
});
</script>
```

## Schritt 11: Seite speichern und testen

1. Speichern Sie die Confluence-Seite
2. Testen Sie das Formular mit einem Test-Epic-Namen
3. Überprüfen Sie, ob das Epic in Jira erstellt wurde
4. Validieren Sie, dass der Link korrekt funktioniert

## Fehlerbehebung

### Häufige Probleme und Lösungen:

**Problem**: "Application Link nicht gefunden"
- **Lösung**: Überprüfen Sie die Application Link Konfiguration zwischen Confluence und Jira

**Problem**: "Berechtigung verweigert"
- **Lösung**: Stellen Sie sicher, dass der Benutzer Berechtigung hat, Epics im Projekt JIRAPRO24 zu erstellen

**Problem**: "JSON-Formatierungsfehler"
- **Lösung**: Verwenden Sie das "No Format" Makro um den JSON-Code

**Problem**: "Epic wird nicht erstellt"
- **Lösung**: Überprüfen Sie, ob "Epic" als Issue-Type in Ihrem Jira-Projekt verfügbar ist

**Problem**: "customfield_10103 nicht gefunden"
- **Lösung**: Überprüfen Sie die Custom Field ID in Ihrer Jira-Instanz oder entfernen Sie diese Zeile aus dem JSON

## Anpassungen

### Jira-URL anpassen:
Ersetzen Sie in Schritt 6 die URL durch Ihre tatsächliche Jira-Instanz-URL.

### Custom Field anpassen:
Falls customfield_10103 in Ihrer Jira-Instanz nicht existiert, können Sie:
1. Die Zeile aus dem JSON entfernen
2. Die korrekte Custom Field ID ermitteln und verwenden
3. Ein anderes verfügbares Custom Field verwenden

### Styling anpassen:
Das HTML in der ListView kann nach Ihren Corporate Design-Vorgaben angepasst werden.

## Wartung

- Überprüfen Sie regelmäßig die Application Link-Verbindung
- Testen Sie das Formular nach Jira-Updates
- Überwachen Sie die Confiforms-Logs bei Problemen
- Aktualisieren Sie die Jira-URL bei Systemänderungen

Diese Implementierung bietet eine solide Grundlage für die automatisierte Epic-Erstellung und kann je nach Bedarf erweitert werden.

