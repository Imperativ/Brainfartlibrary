Okay, ich verstehe die Aufgabe. Du möchtest einen Prozess in Confluence
mit ConfiForms abbilden, der bei der Eingabe in ein Formular automatisch
ein Epic und optional bis zu vier verknüpfte Issues (Unteraufgaben) in
Jira erstellt, inklusive spezifischer Checklisten in den Beschreibungen.
Das Ganze soll ohne Adminrechte und Storage Format Editor umgesetzt
werden, nur mit den Bordmitteln von ConfiForms in deiner Server-Umgebung
(Confluence 8.5 / Jira 9.12).

Hier ist ein detaillierter Plan, wie du diesen Prototypen Schritt für
Schritt aufbauen kannst.

**Voraussetzungen:**

1.  **ConfiForms App:** Muss auf Confluence installiert und lizenziert

    > sein.

2.  **Jira Application Link:** Eine funktionierende

    > Anwendungs-Verknüpfung (Application Link) zwischen Confluence und
    > Jira muss bestehen und für ConfiForms konfiguriert sein (das
    > erledigt normalerweise ein Admin, aber es muss vorhanden sein).

3.  **Berechtigungen:** Der Benutzer, der das Formular abschickt,

    > benötigt die Berechtigung, in dem ausgewählten Jira-Projekt Epics
    > und Issues zu erstellen.

4.  **Checklisten-Texte:** Du musst die genauen Texte der fünf

    > Checklisten (1 für das Epic, 4 unterschiedliche für die Issues)
    > parat haben. Wir fügen sie direkt in die Konfiguration ein.

5.  **Jira Projekt-Schlüssel:** Du benötigst den Schlüssel des

    > Jira-Projekts (z.B. "PROJ"), in dem die Vorgänge erstellt werden
    > sollen.

6.  **Jira Prioritäts-IDs/Namen:** Du benötigst die Namen oder IDs der

    > Prioritäten, die in Jira verwendet werden sollen.

7.  **Jira Vorgangstypen:** Du musst wissen, wie der Vorgangstyp für das

    > Epic ("Epic") und die Unteraufgaben (z.B. "Task", "Sub-task",
    > "Unteraufgabe") in deinem Jira heißen.

**Schritt 1: Confluence-Seite erstellen und Formular-Grundgerüst
anlegen**

1.  Erstelle eine neue Seite in Confluence.

2.  Füge das Makro ConfiForms Form hinzu. Dieses Makro ist der Container

    > für dein gesamtes Formular und die Logik.

**Schritt 2: Formularfelder definieren (Innerhalb des ConfiForms Form
Makros)**

Füge für jedes benötigte Feld ein ConfiForms Field Definition Makro und
direkt darunter das zugehörige ConfiForms Field Makro ein:

1.  **Epic Name:**

    -   ConfiForms Field Definition: Name = epicName, Typ = Text, Label

        > = Epic Name

    -   ConfiForms Field: Name = epicName (Optional: als Pflichtfeld

        > markieren)

2.  **Epic Beschreibung:**

    -   ConfiForms Field Definition: Name = epicDescription, Typ =

        > Textarea, Label = Epic Beschreibung

    -   ConfiForms Field: Name = epicDescription

3.  **Priorität:**

    -   ConfiForms Field Definition: Name = priority, Typ = Dropdown,

        > Label = Priorität

        -   *Optionen:* Füge hier die Jira-Prioritäten als Optionen

            > hinzu (z.B. Highest, High, Medium, Low). Du brauchst den
            > genauen Namen oder die ID, die Jira erwartet. Wenn du die
            > ID nicht kennst, versuche es erstmal mit dem Namen.

    -   ConfiForms Field: Name = priority (Optional: Standardwert

        > setzen)

4.  **Zugewiesen an:**

    -   ConfiForms Field Definition: Name = assignee, Typ = User

        > Picker - Jira User, Label = Zugewiesen an

    -   ConfiForms Field: Name = assignee

