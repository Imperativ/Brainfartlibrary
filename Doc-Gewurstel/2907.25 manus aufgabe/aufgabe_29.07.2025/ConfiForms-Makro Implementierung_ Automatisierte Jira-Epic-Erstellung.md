# ConfiForms-Makro Implementierung: Automatisierte Jira-Epic-Erstellung

**Autor:** Manus AI  
**Version:** 1.0  
**Datum:** 29. Juli 2025  
**Zielumgebung:** Confluence 9.2.4, Jira 10.3.6 Data Center, ConfiForms 3.17.7

## Einführung

Diese Implementierungsanleitung beschreibt die vollständige Erstellung eines ConfiForms-Makros zur automatisierten Jira-Epic-Erstellung im Projekt BWPTLS24. Das Makro ermöglicht es authentifizierten Benutzern, über ein benutzerfreundliches Formular Epic-Tickets zu erstellen, die automatisch mit allen erforderlichen Feldern befüllt und in Jira angelegt werden.

Die Lösung basiert auf den aktuellen Versionen der Atlassian-Produkte und nutzt ausschließlich Standardfunktionalitäten ohne Administratorrechte. Durch die Verwendung der Application Link-Authentifizierung wird eine nahtlose Integration zwischen Confluence und Jira gewährleistet, während gleichzeitig die Sicherheitsrichtlinien des Unternehmens eingehalten werden.

Das implementierte System bietet nicht nur die Möglichkeit zur Epic-Erstellung, sondern auch eine tabellarische Übersicht der fünf zuletzt erstellten Tickets, umfassende Fehlerbehandlung und eine intuitive Benutzeroberfläche, die sowohl auf Desktop- als auch auf mobilen Geräten optimal funktioniert.

## Systemarchitektur und technische Grundlagen

Die Architektur des ConfiForms-Makros basiert auf einer modularen Struktur, die verschiedene Komponenten miteinander verbindet, um eine robuste und erweiterbare Lösung zu schaffen. Im Zentrum steht das ConfiForms Form Definition-Makro, das als Container für alle anderen Komponenten fungiert und die grundlegenden Eigenschaften des Formulars definiert.

Die Datenerfassung erfolgt über spezialisierte ConfiForms Field Definition-Makros, die für jeden Eingabetyp optimiert sind. Diese Felddefinitiionen unterstützen verschiedene Eingabetypen wie einfache Textfelder, Dropdown-Menüs, Multi-Select-Felder und Benutzerauswahl-Komponenten. Jedes Feld verfügt über eigene Validierungsregeln und Konfigurationsoptionen, die eine konsistente Datenqualität gewährleisten.

Die Integration mit Jira erfolgt über das ConfiForms IFTTT Integration Rules-Makro, das als Brücke zwischen dem Confluence-Formular und der Jira-REST-API fungiert. Diese Komponente übersetzt die Formulardaten in das von Jira erwartete JSON-Format und übermittelt sie über die etablierte Application Link-Verbindung. Die Verwendung von Application Links bietet den Vorteil der automatischen Authentifizierung und der nahtlosen Integration in die bestehende Sicherheitsinfrastruktur.

Für die Anzeige der Ergebnisse und die Bereitstellung einer Übersicht über kürzlich erstellte Tickets kommt das ConfiForms TableView-Makro zum Einsatz. Diese Komponente ermöglicht es, Daten aus verschiedenen Quellen zu aggregieren und in einer benutzerfreundlichen tabellarischen Form darzustellen. Die Tabelle wird automatisch aktualisiert, sobald neue Epics erstellt werden, und bietet direkte Links zu den entsprechenden Jira-Tickets.

Die Fehlerbehandlung ist als durchgängiges Prinzip in alle Komponenten integriert. Validierungsfehler werden bereits auf Client-Seite abgefangen und dem Benutzer in verständlicher Form präsentiert. API-Fehler und Netzwerkprobleme werden durch das IFTTT-System erkannt und entsprechende Fehlermeldungen generiert, die dem Benutzer konkrete Handlungsempfehlungen geben.

## Schritt-für-Schritt Implementierung

### Schritt 1: Vorbereitung der Confluence-Seite

