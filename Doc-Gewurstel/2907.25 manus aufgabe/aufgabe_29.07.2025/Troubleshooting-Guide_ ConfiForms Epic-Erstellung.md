# Troubleshooting-Guide: ConfiForms Epic-Erstellung

**Version:** 1.0  
**Datum:** 29. Juli 2025  
**Zielgruppe:** Administratoren und technische Betreuer

## Häufige Probleme und Diagnose

### 1. Application Link-Probleme

**Symptome:**
- "Unauthorized" oder "403 Forbidden" Fehler
- IFTTT-Regel schlägt fehl
- Keine Verbindung zu Jira möglich

**Diagnose:**
```bash
# Prüfung der Application Link-Konfiguration
1. Confluence Admin → General Configuration → Application Links
2. Jira-Verbindung überprüfen
3. Test-Verbindung durchführen
```

**Lösungsansätze:**
- Application Link neu konfigurieren
- Zertifikate überprüfen und aktualisieren
- Benutzerberechtigungen in beiden Systemen prüfen
- Netzwerkverbindung zwischen Servern testen

### 2. JSON-Mapping-Fehler

**Symptome:**
- "Invalid JSON" Fehlermeldungen
- Felder werden nicht korrekt übertragen
- Epic wird mit falschen Werten erstellt

**Diagnose:**
```json
// Test-JSON für Validierung:
{
    "fields": {
        "project": {"key": "BWPTLS24"},
        "issuetype": {"name": "Epic"},
        "summary": "Test Epic"
    }
}
```

**Lösungsansätze:**
- JSON-Syntax mit Online-Validator prüfen
- Velocity-Template-Syntax überprüfen
- Feldnamen gegen Jira-Schema validieren
- Schrittweise Komplexität erhöhen

### 3. Custom Field-Probleme

**Symptome:**
- "Field does not exist" Fehler
- Custom Fields werden nicht befüllt
- Ungültige Werte in Dropdown-Feldern

**Diagnose:**
```bash
# Jira REST API Test:
curl -u username:password \
  "https://jira.franz.extraklaus.de/rest/api/2/issue/createmeta?projectKeys=BWPTLS24&issuetypeNames=Epic&expand=projects.issuetypes.fields"
```

**Lösungsansätze:**
- Custom Field-IDs in Jira überprüfen
- Feldkonfiguration für Epic-Issue-Type prüfen
- Berechtigungen für Custom Fields validieren
- Feldtypen und erlaubte Werte abgleichen

### 4. Performance-Probleme

**Symptome:**
- Langsame Formular-Reaktionszeiten
- Timeouts bei Epic-Erstellung
- Hohe Server-Last

**Diagnose:**
```sql
-- ConfiForms-Logs prüfen (falls verfügbar):
SELECT * FROM confluence_logs 
WHERE message LIKE '%ConfiForms%' 
ORDER BY created_date DESC LIMIT 100;
```

**Lösungsansätze:**
- IFTTT-Regel-Anzahl reduzieren
- Caching für dynamische Inhalte implementieren
- Batch-Processing für API-Aufrufe
- Database-Performance optimieren

## Monitoring und Logging

### ConfiForms-Logs aktivieren

1. **Confluence Administration** → **Logging and Profiling**
2. **Configure Logging Level for Another Class**
3. **Package Name:** `com.vertuna.confluence.plugins.confiforms`
4. **Logging Level:** `DEBUG` (temporär für Diagnose)

### Wichtige Log-Einträge

```log
# Erfolgreiche Epic-Erstellung:
INFO [ConfiForms] IFTTT action completed successfully: jira_epic_result=BWPTLS24-123

# API-Fehler:
ERROR [ConfiForms] Jira API error: 400 Bad Request - Invalid field value

# Authentifizierungsfehler:
WARN [ConfiForms] Application Link authentication failed
```

### Metriken überwachen

- Anzahl erfolgreicher Epic-Erstellungen pro Tag
- Fehlerrate der IFTTT-Regeln
- Durchschnittliche Antwortzeit der Jira-API
- Benutzeraktivität auf der Confluence-Seite

