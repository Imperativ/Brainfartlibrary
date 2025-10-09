Absolut! Gerne führe ich die einzelnen Schritte zur Erstellung des
ConfiForms Makros detaillierter aus, unter Berücksichtigung der neuen
Quellen und unserer bisherigen Konversation.Schritt 1: Erstellung der
Confluence-Seite und des Formular-Grundgerüsts

•

Erstellen Sie zunächst eine neue leere Seite in Ihrem Confluence-Bereich

.

•

Fügen Sie auf dieser Seite das Makro ConfiForms Form ein

. Dieses Makro dient als Hauptcontainer für alle Ihre Formularfelder und
die gesamte Logik, die Sie definieren werden. Alle weiteren
ConfiForms-Makros für dieses Formular müssen innerhalb dieses ConfiForms
Form Makros platziert werden.Schritt 2: Definition der Formularfelder
(innerhalb des ConfiForms Form Makros)Für jedes Feld, das Ihr Formular
enthalten soll, benötigen Sie zwei Makros: .

•

ConfiForms Field Definition: Dieses Makro definiert die Eigenschaften
des Feldes, wie den internen Namen, den Typ des Eingabefelds (z.B. Text,
Dropdown, Checkbox) und die Beschriftung, die dem Benutzer angezeigt
wird

.

•

ConfiForms Field: Dieses Makro zeigt das definierte Feld tatsächlich im
Formular für den Benutzer an