5.  **Fällig am:**

    -   ConfiForms Field Definition: Name = dueDate, Typ = Date, Label =

        > Fällig am

    -   ConfiForms Field: Name = dueDate

6.  **Zugehöriges Jira-Projekt:**

    -   ConfiForms Field Definition: Name = projectKey, Typ = Text (oder

        > Dropdown, wenn du die Keys kennst), Label = Jira Projekt Key

    -   ConfiForms Field: Name = projectKey (Wichtig: Hier muss der User

        > den korrekten Key eintragen, z.B. "PROJ")

7.  **(Optional) Jira Key (falls bereits bekannt):**

    -   ConfiForms Field Definition: Name = existingJiraKey, Typ = Text,

        > Label = Jira Key (falls vorhanden)

    -   ConfiForms Field: Name = existingJiraKey

    -   *Hinweis:* Dieses Feld wird für die *Erstellung* nicht direkt

        > benötigt, aber du hast es erwähnt. Wir lassen es erstmal drin,
        > nutzen es aber in der Logik noch nicht.

8.  **Checkboxes für Sub-Tasks:**

    -   ConfiForms Field Definition: Name = createIssue1, Typ =

        > Checkbox, Label = Issue 1 erstellen?

    -   ConfiForms Field: Name = createIssue1

    -   Wiederhole dies für createIssue2, createIssue3, createIssue4.

9.  \*\*Versteckte Felder zum Speichern der erstellten Keys (Wichtig für

    > Verknüpfung und Anzeige):\*\*

    -   ConfiForms Field Definition: Name = createdEpicKey, Typ = Text,

        > Label = Erstellter Epic Key (Dieses Feld muss nicht angezeigt
        > werden, kann also ohne ConfiForms Field auskommen oder später
        > ausgeblendet werden).

    -   Wiederhole dies für createdIssue1Key, createdIssue2Key,

        > createdIssue3Key, createdIssue4Key.

**Schritt 3: IFTTT-Regeln für die Jira-Erstellung definieren (Innerhalb
des ConfiForms Form Makros)**

Füge *unterhalb* der Felddefinitionen, aber *innerhalb* des ConfiForms
Form Makros, ein ConfiForms IFTTT Integration Rules Makro ein. Innerhalb
dieses Makros definierst du die Aktionen:

1.  **Aktion 1: Epic erstellen (Immer ausführen)**

    -   Klicke auf "Add Action".

    -   Wähle den Typ: Create Jira Issue.

    -   **Jira Connection:** Wähle die konfigurierte Application Link

        > Verbindung zu eurem Jira Server aus.

    -   **Project:** Wähle "Field reference" und gib projectKey ein

        > (oder \[entry.projectKey\]).

    -   **Issue Type:** Gib den exakten Namen für Epics in eurem Jira

        > ein (oft einfach Epic).

    -   **Summary:** Wähle "Field reference" und gib epicName ein (oder

        > \[entry.epicName\]).

    -   **Description:** Wähle "Formula / Value reference". Gib hier

        > eine Kombination aus dem Feldinhalt und dem Checklisten-Text
        > ein. Beispiel:  
        > \[entry.epicDescription\]
        >
        > --- Checklist Epic ---  
        > \* \[ \] Schritt 1  
        > \* \[ \] Schritt 2  
        > \* ... (füge hier deine komplette Epic-Checkliste ein)

    -   **Priority:** Wähle "Field reference" und gib priority ein (oder

        > \[entry.priority\]).

    -   **Assignee:** Wähle "Field reference" und gib assignee ein (oder

        > \[entry.assignee\]).

    -   **Due Date:** Wähle "Field reference" und gib dueDate ein (oder

        > \[entry.dueDate\]).

    -   **Epic Name (Jira Custom Field):** Jira Epics haben oft ein

        > separates Feld namens "Epic Name". Suche dieses Feld in der
        > Liste der zusätzlichen Felder und mappe es ebenfalls auf
        > epicName (\[entry.epicName\]). Wenn du das Feld nicht findest,
        > ist es vielleicht nicht zwingend nötig oder heißt anders.

    -   **Store result info:** Wähle "Issue Key" und gib als Feldnamen

        > createdEpicKey ein. Das speichert den Key des erstellten Epics
        > in unserem versteckten Feld.