Bevor mit der Implementierung des ConfiForms-Makros begonnen werden kann, muss eine neue Confluence-Seite erstellt oder eine bestehende Seite für die Aufnahme des Makros vorbereitet werden. Die Seite sollte in einem Bereich platziert werden, der für alle berechtigten Benutzer zugänglich ist, die Epic-Tickets erstellen dürfen.

Erstellen Sie eine neue Confluence-Seite mit einem aussagekräftigen Titel wie "Epic-Erstellung für Projekt BWPTLS24" oder "Jira-Epic-Generator". Der Titel sollte klar kommunizieren, welchen Zweck die Seite erfüllt und für welches Projekt sie bestimmt ist. Dies erleichtert den Benutzern die Navigation und das Auffinden der Funktionalität.

Fügen Sie eine kurze Einführung hinzu, die den Zweck des Formulars erklärt und eventuelle Hinweise zur Nutzung enthält. Diese Einführung sollte auch Informationen darüber enthalten, welche Berechtigungen erforderlich sind und an wen sich Benutzer bei Problemen wenden können.

### Schritt 2: ConfiForms Form Definition erstellen

Der erste technische Schritt besteht in der Erstellung des Haupt-Container-Makros. Wechseln Sie in den Bearbeitungsmodus der Confluence-Seite und fügen Sie das ConfiForms Form Definition-Makro hinzu. Dies kann durch Drücken von Strg+Shift+A und die Eingabe von "ConfiForms Form" erfolgen.

Konfigurieren Sie das Form Definition-Makro mit folgenden Parametern:

**Form Name:** epic_creation_form  
**Entity Name:** epic_entries  
**Description:** Formular zur automatisierten Erstellung von Jira-Epics im Projekt BWPTLS24

Die Wahl eines eindeutigen Formularnamens ist wichtig, da dieser als Referenz für alle anderen Makros dient, die auf dieses Formular zugreifen. Der Entity Name definiert, wie die gespeicherten Daten intern referenziert werden, und sollte ebenfalls eindeutig und beschreibend sein.

In den erweiterten Einstellungen des Form Definition-Makros können zusätzliche Optionen konfiguriert werden. Aktivieren Sie die Option "Store entries" um sicherzustellen, dass die Formulardaten für spätere Referenz und für die Anzeige in der Übersichtstabelle gespeichert werden. Die Option "Allow anonymous submissions" sollte deaktiviert bleiben, da nur authentifizierte Benutzer Epic-Tickets erstellen dürfen.

### Schritt 3: Formularfelder definieren

Innerhalb des ConfiForms Form Definition-Makros müssen nun die einzelnen Formularfelder definiert werden. Jedes Feld wird durch ein separates ConfiForms Field Definition-Makro repräsentiert, das spezifische Eigenschaften und Validierungsregeln definiert.

#### Feld 1: Zusammenfassung (Summary)

Das erste und wichtigste Feld ist die Zusammenfassung des Epics. Fügen Sie ein ConfiForms Field Definition-Makro innerhalb des Form Definition-Makros hinzu und konfigurieren Sie es wie folgt:

**Field Name:** summary  
**Field Type:** text  
**Field Label:** Zusammenfassung  
**Required:** true  
**Validation Pattern:** ^.{5,255}$  
**Validation Message:** Die Zusammenfassung muss zwischen 5 und 255 Zeichen lang sein.

Die Validierung stellt sicher, dass die Zusammenfassung weder zu kurz noch zu lang ist, was sowohl die Datenqualität als auch die Kompatibilität mit Jira-Feldlängen gewährleistet. Das Regex-Pattern ^.{5,255}$ akzeptiert alle Zeichen, beschränkt jedoch die Länge auf den gewünschten Bereich.

#### Feld 2: Epic Name

Da der Epic Name in den meisten Fällen identisch mit der Zusammenfassung ist, wird dieses Feld als verstecktes Feld implementiert, das automatisch den Wert der Zusammenfassung übernimmt:

**Field Name:** epic_name  
**Field Type:** hidden  
**Field Label:** Epic Name  
**Default Value:** [entry.summary]

Die Verwendung der [entry.summary]-Notation ermöglicht es, den Wert eines anderen Feldes dynamisch zu referenzieren. Dies reduziert die Eingabearbeit für den Benutzer und stellt sicher, dass beide Felder konsistent bleiben.

