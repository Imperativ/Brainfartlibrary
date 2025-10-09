# Test- und Validierungsplan für Confiforms Epic Creator

## Übersicht

Dieses Dokument beschreibt den umfassenden Test- und Validierungsplan für das Confiforms-Makro zur automatisierten Jira-Epic-Erstellung. Die Tests sind in verschiedene Kategorien unterteilt, um alle Aspekte der Funktionalität zu überprüfen.

## Test-Kategorien

### 1. Funktionale Tests

#### 1.1 Grundfunktionalität
- **Test 1.1.1**: Epic-Name Eingabe
  - **Ziel**: Validierung der Eingabefunktionalität
  - **Schritte**: 
    1. Öffne die Confluence-Seite mit dem Confiforms-Makro
    2. Klicke auf "Neues Epic erstellen"
    3. Gebe einen gültigen Epic-Namen ein
    4. Überprüfe, dass die Eingabe akzeptiert wird
  - **Erwartetes Ergebnis**: Eingabe wird korrekt angezeigt und validiert

- **Test 1.1.2**: Epic-Erstellung
  - **Ziel**: Validierung der Epic-Erstellung in Jira
  - **Schritte**:
    1. Gebe einen eindeutigen Epic-Namen ein
    2. Klicke auf "Epic erstellen"
    3. Warte auf die Verarbeitung
    4. Überprüfe das Ergebnis
  - **Erwartetes Ergebnis**: Epic wird in Jira-Projekt JIRAPRO24 erstellt

- **Test 1.1.3**: Link-Generierung
  - **Ziel**: Validierung der automatischen Link-Erstellung
  - **Schritte**:
    1. Nach erfolgreicher Epic-Erstellung
    2. Überprüfe die Anzeige des Jira-Links
    3. Klicke auf den generierten Link
  - **Erwartetes Ergebnis**: Link führt zum korrekten Epic in Jira

#### 1.2 Datenvalidierung
- **Test 1.2.1**: Pflichtfeld-Validierung
  - **Ziel**: Überprüfung der Pflichtfeld-Validierung
  - **Schritte**:
    1. Versuche Epic ohne Namen zu erstellen
    2. Überprüfe Fehlermeldung
  - **Erwartetes Ergebnis**: Fehlermeldung wird angezeigt

- **Test 1.2.2**: Maximale Länge
  - **Ziel**: Validierung der Längenbegrenzung
  - **Schritte**:
    1. Gebe einen Epic-Namen mit >255 Zeichen ein
    2. Versuche Epic zu erstellen
  - **Erwartetes Ergebnis**: Eingabe wird begrenzt oder Fehlermeldung angezeigt

- **Test 1.2.3**: Sonderzeichen
  - **Ziel**: Überprüfung der Sonderzeichen-Behandlung
  - **Schritte**:
    1. Gebe Epic-Namen mit Sonderzeichen ein (ä, ö, ü, ß, &, <, >)
    2. Erstelle Epic
  - **Erwartetes Ergebnis**: Sonderzeichen werden korrekt übertragen

### 2. Integration Tests

#### 2.1 Jira-Integration
- **Test 2.1.1**: Application Link
  - **Ziel**: Validierung der Confluence-Jira Verbindung
  - **Schritte**:
    1. Überprüfe Application Link Status
    2. Teste Authentifizierung
  - **Erwartetes Ergebnis**: Verbindung ist aktiv und funktional

- **Test 2.1.2**: Projekt-Zugriff
  - **Ziel**: Überprüfung der Berechtigung für JIRAPRO24
  - **Schritte**:
    1. Versuche Epic in JIRAPRO24 zu erstellen
    2. Überprüfe Berechtigungen
  - **Erwartetes Ergebnis**: Epic wird erfolgreich erstellt