2.  **Aktion 2: Issue 1 erstellen (Bedingt ausführen)**

    -   Klicke auf "Add Action".

    -   Wähle den Typ: Create Jira Issue.

    -   **Condition:** Gib hier die Bedingung ein, dass die Checkbox

        > aktiviert sein muss. Die genaue Syntax hängt davon ab, was
        > ConfiForms für eine aktivierte Checkbox speichert (oft true
        > oder on). Versuche es mit: \[entry.createIssue1\] = true

    -   **Jira Connection:** Wähle dieselbe Verbindung wie oben.

    -   **Project:** \[entry.projectKey\]

    -   **Issue Type:** Gib den Namen für eure Unteraufgaben ein (z.B.

        > Task oder Sub-task).

    -   **Summary:** Setze einen sinnvollen Namen, z.B. Issue 1 für

        > \[entry.epicName\].

    -   **Description:** Gib hier den Text für die *erste* spezifische

        > Checkliste ein:  
        > --- Checklist Issue 1 ---  
        > \* \[ \] Aufgabe 1.1  
        > \* \[ \] Aufgabe 1.2  
        > \* ... (füge hier deine komplette Checkliste für Issue 1 ein)

    -   **Epic Link:** Suche das Feld "Epic Link" (oder ähnlich) in den

        > zusätzlichen Feldern. Wähle "Field reference" und gib
        > createdEpicKey ein (oder \[entry.createdEpicKey\]). *Das ist
        > entscheidend für die Verknüpfung!*

    -   *(Optional)* Setze Assignee, Priority, Due Date analog zum Epic

        > oder lasse sie weg.

    -   **Store result info:** Wähle "Issue Key" und gib

        > createdIssue1Key ein.

3.  **Aktionen 3, 4, 5: Issues 2, 3, 4 erstellen (Bedingt ausführen)**

    -   Wiederhole die Schritte für Aktion 2 für die Issues 2, 3 und 4.

    -   Passe jeweils die **Condition** an (\[entry.createIssue2\] =

        > true, \[entry.createIssue3\] = true, \[entry.createIssue4\] =
        > true).

    -   Passe die **Summary** an (Issue 2 für \[entry.epicName\], etc.).

    -   Füge die **unterschiedlichen Checklisten-Texte** in die

        > **Description** ein.

    -   Verknüpfe jede Issue über das **Epic Link** Feld mit

        > \[entry.createdEpicKey\].

    -   Speichere den jeweiligen Key in **Store result info**

        > (createdIssue2Key, createdIssue3Key, createdIssue4Key).

**Schritt 4: Absende-Button hinzufügen (Innerhalb des ConfiForms Form
Makros)**

-   Füge am Ende des Formulars (innerhalb des ConfiForms Form Makros)

    > das ConfiForms Registration Control Makro hinzu. Dies stellt den
    > "Speichern" oder "Senden"-Button bereit.

**Schritt 5: Bestätigungsanzeige einrichten (Außerhalb des ConfiForms
Form Makros)**

-   Füge *unterhalb* des ConfiForms Form Makros ein ConfiForms Table

    > View oder ConfiForms Records View Makro ein. Eine Records View ist
    > vielleicht besser, um nur den letzten Eintrag anzuzeigen.

