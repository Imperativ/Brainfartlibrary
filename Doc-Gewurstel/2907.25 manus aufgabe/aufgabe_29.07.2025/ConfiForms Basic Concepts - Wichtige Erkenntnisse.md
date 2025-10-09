# ConfiForms Basic Concepts - Wichtige Erkenntnisse

## Grundlegende Makro-Struktur

### Kern-Makros für Formulare:
1. **ConfiForms Form Definition** - Definiert das Formular und sein Verhalten
2. **ConfiForms Field Definition** - Definiert Formularfelder (innerhalb der Form Definition)
3. **ConfiForms Registration Control** - Konfiguriert Anzeige und ermöglicht Formular-Submission

### Wichtige Erkenntnisse:
- Nur 2 Makros nötig für einfaches Formular: Form Definition + Field Definition
- Registration Control kann als Dialog oder eingebettet angezeigt werden
- Mehrere Registration Controls pro Formular möglich
- Daten können auf verschiedenen Seiten mit View-Makros angezeigt werden

## Für Jira-Integration relevante Makros:
- **ConfiForms IFTTT Integration Rules** - Definiert Integrationsregeln
  - Kann E-Mail-Benachrichtigungen senden
  - Kann HTTP-Requests an andere Systeme senden
  - Kann neue Seiten mit Templates erstellen
  - **Wichtig für Jira-API-Aufrufe**

## View-Makros für Datenausgabe:
- **ConfiForms TableView** - Tabellarische Darstellung (für die 5 letzten Tickets)
- **ConfiForms ListView** - WYSIWYG-Ansicht
- **ConfiForms Field** - Definiert Felder für Anzeige in Views

## Technische Details:
- Version: ConfiForms 3.17.7 für Server/Data Center
- Confluence 9.2.4 kompatibel
- Makros werden über Ctrl+Shift+A eingefügt
- Field Definitions müssen innerhalb der Form Definition stehen



## Jira-Integration mit ConfiForms IFTTT

### Create Jira Issue Aktion:
- **Verfügbar in**: SERVER/DC Version
- **Funktion**: Erstellt Jira Issues basierend auf JSON-Mapping
- **Rückgabe**: Issue Key als Text (z.B. ${iftttResult_MYRESULT})
- **Authentifizierung**: Über Jira-Server-Konfiguration

### Wichtige technische Details:
- **Velocity Templates**: Makro-Body wird als Velocity Template evaluiert
- **Feldwerte**: Zugriff über ${somefield} oder [entry.field_name]
- **Kontext-Objekte**: 
  - context.put("entry", entry) - ConfiForms Entry
  - context.put("user", user) - Confluence User Object
  - context.put("page", contentObject) - Abstract Page

### Verfügbare Hilfsobjekte (seit Version 2.27.3):
- context.put("null", new NullTool())
- context.put("esc", new EscapeTool())
- context.put("list", new ListTool())

### Feldvalidierung in Velocity:
```velocity
#if(${somefield})
#end

--- check if field has no values
#if(${somefield.isEmpty()})
#end

--- check if field is NOT empty and has values
#if(!${somefield.isEmpty()})
#end
```

### Multi-Value Felder:
```velocity
--- check if field has label (stored in values)
#if(${somefield.hasLabel("some_label")})
#end

--- check if field has id (stored in values)  
#if(${somefield.hasId("some_id")})
#end
```


## Praktisches JSON-Beispiel für Jira-Issue-Erstellung

### Basis JSON-Struktur:
```json
{
    "fields": {
        "project": {
            "key": "TEST"
        },
        "summary": "REST ye merry gentlemen.",
        "description": "Creating of an issue using project keys and issue type names using the REST API",
        "issuetype": {
            "name": "Bug"
        }
    }
}
```

### Mit ConfiForms-Feldmapping:
```json
{
    "fields": {
        "project": {
            "key": "BWPTLS24"
        },
        "summary": "[entry.summary]",
        "description": "[entry.details.escapeJSON]",
        "issuetype": {
            "name": "Epic"
        }
    }
}
```

### Wichtige Erkenntnisse:
- **Feldmapping**: [entry.fieldname] für ConfiForms-Felder
- **JSON-Escaping**: [entry.fieldname.escapeJSON] für Textfelder mit Zeilenumbrüchen
- **NoFormat-Makro**: Kann verwendet werden, um Formatierungsprobleme zu vermeiden
- **IFTTT-Ergebnis**: ${iftttResult_0} oder [iftttResult_0] für Issue-Key
- **Fehlerbehandlung**: "Do not report error" Option verfügbar

### Für File-Attachments:
- File-Type-Feld kann direkt in IFTTT-Body eingefügt werden
- Automatischer Upload zu Jira möglich

### Rückgabe des Issue-Keys:
- Ergebnis verfügbar als ${iftttResult_0} oder [iftttResult_0]
- Kann für weitere IFTTT-Aktionen verwendet werden
- Kann zurück in ConfiForms-Feld gespeichert werden