- **Test 2.1.3**: Custom Field Mapping
  - **Ziel**: Validierung des customfield_10103 Mappings
  - **Schritte**:
    1. Erstelle Epic mit spezifischem Namen
    2. Überprüfe in Jira, ob customfield_10103 korrekt befüllt ist
  - **Erwartetes Ergebnis**: Custom Field enthält den Epic-Namen

#### 2.2 Confiforms-Integration
- **Test 2.2.1**: IFTTT-Ausführung
  - **Ziel**: Überprüfung der IFTTT-Regel-Ausführung
  - **Schritte**:
    1. Erstelle Epic
    2. Überprüfe IFTTT-Logs (falls verfügbar)
  - **Erwartetes Ergebnis**: IFTTT wird erfolgreich ausgeführt

- **Test 2.2.2**: Datenrückgabe
  - **Ziel**: Validierung der IFTTT-Ergebnis-Verarbeitung
  - **Schritte**:
    1. Erstelle Epic
    2. Überprüfe Rückgabe-Daten
  - **Erwartetes Ergebnis**: Jira-Key und URL werden korrekt zurückgegeben

### 3. Benutzeroberflächen Tests

#### 3.1 Usability
- **Test 3.1.1**: Benutzerfreundlichkeit
  - **Ziel**: Bewertung der Benutzerfreundlichkeit
  - **Schritte**:
    1. Lasse verschiedene Benutzer das Formular testen
    2. Sammle Feedback
  - **Erwartetes Ergebnis**: Intuitive Bedienung

- **Test 3.1.2**: Responsive Design
  - **Ziel**: Überprüfung auf verschiedenen Bildschirmgrößen
  - **Schritte**:
    1. Teste auf Desktop, Tablet, Mobile
    2. Überprüfe Layout und Funktionalität
  - **Erwartetes Ergebnis**: Funktioniert auf allen Geräten

#### 3.2 Visuelles Design
- **Test 3.2.1**: CSS-Styling
  - **Ziel**: Überprüfung des visuellen Designs
  - **Schritte**:
    1. Überprüfe Styling in verschiedenen Browsern
    2. Teste mit und ohne Custom CSS
  - **Erwartetes Ergebnis**: Konsistentes Design

### 4. Performance Tests

#### 4.1 Antwortzeiten
- **Test 4.1.1**: Epic-Erstellung Performance
  - **Ziel**: Messung der Antwortzeiten
  - **Schritte**:
    1. Messe Zeit von Klick bis Ergebnis-Anzeige
    2. Wiederhole Test mehrmals
  - **Erwartetes Ergebnis**: < 10 Sekunden

#### 4.2 Concurrent Users
- **Test 4.2.1**: Mehrere gleichzeitige Benutzer
  - **Ziel**: Test mit mehreren Benutzern gleichzeitig
  - **Schritte**:
    1. Lasse 5+ Benutzer gleichzeitig Epics erstellen
    2. Überprüfe Erfolgsrate
  - **Erwartetes Ergebnis**: Alle Epics werden erfolgreich erstellt

### 5. Fehlerbehandlung Tests

#### 5.1 Netzwerk-Fehler
- **Test 5.1.1**: Jira nicht erreichbar
  - **Ziel**: Verhalten bei Jira-Ausfall
  - **Schritte**:
    1. Simuliere Jira-Ausfall
    2. Versuche Epic zu erstellen
  - **Erwartetes Ergebnis**: Aussagekräftige Fehlermeldung

#### 5.2 Authentifizierung-Fehler
- **Test 5.2.1**: Ungültige Credentials
  - **Ziel**: Verhalten bei Authentifizierungsfehlern
  - **Schritte**:
    1. Konfiguriere ungültige Application Link
    2. Versuche Epic zu erstellen
  - **Erwartetes Ergebnis**: Fehlermeldung über Authentifizierungsproblem

### 6. Sicherheits Tests