-   **Konfiguriere die Ansicht:**

    -   Wähle die Form aus, die du oben erstellt hast.

    -   **Filterung (Wichtig):** Du willst wahrscheinlich nur den

        > Eintrag sehen, den du gerade erstellt hast. Eine einfache
        > Möglichkeit ist, nach dem Ersteller zu filtern: Created By =
        > \_currentUser. Sortiere absteigend nach Erstellungsdatum
        > (Created Date DESC) und begrenze die Anzeige auf 1 Eintrag
        > (Limit results = 1), um nur den neuesten Eintrag des aktuellen
        > Benutzers zu sehen.

    -   **Angezeigte Felder:** Füge die Felder hinzu, die du sehen

        > möchtest:

        -   createdEpicKey (Zeigt den Key des Epics)

        -   epicName (Zeigt den Namen des Epics)

        -   createdIssue1Key (Wird nur angezeigt, wenn ein Wert

            > drinsteht)

        -   createdIssue2Key

        -   createdIssue3Key

        -   createdIssue4Key

        -   Created By (ConfiForms Systemfeld, um den Ersteller

            > anzuzeigen)

    -   *(Optional)* Du könntest versuchen, die Keys klickbar zu machen,

        > indem du ein "Formula"-Feld in der Ansicht hinzufügst und den
        > Link zu Jira konstruierst (z.B.
        > concat('https://euer.jira.server/browse/',
        > \[entry.createdEpicKey\])), aber das Anzeigen des Keys erfüllt
        > erstmal die Anforderung.

**Zusammenfassung und Test:**

1.  Speichere die Confluence-Seite.

2.  Fülle das Formular mit Testdaten aus.

3.  Wähle zunächst *keine* der Checkboxen für die Issues aus und klicke

    > auf "Speichern".

4.  Überprüfe:

    -   Wird das Epic in Jira korrekt erstellt (Projekt, Typ, Name,

        > Beschreibung inkl. Checkliste, Prio, Zugewiesener,
        > Fälligkeit)?

    -   Wird in der Bestätigungsansicht unter dem Formular der Key und

        > Name des Epics sowie dein Name als Ersteller angezeigt?

5.  Bearbeite den Eintrag (wenn ConfiForms das erlaubt) oder erstelle

    > einen neuen Eintrag.

6.  Wähle diesmal eine oder mehrere Checkboxen für die Issues aus.

7.  Überprüfe:

    -   Wird das Epic wieder korrekt erstellt?

    -   Werden die ausgewählten Issues in Jira erstellt?

    -   Sind die Issues korrekt mit dem Epic verknüpft (über den "Epic

        > Link")?

    -   Enthalten die Issues die *korrekten, unterschiedlichen*

        > Checklisten in ihrer Beschreibung?

    -   Zeigt die Bestätigungsansicht jetzt auch die Keys der erstellten

        > Issues an?

**Benötigst du weitere Informationen?**

Für diesen Prototypen sind die von dir gegebenen Informationen
ausreichend, um die Struktur zu erstellen. Was ich zur *konkreten*
Umsetzung bräuchte (was du aber selbst einfügen musst):

1.  **Genaue Texte der 5 Checklisten.**

2.  **Genaue Namen/IDs der Jira-Prioritäten.**

3.  **Genaue Namen der Jira-Vorgangstypen** für "Epic" und die

    > Unteraufgaben (z.B. "Task", "Sub-task").

4.  **Den/die relevanten Jira Projekt-Schlüssel.**

5.  \*\*Den Namen des Jira Custom Fields für "Epic Link" und ggf. "Epic

    > Name"\*\*, falls sie nicht Standard sind (kannst du in Jira
    > nachsehen oder im IFTTT-Makro in der Feldliste suchen).

6.  **Die Basis-URL eures Jira-Servers**, falls du später klickbare

    > Links in der Bestätigung bauen willst.

Dieser Plan sollte dir helfen, einen ersten funktionierenden Prototypen
zu erstellen, der die Kernanforderungen abdeckt. Viel Erfolg!
