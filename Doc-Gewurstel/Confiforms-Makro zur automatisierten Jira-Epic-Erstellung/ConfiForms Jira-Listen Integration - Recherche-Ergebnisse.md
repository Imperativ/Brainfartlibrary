# ConfiForms Jira-Listen Integration - Recherche-Ergebnisse

## Übersicht

Die Recherche zeigt, dass ConfiForms definitiv auf Jira-Listen wie Components und Fix Versions zugreifen kann. Dies wird über **Webservice-basierte Field Definitions** realisiert, die Jira REST API-Endpunkte aufrufen.

## Gefundene Lösungsansätze

### 1. Components Integration

**Quelle**: https://wiki.vertuna.com/spaces/TEST/pages/39878766/Building+a+dropdown+field+in+ConfiForms+backed+by+webservice+call+to+Jira+Rest+API+-+components+field

**Funktionsweise**:
- **Field Type**: Webservice Multi-select
- **Service URL**: `/rest/api/2/project/TEST/components`
- **Field to use as "ID"**: `id`
- **Field to use as "Label"**: `name`
- **Transformation**: `asArrayOfKVPairs` Virtual function

**JSON Response Struktur**:
```json
[
  {
    "self": "https://vertuna.atlassian.net/rest/api/2/component/10001",
    "id": "10001",
    "name": "comp1",
    "description": "my test component 1",
    "assigneeType": "PROJECT_DEFAULT",
    "realAssigneeType": "PROJECT_DEFAULT",
    "isAssigneeTypeValid": false,
    "project": "TEST",
    "projectId": 10200
  },
  {
    "self": "https://vertuna.atlassian.net/rest/api/2/component/10002",
    "id": "10002",
    "name": "test 2",
    "description": "My test component 2",
    "assigneeType": "PROJECT_DEFAULT",
    "realAssigneeType": "PROJECT_DEFAULT",
    "isAssigneeTypeValid": false,
    "project": "TEST",
    "projectId": 10200
  }
]
```

**Transformation Function**:
```
entry.components.transform(name).asArrayOfKVPairs(name)
```

### 2. Weitere Jira-Listen

**Quelle**: https://wiki.vertuna.com/spaces/TEST/pages/23265805/Building+a+dropdown+field+in+ConfiForms+backed+by+webservice+call+to+Jira+Rest+API+-+createmeta

Diese Seite zeigt, wie man andere Jira-Listen wie Priorities über die createmeta API abruft.

## Technische Anforderungen

### Webservice Connection
- **Connection Type**: Application Link zu Jira
- **Authentication**: Über bestehende Confluence-Jira Integration
- **Connection Name**: Konfigurierbar (z.B. "vertuna-test")

### Field Definition Konfiguration
- **Field Type**: Webservice Multi-select oder Webservice Single-select
- **Service URL**: Jira REST API Endpunkt
- **Root to use**: Leer (für direkte Array-Responses)
- **Field to use as "ID"**: JSON-Feld für Wert
- **Field to use as "Label"**: JSON-Feld für Anzeige

## Verfügbare Jira REST API Endpunkte

### Components
- **URL**: `/rest/api/2/project/{projectKey}/components`
- **Response**: Array von Component-Objekten
- **ID Field**: `id`
- **Label Field**: `name`

### Fix Versions (Lösungsversionen)
- **URL**: `/rest/api/2/project/{projectKey}/versions`
- **Response**: Array von Version-Objekten
- **ID Field**: `id`
- **Label Field**: `name`

### Priorities
- **URL**: `/rest/api/2/priority`
- **Response**: Array von Priority-Objekten
- **ID Field**: `id`
- **Label Field**: `name`

### Issue Types
- **URL**: `/rest/api/2/project/{projectKey}/issuetypes`
- **Response**: Array von IssueType-Objekten
- **ID Field**: `id`
- **Label Field**: `name`

## Implementierungsschritte

1. **Webservice Connection konfigurieren**
   - Application Link zu Jira verwenden
   - Connection testen

2. **Field Definition erstellen**
   - Field Type: Webservice Multi-select
   - Service URL konfigurieren
   - ID und Label Fields mappen

3. **In Epic Creator integrieren**
   - Neue Felder zur Form Definition hinzufügen
   - IFTTT-Regeln erweitern für zusätzliche Felder

## Vorteile

