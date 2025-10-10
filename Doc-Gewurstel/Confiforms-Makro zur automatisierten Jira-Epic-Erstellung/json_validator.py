#!/usr/bin/env python3
"""
JSON-Validator für Confiforms IFTTT Jira-Integration
Validiert die JSON-Struktur für die Epic-Erstellung
"""

import json
import re
from typing import Dict, List, Any, Optional

class ConfiformsJSONValidator:
    """Validator für Confiforms IFTTT JSON-Strukturen"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        
    def validate_epic_json(self, json_string: str) -> Dict[str, Any]:
        """
        Validiert JSON für Epic-Erstellung
        
        Args:
            json_string (str): JSON-String aus dem Confiforms IFTTT Makro
            
        Returns:
            Dict mit Validierungsergebnissen
        """
        self.errors = []
        self.warnings = []
        
        # 1. JSON-Syntax validieren
        try:
            json_data = json.loads(json_string)
        except json.JSONDecodeError as e:
            self.errors.append(f"Ungültiger JSON-Syntax: {str(e)}")
            return self._create_result(False)
        
        # 2. Grundstruktur validieren
        if not self._validate_basic_structure(json_data):
            return self._create_result(False)
        
        # 3. Pflichtfelder validieren
        if not self._validate_required_fields(json_data):
            return self._create_result(False)
        
        # 4. Confiforms-Referenzen validieren
        self._validate_confiforms_references(json_data)
        
        # 5. Jira-spezifische Validierung
        self._validate_jira_specifics(json_data)
        
        return self._create_result(len(self.errors) == 0, json_data)
    
    def _validate_basic_structure(self, json_data: Any) -> bool:
        """Validiert die Grundstruktur des JSON"""
        if not isinstance(json_data, dict):
            self.errors.append("JSON muss ein Objekt sein")
            return False
        
        if 'fields' not in json_data:
            self.errors.append("'fields' Objekt fehlt")
            return False
        
        if not isinstance(json_data['fields'], dict):
            self.errors.append("'fields' muss ein Objekt sein")
            return False
        
        return True
    
    def _validate_required_fields(self, json_data: Dict[str, Any]) -> bool:
        """Validiert Pflichtfelder für Epic-Erstellung"""
        fields = json_data['fields']
        required_fields = ['project', 'summary', 'issuetype']
        
        for field in required_fields:
            if field not in fields:
                self.errors.append(f"Pflichtfeld '{field}' fehlt")
                return False
        
        # Projekt-Validierung
        project = fields['project']
        if not isinstance(project, dict):
            self.errors.append("'project' muss ein Objekt sein")
            return False
        
        if 'key' not in project:
            self.errors.append("'project.key' fehlt")
            return False
        
        # Issue Type-Validierung
        issuetype = fields['issuetype']
        if not isinstance(issuetype, dict):
            self.errors.append("'issuetype' muss ein Objekt sein")
            return False
        
        if 'name' not in issuetype:
            self.errors.append("'issuetype.name' fehlt")
            return False
        
        if issuetype['name'] != 'Epic':
            self.errors.append("'issuetype.name' muss 'Epic' sein")
            return False
        
        return True
    
    def _validate_confiforms_references(self, json_data: Dict[str, Any]) -> None:
        """Validiert Confiforms-Feldverweise"""
        json_string = json.dumps(json_data)
        
        # Suche nach Confiforms-Referenzen
        confiforms_pattern = r'\[entry\.(\w+)(?:\.(\w+))?\]'
        matches = re.findall(confiforms_pattern, json_string)
        
        if not matches:
            self.warnings.append("Keine Confiforms-Feldverweise gefunden")
            return
        
        for match in matches:
            field_name = match[0]
            method = match[1] if match[1] else None
            
            # Validiere Feldnamen
            if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', field_name):
                self.errors.append(f"Ungültiger Feldname: '{field_name}'")
            
            # Validiere Methoden
            if method:
                valid_methods = ['escapeJSON', 'formatDate', 'transform', 'asList']
                if method not in valid_methods:
                    self.warnings.append(f"Unbekannte Methode: '{method}' für Feld '{field_name}'")
        
        # Spezielle Validierung für Epic-Name
        if '[entry.epicName]' not in json_string:
            self.warnings.append("Empfehlung: Verwenden Sie '[entry.epicName]' für den Epic-Namen")
    
    def _validate_jira_specifics(self, json_data: Dict[str, Any]) -> None:
        """Validiert Jira-spezifische Aspekte"""
        fields = json_data['fields']
        
        # Projekt-Key Validierung
        project_key = fields['project']['key']
        if not re.match(r'^[A-Z][A-Z0-9_]*$', project_key):
            self.warnings.append(f"Projekt-Key '{project_key}' entspricht nicht dem üblichen Jira-Format")
        
        if project_key != 'JIRAPRO24':
            self.warnings.append(f"Projekt-Key ist '{project_key}', erwartet wurde 'JIRAPRO24'")
        
        # Custom Fields validieren
        custom_fields = [key for key in fields.keys() if key.startswith('customfield_')]
        for cf in custom_fields:
            if not re.match(r'^customfield_\d+$', cf):
                self.errors.append(f"Ungültiges Custom Field Format: '{cf}'")
        
        # Summary-Feld validieren
        summary = fields.get('summary', '')
        if isinstance(summary, str) and len(summary) > 255:
            self.warnings.append("Summary-Feld könnte zu lang sein (>255 Zeichen)")
    
    def _create_result(self, is_valid: bool, json_data: Optional[Dict] = None) -> Dict[str, Any]:
        """Erstellt das Validierungsergebnis"""
        return {
            'valid': is_valid,
            'errors': self.errors,
            'warnings': self.warnings,
            'json_data': json_data
        }
    
    def generate_corrected_json(self, epic_name_field: str = 'epicName', 
                              project_key: str = 'JIRAPRO24',
                              include_custom_field: bool = True) -> str:
        """Generiert korrekten JSON für Confiforms IFTTT"""
        json_structure = {
            "fields": {
                "project": {
                    "key": project_key
                },
                "summary": f"[entry.{epic_name_field}]",
                "issuetype": {
                    "name": "Epic"
                }
            }
        }
        
        if include_custom_field:
            json_structure["fields"]["customfield_10103"] = f"[entry.{epic_name_field}]"
        
        return json.dumps(json_structure, indent=4)

def main():
    """Interaktive JSON-Validierung"""
    print("🔍 CONFIFORMS JSON VALIDATOR")
    print("=" * 40)
    
    validator = ConfiformsJSONValidator()
    
    while True:
        print("\nOptionen:")
        print("1. JSON validieren")
        print("2. Korrekten JSON generieren")
        print("3. Beenden")
        
        choice = input("\nWählen Sie eine Option (1-3): ").strip()
        
        if choice == '1':
            print("\nFügen Sie Ihren JSON-Code ein (beenden mit leerer Zeile):")
            json_lines = []
            while True:
                line = input()
                if line.strip() == '':
                    break
                json_lines.append(line)
            
            json_string = '\n'.join(json_lines)
            
            if json_string.strip():
                result = validator.validate_epic_json(json_string)
                
                print("\n" + "=" * 40)
                if result['valid']:
                    print("✅ JSON ist gültig!")
                else:
                    print("❌ JSON ist ungültig!")
                
                if result['errors']:
                    print("\n🚨 Fehler:")
                    for error in result['errors']:
                        print(f"   - {error}")
                
                if result['warnings']:
                    print("\n⚠️ Warnungen:")
                    for warning in result['warnings']:
                        print(f"   - {warning}")
                
                print("=" * 40)
            else:
                print("❌ Kein JSON eingegeben")
        
        elif choice == '2':
            epic_field = input("Feldname für Epic-Name (Standard: epicName): ").strip() or 'epicName'
            project = input("Projekt-Key (Standard: JIRAPRO24): ").strip() or 'JIRAPRO24'
            custom_field = input("Custom Field hinzufügen? (j/n, Standard: j): ").strip().lower()
            include_cf = custom_field in ['', 'j', 'ja', 'y', 'yes']
            
            correct_json = validator.generate_corrected_json(epic_field, project, include_cf)
            
            print("\n" + "=" * 40)
            print("📋 KORREKTER JSON FÜR CONFIFORMS IFTTT:")
            print("=" * 40)
            print(correct_json)
            print("=" * 40)
            print("\n💡 Kopieren Sie diesen JSON-Code in Ihr ConfiForms IFTTT Makro")
        
        elif choice == '3':
            print("👋 Auf Wiedersehen!")
            break
        
        else:
            print("❌ Ungültige Auswahl")

if __name__ == "__main__":
    main()

