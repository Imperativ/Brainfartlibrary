#!/usr/bin/env python3
"""
Jira REST API Test Script für Epic-Erstellung
Testet die JSON-Struktur und API-Integration für das Confiforms-Makro
"""

import requests
import json
import base64
from datetime import datetime

class JiraEpicTester:
    def __init__(self, jira_url, username, api_token):
        """
        Initialisiert den Jira Epic Tester
        
        Args:
            jira_url (str): Base URL der Jira-Instanz (z.B. https://company.atlassian.net)
            username (str): Jira-Benutzername
            api_token (str): Jira API Token
        """
        self.jira_url = jira_url.rstrip('/')
        self.username = username
        self.api_token = api_token
        self.auth_header = self._create_auth_header()
        
    def _create_auth_header(self):
        """Erstellt den Authorization Header für Basic Auth"""
        credentials = f"{self.username}:{self.api_token}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return f"Basic {encoded_credentials}"
    
    def test_connection(self):
        """Testet die Verbindung zur Jira-Instanz"""
        url = f"{self.jira_url}/rest/api/3/myself"
        headers = {
            "Authorization": self.auth_header,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                user_info = response.json()
                print(f"✅ Verbindung erfolgreich! Angemeldet als: {user_info.get('displayName')}")
                return True
            else:
                print(f"❌ Verbindungsfehler: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Verbindungsfehler: {str(e)}")
            return False
    
    def get_project_info(self, project_key):
        """Holt Informationen über das Projekt"""
        url = f"{self.jira_url}/rest/api/3/project/{project_key}"
        headers = {
            "Authorization": self.auth_header,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                project_info = response.json()
                print(f"✅ Projekt gefunden: {project_info.get('name')} ({project_key})")
                return project_info
            else:
                print(f"❌ Projekt nicht gefunden: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            print(f"❌ Fehler beim Abrufen der Projektinformationen: {str(e)}")
            return None
    
    def get_issue_types(self, project_key):
        """Holt verfügbare Issue Types für das Projekt"""
        url = f"{self.jira_url}/rest/api/3/issue/createmeta/{project_key}/issuetypes"
        headers = {
            "Authorization": self.auth_header,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                issue_types = response.json()
                print("✅ Verfügbare Issue Types:")
                for issue_type in issue_types.get('values', []):
                    print(f"   - {issue_type.get('name')} (ID: {issue_type.get('id')})")
                
                # Prüfe ob Epic verfügbar ist
                epic_type = next((it for it in issue_types.get('values', []) if it.get('name') == 'Epic'), None)
                if epic_type:
                    print(f"✅ Epic Issue Type gefunden (ID: {epic_type.get('id')})")
                    return epic_type
                else:
                    print("❌ Epic Issue Type nicht gefunden!")
                    return None
            else:
                print(f"❌ Fehler beim Abrufen der Issue Types: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            print(f"❌ Fehler beim Abrufen der Issue Types: {str(e)}")
            return None
    
    def get_epic_fields(self, project_key, issue_type_id):
        """Holt verfügbare Felder für Epic Issue Type"""
        url = f"{self.jira_url}/rest/api/3/issue/createmeta/{project_key}/issuetypes/{issue_type_id}"
        headers = {
            "Authorization": self.auth_header,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                fields_info = response.json()
                fields = fields_info.get('fields', {})
                print("✅ Verfügbare Felder für Epic:")
                
                # Wichtige Felder anzeigen
                important_fields = ['summary', 'description', 'project', 'issuetype']
                for field_key, field_info in fields.items():
                    field_name = field_info.get('name', 'Unbekannt')
                    required = field_info.get('required', False)
                    if field_key in important_fields or 'epic' in field_name.lower():
                        status = "✅ (Pflichtfeld)" if required else "⚪ (Optional)"
                        print(f"   {status} {field_key}: {field_name}")
                
                return fields
            else:
                print(f"❌ Fehler beim Abrufen der Epic-Felder: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            print(f"❌ Fehler beim Abrufen der Epic-Felder: {str(e)}")
            return None
    
    def create_test_epic(self, project_key, epic_name):
        """Erstellt ein Test-Epic mit der Confiforms JSON-Struktur"""
        url = f"{self.jira_url}/rest/api/3/issue"
        headers = {
            "Authorization": self.auth_header,
            "Content-Type": "application/json"
        }
        
        # JSON-Struktur wie im Confiforms-Makro
        payload = {
            "fields": {
                "project": {
                    "key": project_key
                },
                "summary": epic_name,
                "issuetype": {
                    "name": "Epic"
                }
            }
        }
        
        # Füge customfield_10103 hinzu, falls verfügbar
        # (In der Praxis sollte dies vorher validiert werden)
        # payload["fields"]["customfield_10103"] = epic_name
        
        print(f"🔄 Erstelle Test-Epic: {epic_name}")
        print(f"📤 JSON Payload: {json.dumps(payload, indent=2)}")
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 201:
                epic_info = response.json()
                epic_key = epic_info.get('key')
                epic_id = epic_info.get('id')
                epic_url = f"{self.jira_url}/browse/{epic_key}"
                
                print(f"✅ Epic erfolgreich erstellt!")
                print(f"   Epic Key: {epic_key}")
                print(f"   Epic ID: {epic_id}")
                print(f"   Epic URL: {epic_url}")
                
                return {
                    'key': epic_key,
                    'id': epic_id,
                    'url': epic_url,
                    'self': epic_info.get('self')
                }
            else:
                print(f"❌ Fehler beim Erstellen des Epics: {response.status_code}")
                print(f"   Response: {response.text}")
                return None
        except Exception as e:
            print(f"❌ Fehler beim Erstellen des Epics: {str(e)}")
            return None
    
    def delete_test_epic(self, epic_key):
        """Löscht ein Test-Epic (für Cleanup)"""
        url = f"{self.jira_url}/rest/api/3/issue/{epic_key}"
        headers = {
            "Authorization": self.auth_header,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.delete(url, headers=headers)
            if response.status_code == 204:
                print(f"✅ Test-Epic {epic_key} erfolgreich gelöscht")
                return True
            else:
                print(f"❌ Fehler beim Löschen des Test-Epics: {response.status_code} - {response.text}")
                return False
        except Exception as e:
            print(f"❌ Fehler beim Löschen des Test-Epics: {str(e)}")
            return False
    
    def run_full_test(self, project_key, test_epic_name=None):
        """Führt einen vollständigen Test durch"""
        if test_epic_name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_epic_name = f"TEST Epic - Confiforms Integration {timestamp}"
        
        print("=" * 60)
        print("🧪 JIRA REST API TEST FÜR CONFIFORMS EPIC-ERSTELLUNG")
        print("=" * 60)
        
        # 1. Verbindung testen
        print("\n1️⃣ Teste Verbindung zur Jira-Instanz...")
        if not self.test_connection():
            return False
        
        # 2. Projekt-Informationen abrufen
        print(f"\n2️⃣ Teste Projekt {project_key}...")
        project_info = self.get_project_info(project_key)
        if not project_info:
            return False
        
        # 3. Issue Types abrufen
        print(f"\n3️⃣ Teste verfügbare Issue Types...")
        epic_type = self.get_issue_types(project_key)
        if not epic_type:
            return False
        
        # 4. Epic-Felder abrufen
        print(f"\n4️⃣ Teste Epic-Felder...")
        epic_fields = self.get_epic_fields(project_key, epic_type.get('id'))
        if not epic_fields:
            return False
        
        # 5. Test-Epic erstellen
        print(f"\n5️⃣ Teste Epic-Erstellung...")
        epic_result = self.create_test_epic(project_key, test_epic_name)
        if not epic_result:
            return False
        
        # 6. Cleanup (optional)
        print(f"\n6️⃣ Cleanup...")
        cleanup = input("Soll das Test-Epic gelöscht werden? (j/n): ").lower().strip()
        if cleanup in ['j', 'ja', 'y', 'yes']:
            self.delete_test_epic(epic_result['key'])
        else:
            print(f"ℹ️ Test-Epic bleibt bestehen: {epic_result['url']}")
        
        print("\n" + "=" * 60)
        print("✅ TEST ERFOLGREICH ABGESCHLOSSEN!")
        print("🎯 Die Confiforms JSON-Struktur ist kompatibel mit Ihrer Jira-Instanz.")
        print("=" * 60)
        
        return True

def main():
    """Hauptfunktion für interaktive Nutzung"""
    print("🔧 JIRA REST API TESTER FÜR CONFIFORMS")
    print("=" * 50)
    
    # Konfiguration abfragen
    jira_url = input("Jira URL (z.B. https://company.atlassian.net): ").strip()
    username = input("Jira Benutzername: ").strip()
    api_token = input("Jira API Token: ").strip()
    project_key = input("Projekt Key (Standard: JIRAPRO24): ").strip() or "JIRAPRO24"
    
    # Tester initialisieren
    tester = JiraEpicTester(jira_url, username, api_token)
    
    # Test ausführen
    success = tester.run_full_test(project_key)
    
    if success:
        print("\n🎉 Ihr Confiforms-Makro sollte funktionieren!")
        print("📋 Nächste Schritte:")
        print("   1. Implementieren Sie das Confiforms-Makro in Confluence")
        print("   2. Konfigurieren Sie die Application Link zwischen Confluence und Jira")
        print("   3. Testen Sie das Makro mit echten Benutzern")
    else:
        print("\n⚠️ Es gab Probleme beim Test.")
        print("📋 Mögliche Lösungen:")
        print("   1. Überprüfen Sie Ihre Jira-Zugangsdaten")
        print("   2. Stellen Sie sicher, dass das Projekt JIRAPRO24 existiert")
        print("   3. Überprüfen Sie die Berechtigungen für Epic-Erstellung")
        print("   4. Kontaktieren Sie Ihren Jira-Administrator")

if __name__ == "__main__":
    main()

