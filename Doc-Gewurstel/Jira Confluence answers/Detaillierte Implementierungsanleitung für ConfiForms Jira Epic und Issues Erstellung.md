# Detaillierte Implementierungsanleitung für ConfiForms Jira Epic und Issues Erstellung

## Einführung

Diese Anleitung führt Sie Schritt für Schritt durch die Implementierung eines ConfiForms-Formulars in Confluence, das automatisch Jira Epics und Issues mit spezifischen Checklisten erstellt. Die Anleitung enthält detaillierte Erklärungen und visuelle Hilfen für jeden Schritt.

## Voraussetzungen

- Confluence 8.5 (Server/Data Center)
- Jira 9.12 (Server/Data Center)
- ConfiForms Plugin installiert und lizenziert
- Funktionierende Application Link-Verbindung zwischen Confluence und Jira
- Berechtigungen zum Erstellen von Epics und Issues im Jira-Projekt "JIRAPROJ24"

## Schritt 1: Confluence-Seite erstellen

1. Melden Sie sich in Ihrer Confluence-Instanz an
2. Navigieren Sie zu dem Bereich, in dem Sie die neue Seite erstellen möchten
3. Klicken Sie auf "Erstellen" oder "+" in der oberen Menüleiste
4. Wählen Sie "Leere Seite"
5. Geben Sie einen aussagekräftigen Titel ein, z.B. "Jira Epic und Issues Erstellung"

