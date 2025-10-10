# Erweiterte ConfiForms-Konfiguration mit bidirektionaler Datenverknüpfung

## Übersicht der Erweiterung

Die ursprüngliche Epic-Creator-Lösung wird um ein zusätzliches `jiraKey`-Feld und entsprechende Field Definition Rules erweitert, um die bidirektionale Datenverknüpfung zu ermöglichen. Diese Erweiterung speichert den von Jira generierten Epic-Key automatisch zurück in das ConfiForms-Entry und ermöglicht erweiterte Tracking- und Reporting-Funktionalitäten.

## Erweiterte Makro-Konfiguration

### Schritt 1: Erweiterte Confiforms Form Definition

Die Basis-Konfiguration bleibt unverändert, wird jedoch um zusätzliche Metadaten erweitert:

```
Makro: ConfiForms Form
Parameter:
- ConfiForms Form name: epicCreator
- Registration form title: Neues Jira Epic erstellen
- Save button label: Epic erstellen
- Close button label: Schließen
- Lock form: false
- Secure storage: false
- Enable versioning: true
- Enable audit trail: true
```

Die Aktivierung von Versioning und Audit Trail ermöglicht die Nachverfolgung von Änderungen an den ConfiForms-Entries, was bei der bidirektionalen Datenverknüpfung besonders wertvoll ist.

### Schritt 2: Bestehende Field Definition für Epic-Name

Das ursprüngliche epicName-Feld bleibt unverändert:

```
Makro: ConfiForms Field Definition
Parameter:
- Field Name: epicName
- Field Type: text
- Field Label: Epic Name
- Required: true
- Max Length: 255
- Help text: Geben Sie einen aussagekräftigen Namen für das neue Epic ein
```

### Schritt 3: Neue Field Definition für Jira-Key

Ein neues Feld für die Speicherung des Jira-Keys wird hinzugefügt:

```
Makro: ConfiForms Field Definition
Parameter:
- Field Name: jiraKey
- Field Type: text
- Field Label: Jira Epic Key
- Required: false
- Max Length: 50
- Read only: true
- Help text: Wird automatisch nach der Epic-Erstellung befüllt
```

Das jiraKey-Feld ist als "Read only" konfiguriert, da es ausschließlich durch IFTTT-Aktionen befüllt wird und nicht durch Benutzereingaben geändert werden soll.

### Schritt 4: Field Definition Rules für dynamische Anzeige

Field Definition Rules steuern die dynamische Anzeige des jiraKey-Feldes:

```
Makro: ConfiForms Field Definition Rules
Parameter:
- Condition: id:[empty]
- Field Name: jiraKey
- Action: Hide field
```

Diese Regel versteckt das jiraKey-Feld initial, wenn noch kein Entry erstellt wurde (id ist leer). Nach der Epic-Erstellung und Rückspeicherung wird das Feld automatisch sichtbar.

### Schritt 5: Zusätzliche Field Definition für Status-Tracking

Ein Status-Feld ermöglicht die Verfolgung des Epic-Erstellungsprozesses:

```
Makro: ConfiForms Field Definition
Parameter:
- Field Name: epicStatus
- Field Type: dropdown
- Field Label: Status
- Required: false
- Values: Erstellt,In Bearbeitung,Abgeschlossen,Fehler
- Default value: Erstellt
- Read only: true
```

### Schritt 6: Field Definition für Jira-URL

Ein zusätzliches Feld für die vollständige Jira-URL:

```
Makro: ConfiForms Field Definition
Parameter:
- Field Name: jiraUrl
- Field Type: text
- Field Label: Jira Link
- Required: false
- Max Length: 500
- Read only: true
- Help text: Direkter Link zum Epic in Jira
```

### Schritt 7: Erweiterte Field Definition Rules für Status-Anzeige

Zusätzliche Rules für die Status-Anzeige:

```
Makro: ConfiForms Field Definition Rules
Parameter:
- Condition: epicStatus:Fehler
- Field Name: epicStatus
- Action: Set field color
- Value: red
```

```
Makro: ConfiForms Field Definition Rules
Parameter:
- Condition: epicStatus:Abgeschlossen
- Field Name: epicStatus
- Action: Set field color
- Value: green
```

Diese Rules färben das Status-Feld entsprechend dem aktuellen Status ein, um eine bessere visuelle Rückmeldung zu geben.

## Erweiterte Registration Control

### Schritt 8: Angepasste Registration Control