#### Feld 3: Anforderungskategorie

Dieses Dropdown-Feld bietet die vier vordefinierten Kategorien zur Auswahl:

**Field Name:** anforderungskategorie  
**Field Type:** dropdown  
**Field Label:** Anforderungskategorie  
**Required:** true  
**Options:**
- technische Anforderung
- fachliche Anforderung  
- betriebliche Anforderung
- Qualitätsanforderung

Die Optionen werden als kommagetrennte Liste in das Options-Feld eingetragen. Jede Option wird automatisch als auswählbarer Eintrag im Dropdown-Menü verfügbar gemacht.

#### Feld 4: Komponenten (Multi-Select)

Für die Komponentenauswahl wird ein Multi-Select-Feld verwendet, das dynamisch die verfügbaren Komponenten aus dem Jira-Projekt lädt:

**Field Name:** components  
**Field Type:** multiselect  
**Field Label:** Komponenten  
**Required:** false  
**Data Source:** Dynamic (wird über separate IFTTT-Regel geladen)

Die dynamische Befüllung der Komponentenliste erfordert eine zusätzliche IFTTT-Integration, die beim Laden des Formulars die verfügbaren Komponenten aus Jira abruft und in das Feld einträgt.

#### Feld 5: Priorität

Das Prioritätsfeld bietet die Standard-Jira-Prioritäten zur Auswahl:

**Field Name:** priority  
**Field Type:** dropdown  
**Field Label:** Priorität  
**Required:** true  
**Default Value:** Mittel  
**Options:**
- Sehr niedrig
- Niedrig
- Mittel
- Hoch
- Sehr hoch

Der Standardwert "Mittel" entspricht der üblichen Praxis und reduziert die Anzahl der erforderlichen Benutzerinteraktionen.

#### Feld 6: Bearbeiter (Assignee)

Für die Zuweisung des Tickets wird ein Benutzerauswahlfeld verwendet:

**Field Name:** assignee  
**Field Type:** user  
**Field Label:** Bearbeiter  
**Required:** false  
**Default Value:** [entry._user]

Die Verwendung von [entry._user] als Standardwert stellt sicher, dass der aktuell angemeldete Benutzer automatisch als Bearbeiter vorausgewählt wird, was in den meisten Fällen der gewünschten Zuweisung entspricht.

#### Feld 7: Co-Bearbeiter

Für zusätzliche Bearbeiter wird ein Multi-User-Feld implementiert:

**Field Name:** co_bearbeiter  
**Field Type:** multiuser  
**Field Label:** Co-Bearbeiter/-in (Mehrfachauswahl)  
**Required:** false

Dieses Feld ermöglicht die Auswahl mehrerer Benutzer, die als zusätzliche Bearbeiter dem Epic zugewiesen werden.

#### Feld 8: Beschreibung

Für detailliertere Informationen wird ein Textarea-Feld bereitgestellt:

**Field Name:** description  
**Field Type:** textarea  
**Field Label:** Beschreibung  
**Required:** false  
**Rows:** 5

Die Anzahl der Zeilen kann je nach verfügbarem Platz und erwarteter Textmenge angepasst werden.

#### Feld 9: Lösungsversion (Fix Versions)

Ähnlich wie bei den Komponenten wird auch hier ein Multi-Select-Feld mit dynamischer Befüllung verwendet:

**Field Name:** fix_versions  
**Field Type:** multiselect  
**Field Label:** Lösungsversion  
**Required:** false  
**Data Source:** Dynamic (wird über separate IFTTT-Regel geladen)

#### Versteckte Felder für Datum

Zusätzlich werden zwei versteckte Felder für die automatische Datumssetzung benötigt:

**Field Name:** duedate  
**Field Type:** hidden  
**Default Value:** [entry._now.jiraDate]

**Field Name:** customfield_10524  
**Field Type:** hidden  
**Default Value:** [entry._now.jiraDate]

Die [entry._now.jiraDate]-Notation generiert automatisch das aktuelle Datum im von Jira erwarteten Format.

### Schritt 4: Registration Control konfigurieren