.Hier ist eine detaillierte Auflistung der benötigten Felder und ihrer
Konfigurationen (jeweils als Paar von

•

Epic Name:

◦

ConfiForms Field Definition:

▪

Name: epicName

▪

Type: Text

(ein einfaches Textfeld für den Namen des Epics)

▪

Label: Epic Name

▪

Erforderlich: Ja (optional, aber empfehlenswert)

◦

ConfiForms Field:

▪

Field name: epicName

▪

(Weitere Optionen sind optional)

•

Epic Beschreibung:

◦

ConfiForms Field Definition:

▪

Name: epicDescription

▪

Type: Textarea

(ein größeres Textfeld für die Beschreibung)

▪

Label: Epic Beschreibung

▪

Erforderlich: Ja (optional, aber empfehlenswert)

◦

ConfiForms Field:

▪

Field name: epicDescription

▪

(Weitere Optionen sind optional)

•

Priorität:

◦

ConfiForms Field Definition:

▪

Name: priority

▪

Type: Dropdown

(Select) (eine Auswahlliste)

▪

Label: Priorität

▪

Optionen: Sehr Hoch|Hoch|Mittel|Niedrig|Sehr Niedrig (entsprechend Ihrer
Angabe

)

▪

Erforderlich: Ja (optional, aber empfehlenswert)

◦

ConfiForms Field:

▪

Field name: priority

▪

(Weitere Optionen sind optional)

•

Zugewiesen an:

◦

ConfiForms Field Definition:

▪

Name: assignee

▪

Type: User Picker - Jira User

(User Picker) (ermöglicht die Auswahl eines Jira-Benutzers)

▪

Label: Zugewiesen an

▪

Erforderlich: Ja (optional, aber empfehlenswert)

◦

ConfiForms Field:

▪

Field name: assignee

▪

(Weitere Optionen sind optional)

•

Fällig am:

◦

ConfiForms Field Definition:

▪

Name: dueDate

▪

Type: Date

(ein Kalender zur Auswahl eines Datums)

▪

Label: Fällig am

▪

Erforderlich: Ja (optional, aber empfehlenswert)

◦

ConfiForms Field:

▪

Field name: dueDate

▪

(Weitere Optionen sind optional)

•

Zugehöriges Jira-Projekt:

◦

ConfiForms Field Definition:

▪

Name: projectKey

(jiraProject)

▪

Type: Text

(Select) (entweder ein Textfeld, in das der Jira-Projektschlüssel
eingegeben wird, oder optional ein Dropdown-Menü, falls Sie die
möglichen Projektschlüssel statisch hinterlegen möchten). Da Sie keine
Adminrechte haben, ist ein Textfeld flexibler.

▪

Label: Jira Projekt Key

(Jira-Projekt)

▪

Erforderlich: Ja (optional, aber empfehlenswert)

◦

ConfiForms Field:

▪

Field name: projectKey

▪

(Weitere Optionen sind optional)

•

(Optional) Jira Key (falls bereits vergeben):

◦

ConfiForms Field Definition:

▪

Name: existingJiraKey

(jiraKey)

▪

Type: Text

▪

Label: Jira-Key (falls bereits vergeben)

▪

Erforderlich: Nein

◦

ConfiForms Field:

▪

Field name: existingJiraKey

▪

(Weitere Optionen sind optional)

•

Checkboxes für die Issues:

◦

Für jede der vier Issues (Issue 1 bis 4) benötigen Sie ebenfalls ein
ConfiForms Field Definition und ein ConfiForms Field Makro:

▪

Issue 1 erstellen:

•

ConfiForms Field Definition: Name: createIssue1, Type: Checkbox, Label:
Issue 1 erstellen?

•

ConfiForms Field: Field name: createIssue1

▪

Issue 2 erstellen:

•

ConfiForms Field Definition: Name: createIssue2, Type: Checkbox, Label:
Issue 2 erstellen?

•

ConfiForms Field: Field name: createIssue2

▪

Issue 3 erstellen:

•

ConfiForms Field Definition: Name: createIssue3, Type: Checkbox, Label:
Issue 3 erstellen?

•

ConfiForms Field: Field name: createIssue3

▪

Issue 4 erstellen:

•

ConfiForms Field Definition: Name: createIssue4, Type: Checkbox, Label:
Issue 4 erstellen?

•

ConfiForms Field: Field name: createIssue4

•

Versteckte Felder zum Speichern der erstellten Jira-Keys:

◦

Für das Epic und jede der vier optionalen Issues benötigen Sie
zusätzlich ConfiForms Field Definition Makros, die nicht im Formular
angezeigt werden müssen (also kein entsprechendes ConfiForms Field
Makro):

▪

ConfiForms Field Definition: Name: createdEpicKey, Type: Text

▪

ConfiForms Field Definition: Name: createdIssue1Key, Type: Text

▪

ConfiForms Field Definition: Name: createdIssue2Key, Type: Text

▪

ConfiForms Field Definition: Name: createdIssue3Key, Type: Text

▪

ConfiForms Field Definition: Name: createdIssue4Key, Type: Text

Diese Felder dienen dazu, die von Jira zurückgelieferten Keys der
erstellten Vorgänge zu speichern, um sie später für die Verknüpfung und
die Bestätigungsanzeige zu verwenden.Schritt 3: Konfiguration der
IFTTT-Regeln für die Jira-Erstellung (innerhalb des ConfiForms Form
Makros)Unterhalb Ihrer Felddefinitionen, aber immer noch innerhalb des .
In diesem Makro definieren Sie die Aktionen, die beim Absenden des
Formulars ausgelöst werden sollen.

•

Aktion 1: Epic erstellen (immer ausführen):

◦

Klicken Sie im ConfiForms IFTTT Integration Rules Makro auf "Add Action"

.

◦

Type: Wählen Sie Create Jira Issue

.

◦

Jira Connection: Wählen Sie JIRA aus Ihrer Liste (entsprechend Ihrer
Angabe

).

◦

Project: Wählen Sie Field reference und geben Sie projectKey ein (oder
verwenden Sie die Notation \[entry.projectKey\])

. Dies liest den im Formular eingegebenen Jira-Projektschlüssel aus. Ihr
spezifischer Projektschlüssel ist JIRAPROJ24.

◦

Issue Type: Geben Sie den exakten Namen für Epics in Ihrem Jira ein.
Dies ist üblicherweise Epic

.

◦

Summary: Wählen Sie Field reference und geben Sie epicName ein (oder
\[entry.epicName\])

.

◦

Description: Wählen Sie Formula / Value reference

. Hier müssen Sie die Beschreibung aus dem Formularfeld und den Inhalt
Ihrer Epic-Checkliste kombinieren. Verwenden Sie die Notation
\[entry.epicDescription\] für den Feldinhalt. Fügen Sie dann den Inhalt
der Datei checkliste produkt (die Sie in den Quellen finden) direkt als
formatierten Text hinzu. Achten Sie auf die korrekte Formatierung für
Checklisten in Jira (üblicherweise mit

◦

Priority: Wählen Sie Field reference und geben Sie priority ein (oder
\[entry.priority\])

. ConfiForms sollte die deutsche Übersetzung ("Sehr Hoch", "Hoch",
"Mittel", "Niedrig", "Sehr Niedrig") korrekt an Jira übergeben.

◦

Assignee: Wählen Sie Field reference und geben Sie assignee ein (oder
\[entry.assignee\])

. Die Logik, dass bei einem leeren Feld der Autor gesetzt wird, muss
später in einer weiteren IFTTT-Regel oder möglicherweise durch
Jira-Standardverhalten abgedeckt werden, da die "Create Jira Issue"
Aktion selbst diese Bedingung nicht direkt unterstützt. Für den ersten
Prototypen stellen Sie sicher, dass Sie im Feld "Zugewiesen an" einen
Benutzer auswählen.

◦

Due Date: Wählen Sie Field reference und geben Sie dueDate ein (oder
\[entry.dueDate\])

.

◦

Epic Name (Jira Feld): Suchen Sie in der Liste der zusätzlichen
Jira-Felder nach epicLink (entsprechend Ihrer Angabe

). Wählen Sie dieses Feld aus und mappen Sie es auf \[entry.epicName\].

◦

Store result info: Wählen Sie Issue Key und geben Sie createdEpicKey als
Feldnamen ein

.

•

Aktion 2: Issue 1 erstellen (bedingt ausführen):

◦

Klicken Sie auf "Add Action".

◦

Type: Wählen Sie Create Jira Issue.

◦

Condition: Geben Sie \[entry.createIssue1\] == true ein

. Diese Aktion wird nur ausgeführt, wenn die Checkbox "Issue 1
erstellen?" aktiviert ist.

◦

Jira Connection: Wählen Sie JIRA.

◦

Project: Wählen Sie Field reference und geben Sie projectKey ein (oder
\[entry.projectKey\]).

◦

Issue Type: Geben Sie den Namen für Ihre Standard-Issues/Unteraufgaben
in Jira ein (z.B. Task, Sub-task, Aufgabe).

◦

Summary: Setzen Sie einen aussagekräftigen Namen, z.B. Issue 1 für
\[entry.epicName\]

.

◦

Description: Wählen Sie Formula / Value reference und fügen Sie den
Inhalt der Datei checkliste dev (siehe Quellen

) als formatierten Text ein. Beispiel:

◦

Epic Link: Suchen Sie das Feld epicLink und wählen Sie Field reference.
Geben Sie createdEpicKey ein (oder \[entry.createdEpicKey\])

.

◦

(Optionale Felder): Sie können hier auch Felder wie "Assignee",
"Priority" und "Due Date" setzen, entweder basierend auf den
Formularfeldern oder mit festen Werten.

◦

Store result info: Wählen Sie Issue Key und geben Sie createdIssue1Key
ein

.

•

Aktionen 3, 4 und 5: Issues 2, 3 und 4 erstellen (bedingt ausführen):

◦

Wiederholen Sie die Schritte für Aktion 2 für die Issues 2, 3 und 4

.

◦

Passen Sie die Condition entsprechend an: \[entry.createIssue2\] ==
true, \[entry.createIssue3\] == true, \[entry.createIssue4\] == true.

◦

Ändern Sie die Summary: Issue 2 für \[entry.epicName\], etc.

◦

Fügen Sie die korrekten Checklisten-Texte in die Description ein:

▪

Issue 2: Inhalt aus checkliste schulung

▪

Issue 3: Inhalt aus checkliste QS

▪

Issue 4: Inhalt aus checkliste prod

◦

Stellen Sie sicher, dass das Feld epicLink immer auf
\[entry.createdEpicKey\] verweist.

◦

Speichern Sie die Ergebnis-Keys in den entsprechenden Feldern:
createdIssue2Key, createdIssue3Key, createdIssue4Key.

Schritt 4: Hinzufügen des Absenden-Buttons (innerhalb des ConfiForms
Form Makros)Am Ende Ihres Formulars, innerhalb des . Dieses Makro
erzeugt den "Speichern" oder "Senden"-Button, den der Benutzer zum
Abschicken des Formulars verwendet.Schritt 5: Einrichten der
Bestätigungsanzeige (außerhalb des ConfiForms Form Makros)Unterhalb
(außerhalb) des . Eine

•

Form: Wählen Sie das Formular aus, das Sie in Schritt 1 erstellt haben

.

•

Filter: Um nur den Eintrag anzuzeigen, der gerade erstellt wurde, können
Sie folgende Filter konfigurieren

:

◦

Created By: \_currentUser (zeigt nur Einträge des aktuellen Benutzers)

◦

Sortieren nach: Created Date DESC (neueste Einträge zuerst)

◦

Limit results: 1 (zeigt nur den obersten, also neuesten Eintrag)

•

Angezeigte Felder: Fügen Sie die folgenden Felder hinzu, um die
gewünschte Bestätigung anzuzeigen

:

◦

createdEpicKey

◦

epicName

◦

createdIssue1Key

◦

createdIssue2Key

◦

createdIssue3Key

◦

createdIssue4Key

◦

Created By (zeigt den Ersteller des Formulareintrags)

•

Diese Felder werden nur dann einen Wert anzeigen, wenn die
entsprechenden Jira-Tickets erfolgreich erstellt wurden.

Da Sie für den ersten Prototyp primär eine Information über die
erfolgreiche Erstellung wünschen, ist diese einfache Anzeige der
gespeicherten Jira-Keys ausreichend.Mit diesen detaillierten Schritten
sollten Sie in der Lage sein, den ersten lauffähigen Prototypen zu
erstellen, der ein Epic mit den angegebenen Informationen in Ihrem
Jira-Projekt
