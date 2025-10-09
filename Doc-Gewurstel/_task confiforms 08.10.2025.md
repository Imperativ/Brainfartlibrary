\# You are an expert in creating Confluence and Jira macros and
interactive forms using the Confiforms plugin

(\[confiforms.com\](https://confiforms.com)).

First, familiarize yourself with the \*\*basic concepts\*\* at

\[https://wiki.vertuna.com/spaces/CONFIFORMS/pages/1212419/Basic+concepts\](https://wiki.vertuna.com/spaces/CONFIFORMS/pages/1212419/Basic+concepts)

and all necessary information to assist me with the following task.

You can find everything you need either at
\[confiforms.com\](https://confiforms.com/),

or on one of these pages:

\*
\[https://wiki.vertuna.com/spaces/CONFIFORMS/pages/557099/Tutorials\](https://wiki.vertuna.com/spaces/CONFIFORMS/pages/557099/Tutorials)

\*
\[https://wiki.vertuna.com/spaces/CONFIFORMS/pages/1212529/Cookbook\](https://wiki.vertuna.com/spaces/CONFIFORMS/pages/1212529/Cookbook)

\*
\[https://wiki.vertuna.com/spaces/CONFIFORMS/pages/1212428/Documentation\](https://wiki.vertuna.com/spaces/CONFIFORMS/pages/1212428/Documentation)

Also make sure to check the official Atlassian social media channels and
community forums.

------------------------------------------------------------------------

\## Task: Confiforms Macro for Automated Jira Epic Creation

\### Goal

Develop a Confiforms macro for Confluence that allows users to create an
\*\*Epic\*\* ticket via a button.

In the first step, the user is prompted to enter a name for the ticket.

In the next step, the user must fill out the form fields listed below
(if required fields),

or leave the pre-filled information as is and save.

After clicking “Okay,” an Epic should automatically be created in the
Jira project \*\*BWPTLS24\*\* with the corresponding name.

If an error occurs during creation, the user must be clearly informed in
real time.

Upon successful creation, the user should see the resulted ticket as a
link to Jira.

Both the \*\*ticket name\*\* and the \*\*assigned ticket number\*\*
should appear as clickable links to the corresponding Jira Epic page.

------------------------------------------------------------------------

\### Requirements

1\. \*\*Authentication\*\*

\* The Jira API is accessed via an API token. The user can provide a API
Key Token for the Jira and Confluence environment. Just ask, when you
reach the step.

2\. \*\*Fields\*\*

The Epic ticket should include the following fields, in the exact order
and specifications shown below.

The list is presented as a pseudo-formatted JSON structure:

\`\`\`json

{

"fields": {

"project": { "key": "BWPTLS24" },

"issuetype": { "name": "Epic" },

"summary": "Zusammenfassung \[entry.field\_name\]",

"customfield\_10103": "Epic Name \[entry.field\_name\]",

"customfield\_10403": { "id": "Anforderungskategorie
\[entry.field\_name\]" },

"components": \[{ "name": "Component/s \[entry.field\_name\]" }\],

"priority": { "name": "Priorität \[entry.field\_name\]" },

"duedate": "\[entry.\_now.jiraDate\]",

"customfield\_10524": "\[entry.\_now.jiraDate\]",

"assignee": { "name": "\[entry.\_user\]" },

"customfield\_12500": { "name": "Co-Bearbeiter/-in (Mehrfachauswahl)
\[entry.field\_name\]" },

"description": "Beschreibung \[entry.field\_name\]",

"fixVersions": \[{ "name": "Lösungsversion \[entry.field\_name\]" }\]

}

}

\`\`\`

\#### Additional Field Details:

\* \*\*project\*\*: Label “Projekt”; required field; always pre-filled
with “BWPTLS24”.

\* \*\*issuetype\*\*: Label “Typ”; required field; always pre-filled
with “Epic”.

\* \*\*summary\*\*: Label “Zusammenfassung”; required field.

→ Final value should be the string “Einführung von ” + user input.

\* \*\*customfield\_10103\*\*: Label “Epic Name”; required field; must
mirror the \*Summary\* field input.

\* \*\*customfield\_10403\*\*: Label “Anforderungskategorie”; dropdown
with 4 options. List ist provided in Jiraprojekt.

\* \*\*components\*\*: Label “Komponenten”; multi-select list of Jira
components available for the project.

\* \*\*priority\*\*: Label “Priorität”; dropdown list of Jira priorities
(Sehr niedrig, Niedrig, Mittel, Hoch, Sehr Hoch).

\* \*\*duedate\*\*: Hidden for now; automatically filled with the ticket
creation date.

\* \*\*customfield\_10524\*\*: Hidden for now; automatically filled with
the ticket creation date.

\* \*\*assignee\*\*: Label “Bearbeiter”; if left blank, the Epic creator
is automatically assigned.

\* \*\*customfield\_12500\*\*: Label “Co-Bearbeiter”; allows
multi-select of Jira users to assign as collaborators.

\* \*\*description\*\*: Label “Beschreibung”; text area for free input.

\* \*\*fixVersions\*\*: Label “Lösungsversion”; multi-select list from
existing Jira fix versions in the project.

3\. \*\*Project\*\*

\* The Epic is always created in the Jira project with key
\*\*BEPTLS24\*\*.

4\. \*\*Permissions\*\*

\* All users who use the macro have the necessary rights to create an
Epic in the project.

Authentication uses their individual credentials.

5\. \*\*Error Handling\*\*

\* Any creation errors (e.g., insufficient permissions, invalid name,
network issue) must be shown clearly on the Confluence page.

6\. \*\*Return Output\*\*

\* After successful creation, display a link to the new Epic.

The link text should include both the Jira ticket number and the given
name.

7\. \*\*Page Refresh\*\*

\* After successful creation, the page should automatically refresh to
show the new status.

------------------------------------------------------------------------

\### Technical Notes

\* Confluence \*\*version 9.2.4\*\* and Jira \*\*version 10.3.6\*\* are
used, along with Confiforms \*\*version 3.17.7\*\* by Vertuna.com.

\* Use \*\*only\*\* elements available through Confiforms’ graphical
interface, (e.g., “Confiforms Field Definition”, “Confiforms IFTTT
Integration Rules”, etc.) or a grafical GUI element provided by
confluence.

\* For “Confiforms IFTTT Integration Rules,” show any code for field
mapping or JSON payloads in \*\*cleanly formatted JSON\*\*.

\* You do \*\*not\*\* have admin rights and \*\*cannot\*\* access the
integrated \*Storage Format Editor\* in Confiforms.

\* User inputs for required fields must be validated (e.g., no empty
entries, no special characters, length 5–255 characters).

\* Only \*\*Data Center versions\*\* of Jira and Confluence are used.

\* The implementation should prioritize \*\*maximum
user-friendliness\*\* and \*\*fault tolerance\*\*.
