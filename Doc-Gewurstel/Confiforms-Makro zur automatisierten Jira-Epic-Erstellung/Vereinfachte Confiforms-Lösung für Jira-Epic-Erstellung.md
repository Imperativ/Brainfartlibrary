# Vereinfachte Confiforms-Lösung für Jira-Epic-Erstellung

## Minimale Konfiguration

Falls die vollständige Lösung zu komplex erscheint oder technische Probleme auftreten, hier eine vereinfachte Version, die die Grundanforderungen erfüllt:

## Schritt 1: Basis-Formular

### ConfiForms Form Definition:
```
ConfiForms Form name: simpleEpicCreator
Registration form title: Epic erstellen
Save button label: Erstellen
```

### Field Definition:
```
Field Name: epicName
Field Type: text
Field Label: Epic Name
Required: true
```

### Registration Control:
```
Form name: simpleEpicCreator
Button label: Neues Epic erstellen
```

## Schritt 2: Einfache IFTTT-Integration

### IFTTT für Jira-Erstellung:
```
Event: onCreated
Action to perform: Create Jira Issue
```

**Makro-Body (minimaler JSON):**
```json
{
    "fields": {
        "project": {
            "key": "JIRAPRO24"
        },
        "summary": "[entry.epicName]",
        "issuetype": {
            "name": "Epic"
        }
    }
}
```

## Schritt 3: Einfache Ergebnisanzeige

### ListView:
```
Form name: simpleEpicCreator
```

**ListView-Body:**
```html
<p>Epic erstellt: [entry.epicName]</p>
<p>Erstellt am: [entry._created]</p>
```

## Vorteile der vereinfachten Lösung:

1. **Weniger Fehlerquellen**: Reduzierte Komplexität minimiert potenzielle Probleme
2. **Einfachere Wartung**: Weniger Komponenten bedeuten einfachere Pflege
3. **Schnellere Implementierung**: Kann in wenigen Minuten eingerichtet werden
4. **Grundfunktionalität**: Erfüllt die Kernforderung der Epic-Erstellung

## Erweiterungsmöglichkeiten:

Die vereinfachte Lösung kann schrittweise erweitert werden:
1. Hinzufügung der Ergebnis-Rückmeldung
2. Implementation der Link-Generierung
3. Verbesserung der Benutzeroberfläche
4. Hinzufügung der Fehlerbehandlung

## Entscheidungshilfe:

**Verwenden Sie die vollständige Lösung, wenn:**
- Sie Erfahrung mit Confiforms haben
- Vollständige Funktionalität gewünscht ist
- Zeit für Testing und Debugging verfügbar ist

**Verwenden Sie die vereinfachte Lösung, wenn:**
- Schnelle Implementierung erforderlich ist
- Minimale Funktionalität ausreicht
- Wenig Erfahrung mit Confiforms vorhanden ist
- Als Prototyp für spätere Erweiterung

## Nächste Schritte:

1. Entscheiden Sie sich für eine der beiden Lösungen
2. Implementieren Sie die gewählte Variante
3. Testen Sie die Funktionalität
4. Bei Bedarf schrittweise Erweiterung zur vollständigen Lösung