Die Registration Control wird um zusätzliche Parameter erweitert:

```
Makro: ConfiForms Registration Control
Parameter:
- Form name: epicCreator
- Show as: dialog
- Button label: Neues Epic erstellen
- Success message: Epic wird erstellt... Bitte warten Sie auf die Bestätigung.
- Show success message for: 3
- Redirect after submission: false
```

Die angepasste Success Message informiert den Benutzer über den asynchronen Prozess der Epic-Erstellung und Rückspeicherung.

## Datenmodell-Übersicht

### Erweiterte Feldstruktur

Die erweiterte ConfiForms-Definition umfasst folgende Felder:

| Feldname | Typ | Erforderlich | Beschreibung |
|----------|-----|--------------|--------------|
| epicName | text | Ja | Benutzereingabe für Epic-Name |
| jiraKey | text | Nein | Automatisch generierter Jira-Key |
| jiraUrl | text | Nein | Vollständige URL zum Jira-Epic |
| epicStatus | dropdown | Nein | Status des Epic-Erstellungsprozesses |
| createdDate | datetime | Nein | Zeitstempel der Entry-Erstellung |
| lastModified | datetime | Nein | Zeitstempel der letzten Änderung |

### Datenfluss-Diagramm

```
Benutzereingabe (epicName)
         ↓
ConfiForms Entry erstellt
         ↓
IFTTT 1: Jira Epic erstellen
         ↓
Jira API Response (Epic Key)
         ↓
IFTTT 2: ConfiForms Entry aktualisieren
         ↓
jiraKey, jiraUrl, epicStatus befüllt
         ↓
ListView aktualisiert
```

## Validierung und Constraints

### Field Validation Rules

Zusätzliche Validierungsregeln für die erweiterten Felder:

```
Makro: ConfiForms Field Validation Rules
Parameter:
- Field Name: epicName
- Validation type: regex
- Pattern: ^[A-Za-z0-9\s\-_]{3,255}$
- Error message: Epic-Name muss zwischen 3 und 255 Zeichen lang sein und darf nur Buchstaben, Zahlen, Leerzeichen, Bindestriche und Unterstriche enthalten
```

```
Makro: ConfiForms Field Validation Rules
Parameter:
- Field Name: jiraKey
- Validation type: regex
- Pattern: ^[A-Z]+-[0-9]+$
- Error message: Ungültiges Jira-Key-Format
```

### Conditional Field Display

Erweiterte Conditional Display Rules:

```
Makro: ConfiForms Field Definition Rules
Parameter:
- Condition: jiraKey:[empty]
- Field Name: jiraUrl
- Action: Hide field
```

```
Makro: ConfiForms Field Definition Rules
Parameter:
- Condition: epicStatus:Fehler
- Field Name: jiraKey
- Action: Hide field
```

## CSS-Styling für erweiterte Felder

### Erweiterte CSS-Klassen

```css
/* Styling für Jira-Key-Anzeige */
.confiform-field-jiraKey {
    background-color: #e8f5e8;
    border: 1px solid #4caf50;
    border-radius: 4px;
    padding: 8px;
    font-family: monospace;
    font-weight: bold;
}

/* Status-Feld Styling */
.confiform-field-epicStatus {
    padding: 4px 8px;
    border-radius: 12px;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
}

.confiform-field-epicStatus[data-value="Abgeschlossen"] {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.confiform-field-epicStatus[data-value="Fehler"] {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}

.confiform-field-epicStatus[data-value="In Bearbeitung"] {
    background-color: #fff3cd;
    color: #856404;
    border: 1px solid #ffeaa7;
}

/* Jira-URL Link-Styling */
.confiform-field-jiraUrl a {
    display: inline-flex;
    align-items: center;
    padding: 8px 12px;
    background-color: #0052cc;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    font-weight: 500;
    transition: background-color 0.2s ease;
}

.confiform-field-jiraUrl a:hover {
    background-color: #0065ff;
    text-decoration: none;
}

.confiform-field-jiraUrl a::before {
    content: "🔗 ";
    margin-right: 4px;
}
```

## JavaScript für erweiterte Funktionalitäten

### Auto-Refresh für bidirektionale Updates

