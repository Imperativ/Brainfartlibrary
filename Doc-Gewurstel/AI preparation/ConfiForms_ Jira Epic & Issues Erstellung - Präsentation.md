## **Folie 1: Titel & Ziel**

**Automatisierte Jira Epic & Issue Erstellung mit ConfiForms**

Ziel:

Ein Confluence-Formular erstellen, das automatisch:

1.  Ein Epic in Jira anlegt (basierend auf Formulareingaben).

2.  Optional bis zu 4 verknüpfte Issues (Unteraufgaben) erstellt.

3.  Spezifische Checklisten in die Beschreibungen von Epic und Issues

    > einfügt.

4.  Eine Bestätigung der erstellten Vorgänge anzeigt.

**Umgebung:**

-   Confluence Server 8.5

-   Jira Server 9.12 (verbunden via Application Link)

-   ConfiForms App

-   Keine Admin-Rechte, kein Storage Format Editor Zugriff

## **Folie 2: Voraussetzungen**

**Was wird benötigt, bevor wir starten?**

-   **ConfiForms App:** Installiert und lizenziert in Confluence.

-   **Jira Application Link:** Funktionierende, konfigurierte Verbindung

    > zwischen Confluence & Jira.

-   **Jira Berechtigungen:** Erlaubnis, Epics & Issues im Zielprojekt zu

    > erstellen.

-   **Checklisten-Texte:** Die 5 genauen Texte (1x Epic, 4x Issues)

    > müssen bereitliegen.

-   **Jira Infos:**

    -   Projekt-Schlüssel (z.B. "PROJ")

    -   Prioritäts-Namen/-IDs (z.B. "High", "Medium")

    -   Vorgangstyp-Namen für Epic (z.B. "Epic") und Unteraufgaben (z.B.

        > "Task", "Sub-task")

\[Bild: Logos von Confluence, Jira, ConfiForms\]

## **Folie 3: Schritt 1 - Formular-Grundgerüst**

**Die Basis legen**

1.  **Neue Confluence Seite:** Erstelle eine leere Seite.

2.  **ConfiForms Form** Makro einfügen:

    -   Dies ist der Hauptcontainer für alle Felder und Logik.

    -   Alle weiteren ConfiForms-Makros für dieses Formular kommen

        > *innerhalb* dieses Makros.

\[Bild: Leere Confluence Seite mit hervorgehobenem Einfügen-Menü und dem
ConfiForms Form Makro\]

## **Folie 4: Schritt 2a - Felder definieren (Basisinfos)**

**Eingabefelder für das Epic**

Füge *innerhalb* des ConfiForms Form Makros für jedes Feld hinzu:

1.  Ein ConfiForms Field Definition Makro (definiert Name, Typ, Label)

2.  Ein ConfiForms Field Makro (zeigt das Feld im Formular an)

**Benötigte Felder:**

-   epicName (Typ: Text) - *Epic Name*

-   epicDescription (Typ: Textarea) - *Epic Beschreibung*

-   priority (Typ: Dropdown) - *Priorität* (Optionen: Jira-Prioritäten

    > eintragen)

-   assignee (Typ: User Picker - Jira User) - *Zugewiesen an*

-   dueDate (Typ: Date) - *Fällig am*

-   projectKey (Typ: Text oder Dropdown) - *Jira Projekt Key*

\[Bild: Confluence Editor zeigt verschachtelte Field Definition und
Field Makros innerhalb des Form Makros\]

## **Folie 5: Schritt 2b - Felder definieren (Bedingungen & Speicher)**

**Optionale Issues & interne Speicherfelder**

Füge weiterhin *innerhalb* des ConfiForms Form Makros hinzu:

1.  **Checkboxes für Issues:**

    -   createIssue1 (Typ: Checkbox) - *Issue 1 erstellen?*

    -   createIssue2 (Typ: Checkbox) - *Issue 2 erstellen?*

    -   createIssue3 (Typ: Checkbox) - *Issue 3 erstellen?*

    -   createIssue4 (Typ: Checkbox) - Issue 4 erstellen?

        > (Jeweils mit Field Definition und Field Makro)

2.  **Versteckte Speicherfelder (Nur Field Definition nötig):**

    -   createdEpicKey (Typ: Text) - \*Speichert den Key des erstellten

        > Epics\*

    -   createdIssue1Key (Typ: Text) - *Speichert Key von Issue 1*

    -   createdIssue2Key (Typ: Text) - *Speichert Key von Issue 2*

    -   createdIssue3Key (Typ: Text) - *Speichert Key von Issue 3*

    -   createdIssue4Key (Typ: Text) - *Speichert Key von Issue 4*

\[Bild: Ausschnitt des Formulars mit Checkboxen und Hinweis auf
versteckte Felder\]

## **Folie 6: Schritt 3a - Logik (IFTTT): Epic erstellen**