Nach der Definition aller Formularfelder muss ein ConfiForms Registration Control-Makro hinzugefügt werden, das den Submit-Button und die Formularanzeige steuert. Fügen Sie dieses Makro innerhalb des Form Definition-Makros hinzu:

**Button Label:** Epic erstellen  
**Success Message:** Epic wurde erfolgreich erstellt!  
**Error Message:** Fehler bei der Epic-Erstellung. Bitte versuchen Sie es erneut.  
**Form Layout:** embedded

Die eingebettete Darstellung (embedded) zeigt das Formular direkt auf der Seite an, anstatt es in einem Dialog zu öffnen. Dies bietet eine bessere Benutzererfahrung, insbesondere bei komplexeren Formularen mit vielen Feldern.

### Schritt 5: IFTTT Integration Rules implementieren

Der kritischste Teil der Implementierung ist die Konfiguration der IFTTT Integration Rules, die die Verbindung zu Jira herstellen und die Epic-Erstellung durchführen. Fügen Sie ein ConfiForms IFTTT Integration Rules-Makro innerhalb des Form Definition-Makros hinzu.

#### Hauptkonfiguration der IFTTT-Regel

**Event:** onCreated  
**Action:** Create Jira Issue  
**Result Name:** jira_epic_result  
**Jira Server:** (Wählen Sie die konfigurierte Application Link-Verbindung)

#### JSON-Mapping für die Epic-Erstellung

Im Body-Bereich des IFTTT-Makros muss das folgende JSON-Mapping eingefügt werden:


```json
{
    "fields": {
        "project": {
            "key": "BWPTLS24"
        },
        "issuetype": {
            "name": "Epic"
        },
        "summary": "Einführung von [entry.summary]",
        "customfield_10103": "[entry.summary]",
        "customfield_10403": {
            "id": "[entry.anforderungskategorie]"
        },
        "components": [
            {
                "name": "[entry.components]"
            }
        ],
        "priority": {
            "name": "[entry.priority]"
        },
        "duedate": "[entry._now.jiraDate]",
        "customfield_10524": "[entry._now.jiraDate]",
        "assignee": {
            "name": "#if([entry.assignee])[entry.assignee]#else[entry._user]#end"
        },
        "customfield_12500": {
            "name": "[entry.co_bearbeiter]"
        },
        "description": "[entry.description.escapeJSON]",
        "fixVersions": [
            {
                "name": "[entry.fix_versions]"
            }
        ]
    }
}
```