- **Dynamische Listen**: Automatische Synchronisation mit Jira
- **Konsistenz**: Gleiche Werte wie in Jira verfügbar
- **Wartungsarm**: Keine manuelle Pflege der Listen erforderlich
- **Skalierbar**: Funktioniert für alle Jira-Projekte

## Einschränkungen

- **Netzwerkabhängig**: Erfordert aktive Verbindung zu Jira
- **Performance**: API-Aufrufe können Ladezeiten erhöhen
- **Berechtigungen**: Benutzer müssen Zugriff auf Jira-Projekt haben
- **Caching**: Möglicherweise verzögerte Updates bei Änderungen in Jira


## Alternative Lösung: Jira Select Field (seit ConfiForms 3.13)

**Quelle**: https://wiki.vertuna.com/spaces/CONFIFORMS/pages/193724685/How+to+configure+and+use+the+Jira+Select+Field+in+ConfiForms

### Übersicht
ConfiForms bietet seit Version 3.13 ein spezielles **Jira Select Field**, das eine vereinfachte Integration mit Jira-Feldern ermöglicht. Dies ist eine elegantere Alternative zu den Webservice-basierten Ansätzen.

### Konfiguration
- **Field Type**: Jira Select Field
- **Webservice Connection**: Bestehende Application Link Connection (z.B. "vertuna-live")
- **Project Key**: Jira-Projekt-Schlüssel (z.B. "JIRAPRO24")
- **Issue Type**: Issue Type, in dem das gewünschte Feld aktiviert ist
- **Field Name**: Name des Jira-Feldes (z.B. "components", "fixVersions")

### Vorteile gegenüber Webservice-Ansatz
- **Einfachere Konfiguration**: Keine komplexe JSON-Navigation erforderlich
- **Automatische Feldtyp-Erkennung**: ConfiForms erkennt automatisch Single-Select vs. Multi-Select
- **Bessere Performance**: Optimierte Integration ohne manuelle API-Aufrufe
- **Wartungsarm**: Weniger fehleranfällig als Webservice-Konfigurationen

### Unterstützte Jira-Felder
- **Components**: Projekt-Komponenten
- **Fix Versions**: Lösungsversionen
- **Affects Versions**: Betroffene Versionen
- **Priority**: Prioritäten
- **Labels**: Labels
- **Custom Fields**: Benutzerdefinierte Felder (je nach Typ)

## Empfohlene Implementierungsstrategie

### Für JIRAPRO24 Epic Creator

1. **Components Dropdown**:
   - Field Type: Jira Select Field
   - Project Key: JIRAPRO24
   - Issue Type: Epic
   - Field Name: components

2. **Fix Versions Dropdown**:
   - Field Type: Jira Select Field
   - Project Key: JIRAPRO24
   - Issue Type: Epic
   - Field Name: fixVersions

### Fallback-Optionen

Falls das Jira Select Field nicht verfügbar ist oder nicht funktioniert:

1. **Webservice Multi-select** mit direkten API-Endpunkten:
   - Components: `/rest/api/2/project/JIRAPRO24/components`
   - Fix Versions: `/rest/api/2/project/JIRAPRO24/versions`

2. **Webservice Single-select** mit createmeta API:
   - URL: `/rest/api/2/issue/createmeta/{projectKey}/issuetypes/{issueTypeId}`
   - Root to use: `fields.(fieldId=components).allowedValues` oder `fields.(fieldId=fixVersions).allowedValues`

## Technische Anforderungen

### Voraussetzungen
- **ConfiForms Version**: 3.13+ (für Jira Select Field)
- **Application Link**: Konfigurierte Verbindung zwischen Confluence und Jira
- **Berechtigungen**: Benutzer müssen Zugriff auf das Jira-Projekt haben
- **Feldkonfiguration**: Components und Fix Versions müssen im Epic Issue Type aktiviert sein

### Berechtigungsüberlegungen
- **Webservice-Zugriff**: Manche Organisationen beschränken Webservice-Aufrufe
- **Jira Select Field**: Nutzt bestehende Application Link-Berechtigungen
- **Fallback-Strategie**: Bei Berechtigungsproblemen auf statische Listen ausweichen

## Implementierungsempfehlung

**Priorität 1**: Jira Select Field (einfachste Lösung)
**Priorität 2**: Webservice mit direkten API-Endpunkten
**Priorität 3**: Webservice mit createmeta API
**Priorität 4**: Statische Listen als Fallback