## Wartungsaufgaben

### Wöchentlich
- [ ] Application Link-Status prüfen
- [ ] Fehlerprotokolle überprüfen
- [ ] Performance-Metriken analysieren

### Monatlich
- [ ] Custom Field-Konfiguration validieren
- [ ] Backup der ConfiForms-Konfiguration
- [ ] Benutzer-Feedback auswerten

### Bei System-Updates
- [ ] ConfiForms-Kompatibilität prüfen
- [ ] JSON-Mapping nach Jira-Updates validieren
- [ ] Funktionstest durchführen

## Backup und Recovery

### ConfiForms-Konfiguration exportieren

1. **Confluence-Seite** → **Bearbeiten**
2. **ConfiForms Form Definition** → **Makro-Einstellungen**
3. **Export/Import** → **Export Configuration**
4. JSON-Datei sicher speichern

### Wiederherstellung

1. **Neue Confluence-Seite** erstellen
2. **ConfiForms Form Definition** einfügen
3. **Import Configuration** verwenden
4. **Gespeicherte JSON-Datei** importieren
5. **Jira-Verbindung** neu konfigurieren

## Notfall-Prozeduren

### Kompletter Ausfall des ConfiForms-Makros

**Sofortmaßnahmen:**
1. Benutzer über alternativen Epic-Erstellungsprozess informieren
2. Direkte Jira-Nutzung als Fallback kommunizieren
3. Problem-Ticket im IT-Service-Management erstellen

**Wiederherstellung:**
1. Systemstatus aller beteiligten Komponenten prüfen
2. Application Link-Verbindung wiederherstellen
3. ConfiForms-Konfiguration aus Backup wiederherstellen
4. Funktionstest durchführen
5. Benutzer über Wiederherstellung informieren

### Dateninkonsistenzen

**Erkennung:**
- Epics in Jira ohne entsprechende ConfiForms-Einträge
- Fehlerhafte Feldwerte in erstellten Epics
- Fehlende Links in der Übersichtstabelle

**Korrektur:**
1. Betroffene Epics identifizieren
2. Manuelle Korrektur in Jira durchführen
3. ConfiForms-Einträge synchronisieren
4. Ursache der Inkonsistenz beheben

## Kontakte und Eskalation

### Level 1 Support (Benutzerprobleme)
- **Confluence-Administratoren**
- **Jira-Key-User**
- **IT-Helpdesk**

### Level 2 Support (Technische Probleme)
- **Atlassian-Administratoren**
- **System-Administratoren**
- **Netzwerk-Team**

### Level 3 Support (Kritische Probleme)
- **Vertuna ConfiForms Support**
- **Atlassian Support**
- **Externe Berater**

### Eskalationsmatrix

| Problem-Kategorie | Reaktionszeit | Verantwortlich |
|-------------------|---------------|----------------|
| Benutzer-Fragen | 4 Stunden | Level 1 |
| Funktions-Ausfall | 2 Stunden | Level 2 |
| System-Ausfall | 1 Stunde | Level 3 |
| Sicherheits-Problem | Sofort | Level 3 |

## Versionskontrolle

### Änderungsprotokoll führen

```markdown
## Änderungsprotokoll

### Version 1.1 - [Datum]
- **Geändert:** JSON-Mapping für neue Custom Fields
- **Grund:** Jira-Projekt-Anforderungen erweitert
- **Getestet von:** [Name]
- **Genehmigt von:** [Name]

### Version 1.0 - 29.07.2025
- **Erstellt:** Initiale Version des ConfiForms-Makros
- **Implementiert von:** Manus AI
- **Status:** Produktiv
```

### Rollback-Verfahren

1. **Aktuelle Konfiguration** exportieren
2. **Vorherige Version** aus Backup laden
3. **Funktionstest** durchführen
4. **Benutzer** über Änderungen informieren
5. **Dokumentation** aktualisieren