Dieses JSON-Mapping übersetzt die ConfiForms-Feldwerte in das von der Jira-REST-API erwartete Format. Besonders wichtig ist die Verwendung der escapeJSON-Funktion für das Beschreibungsfeld, um Probleme mit Zeilenumbrüchen und Sonderzeichen zu vermeiden. Die Velocity-Template-Syntax (#if...#else...#end) im Assignee-Feld stellt sicher, dass automatisch der aktuelle Benutzer zugewiesen wird, falls kein expliziter Bearbeiter ausgewählt wurde.

Die Zusammenfassung wird automatisch mit dem Präfix "Einführung von" versehen, wie in den Anforderungen spezifiziert. Das customfield_10103 entspricht dem Epic Name-Feld in Jira und wird mit dem gleichen Wert wie die Zusammenfassung befüllt. Das customfield_10403 repräsentiert die Anforderungskategorie und erwartet eine ID anstelle des Textwertes.

#### Fehlerbehandlung in der IFTTT-Regel

Für eine robuste Fehlerbehandlung sollten zusätzliche Parameter in der IFTTT-Konfiguration gesetzt werden:

**Do not report error:** false (deaktiviert)  
**Conditions:** Keine spezifischen Bedingungen erforderlich  
**Additional Context:** Alle verfügbaren Kontextinformationen aktivieren

Die Deaktivierung der "Do not report error"-Option stellt sicher, dass Fehler bei der Jira-API-Kommunikation an den Benutzer weitergegeben werden. Dies ist essentiell für die Diagnose von Problemen und die Bereitstellung hilfreicher Fehlermeldungen.

### Schritt 6: Erfolgsanzeige und Rückgabe-Verarbeitung

Nach der erfolgreichen Erstellung eines Epics muss das System dem Benutzer eine Bestätigung anzeigen und einen Link zum neuen Ticket bereitstellen. Dies wird durch eine zusätzliche IFTTT-Regel realisiert, die auf das Ergebnis der ersten Regel reagiert.

Fügen Sie eine zweite ConfiForms IFTTT Integration Rules hinzu:

**Event:** onCreated  
**Action:** Create (Update) ConfiForms Entry  
**Target Form:** epic_creation_form  
**Conditions:** [iftttResult_jira_epic_result] is not empty

#### Body für die Erfolgsanzeige:

```velocity
#if([iftttResult_jira_epic_result])
Das Epic wurde erfolgreich erstellt!

**Epic-Nummer:** [iftttResult_jira_epic_result]  
**Epic-Name:** [entry.summary]  
**Jira-Link:** [https://jira.franz.extraklaus.de/browse/[iftttResult_jira_epic_result]]

Sie können das Epic direkt in Jira öffnen, indem Sie auf den obigen Link klicken.
#else
Bei der Epic-Erstellung ist ein Fehler aufgetreten. Bitte überprüfen Sie Ihre Eingaben und versuchen Sie es erneut. Falls das Problem weiterhin besteht, wenden Sie sich an den Administrator.
#end
```

Diese Velocity-Template-Logik überprüft, ob die Jira-API-Integration erfolgreich war und zeigt entsprechend eine Erfolgs- oder Fehlermeldung an. Der generierte Link führt direkt zum neu erstellten Epic in Jira und verwendet die zurückgegebene Issue-Nummer.

### Schritt 7: Übersichtstabelle für die letzten 5 Epics

Um den Benutzern eine Übersicht über kürzlich erstellte Epics zu bieten, wird ein ConfiForms TableView-Makro implementiert. Dieses Makro sollte außerhalb des Form Definition-Makros, aber auf derselben Confluence-Seite platziert werden.

#### TableView-Konfiguration:

**Form Name:** epic_creation_form  
**Filter:** Keine spezifischen Filter (zeigt alle Einträge)  
**Sort:** _tstamp desc (neueste zuerst)  
**Page Size:** 5  
**Show Search:** false  
**Show Export:** false

#### Spaltendefinitionen:

Innerhalb des TableView-Makros müssen ConfiForms Field-Makros für jede anzuzeigende Spalte definiert werden:

**Spalte 1: Epic-Nummer**
```
Field Name: jira_epic_result
Field Label: Epic-Nummer
Field Type: link
Link Pattern: https://jira.franz.extraklaus.de/browse/[entry.jira_epic_result]
Link Text: [entry.jira_epic_result]
```

**Spalte 2: Epic-Name**
```
Field Name: summary
Field Label: Epic-Name
Field Type: link
Link Pattern: https://jira.franz.extraklaus.de/browse/[entry.jira_epic_result]
Link Text: [entry.summary]
```

**Spalte 3: Ersteller**
```
Field Name: _user
Field Label: Ersteller
Field Type: text
```

**Spalte 4: Erstellungsdatum**
```
Field Name: _tstamp
Field Label: Erstellt am
Field Type: datetime
Format: dd.MM.yyyy HH:mm
```

**Spalte 5: Status**
```
Field Name: jira_epic_result
Field Label: Status
Field Type: text
Display Logic: #if([entry.jira_epic_result])Erstellt#else Fehler#end
```

Diese Konfiguration erstellt eine übersichtliche Tabelle, die die wichtigsten Informationen zu den kürzlich erstellten Epics anzeigt. Die Verwendung von Links in den ersten beiden Spalten ermöglicht es den Benutzern, direkt zu den entsprechenden Jira-Tickets zu navigieren.

### Schritt 8: Dynamische Befüllung von Dropdown-Feldern

Für die dynamische Befüllung der Komponenten- und Fix-Versions-Felder aus Jira sind zusätzliche IFTTT-Regeln erforderlich, die beim Laden der Seite ausgeführt werden. Diese Implementierung ist komplex und erfordert sorgfältige Konfiguration.

#### IFTTT-Regel für Komponenten-Abruf:

**Event:** onPageLoad (falls verfügbar) oder onCreated mit spezieller Bedingung  
**Action:** WebService Request  
**URL:** https://jira.franz.extraklaus.de/rest/api/2/project/BWPTLS24/components  
**Method:** GET  
**Authentication:** Application Link

#### Verarbeitung der Komponenten-Antwort:

```velocity
#set($components = $response.parseJSON())
#foreach($component in $components)
    $component.name
    #if($foreach.hasNext),#end
#end
```

Diese Velocity-Logik parst die JSON-Antwort der Jira-API und extrahiert die Komponentennamen in einem Format, das von ConfiForms-Dropdown-Feldern verwendet werden kann.

#### Ähnliche Implementierung für Fix-Versions:

**URL:** https://jira.franz.extraklaus.de/rest/api/2/project/BWPTLS24/versions  
**Verarbeitung:** Analog zu Komponenten, aber mit $version.name

Die dynamische Befüllung stellt sicher, dass die Dropdown-Felder immer die aktuellen Werte aus Jira enthalten, ohne dass manuelle Aktualisierungen erforderlich sind.

## Erweiterte Konfiguration und Optimierung

### Performance-Optimierung

Für eine optimale Performance des ConfiForms-Makros sollten verschiedene Aspekte berücksichtigt werden. Die Anzahl der gleichzeitigen IFTTT-Regeln sollte minimiert werden, um die Serverbelastung zu reduzieren. Caching-Mechanismen können für die dynamischen Dropdown-Inhalte implementiert werden, indem die Jira-API-Aufrufe nur in bestimmten Intervallen durchgeführt werden.

Die Verwendung von Bedingungen in IFTTT-Regeln kann dazu beitragen, unnötige API-Aufrufe zu vermeiden. Beispielsweise sollten Komponenten und Fix-Versions nur dann abgerufen werden, wenn sie tatsächlich benötigt werden oder wenn sich die Projektdaten geändert haben.

### Sicherheitsaspekte

Die Sicherheit des ConfiForms-Makros basiert auf mehreren Ebenen. Die Application Link-Authentifizierung stellt sicher, dass nur berechtigte Benutzer auf die Jira-API zugreifen können. Die Confluence-Seitenberechtigungen kontrollieren, wer das Formular überhaupt sehen und verwenden kann.

Zusätzliche Sicherheitsmaßnahmen können durch die Implementierung von Eingabevalidierung und Sanitization erreicht werden. Die escapeJSON-Funktion ist ein Beispiel für eine solche Maßnahme, die verhindert, dass schädlicher Code über Formulareingaben eingeschleust wird.

### Monitoring und Logging

Für die Überwachung der Makro-Funktionalität sollten Logging-Mechanismen implementiert werden. ConfiForms bietet verschiedene Möglichkeiten zur Protokollierung von Ereignissen und Fehlern. Diese Informationen können für die Diagnose von Problemen und die Optimierung der Performance verwendet werden.

Die Implementierung von Metriken zur Verfolgung der Nutzung des Makros kann wertvolle Einblicke in die Benutzerakzeptanz und die Effektivität der Lösung liefern. Solche Metriken können die Anzahl der erstellten Epics, die Häufigkeit von Fehlern und die durchschnittliche Bearbeitungszeit umfassen.

## Fehlerbehebung und häufige Probleme

### Application Link-Probleme

Eines der häufigsten Probleme bei der Implementierung von ConfiForms-Jira-Integrationen sind Schwierigkeiten mit der Application Link-Konfiguration. Falls die IFTTT-Regel Fehler beim Zugriff auf Jira meldet, sollten zunächst die Application Link-Einstellungen überprüft werden.

Stellen Sie sicher, dass die Application Link-Verbindung zwischen Confluence und Jira korrekt konfiguriert ist und dass beide Systeme erreichbar sind. Die Authentifizierung sollte für den verwendeten Benutzerkontext funktionieren, und die erforderlichen Berechtigungen müssen in Jira vorhanden sein.

### JSON-Formatierungsfehler

Fehler im JSON-Mapping sind eine weitere häufige Fehlerquelle. Achten Sie darauf, dass alle JSON-Syntax korrekt ist und dass die Feldnamen exakt den Jira-Feldbezeichnungen entsprechen. Die Verwendung von Velocity-Templates innerhalb des JSON kann zu Syntaxfehlern führen, wenn die Template-Logik nicht korrekt implementiert ist.

Testen Sie das JSON-Mapping zunächst mit statischen Werten, bevor Sie dynamische ConfiForms-Referenzen einführen. Dies erleichtert die Identifikation von Problemen und die schrittweise Implementierung der Funktionalität.

### Feldmapping-Probleme

Probleme beim Mapping von ConfiForms-Feldern zu Jira-Feldern können durch Unterschiede in den Datentypen oder durch fehlende Feldkonfigurationen in Jira entstehen. Überprüfen Sie, dass alle referenzierten Custom Fields in Jira existieren und für das Projekt BWPTLS24 verfügbar sind.

Die Verwendung der korrekten Feld-IDs ist kritisch für den Erfolg der Integration. Custom Fields in Jira haben numerische IDs (wie customfield_10103), die exakt verwendet werden müssen. Standard-Felder verwenden hingegen ihre englischen Namen (wie "summary" oder "priority").

### Performance-Probleme

Bei Performance-Problemen sollten zunächst die IFTTT-Regeln überprüft werden. Zu viele gleichzeitige API-Aufrufe können die Systemleistung beeinträchtigen. Die Implementierung von Caching-Mechanismen und die Optimierung der API-Aufrufe können zur Verbesserung der Performance beitragen.

Die Größe der TableView-Ergebnisse sollte begrenzt werden, um die Ladezeiten zu reduzieren. Die Konfiguration von Paging und Filtering kann dazu beitragen, große Datenmengen effizienter zu handhaben.

## Wartung und Weiterentwicklung

### Regelmäßige Wartungsaufgaben

Die Wartung des ConfiForms-Makros umfasst verschiedene regelmäßige Aufgaben. Die Überprüfung der Application Link-Verbindung sollte in regelmäßigen Abständen erfolgen, um sicherzustellen, dass die Integration weiterhin funktioniert. Änderungen in der Jira-Konfiguration, wie neue Custom Fields oder geänderte Workflows, können Anpassungen im ConfiForms-Makro erforderlich machen.

Die Überwachung der Fehlerprotokolle kann dabei helfen, Probleme frühzeitig zu erkennen und zu beheben. Regelmäßige Tests der Funktionalität, insbesondere nach System-Updates, sind empfehlenswert, um die kontinuierliche Verfügbarkeit sicherzustellen.

### Erweiterungsmöglichkeiten

Das implementierte ConfiForms-Makro bietet verschiedene Möglichkeiten für zukünftige Erweiterungen. Die Integration zusätzlicher Jira-Felder kann durch die Erweiterung des JSON-Mappings und die Hinzufügung entsprechender Formularfelder erreicht werden.

Die Implementierung von Workflow-Funktionalitäten, wie automatische Benachrichtigungen oder Genehmigungsprozesse, kann den Nutzen des Makros erheblich erweitern. ConfiForms bietet umfangreiche Möglichkeiten für die Implementierung komplexer Geschäftslogik durch die Kombination verschiedener IFTTT-Regeln.

Die Integration mit anderen Atlassian-Produkten, wie Bitbucket oder Bamboo, kann durch zusätzliche IFTTT-Regeln und WebService-Aufrufe realisiert werden. Dies ermöglicht die Erstellung umfassender DevOps-Workflows, die über die reine Epic-Erstellung hinausgehen.

### Versionskontrolle und Backup

Für die langfristige Wartbarkeit des ConfiForms-Makros ist es wichtig, eine Versionskontrolle für die Konfiguration zu implementieren. ConfiForms bietet Export- und Import-Funktionalitäten, die für Backup-Zwecke und für die Migration zwischen Umgebungen verwendet werden können.

Die Dokumentation aller Konfigurationsänderungen ist essentiell für die Nachvollziehbarkeit und für die Schulung neuer Administratoren. Ein Change-Management-Prozess sollte etabliert werden, um sicherzustellen, dass Änderungen getestet und dokumentiert werden, bevor sie in die Produktionsumgebung übernommen werden.

## Schulung und Benutzerakzeptanz

### Benutzerhandbuch und Schulungsmaterialien

Für eine erfolgreiche Einführung des ConfiForms-Makros ist die Erstellung umfassender Schulungsmaterialien erforderlich. Ein Benutzerhandbuch sollte Schritt-für-Schritt-Anleitungen für die Verwendung des Formulars enthalten, einschließlich Screenshots und Beispielen für typische Anwendungsfälle.

Video-Tutorials können besonders effektiv sein, um komplexere Aspekte der Formularnutzung zu erklären. Diese sollten sowohl die grundlegende Bedienung als auch erweiterte Funktionen wie die Verwendung von Multi-Select-Feldern und die Interpretation von Fehlermeldungen abdecken.

### Change Management

Die Einführung des automatisierten Epic-Erstellungsprozesses stellt eine Änderung in den etablierten Arbeitsabläufen dar. Ein strukturierter Change-Management-Ansatz kann dazu beitragen, die Benutzerakzeptanz zu erhöhen und Widerstand gegen die neue Technologie zu minimieren.

Die Kommunikation der Vorteile des neuen Systems ist entscheidend für den Erfolg. Benutzer sollten verstehen, wie das ConfiForms-Makro ihre Arbeit vereinfacht und die Effizienz steigert. Die Bereitstellung von Support während der Einführungsphase kann dazu beitragen, Probleme schnell zu lösen und das Vertrauen in das neue System zu stärken.

### Feedback-Mechanismen

Die Implementierung von Feedback-Mechanismen ermöglicht es, kontinuierliche Verbesserungen am ConfiForms-Makro vorzunehmen. Dies kann durch die Integration von Bewertungsfeldern in das Formular selbst oder durch separate Feedback-Formulare erreicht werden.

Die regelmäßige Sammlung und Auswertung von Benutzerfeedback kann wertvolle Einblicke in Verbesserungsmöglichkeiten liefern. Diese Informationen können für die Priorisierung zukünftiger Entwicklungsarbeiten und für die Optimierung der Benutzeroberfläche verwendet werden.

## Fazit und Ausblick

Die Implementierung des ConfiForms-Makros zur automatisierten Jira-Epic-Erstellung stellt eine signifikante Verbesserung der Arbeitsabläufe im Projekt BWPTLS24 dar. Durch die Automatisierung des Epic-Erstellungsprozesses werden manuelle Fehler reduziert, die Konsistenz der Datenerfassung verbessert und die Effizienz der Projektarbeit gesteigert.

Die modulare Architektur der Lösung ermöglicht es, zukünftige Anforderungen flexibel zu berücksichtigen und das System schrittweise zu erweitern. Die Verwendung von Standardkomponenten und die Einhaltung bewährter Praktiken gewährleisten die langfristige Wartbarkeit und Skalierbarkeit der Implementierung.

Der Erfolg der Lösung hängt maßgeblich von der sorgfältigen Implementierung, der umfassenden Schulung der Benutzer und der kontinuierlichen Wartung ab. Mit der richtigen Herangehensweise kann das ConfiForms-Makro zu einem wertvollen Werkzeug für die Projektarbeit werden und als Grundlage für weitere Automatisierungsinitiative dienen.

Die Zukunft der Lösung liegt in der kontinuierlichen Weiterentwicklung und Anpassung an sich ändernde Anforderungen. Die Integration mit anderen Systemen und die Implementierung erweiterte Workflow-Funktionalitäten bieten erhebliches Potenzial für weitere Effizienzsteigerungen und Verbesserungen der Benutzerexperience.

## Referenzen

[1] Vertuna ConfiForms Documentation - Basic Concepts: https://wiki.vertuna.com/spaces/CONFIFORMS/pages/1212419/Basic+concepts

[2] ConfiForms IFTTT Integration Rules Documentation: https://wiki.vertuna.com/spaces/CONFIFORMS/pages/9864128/Configuring+ConfiForms+IFTTT+actions+and+rules

[3] Creating Jira Issues from Confluence with ConfiForms: https://wiki.vertuna.com/spaces/CONFIFORMS/pages/1212664/Creating+Jira+issue+from+Confluence+with+ConfiForms

[4] ConfiForms Official Website: https://confiforms.com/

[5] Atlassian Jira REST API Documentation: https://developer.atlassian.com/server/jira/platform/rest-apis/

[6] ConfiForms Tutorials and Cookbook: https://wiki.vertuna.com/spaces/CONFIFORMS/pages/557099/Tutorials