![Confluence Seite erstellen](https://example.com/images/create_page.png)

## Schritt 2: ConfiForms Form Definition hinzufügen

1. Platzieren Sie den Cursor an der Stelle, wo das Formular erscheinen soll
2. Drücken Sie `/` (Schrägstrich), um das Makro-Menü zu öffnen
3. Suchen Sie nach "ConfiForms Form Definition"
4. Wählen Sie das Makro aus
5. Im Konfigurationsdialog:
   - Geben Sie als Form-Namen "EpicCreationForm" ein
   - Lassen Sie die anderen Einstellungen unverändert
6. Klicken Sie auf "Einfügen"

![ConfiForms Form Definition](https://example.com/images/form_definition.png)

## Schritt 3: Formularfelder definieren

Wir werden nun alle benötigten Felder für das Formular definieren. Für jedes Feld müssen wir zwei Makros hinzufügen:
1. "ConfiForms Field Definition" - definiert die Eigenschaften des Feldes
2. "ConfiForms Field" - zeigt das Feld im Formular an

### 3.1 Epic Name

1. Platzieren Sie den Cursor innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `epicName`
   - Typ: `Text`
   - Label: `Epic Name`
   - Erforderlich: `Ja`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `epicName`
6. Klicken Sie auf "Einfügen"

![Epic Name Feld](https://example.com/images/epic_name_field.png)

### 3.2 Epic Beschreibung

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `epicDescription`
   - Typ: `Textarea`
   - Label: `Epic Beschreibung`
   - Erforderlich: `Ja`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `epicDescription`
6. Klicken Sie auf "Einfügen"

![Epic Beschreibung Feld](https://example.com/images/epic_description_field.png)

### 3.3 Priorität

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `priority`
   - Typ: `Select`
   - Label: `Priorität`
   - Optionen: `Sehr Hoch|Hoch|Mittel|Niedrig|Sehr Niedrig`
   - Erforderlich: `Ja`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `priority`
6. Klicken Sie auf "Einfügen"

![Priorität Feld](https://example.com/images/priority_field.png)

### 3.4 Zugewiesen an

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `assignee`
   - Typ: `User Picker - Jira User`
   - Label: `Zugewiesen an`
   - Erforderlich: `Ja`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `assignee`
6. Klicken Sie auf "Einfügen"

![Zugewiesen an Feld](https://example.com/images/assignee_field.png)

### 3.5 Fällig am

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `dueDate`
   - Typ: `Date`
   - Label: `Fällig am`
   - Erforderlich: `Ja`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `dueDate`
6. Klicken Sie auf "Einfügen"

![Fällig am Feld](https://example.com/images/due_date_field.png)

### 3.6 Issue-Typ

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `issueType`
   - Typ: `Select`
   - Label: `Issue-Typ`
   - Optionen: `Epic`
   - Default: `Epic`
   - Erforderlich: `Ja`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `issueType`
6. Klicken Sie auf "Einfügen"

![Issue-Typ Feld](https://example.com/images/issue_type_field.png)

### 3.7 Jira-Projekt

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `jiraProject`
   - Typ: `Select`
   - Label: `Jira-Projekt`
   - Optionen: `JIRAPROJ24`
   - Default: `JIRAPROJ24`
   - Erforderlich: `Ja`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `jiraProject`
6. Klicken Sie auf "Einfügen"

![Jira-Projekt Feld](https://example.com/images/jira_project_field.png)

### 3.8 Jira-Key (optional)

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `jiraKey`
   - Typ: `Text`
   - Label: `Jira-Key (falls bereits vergeben)`
   - Erforderlich: `Nein`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `jiraKey`
6. Klicken Sie auf "Einfügen"

![Jira-Key Feld](https://example.com/images/jira_key_field.png)

### 3.9 Issue 1 erstellen

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `createIssue1`
   - Typ: `Checkbox`
   - Label: `Issue 1 erstellen?`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `createIssue1`
6. Klicken Sie auf "Einfügen"

![Issue 1 erstellen Feld](https://example.com/images/create_issue1_field.png)

### 3.10 Issue 2 erstellen

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `createIssue2`
   - Typ: `Checkbox`
   - Label: `Issue 2 erstellen?`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `createIssue2`
6. Klicken Sie auf "Einfügen"

![Issue 2 erstellen Feld](https://example.com/images/create_issue2_field.png)

### 3.11 Issue 3 erstellen

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `createIssue3`
   - Typ: `Checkbox`
   - Label: `Issue 3 erstellen?`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `createIssue3`
6. Klicken Sie auf "Einfügen"

![Issue 3 erstellen Feld](https://example.com/images/create_issue3_field.png)

### 3.12 Issue 4 erstellen

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `createIssue4`
   - Typ: `Checkbox`
   - Label: `Issue 4 erstellen?`
4. Klicken Sie auf "Einfügen"
5. Direkt darunter fügen Sie das "ConfiForms Field" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "ConfiForms Field"
   - Name: `createIssue4`
6. Klicken Sie auf "Einfügen"

![Issue 4 erstellen Feld](https://example.com/images/create_issue4_field.png)

### 3.13 Versteckte Felder für Ergebnisse

Diese Felder werden nicht im Formular angezeigt, sondern dienen nur zur Speicherung der erstellten Jira-Keys.

#### 3.13.1 Epic Jira Key

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `epicJiraKey`
   - Typ: `Text`
   - Label: `Erstellter Epic-Key`
   - Versteckt: `Ja`
4. Klicken Sie auf "Einfügen"

#### 3.13.2 Issue 1 Jira Key

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field Definition" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `issue1JiraKey`
   - Typ: `Text`
   - Label: `Erstellter Issue 1-Key`
   - Versteckt: `Ja`
4. Klicken Sie auf "Einfügen"

#### 3.13.3 Issue 2 Jira Key

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field Definition" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `issue2JiraKey`
   - Typ: `Text`
   - Label: `Erstellter Issue 2-Key`
   - Versteckt: `Ja`
4. Klicken Sie auf "Einfügen"

#### 3.13.4 Issue 3 Jira Key

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field Definition" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `issue3JiraKey`
   - Typ: `Text`
   - Label: `Erstellter Issue 3-Key`
   - Versteckt: `Ja`
4. Klicken Sie auf "Einfügen"

#### 3.13.5 Issue 4 Jira Key

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms Field Definition" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Field Definition"
3. Im Konfigurationsdialog:
   - Name: `issue4JiraKey`
   - Typ: `Text`
   - Label: `Erstellter Issue 4-Key`
   - Versteckt: `Ja`
4. Klicken Sie auf "Einfügen"

![Versteckte Felder](https://example.com/images/hidden_fields.png)

## Schritt 4: Formular-Steuerelemente hinzufügen

1. Platzieren Sie den Cursor nach dem letzten "ConfiForms Field Definition" Makro
2. Drücken Sie `/` und suchen Sie nach "ConfiForms Registration Control"
3. Klicken Sie auf "Einfügen"

![Registration Control](https://example.com/images/registration_control.png)

## Schritt 5: IFTTT-Regeln für die Jira-Integration konfigurieren

Nun werden wir die IFTTT-Regeln (If This Then That) konfigurieren, die die Jira-Integration steuern.

### 5.1 IFTTT-Regel für Epic-Erstellung

1. Platzieren Sie den Cursor nach dem "ConfiForms Registration Control" Makro, aber immer noch innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms IFTTT Integration Rules"
3. Klicken Sie auf "Einfügen"
4. Im Konfigurationsdialog:
   - Event: `onCreated`
   - Action: `Create JIRA Issue`
5. Klicken Sie auf "Einfügen"
6. Innerhalb des IFTTT-Makros fügen Sie ein "No Format" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "No Format"
   - Klicken Sie auf "Einfügen"
7. Fügen Sie folgenden JSON-Code in das "No Format" Makro ein:

```json
{
  "fields": {
    "project": {
      "key": "[entry.jiraProject]"
    },
    "summary": "[entry.epicName]",
    "description": "[entry.epicDescription]\n\n!* Muss zuerst abgearbeitet werden\n[ ]* Annahmen und Entscheidungen dokumentiert\n[ ]* Risiken und Abhängigkeiten ermittelt\n[ ]* Keine kritischen offenen Fragen/Punkte\n[ ]* Einfluss nicht-funktionaler Anforderungen bewertet\n[ ]* Testbarkeit bestätigt\n[ ]* Grobschätzung liegt vor",
    "issuetype": {
      "name": "Epic"
    },
    "priority": {
      "name": "[entry.priority]"
    },
    "assignee": {
      "name": "[entry.assignee]"
    },
    "duedate": "[entry.dueDate]"
  }
}
```

![IFTTT Epic Erstellung](https://example.com/images/ifttt_epic_creation.png)

### 5.2 IFTTT-Regel zum Speichern des Epic-Keys

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms IFTTT Integration Rules" Makro, aber immer noch innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms IFTTT Integration Rules"
3. Klicken Sie auf "Einfügen"
4. Im Konfigurationsdialog:
   - Event: `onCreated`
   - Action: `Update Entry`
5. Klicken Sie auf "Einfügen"
6. Fügen Sie folgenden Text direkt in das IFTTT-Makro ein (ohne "No Format" Makro):

```
epicJiraKey=[iftttResult_0]
```

![IFTTT Epic Key Speichern](https://example.com/images/ifttt_save_epic_key.png)

### 5.3 IFTTT-Regel für Issue 1 Erstellung

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms IFTTT Integration Rules" Makro, aber immer noch innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms IFTTT Integration Rules"
3. Klicken Sie auf "Einfügen"
4. Im Konfigurationsdialog:
   - Event: `onCreated`
   - Action: `Create JIRA Issue`
   - Condition: `[entry.createIssue1] == "true"`
5. Klicken Sie auf "Einfügen"
6. Innerhalb des IFTTT-Makros fügen Sie ein "No Format" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "No Format"
   - Klicken Sie auf "Einfügen"
7. Fügen Sie folgenden JSON-Code in das "No Format" Makro ein:

```json
{
  "fields": {
    "project": {
      "key": "[entry.jiraProject]"
    },
    "summary": "Issue 1 für [entry.epicName]",
    "description": "Unteraufgabe 1 für Epic [entry.epicJiraKey]\n\n#! nach Ticketerstellung, vor weiterer Beauftragung; durch Produktverantwortung\n[ ]* Patch im DevNet abgenommen\n[ ]* Patchname als Lösungsversion in allen zugehörigen Tickets eintragen; wenn nicht auswählbar dann ggf. über Stephan Vogt (Vertretung Michael Malburg) Lösungsversion anlegen lassen. Im Anschluss in den Tickets nachpflegen.\n[ ]* Confluence-Seite der Auslieferung anlegen und befüllen\n[ ]* neue Zeile in der Installationsübersicht mit Grunddaten befüllen\n[ ]* Installationsvoraussetzungen: Gibt es Abhängigkeiten / Voraussetzungen die der Installation dieses Produkts entgegenstehen? Bspw. abhängige Versionen die installiert sein müssen / offene Abnahmen von vorangegangenen Produkten auf dieser oder vorgelagerter Umgebung ... Dann Tickets entsprechend verknüpfen: bspw. \"wird blockiert durch\"\n#! vor Beauftragung mündliche Absprache zur Installation; durch Produktverantwortung\n[ ]* Datenbankadministrator\n[ ]* Applikationsadministrator\n[ ]* Testkoordination\n#! Ticketabarbeitung nach erfolgter Absprache; primär durch Produktverantwortung\n[ ]* SG Mobile Apps über geplante Änderungen in Kenntnis setzen\n[ ]* Fälligkeitsdatum der Aufgabe / des Tickets auf das vereinbarte Installations-Datum setzen\n[ ]* Aufgabe / Ticket in den Status \"geplant\" setzen\n[ ]* Aufgabe / Ticket dem abgesprochenen Admin zuweisen\n#! Ticketabarbeitung; durch Administratoren\n[ ]* Zabbix-Wartungsfenster vor Beenden der Applikation eintragen\n[ ]* Schnittstellen bei Windows schließen lassen\n[ ]* Aufgabe / Ticket durch Admin ggf. in den Status \"in Arbeit\" setzen\n[ ]* durchgeführte Arbeiten im Ticket kommentieren, ggf. an folgende Administratoren zuweisen\n[ ]* Schnittstellen bei Windows öffnen lassen\n[ ]* nach Abschluss der Installationen, Aufgabe / Ticket in den Status \"in Review\" setzen und der beauftragenden Produktverantwortung zuweisen\n#! nach Installation; durch Produktverantwortung\n[ ]* Testkoordination über Abschluss der Arbeiten und Verfügbarkeit der Umgebung informieren\n[ ]* Installationsübersicht mit Installationsdatum ergänzen\n[ ]* Produkt abnehmen\n[ ]* Prüfung ob alle Beauftragungen / Unteraufgaben umgesetzt sind, ggf. nachhaken\n[ ]* nach erfolgreicher Abnahme Aufgabe / Ticket in den Status \"abgeschlossen\" / \"fertig\" setzen",
    "issuetype": {
      "name": "Task"
    },
    "priority": {
      "name": "[entry.priority]"
    },
    "assignee": {
      "name": "[entry.assignee]"
    },
    "epiclink": "[entry.epicJiraKey]"
  }
}
```

![IFTTT Issue 1 Erstellung](https://example.com/images/ifttt_issue1_creation.png)

### 5.4 IFTTT-Regel zum Speichern des Issue 1-Keys

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms IFTTT Integration Rules" Makro, aber immer noch innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms IFTTT Integration Rules"
3. Klicken Sie auf "Einfügen"
4. Im Konfigurationsdialog:
   - Event: `onCreated`
   - Action: `Update Entry`
   - Condition: `[entry.createIssue1] == "true"`
5. Klicken Sie auf "Einfügen"
6. Fügen Sie folgenden Text direkt in das IFTTT-Makro ein (ohne "No Format" Makro):

```
issue1JiraKey=[iftttResult_2]
```

![IFTTT Issue 1 Key Speichern](https://example.com/images/ifttt_save_issue1_key.png)

### 5.5 IFTTT-Regel für Issue 2 Erstellung

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms IFTTT Integration Rules" Makro, aber immer noch innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms IFTTT Integration Rules"
3. Klicken Sie auf "Einfügen"
4. Im Konfigurationsdialog:
   - Event: `onCreated`
   - Action: `Create JIRA Issue`
   - Condition: `[entry.createIssue2] == "true"`
5. Klicken Sie auf "Einfügen"
6. Innerhalb des IFTTT-Makros fügen Sie ein "No Format" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "No Format"
   - Klicken Sie auf "Einfügen"
7. Fügen Sie folgenden JSON-Code in das "No Format" Makro ein:

```json
{
  "fields": {
    "project": {
      "key": "[entry.jiraProject]"
    },
    "summary": "Issue 2 für [entry.epicName]",
    "description": "Unteraufgabe 2 für Epic [entry.epicJiraKey]\n\n#! vor Beauftragung mündliche Absprache zur Installation; durch Produktverantwortung\n[ ]* Installationsvoraussetzungen: Gibt es Abhängigkeiten / Voraussetzungen die der Installation dieses Produkts entgegenstehen? Bspw. abhängige Versionen die installiert sein müssen / offene Abnahmen von vorangegangenen Produkten auf dieser oder vorgelagerter Umgebung ... Dann Tickets entsprechend verknüpfen: bspw. \"wird blockiert durch\"\n[ ]* Datenbankadministrator verfügbar? Im Feld \"Beschreibung\" des Sammeltickets oder der einzelnen Aufgabe erfassen wer geplant die Umsetzung durchführen wird\n[ ]* Applikationsadministrator verfügbar? Im Feld \"Beschreibung\" des Sammeltickets oder der einzelnen Aufgabe erfassen wer geplant die Umsetzung durchführen wird\n[ ]* Ansprechpartner Schnittstellen schließen / öffnen, meist Windows, verfügbar? Im Feld \"Beschreibung\" des Sammeltickets oder der einzelnen Aufgabe erfassen wer geplant die Umsetzung durchführen wird\n[ ]* Absprache / Information des Termins mit der Hochschule und Fortbildungseinrichtung der Polizei\n[ ]* Changemanagement\n#! Change; im Regelfall durch Produktverantwortung\n[ ]* Changeantrag erstellen und beantragen\n#! Ticketabarbeitung nach Change-Genehmigung; primär durch Produktverantwortung\n[ ]* Change-Nummer/-Datum/-Uhrzeit/-Dauer im Feld \"Beschreibung\" des Sammeltickets; ist kein Sammelticket vorhanden die Angaben in der Aufgabe erfassen. Ggf. die Change-Beteiligten weitergehend informieren\n[ ]* Fälligkeitsdatum der Aufgabe / des Tickets auf das vereinbarte Change-Datum setzen\n[ ]* Aufgabe / Ticket in den Status \"geplant\" setzen\n[ ]* Aufgabe / Ticket dem abgesprochenen Admin / Ansprechpartner zuweisen\n[ ]* Anwenderinformation / Ausfallankündigung in POLAS-Umgebung für Ausfall einstellen\n[ ]* SG Mobile Apps über geplante Änderungen in Kenntnis setzen\n#! Change Durchführung; durch Administration\n[ ]* Aufgabe / Ticket durch Admin ggf. in den Status \"in Arbeit\" setzen\n[ ]* durchgeführte Arbeiten im Ticket kommentieren, ggf. an folgende Administratoren zuweisen\n[ ]* nach Abschluss der Installationen, Aufgabe / Ticket in den Status \"in Review\" setzen und der beauftragenden Produktverantwortung zuweisen\n[ ]* USU-Aktivität abschließen\n#! nach Installation; durch Produktverantwortung\n[ ]* Installationsübersicht mit Installationsdatum ergänzen\n[ ]* Produkt abnehmen\n[ ]* Prüfung ob alle Beauftragungen / Unteraufgaben umgesetzt sind, ggf. nachhaken\n[ ]* nach erfolgreicher Abnahme Aufgabe / Ticket in den Status \"abgeschlossen\" / \"fertig\" setzen",
    "issuetype": {
      "name": "Task"
    },
    "priority": {
      "name": "[entry.priority]"
    },
    "assignee": {
      "name": "[entry.assignee]"
    },
    "epiclink": "[entry.epicJiraKey]"
  }
}
```

![IFTTT Issue 2 Erstellung](https://example.com/images/ifttt_issue2_creation.png)

### 5.6 IFTTT-Regel zum Speichern des Issue 2-Keys

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms IFTTT Integration Rules" Makro, aber immer noch innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms IFTTT Integration Rules"
3. Klicken Sie auf "Einfügen"
4. Im Konfigurationsdialog:
   - Event: `onCreated`
   - Action: `Update Entry`
   - Condition: `[entry.createIssue2] == "true"`
5. Klicken Sie auf "Einfügen"
6. Fügen Sie folgenden Text direkt in das IFTTT-Makro ein (ohne "No Format" Makro):

```
issue2JiraKey=[iftttResult_4]
```

![IFTTT Issue 2 Key Speichern](https://example.com/images/ifttt_save_issue2_key.png)

### 5.7 IFTTT-Regel für Issue 3 Erstellung

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms IFTTT Integration Rules" Makro, aber immer noch innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms IFTTT Integration Rules"
3. Klicken Sie auf "Einfügen"
4. Im Konfigurationsdialog:
   - Event: `onCreated`
   - Action: `Create JIRA Issue`
   - Condition: `[entry.createIssue3] == "true"`
5. Klicken Sie auf "Einfügen"
6. Innerhalb des IFTTT-Makros fügen Sie ein "No Format" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "No Format"
   - Klicken Sie auf "Einfügen"
7. Fügen Sie folgenden JSON-Code in das "No Format" Makro ein:

```json
{
  "fields": {
    "project": {
      "key": "[entry.jiraProject]"
    },
    "summary": "Issue 3 für [entry.epicName]",
    "description": "Unteraufgabe 3 für Epic [entry.epicJiraKey]\n\n#! vor Beauftragung mündliche Absprache zur Installation; durch Produktverantwortung\n[ ]* Installationsvoraussetzungen: Gibt es Abhängigkeiten / Voraussetzungen die der Installation dieses Produkts entgegenstehen? Bspw. abhängige Versionen die installiert sein müssen / offene Abnahmen von vorangegangenen Produkten auf dieser oder vorgelagerter Umgebung ... Dann Tickets entsprechend verknüpfen: bspw. \"wird blockiert durch\"\n[ ]* gibt des von anderen Produktverantwortlichen auf der Umgebung noch Produkte die im gleichen Zug mit installiert werden können / sollen? Wenn ja, dann prüfen es bereits ein Sammelticket gibt und mit diesem verknüpfen ODER andernfalls ein EPIC als Sammelticket erstellen und die gemeinsam umzusetzenden Tickets mit dem Sammelticket verknüpfen.\n[ ]* Datenbankadministrator verfügbar? Im Feld \"Beschreibung\" des Sammeltickets oder der einzelnen Aufgabe erfassen wer geplant die Umsetzung durchführen wird\n[ ]* Applikationsadministrator verfügbar? Im Feld \"Beschreibung\" des Sammeltickets oder der einzelnen Aufgabe erfassen wer geplant die Umsetzung durchführen wird\n[ ]* Ansprechpartner Schnittstellen schließen / öffnen, meist Windows, verfügbar? Im Feld \"Beschreibung\" des Sammeltickets oder der einzelnen Aufgabe erfassen wer geplant die Umsetzung durchführen wird\n[ ]* Changemanagement\n#! Change; im Regelfall durch Produktverantwortung\n[ ]* Changeantrag erstellen und Change beantragen\n#! Ticketabarbeitung nach Change-Genehmigung; primär durch Produktverantwortung\n[ ]* Change-Nummer/-Datum/-Uhrzeit/-Dauer im Feld \"Beschreibung\" des Sammeltickets; ist kein Sammelticket vorhanden die Angaben in der Aufgabe erfassen. Ggf. die Change-Beteiligten weitergehend informieren\n[ ]* Fälligkeitsdatum der Aufgabe / des Tickets auf das vereinbarte Change-Datum setzen\n[ ]* Aufgabe / Ticket in den Status \"geplant\" setzen\n[ ]* Aufgabe / Ticket dem abgesprochenen Admin / Ansprechpartner zuweisen\n[ ]* Anwenderinformation / Ausfallankündigung in POLAS-Umgebung für Ausfall einstellen\n[ ]* ggf. Dokumentation in P-Online anpassen und Anwenderinformation zu Änderungen in P-Online einstellen\n[ ]* SG Mobile Apps über geplante Änderungen in Kenntnis setzen\n#! Change Durchführung; durch Administration\n[ ]* Aufgabe / Ticket durch Admin ggf. in den Status \"in Arbeit\" setzen\n[ ]* durchgeführte Arbeiten im Ticket kommentieren, ggf. an folgende Administratoren zuweisen\n[ ]* nach Abschluss der Installationen, Aufgabe / Ticket in den Status \"in Review\" setzen und der beauftragenden Produktverantwortung zuweisen\n[ ]* USU-Aktivität abschließen\n#! nach Installation; durch Produktverantwortung\n[ ]* Windows Schnittstellen ggf. öffnen lassen\n[ ]* Installationsübersicht mit Installationsdatum ergänzen\n[ ]* ITK - KM Software-Versionen ergänzen: https://confluence.itk.extrapol.de/confluence/pages/viewpage.action?spaceKey=LB&title=Software+Versionen\n[ ]* Produkt abnehmen\n[ ]* Prüfung ob alle Beauftragungen / Unteraufgaben umgesetzt sind, ggf. nachhaken\n[ ]* nach erfolgreicher Abnahme Aufgabe / Ticket in den Status \"abgeschlossen\" / \"fertig\" setzen\n#! vor Beauftragung mündliche Absprache zur Installation; durch Produktverantwortung\n[ ]* Installationsvoraussetzungen: Gibt es Abhängigkeiten / Voraussetzungen die der Installation dieses Produkts entgegenstehen? Bspw. abhängige Versionen die installiert sein müssen / offene Abnahmen von vorangegangenen Produkten auf dieser oder vorgelagerter Umgebung ... Dann Tickets entsprechend verknüpfen: bspw. \"wird blockiert durch\"\n[ ]* Datenbankadministrator\n[ ]* Applikationsadministrator\n[ ]* ggf. Testkoordination\n#! Ticketabarbeitung nach erfolgter Absprache; primär durch Produktverantwortung\n[ ]* Aufgabe / Ticket in den Status \"geplant\" setzen\n[ ]* Aufgabe / Ticket dem abgesprochenen Admin zuweisen\n#! Ticketabarbeitung; durch Administratoren\n[ ]* Zabbix-Wartungsfenster vor Beenden der Applikation eintragen\n[ ]* Schnittstellen bei Windows schließen lassen\n[ ]* Aufgabe / Ticket durch Admin ggf. in den Status \"in Arbeit\" setzen\n[ ]* durchgeführte Arbeiten im Ticket kommentieren, ggf. an folgende Administratoren zuweisen\n[ ]* Schnittstellen bei Windows öffnen lassen\n[ ]* nach Abschluss der Installationen, Aufgabe / Ticket in den Status \"in Review\" setzen und der beauftragenden Produktverantwortung zuweisen\n#! nach Installation; durch Produktverantwortung\n[ ]* Installationsübersicht mit Installationsdatum ergänzen\n[ ]* Produkt abnehmen\n[ ]* Prüfung ob alle Beauftragungen / Unteraufgaben umgesetzt sind, ggf. nachhaken\n[ ]* nach erfolgreicher Abnahme Aufgabe / Ticket in den Status \"abgeschlossen\" / \"fertig\" setzen",
    "issuetype": {
      "name": "Task"
    },
    "priority": {
      "name": "[entry.priority]"
    },
    "assignee": {
      "name": "[entry.assignee]"
    },
    "epiclink": "[entry.epicJiraKey]"
  }
}
```

![IFTTT Issue 3 Erstellung](https://example.com/images/ifttt_issue3_creation.png)

### 5.8 IFTTT-Regel zum Speichern des Issue 3-Keys

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms IFTTT Integration Rules" Makro, aber immer noch innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms IFTTT Integration Rules"
3. Klicken Sie auf "Einfügen"
4. Im Konfigurationsdialog:
   - Event: `onCreated`
   - Action: `Update Entry`
   - Condition: `[entry.createIssue3] == "true"`
5. Klicken Sie auf "Einfügen"
6. Fügen Sie folgenden Text direkt in das IFTTT-Makro ein (ohne "No Format" Makro):

```
issue3JiraKey=[iftttResult_6]
```

![IFTTT Issue 3 Key Speichern](https://example.com/images/ifttt_save_issue3_key.png)

### 5.9 IFTTT-Regel für Issue 4 Erstellung

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms IFTTT Integration Rules" Makro, aber immer noch innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms IFTTT Integration Rules"
3. Klicken Sie auf "Einfügen"
4. Im Konfigurationsdialog:
   - Event: `onCreated`
   - Action: `Create JIRA Issue`
   - Condition: `[entry.createIssue4] == "true"`
5. Klicken Sie auf "Einfügen"
6. Innerhalb des IFTTT-Makros fügen Sie ein "No Format" Makro ein:
   - Drücken Sie `/` und suchen Sie nach "No Format"
   - Klicken Sie auf "Einfügen"
7. Fügen Sie folgenden JSON-Code in das "No Format" Makro ein:

```json
{
  "fields": {
    "project": {
      "key": "[entry.jiraProject]"
    },
    "summary": "Issue 4 für [entry.epicName]",
    "description": "Unteraufgabe 4 für Epic [entry.epicJiraKey]\n\n#! vor Beauftragung mündliche Absprache zur Installation; durch Produktverantwortung\n[ ]* Installationsvoraussetzungen: Gibt es Abhängigkeiten / Voraussetzungen die der Installation dieses Produkts entgegenstehen? Bspw. abhängige Versionen die installiert sein müssen / offene Abnahmen von vorangegangenen Produkten auf dieser oder vorgelagerter Umgebung ... Dann Tickets entsprechend verknüpfen: bspw. \"wird blockiert durch\"\n[ ]* gibt des von anderen Produktverantwortlichen auf der Umgebung noch Produkte die im gleichen Zug mit installiert werden können / sollen? Wenn ja, dann prüfen es bereits ein Sammelticket gibt und mit diesem verknüpfen ODER andernfalls ein EPIC als Sammelticket erstellen und die gemeinsam umzusetzenden Tickets mit dem Sammelticket verknüpfen.\n[ ]* Datenbankadministrator verfügbar? Im Feld \"Beschreibung\" des Sammeltickets oder der einzelnen Aufgabe erfassen wer geplant die Umsetzung durchführen wird\n[ ]* Applikationsadministrator verfügbar? Im Feld \"Beschreibung\" des Sammeltickets oder der einzelnen Aufgabe erfassen wer geplant die Umsetzung durchführen wird\n[ ]* Ansprechpartner Schnittstellen schließen / öffnen, meist Windows, verfügbar? Im Feld \"Beschreibung\" des Sammeltickets oder der einzelnen Aufgabe erfassen wer geplant die Umsetzung durchführen wird\n[ ]* Changemanagement\n#! Change; im Regelfall durch Produktverantwortung\n[ ]* Changeantrag erstellen und Change beantragen\n#! Ticketabarbeitung nach Change-Genehmigung; primär durch Produktverantwortung\n[ ]* Change-Nummer/-Datum/-Uhrzeit/-Dauer im Feld \"Beschreibung\" des Sammeltickets; ist kein Sammelticket vorhanden die Angaben in der Aufgabe erfassen. Ggf. die Change-Beteiligten weitergehend informieren\n[ ]* Fälligkeitsdatum der Aufgabe / des Tickets auf das vereinbarte Change-Datum setzen\n[ ]* Aufgabe / Ticket in den Status \"geplant\" setzen\n[ ]* Aufgabe / Ticket dem abgesprochenen Admin / Ansprechpartner zuweisen\n[ ]* Anwenderinformation / Ausfallankündigung in POLAS-Umgebung für Ausfall einstellen\n[ ]* ggf. Dokumentation in P-Online anpassen und Anwenderinformation zu Änderungen in P-Online einstellen\n[ ]* SG Mobile Apps über geplante Änderungen in Kenntnis setzen\n#! Change Durchführung; durch Administration\n[ ]* Aufgabe / Ticket durch Admin ggf. in den Status \"in Arbeit\" setzen\n[ ]* durchgeführte Arbeiten im Ticket kommentieren, ggf. an folgende Administratoren zuweisen\n[ ]* nach Abschluss der Installationen, Aufgabe / Ticket in den Status \"in Review\" setzen und der beauftragenden Produktverantwortung zuweisen\n[ ]* USU-Aktivität abschließen\n#! nach Installation; durch Produktverantwortung\n[ ]* Windows Schnittstellen ggf. öffnen lassen\n[ ]* Installationsübersicht mit Installationsdatum ergänzen\n[ ]* ITK - KM Software-Versionen ergänzen: https://confluence.itk.extrapol.de/confluence/pages/viewpage.action?spaceKey=LB&title=Software+Versionen\n[ ]* Produkt abnehmen\n[ ]* Prüfung ob alle Beauftragungen / Unteraufgaben umgesetzt sind, ggf. nachhaken\n[ ]* nach erfolgreicher Abnahme Aufgabe / Ticket in den Status \"abgeschlossen\" / \"fertig\" setzen",
    "issuetype": {
      "name": "Task"
    },
    "priority": {
      "name": "[entry.priority]"
    },
    "assignee": {
      "name": "[entry.assignee]"
    },
    "epiclink": "[entry.epicJiraKey]"
  }
}
```

![IFTTT Issue 4 Erstellung](https://example.com/images/ifttt_issue4_creation.png)

### 5.10 IFTTT-Regel zum Speichern des Issue 4-Keys

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms IFTTT Integration Rules" Makro, aber immer noch innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms IFTTT Integration Rules"
3. Klicken Sie auf "Einfügen"
4. Im Konfigurationsdialog:
   - Event: `onCreated`
   - Action: `Update Entry`
   - Condition: `[entry.createIssue4] == "true"`
5. Klicken Sie auf "Einfügen"
6. Fügen Sie folgenden Text direkt in das IFTTT-Makro ein (ohne "No Format" Makro):

```
issue4JiraKey=[iftttResult_8]
```

![IFTTT Issue 4 Key Speichern](https://example.com/images/ifttt_save_issue4_key.png)

### 5.11 IFTTT-Regel für Bestätigungstabelle

1. Platzieren Sie den Cursor nach dem vorherigen "ConfiForms IFTTT Integration Rules" Makro, aber immer noch innerhalb des "ConfiForms Form Definition" Makros
2. Drücken Sie `/` und suchen Sie nach "ConfiForms IFTTT Integration Rules"
3. Klicken Sie auf "Einfügen"
4. Im Konfigurationsdialog:
   - Event: `onCreated`
   - Action: `Show Message`
5. Klicken Sie auf "Einfügen"
6. Fügen Sie folgenden HTML-Code direkt in das IFTTT-Makro ein:

```html
<h2>Erstellte Jira-Tickets</h2>
<table class="confluenceTable">
  <tr>
    <th>Typ</th>
    <th>Jira-Key</th>
    <th>Name</th>
  </tr>
  <tr>
    <td>Epic</td>
    <td><a href="https://jira.example.com/browse/[entry.epicJiraKey]">[entry.epicJiraKey]</a></td>
    <td>[entry.epicName]</td>
  </tr>
  #if([entry.issue1JiraKey] != "")
  <tr>
    <td>Issue 1</td>
    <td><a href="https://jira.example.com/browse/[entry.issue1JiraKey]">[entry.issue1JiraKey]</a></td>
    <td>Issue 1 für [entry.epicName]</td>
  </tr>
  #end
  #if([entry.issue2JiraKey] != "")
  <tr>
    <td>Issue 2</td>
    <td><a href="https://jira.example.com/browse/[entry.issue2JiraKey]">[entry.issue2JiraKey]</a></td>
    <td>Issue 2 für [entry.epicName]</td>
  </tr>
  #end
  #if([entry.issue3JiraKey] != "")
  <tr>
    <td>Issue 3</td>
    <td><a href="https://jira.example.com/browse/[entry.issue3JiraKey]">[entry.issue3JiraKey]</a></td>
    <td>Issue 3 für [entry.epicName]</td>
  </tr>
  #end
  #if([entry.issue4JiraKey] != "")
  <tr>
    <td>Issue 4</td>
    <td><a href="https://jira.example.com/browse/[entry.issue4JiraKey]">[entry.issue4JiraKey]</a></td>
    <td>Issue 4 für [entry.epicName]</td>
  </tr>
  #end
</table>
```

**Wichtig:** Ersetzen Sie `https://jira.example.com/browse/` mit der tatsächlichen URL Ihres Jira-Systems.

![IFTTT Bestätigungstabelle](https://example.com/images/ifttt_confirmation_table.png)

## Schritt 6: Speichern und Testen

1. Speichern Sie die Confluence-Seite
2. Testen Sie das Formular, indem Sie es mit Testdaten ausfüllen:
   - Geben Sie einen Epic-Namen ein
   - Fügen Sie eine Beschreibung hinzu
   - Wählen Sie eine Priorität aus
   - Wählen Sie einen Benutzer aus, dem das Ticket zugewiesen werden soll
   - Wählen Sie ein Fälligkeitsdatum
   - Aktivieren Sie eine oder mehrere Checkboxen für die Issues
   - Klicken Sie auf "Speichern"

![Formular Testen](https://example.com/images/test_form.png)

3. Überprüfen Sie, ob die Jira-Tickets korrekt erstellt wurden:
   - Wurde das Epic mit der angegebenen Beschreibung und der Epic-Checkliste erstellt?
   - Wurden die ausgewählten Issues erstellt und mit dem Epic verknüpft?
   - Enthalten die Issues die korrekten, unterschiedlichen Checklisten?
   - Wird die Bestätigungstabelle mit den erstellten Tickets angezeigt?

![Bestätigungstabelle](https://example.com/images/confirmation_table.png)

## Fehlerbehebung

Wenn Probleme auftreten:

1. **Epic wird nicht erstellt:**
   - Überprüfen Sie, ob die Jira-Verbindung korrekt konfiguriert ist
   - Stellen Sie sicher, dass der Benutzer die Berechtigung hat, Epics im Projekt "JIRAPROJ24" zu erstellen
   - Überprüfen Sie die JSON-Syntax in der IFTTT-Regel

2. **Issues werden nicht mit dem Epic verknüpft:**
   - Überprüfen Sie, ob das Feld "epiclink" dem tatsächlichen Feldnamen in Ihrem Jira-System entspricht
   - Stellen Sie sicher, dass der Epic-Key korrekt gespeichert und an die Issue-Erstellung weitergegeben wird

3. **Checklisten erscheinen nicht in den Beschreibungen:**
   - Überprüfen Sie die Formatierung der Checklisten in den JSON-Beschreibungsfeldern
   - Stellen Sie sicher, dass keine Sonderzeichen Probleme verursachen

4. **Bestätigungstabelle zeigt keine oder falsche Daten:**
   - Überprüfen Sie die Bedingungen in der HTML-Vorlage
   - Stellen Sie sicher, dass die Jira-Keys korrekt gespeichert werden

## Anpassungen

Sie können das Formular nach Bedarf anpassen:

1. **Feldnamen ändern:**
   - Bearbeiten Sie die "Label"-Werte in den "ConfiForms Field Definition" Makros

2. **Standardwerte hinzufügen:**
   - Fügen Sie "Default"-Werte in den "ConfiForms Field Definition" Makros hinzu

3. **Feldtypen ändern:**
   - Bearbeiten Sie die "Typ"-Werte in den "ConfiForms Field Definition" Makros

4. **Checklisten anpassen:**
   - Bearbeiten Sie die Beschreibungstexte in den JSON-Objekten der IFTTT-Regeln

## Zusammenfassung

Sie haben erfolgreich ein ConfiForms-Formular erstellt, das:

1. Ein Epic in Jira mit den angegebenen Informationen erstellt
2. Die entsprechende Checkliste in das Epic einfügt
3. Optional bis zu vier Issues erstellt, die dem Epic zugeordnet sind
4. In jedes Issue eine unterschiedliche vorhandene Checkliste einfügt
5. Eine Bestätigungstabelle mit den erstellten Tickets anzeigt

Diese Lösung nutzt ausschließlich die grafischen Elemente von ConfiForms und erfordert keine Adminrechte oder Zugriff auf den Storage Format Editor.