#### 6.1 Input Validation
- **Test 6.1.1**: XSS-Schutz
  - **Ziel**: Überprüfung gegen Cross-Site Scripting
  - **Schritte**:
    1. Gebe JavaScript-Code als Epic-Namen ein
    2. Überprüfe, ob Code ausgeführt wird
  - **Erwartetes Ergebnis**: Code wird nicht ausgeführt

#### 6.2 Berechtigungen
- **Test 6.2.1**: Unbefugte Zugriffe
  - **Ziel**: Überprüfung der Zugriffskontrolle
  - **Schritte**:
    1. Teste mit Benutzer ohne Epic-Erstellungsrechte
    2. Versuche Epic zu erstellen
  - **Erwartetes Ergebnis**: Zugriff wird verweigert

## Test-Ausführung

### Vorbereitung
1. **Testumgebung einrichten**
   - Confluence 8.5 mit Confiforms Plugin
   - Jira 9.12 mit Projekt JIRAPRO24
   - Application Link konfiguriert
   - Test-Benutzer mit entsprechenden Berechtigungen

2. **Test-Daten vorbereiten**
   - Liste von Test-Epic-Namen
   - Verschiedene Eingabe-Szenarien
   - Erwartete Ergebnisse dokumentiert

### Durchführung
1. **Systematische Abarbeitung**
   - Tests in der angegebenen Reihenfolge durchführen
   - Ergebnisse dokumentieren
   - Screenshots bei Fehlern erstellen

2. **Regression Tests**
   - Nach jeder Änderung kritische Tests wiederholen
   - Automatisierung wo möglich

### Dokumentation
1. **Test-Protokoll**
   - Datum und Zeit der Durchführung
   - Tester-Name
   - Testergebnisse (Bestanden/Fehlgeschlagen)
   - Bemerkungen und Screenshots

2. **Fehler-Tracking**
   - Fehler-ID
   - Beschreibung
   - Reproduktionsschritte
   - Priorität
   - Status

## Akzeptanzkriterien

### Mindestanforderungen
- ✅ Epic wird erfolgreich in JIRAPRO24 erstellt
- ✅ Epic-Name wird korrekt übertragen
- ✅ Interaktiver Link zum Epic wird angezeigt
- ✅ Grundlegende Fehlerbehandlung funktioniert

### Erweiterte Anforderungen
- ✅ Automatische Seitenaktualisierung
- ✅ Custom Field wird korrekt befüllt
- ✅ Responsive Design
- ✅ Performance < 10 Sekunden

### Nice-to-Have
- ⚪ Erweiterte Fehlerbehandlung
- ⚪ Audit-Logging
- ⚪ Batch-Erstellung
- ⚪ Template-Unterstützung

## Risiken und Mitigation

### Identifizierte Risiken
1. **Application Link Probleme**
   - **Risiko**: Verbindung zwischen Confluence und Jira
   - **Mitigation**: Detaillierte Konfigurationsanleitung

2. **Berechtigungsprobleme**
   - **Risiko**: Benutzer können keine Epics erstellen
   - **Mitigation**: Berechtigungs-Validierung vor Deployment

3. **Performance-Probleme**
   - **Risiko**: Langsame Antwortzeiten
   - **Mitigation**: Performance-Monitoring und Optimierung

## Test-Tools

### Empfohlene Tools
1. **Browser-Entwicklertools**
   - Netzwerk-Monitoring
   - Console-Logs
   - Performance-Analyse

2. **Jira REST API Tester**
   - Verwendung des bereitgestellten Python-Skripts
   - Direkte API-Tests

3. **JSON-Validator**
   - Verwendung des bereitgestellten Validators
   - Syntax-Überprüfung

## Fazit

Dieser umfassende Testplan stellt sicher, dass das Confiforms Epic Creator Makro alle Anforderungen erfüllt und robust in der Produktionsumgebung funktioniert. Die systematische Durchführung aller Tests minimiert das Risiko von Problemen nach dem Deployment.