```javascript
// Erweiterte Auto-Refresh-Funktionalität
(function() {
    'use strict';
    
    // Konfiguration
    const CONFIG = {
        refreshInterval: 2000, // 2 Sekunden
        maxRefreshAttempts: 10,
        formName: 'epicCreator'
    };
    
    let refreshAttempts = 0;
    let lastEntryCount = 0;
    
    // Überwacht neue ConfiForms-Entries
    function monitorNewEntries() {
        const entries = document.querySelectorAll(`[data-form-name="${CONFIG.formName}"] .confiform-entry`);
        const currentEntryCount = entries.length;
        
        if (currentEntryCount > lastEntryCount) {
            lastEntryCount = currentEntryCount;
            
            // Prüft auf unvollständige Entries (ohne jiraKey)
            const incompleteEntries = Array.from(entries).filter(entry => {
                const jiraKeyField = entry.querySelector('.confiform-field-jiraKey');
                return !jiraKeyField || !jiraKeyField.textContent.trim();
            });
            
            if (incompleteEntries.length > 0 && refreshAttempts < CONFIG.maxRefreshAttempts) {
                refreshAttempts++;
                setTimeout(() => {
                    location.reload();
                }, CONFIG.refreshInterval);
            } else {
                refreshAttempts = 0;
            }
        }
    }
    
    // Startet Monitoring
    function startMonitoring() {
        const observer = new MutationObserver(monitorNewEntries);
        const targetNode = document.querySelector('.confluenceTable') || document.body;
        
        observer.observe(targetNode, {
            childList: true,
            subtree: true
        });
        
        // Initial check
        monitorNewEntries();
    }
    
    // Startet nach DOM-Load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startMonitoring);
    } else {
        startMonitoring();
    }
})();
```

### Progress Indicator

```javascript
// Progress Indicator für Epic-Erstellung
function showEpicCreationProgress() {
    const progressHTML = `
        <div id="epic-creation-progress" style="
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 10000;
            text-align: center;
            min-width: 300px;
        ">
            <div style="margin-bottom: 15px;">
                <div style="
                    width: 40px;
                    height: 40px;
                    border: 4px solid #f3f3f3;
                    border-top: 4px solid #0052cc;
                    border-radius: 50%;
                    animation: spin 1s linear infinite;
                    margin: 0 auto;
                "></div>
            </div>
            <h3 style="margin: 0 0 10px 0; color: #333;">Epic wird erstellt...</h3>
            <p style="margin: 0; color: #666; font-size: 14px;">
                Bitte warten Sie, während das Epic in Jira erstellt und verknüpft wird.
            </p>
        </div>
        <style>
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    `;
    
    document.body.insertAdjacentHTML('beforeend', progressHTML);
    
    // Entfernt Progress Indicator nach 10 Sekunden
    setTimeout(() => {
        const progressElement = document.getElementById('epic-creation-progress');
        if (progressElement) {
            progressElement.remove();
        }
    }, 10000);
}

// Event Listener für Form-Submission
document.addEventListener('submit', function(e) {
    if (e.target.closest('.confiform-registration-form')) {
        showEpicCreationProgress();
    }
});
```

## Erweiterte Konfigurationsdatei

### Vollständige Makro-Sequenz

Die erweiterte Konfiguration umfasst folgende Makro-Sequenz:

1. **ConfiForms Form Definition** (mit erweiterten Parametern)
2. **ConfiForms Field Definition** für epicName
3. **ConfiForms Field Definition** für jiraKey
4. **ConfiForms Field Definition** für jiraUrl
5. **ConfiForms Field Definition** für epicStatus
6. **ConfiForms Field Definition Rules** (multiple für verschiedene Bedingungen)
7. **ConfiForms Field Validation Rules** (für Input-Validierung)
8. **ConfiForms Registration Control** (mit erweiterten Parametern)
9. **ConfiForms IFTTT** für Epic-Erstellung (bestehend)
10. **ConfiForms IFTTT** für Rückspeicherung (neu)
11. **ConfiForms ListView** (erweitert)

### Konfigurationsdokumentation

Jede Konfigurationsänderung sollte dokumentiert werden:

```
Änderungsprotokoll:
- Version 1.0: Ursprüngliche Epic-Creator-Funktionalität
- Version 2.0: Bidirektionale Datenverknüpfung hinzugefügt
  - Neues jiraKey-Feld
  - Erweiterte IFTTT-Integration
  - Dynamische Field Rules
  - Verbessertes Status-Tracking
```

Diese erweiterte Konfiguration bildet die Grundlage für die bidirektionale Datenverknüpfung und ermöglicht erweiterte Funktionalitäten wie automatische Jira-Key-Speicherung, verbessertes Status-Tracking und dynamische Benutzeroberflächen.