**Die "Wenn dies, dann das"-Regel für das Epic**

Füge *innerhalb* des ConfiForms Form Makros ein ConfiForms IFTTT
Integration Rules Makro ein.

**Aktion 1: Epic erstellen (Immer ausführen)**

-   **Typ:** Create Jira Issue

-   **Verbindung:** Wähle den Jira Application Link.

-   **Projekt:** \[entry.projectKey\]

-   **Typ:** Epic (oder euer Name)

-   **Summary:** \[entry.epicName\]

-   **Description:** \[entry.epicDescription\] + \*Hier den

    > Epic-Checklisten-Text einfügen!\*

-   **Priorität:** \[entry.priority\]

-   **Assignee:** \[entry.assignee\]

-   **Due Date:** \[entry.dueDate\]

-   **Epic Name (Jira Feld):** \[entry.epicName\] (Wichtiges Jira-Feld!)

-   **Store result info (Issue Key):** createdEpicKey

\[Bild: Screenshot des IFTTT Konfigurationsdialogs für die
Epic-Erstellung\]

## **Folie 7: Schritt 3b - Logik (IFTTT): Issues erstellen (Bedingt)**

**Regeln für die optionalen Issues**

Füge *weitere Aktionen* im *selben* ConfiForms IFTTT Integration Rules
Makro hinzu:

**Aktion 2: Issue 1 erstellen**

-   **Typ:** Create Jira Issue

-   **Bedingung:** \[entry.createIssue1\] = true

-   **Projekt:** \[entry.projectKey\]

-   **Typ:** Task / Sub-task (oder euer Name)

-   **Summary:** Issue 1 für \[entry.epicName\]

-   **Description:** *Hier den Checklisten-Text für Issue 1 einfügen!*

-   **Epic Link:** \[entry.createdEpicKey\] (Entscheidend für

    > Verknüpfung!)

-   **Store result info (Issue Key):** createdIssue1Key

**Wiederhole für Issue 2, 3, 4:**

-   Passe Bedingung an (createIssue2, createIssue3, createIssue4).

-   Passe Summary an.

-   Füge die *jeweilige* Checkliste in die Description ein.

-   Verknüpfe immer mit \[entry.createdEpicKey\] via Epic Link.

-   Speichere Key in createdIssue2Key, createdIssue3Key,

    > createdIssue4Key.

\[Bild: Screenshot des IFTTT Konfigurationsdialogs für eine
Issue-Erstellung mit Bedingung und Epic Link\]

## **Folie 8: Schritt 4 - Absenden-Button**

**Das Formular abschickbar machen**

-   Füge *innerhalb* des ConfiForms Form Makros, üblicherweise am Ende,

    > das ConfiForms Registration Control Makro hinzu.

-   Dieses Makro rendert den "Speichern" / "Senden" Button für den

    > Benutzer.

\[Bild: Confluence Editor zeigt das Registration Control Makro am Ende
des Formulars\]

## **Folie 9: Schritt 5 - Bestätigungsanzeige**

**Feedback für den Benutzer**

-   Füge *unterhalb* (außerhalb) des ConfiForms Form Makros ein

    > ConfiForms Records View (oder Table View) Makro ein.

-   **Konfiguration:**

    -   **Form:** Wähle das erstellte Formular aus.

    -   **Filter:** Zeige nur den letzten Eintrag des aktuellen

        > Benutzers (z.B. Created By = \_currentUser, sortiert nach
        > Created Date DESC, Limit = 1).

    -   **Angezeigte Felder:**

        -   createdEpicKey

        -   epicName

        -   createdIssue1Key (wird nur angezeigt, wenn erstellt)

        -   createdIssue2Key

        -   createdIssue3Key

        -   createdIssue4Key

        -   Created By

\[Bild: Beispielhafte Darstellung der Bestätigungsansicht unter dem
Formular\]

## **Folie 10: Zusammenfassung & Nächste Schritte**

**Testen und Verfeinern**

1.  **Testen (ohne Issues):** Funktioniert die Epic-Erstellung? Wird die

    > Bestätigung angezeigt?

2.  **Testen (mit Issues):** Werden ausgewählte Issues erstellt, korrekt

    > verknüpft und haben die richtigen Checklisten?

3.  **Fehlersuche:** Überprüfe Feldnamen, Bedingungen, Jira-Verbindung

    > und Berechtigungen bei Problemen.

**Benötigte Infos zum Fertigstellen:**

-   Genaue Checklisten-Texte

-   Jira Prioritäten, Projektschlüssel, Vorgangstypen

**Mögliche Verfeinerungen:**

-   Dynamische Dropdowns für Projekte/Prioritäten (evtl. Adminhilfe

    > nötig)

-   Bessere Fehlerbehandlung / Feedback

-   Klickbare Jira-Links in der Bestätigung

\[Bild: Checkliste oder Fragezeichen-Symbol\]
