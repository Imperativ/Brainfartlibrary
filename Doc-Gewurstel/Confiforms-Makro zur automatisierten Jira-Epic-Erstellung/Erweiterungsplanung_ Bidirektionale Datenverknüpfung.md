# Erweiterungsplanung: Bidirektionale Datenverknüpfung

## Analyse der bestehenden Lösung

### Aktuelle Architektur
Unsere ursprüngliche Epic-Creator-Lösung basiert auf einer einfachen, linearen Architektur:

1. **Formular-Definition**: Ein Eingabefeld für `epicName`
2. **IFTTT-Integration**: Eine Regel für Epic-Erstellung in Jira
3. **Ergebnisanzeige**: ListView mit statischen Informationen

### Identifizierte Limitierungen
- **Keine Rückspeicherung**: Der generierte Jira-Key wird nicht in ConfiForms gespeichert
- **Begrenzte Nachverfolgung**: Keine Möglichkeit für erweiterte Queries oder Reports
- **Statische Links**: URLs müssen manuell konstruiert werden

## Erweiterungskonzept

### Ziel der bidirektionalen Datenverknüpfung
Die Erweiterung soll folgende Funktionalitäten hinzufügen:

1. **Automatische Jira-Key-Speicherung**: Der von Jira generierte Epic-Key wird zurück in das ConfiForms-Entry gespeichert
2. **Dynamische Link-Generierung**: Jira-URLs werden automatisch basierend auf dem gespeicherten Key erstellt
3. **Erweiterte Tracking-Möglichkeiten**: Basis für zukünftige Reporting- und Analytics-Funktionen
4. **Verbesserte Datenintegrität**: Zentrale Speicherung aller Epic-Metadaten in ConfiForms

### Technischer Ansatz
Basierend auf der Analyse der alternativen Lösung wird folgender Ansatz implementiert:

1. **Zusätzliches Feld**: `jiraKey` für die Speicherung des Epic-Keys
2. **Field Definition Rules**: Dynamisches Ein-/Ausblenden des jiraKey-Feldes
3. **Zweite IFTTT-Regel**: Rückspeicherung des Jira-Keys nach erfolgreicher Epic-Erstellung
4. **Erweiterte ListView**: Anzeige der gespeicherten Jira-Keys mit direkten Links

## Implementierungsplan

### Phase 1: Datenmodell-Erweiterung
- Hinzufügung des `jiraKey`-Feldes zur ConfiForms-Definition
- Konfiguration von Field Definition Rules für dynamische Anzeige
- Anpassung der bestehenden Field-Struktur

### Phase 2: IFTTT-Erweiterung
- Implementierung einer zweiten IFTTT-Regel für die Rückspeicherung
- Konfiguration der Datenverknüpfung zwischen den IFTTT-Aktionen
- Testing der verketteten IFTTT-Ausführung

### Phase 3: UI-Anpassungen
- Erweiterung der ListView um jiraKey-Anzeige
- Implementierung dynamischer Link-Generierung
- Verbesserung der Benutzeroberfläche

### Phase 4: Testing und Validierung
- Umfassende Tests der bidirektionalen Funktionalität
- Validierung der Datenintegrität
- Performance-Tests mit der erweiterten Architektur

## Risikobewertung

### Technische Risiken
- **Timing-Probleme**: Die zweite IFTTT-Regel muss nach der ersten ausgeführt werden
- **Dateninkonsistenzen**: Mögliche Probleme bei fehlgeschlagenen Rückspeicherungen
- **Performance-Impact**: Zusätzliche API-Aufrufe können die Antwortzeit erhöhen

### Mitigation-Strategien
- **Sequenzielle IFTTT-Ausführung**: Verwendung von Result-Namen für Abhängigkeiten
- **Fehlerbehandlung**: Robuste Error-Handling-Mechanismen
- **Monitoring**: Überwachung der IFTTT-Ausführungszeiten

## Erwartete Vorteile

### Kurzfristige Vorteile
- **Verbesserte Nachverfolgung**: Direkte Verknüpfung zwischen ConfiForms-Entries und Jira-Issues
- **Bessere Benutzererfahrung**: Automatische Link-Generierung ohne manuelle URL-Konstruktion
- **Datenintegrität**: Zentrale Speicherung aller Epic-Metadaten

### Langfristige Vorteile
- **Erweiterte Reporting-Möglichkeiten**: Basis für Analytics und Dashboards
- **Cross-System-Queries**: Möglichkeit für komplexe Abfragen über ConfiForms
- **Workflow-Erweiterungen**: Grundlage für zukünftige Automatisierungen

## Kompatibilität

### Rückwärtskompatibilität
Die Erweiterung ist vollständig rückwärtskompatibel:
- Bestehende Funktionalitäten bleiben unverändert
- Neue Felder sind optional und beeinträchtigen nicht die Grundfunktion
- Bestehende ConfiForms-Entries werden nicht beeinflusst

### Upgrade-Pfad
- **Nahtlose Erweiterung**: Neue Komponenten werden zur bestehenden Konfiguration hinzugefügt
- **Schrittweise Aktivierung**: Funktionalitäten können einzeln getestet und aktiviert werden
- **Rollback-Möglichkeit**: Einfache Rückkehr zur ursprünglichen Konfiguration bei Problemen

