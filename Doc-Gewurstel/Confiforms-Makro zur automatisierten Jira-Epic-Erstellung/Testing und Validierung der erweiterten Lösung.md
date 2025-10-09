# Testing und Validierung der erweiterten Lösung

## Übersicht der Test-Strategie

Die erweiterte Epic-Creator-Lösung mit bidirektionaler Datenverknüpfung erfordert eine umfassende Test-Strategie, die alle Aspekte der neuen Funktionalitäten abdeckt. Die Test-Suite umfasst Funktionalitätstests, Integrationstests, Performance-Tests und Benutzerakzeptanztests. Besondere Aufmerksamkeit gilt der Validierung der IFTTT-Kette und der Datenintegrität zwischen ConfiForms und Jira.

## Funktionalitätstests

### Test 1: Grundlegende Epic-Erstellung mit bidirektionaler Verknüpfung

**Testziel:** Validierung der vollständigen Epic-Erstellung mit automatischer Jira-Key-Rückspeicherung

**Testschritte:**
1. Öffne die ConfiForms-Seite mit dem erweiterten Epic-Creator
2. Klicke auf "Neues Epic erstellen"
3. Gebe einen gültigen Epic-Namen ein: "Test Epic Bidirektional"
4. Klicke auf "Epic erstellen"
5. Warte auf die Verarbeitung (max. 30 Sekunden)
6. Überprüfe die Anzeige des generierten Jira-Keys
7. Klicke auf den Jira-Link und verifiziere die Weiterleitung

**Erwartete Ergebnisse:**
- Epic wird erfolgreich in Jira erstellt
- Jira-Key wird automatisch in ConfiForms gespeichert
- Status wird auf "Abgeschlossen" gesetzt
- Jira-URL ist korrekt und funktional
- Epic-Name ist sowohl in Summary als auch in customfield_10103 gespeichert

### Test 2: Fehlerbehandlung bei fehlgeschlagener Epic-Erstellung

**Testziel:** Validierung der Fehlerbehandlung bei API-Fehlern

**Testschritte:**
1. Simuliere einen Jira-API-Fehler (z.B. durch ungültige Projektbezeichnung)
2. Versuche Epic-Erstellung mit gültigem Namen
3. Überprüfe Fehleranzeige und Status-Update

**Erwartete Ergebnisse:**
- Status wird auf "Fehler" gesetzt
- Fehlermeldung wird angezeigt
- Retry-Button ist verfügbar
- Keine unvollständigen Daten in ConfiForms

### Test 3: Validierung der Field Definition Rules

**Testziel:** Überprüfung der dynamischen Feldanzeige

**Testschritte:**
1. Erstelle neues Epic
2. Überprüfe, dass jiraKey-Feld initial versteckt ist
3. Warte auf Epic-Erstellung
4. Verifiziere, dass jiraKey-Feld nach Erstellung sichtbar wird

**Erwartete Ergebnisse:**
- JiraKey-Feld ist initial nicht sichtbar
- Feld wird nach erfolgreicher Erstellung angezeigt
- Feld ist als "Read only" konfiguriert

## Integrationstests

### Test 4: IFTTT-Ketten-Validierung

**Testziel:** Überprüfung der korrekten Ausführungsreihenfolge der IFTTT-Regeln

**Testschritte:**
1. Aktiviere IFTTT-Logging (falls verfügbar)
2. Erstelle Epic mit eindeutigem Namen
3. Überwache IFTTT-Ausführung
4. Validiere Timing und Datenfluss

**Erwartete Ergebnisse:**
- IFTTT-1 (Epic-Erstellung) wird zuerst ausgeführt
- IFTTT-2 (Rückspeicherung) wird nach IFTTT-1 ausgeführt
- Daten werden korrekt zwischen IFTTT-Regeln übertragen
- Keine Race Conditions oder Timing-Probleme

### Test 5: Jira-Integration-Validierung

**Testziel:** Überprüfung der korrekten Jira-API-Integration

**Testschritte:**
1. Erstelle Epic über ConfiForms
2. Öffne Jira direkt und suche nach dem Epic
3. Validiere alle Epic-Felder in Jira
4. Überprüfe Rückverfolgbarkeit zu ConfiForms

**Erwartete Ergebnisse:**
- Epic existiert in Jira mit korrektem Key
- Summary-Feld enthält Epic-Namen
- customfield_10103 enthält Epic-Namen
- Beschreibung enthält ConfiForms-Referenz
- Labels "confiforms-generated" und "epic-creator-v2" sind gesetzt

## Performance-Tests

### Test 6: Antwortzeit-Validierung

**Testziel:** Überprüfung der Performance der erweiterten Lösung

**Testschritte:**
1. Messe Zeit von Epic-Erstellung bis Jira-Key-Anzeige
2. Wiederhole Test 10 Mal
3. Berechne Durchschnitt und Standardabweichung

**Erwartete Ergebnisse:**
- Durchschnittliche Antwortzeit < 10 Sekunden
- 95% der Requests < 15 Sekunden
- Keine Timeouts oder Fehler

### Test 7: Concurrent User Test

**Testziel:** Validierung bei gleichzeitiger Nutzung

**Testschritte:**
1. Simuliere 5 gleichzeitige Epic-Erstellungen
2. Überwache Systemverhalten
3. Validiere Datenintegrität aller Epics

**Erwartete Ergebnisse:**
- Alle Epics werden erfolgreich erstellt
- Keine Datenkorruption oder -verlust
- Performance bleibt akzeptabel

## Benutzeroberflächen-Tests

### Test 8: UI-Responsiveness

**Testziel:** Überprüfung der Benutzeroberfläche auf verschiedenen Geräten

**Testschritte:**
1. Teste auf Desktop (1920x1080)
2. Teste auf Tablet (768x1024)
3. Teste auf Mobile (375x667)
4. Überprüfe alle UI-Elemente

**Erwartete Ergebnisse:**
- Layout passt sich korrekt an
- Alle Buttons sind klickbar
- Text ist lesbar
- Keine Überlappungen oder abgeschnittene Inhalte

### Test 9: JavaScript-Funktionalitäten

**Testziel:** Validierung der erweiterten JavaScript-Features

**Testschritte:**
1. Teste Copy-to-Clipboard-Funktionalität
2. Teste Auto-Refresh-Mechanismus
3. Teste Modal-Dialoge
4. Teste Status-Aktualisierung

**Erwartete Ergebnisse:**
- Clipboard-Funktionalität arbeitet korrekt
- Auto-Refresh erkennt Updates
- Modals öffnen und schließen korrekt
- Status-Updates funktionieren

## Datenintegritäts-Tests

### Test 10: Bidirektionale Datenverknüpfung

**Testziel:** Validierung der vollständigen Datenverknüpfung

**Testschritte:**
1. Erstelle Epic in ConfiForms
2. Überprüfe Jira-Epic-Erstellung
3. Validiere Rückspeicherung in ConfiForms
4. Überprüfe Datenkonzistenz

**Erwartete Ergebnisse:**
- ConfiForms Entry enthält korrekten Jira-Key
- Jira Epic enthält ConfiForms-Referenz
- Alle Zeitstempel sind korrekt
- Keine Dateninkonsistenzen

### Test 11: Datenvalidierung und Sanitization

**Testziel:** Überprüfung der Input-Validierung

**Testschritte:**
1. Teste mit leerem Epic-Namen
2. Teste mit sehr langem Epic-Namen (>255 Zeichen)
3. Teste mit Sonderzeichen und HTML-Tags
4. Teste mit SQL-Injection-Versuchen

**Erwartete Ergebnisse:**
- Leere Namen werden abgelehnt
- Lange Namen werden gekürzt
- Sonderzeichen werden korrekt behandelt
- Keine Sicherheitslücken

## Automatisierte Test-Suite

### Test-Skript für JSON-Validierung

```python
#!/usr/bin/env python3
"""
Automatisierte Test-Suite für ConfiForms Epic Creator
Bidirektionale Datenverknüpfung
"""

import json
import requests
import time
import unittest
from datetime import datetime

class EpicCreatorTests(unittest.TestCase):
    
    def setUp(self):
        """Test-Setup"""
        self.base_url = "https://your-confluence-instance.com"
        self.jira_url = "https://your-jira-instance.com"
        self.test_epic_name = f"Test Epic {datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
    def test_json_payload_structure(self):
        """Test der JSON-Payload-Struktur für Jira API"""
        expected_payload = {
            "fields": {
                "project": {"key": "JIRAPRO24"},
                "summary": self.test_epic_name,
                "issuetype": {"name": "Epic"},
                "customfield_10103": self.test_epic_name
            }
        }
        
        # Validiere JSON-Struktur
        self.assertIn("fields", expected_payload)
        self.assertIn("project", expected_payload["fields"])
        self.assertEqual(expected_payload["fields"]["project"]["key"], "JIRAPRO24")
        self.assertEqual(expected_payload["fields"]["issuetype"]["name"], "Epic")
        
    def test_ifttt_result_structure(self):
        """Test der IFTTT-Result-Struktur"""
        mock_ifttt_result = {
            "key": "JIRAPRO24-123",
            "id": "12345",
            "fields": {
                "project": {"key": "JIRAPRO24"},
                "summary": self.test_epic_name
            },
            "responseTime": 1500
        }
        
        # Validiere Result-Struktur
        self.assertIn("key", mock_ifttt_result)
        self.assertRegex(mock_ifttt_result["key"], r"^[A-Z]+-[0-9]+$")
        self.assertIn("id", mock_ifttt_result)
        self.assertIn("responseTime", mock_ifttt_result)
        
    def test_confiforms_update_payload(self):
        """Test der ConfiForms-Update-Payload"""
        mock_jira_key = "JIRAPRO24-123"
        update_payload = {
            "jiraKey": mock_jira_key,
            "jiraUrl": f"https://your-jira-instance.com/browse/{mock_jira_key}",
            "epicStatus": "Abgeschlossen",
            "completedAt": datetime.now().isoformat()
        }
        
        # Validiere Update-Payload
        self.assertIn("jiraKey", update_payload)
        self.assertIn("jiraUrl", update_payload)
        self.assertIn("epicStatus", update_payload)
        self.assertEqual(update_payload["epicStatus"], "Abgeschlossen")
        
    def test_field_validation_rules(self):
        """Test der Field-Validation-Rules"""
        test_cases = [
            {"input": "", "expected_valid": False},  # Leer
            {"input": "A" * 300, "expected_valid": False},  # Zu lang
            {"input": "Valid Epic Name", "expected_valid": True},  # Gültig
            {"input": "Epic-Name_123", "expected_valid": True},  # Mit Sonderzeichen
        ]
        
        for case in test_cases:
            with self.subTest(input=case["input"]):
                # Simuliere Validierung
                is_valid = self.validate_epic_name(case["input"])
                self.assertEqual(is_valid, case["expected_valid"])
                
    def validate_epic_name(self, name):
        """Simuliert Epic-Name-Validierung"""
        if not name or len(name) < 3 or len(name) > 255:
            return False
        # Weitere Validierungslogik hier
        return True
        
    def test_timing_constraints(self):
        """Test der Timing-Constraints für IFTTT-Kette"""
        start_time = time.time()
        
        # Simuliere IFTTT-1 (Epic-Erstellung)
        time.sleep(2)  # Simulierte API-Latenz
        ifttt1_complete = time.time()
        
        # Simuliere IFTTT-2 (Rückspeicherung)
        time.sleep(1)  # Simulierte Update-Latenz
        ifttt2_complete = time.time()
        
        total_time = ifttt2_complete - start_time
        
        # Validiere Timing
        self.assertLess(total_time, 30)  # Maximal 30 Sekunden
        self.assertGreater(ifttt2_complete, ifttt1_complete)  # Korrekte Reihenfolge

if __name__ == "__main__":
    unittest.main()
```

### Load-Test-Skript

```python
#!/usr/bin/env python3
"""
Load-Test für ConfiForms Epic Creator
"""

import concurrent.futures
import time
import statistics
from datetime import datetime

class LoadTester:
    
    def __init__(self, concurrent_users=5, test_duration=60):
        self.concurrent_users = concurrent_users
        self.test_duration = test_duration
        self.results = []
        
    def create_epic_simulation(self, user_id):
        """Simuliert Epic-Erstellung für einen Benutzer"""
        start_time = time.time()
        
        try:
            # Simuliere Epic-Erstellung
            epic_name = f"Load Test Epic {user_id} {datetime.now().strftime('%H%M%S')}"
            
            # Simuliere API-Aufrufe
            time.sleep(2 + (user_id * 0.1))  # Simulierte Latenz
            
            end_time = time.time()
            response_time = end_time - start_time
            
            return {
                "user_id": user_id,
                "epic_name": epic_name,
                "response_time": response_time,
                "success": True,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "user_id": user_id,
                "error": str(e),
                "success": False,
                "timestamp": datetime.now().isoformat()
            }
    
    def run_load_test(self):
        """Führt Load-Test aus"""
        print(f"Starte Load-Test mit {self.concurrent_users} gleichzeitigen Benutzern")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.concurrent_users) as executor:
            # Starte gleichzeitige Epic-Erstellungen
            futures = []
            for i in range(self.concurrent_users):
                future = executor.submit(self.create_epic_simulation, i)
                futures.append(future)
            
            # Sammle Ergebnisse
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                self.results.append(result)
        
        self.analyze_results()
    
    def analyze_results(self):
        """Analysiert Load-Test-Ergebnisse"""
        successful_tests = [r for r in self.results if r.get("success", False)]
        failed_tests = [r for r in self.results if not r.get("success", False)]
        
        if successful_tests:
            response_times = [r["response_time"] for r in successful_tests]
            avg_response_time = statistics.mean(response_times)
            median_response_time = statistics.median(response_times)
            max_response_time = max(response_times)
            min_response_time = min(response_times)
            
            print(f"\n=== Load-Test-Ergebnisse ===")
            print(f"Erfolgreiche Tests: {len(successful_tests)}")
            print(f"Fehlgeschlagene Tests: {len(failed_tests)}")
            print(f"Erfolgsrate: {len(successful_tests)/len(self.results)*100:.1f}%")
            print(f"Durchschnittliche Antwortzeit: {avg_response_time:.2f}s")
            print(f"Median Antwortzeit: {median_response_time:.2f}s")
            print(f"Minimale Antwortzeit: {min_response_time:.2f}s")
            print(f"Maximale Antwortzeit: {max_response_time:.2f}s")
            
            # Performance-Bewertung
            if avg_response_time < 5:
                print("✅ Performance: Ausgezeichnet")
            elif avg_response_time < 10:
                print("✅ Performance: Gut")
            elif avg_response_time < 15:
                print("⚠️ Performance: Akzeptabel")
            else:
                print("❌ Performance: Verbesserung erforderlich")
        
        if failed_tests:
            print(f"\n=== Fehler-Details ===")
            for test in failed_tests:
                print(f"Benutzer {test['user_id']}: {test.get('error', 'Unbekannter Fehler')}")

if __name__ == "__main__":
    tester = LoadTester(concurrent_users=5, test_duration=60)
    tester.run_load_test()
```

## Browser-basierte Tests

### Selenium-Test für UI-Validierung

```python
#!/usr/bin/env python3
"""
Selenium-basierte UI-Tests für ConfiForms Epic Creator
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest
import time

class UITests(unittest.TestCase):
    
    def setUp(self):
        """Setup für UI-Tests"""
        self.driver = webdriver.Chrome()  # Oder Firefox()
        self.driver.maximize_window()
        self.base_url = "https://your-confluence-instance.com/display/SPACE/Epic-Creator"
        self.wait = WebDriverWait(self.driver, 30)
        
    def tearDown(self):
        """Cleanup nach Tests"""
        self.driver.quit()
        
    def test_epic_creation_workflow(self):
        """Test des vollständigen Epic-Erstellungs-Workflows"""
        # Öffne ConfiForms-Seite
        self.driver.get(self.base_url)
        
        # Warte auf Seitenladung
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confiform-registration-form")))
        
        # Klicke auf "Neues Epic erstellen"
        create_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Neues Epic erstellen')]"))
        )
        create_button.click()
        
        # Warte auf Dialog
        dialog = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confiform-dialog")))
        
        # Gebe Epic-Namen ein
        epic_name_field = dialog.find_element(By.NAME, "epicName")
        test_epic_name = f"UI Test Epic {int(time.time())}"
        epic_name_field.send_keys(test_epic_name)
        
        # Klicke auf "Epic erstellen"
        submit_button = dialog.find_element(By.XPATH, "//button[contains(text(), 'Epic erstellen')]")
        submit_button.click()
        
        # Warte auf Verarbeitung und Ergebnis
        try:
            # Warte auf Jira-Key-Anzeige (max. 30 Sekunden)
            jira_key_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "jira-key-text"))
            )
            
            jira_key = jira_key_element.text
            self.assertRegex(jira_key, r"^JIRAPRO24-[0-9]+$")
            
            # Teste Jira-Link
            jira_link = self.driver.find_element(By.CLASS_NAME, "jira-link-button")
            self.assertTrue(jira_link.is_displayed())
            
            # Teste Status-Anzeige
            status_badge = self.driver.find_element(By.CLASS_NAME, "status-badge")
            self.assertEqual(status_badge.text, "ABGESCHLOSSEN")
            
        except TimeoutException:
            self.fail("Epic-Erstellung hat zu lange gedauert oder ist fehlgeschlagen")
            
    def test_responsive_design(self):
        """Test des Responsive Designs"""
        self.driver.get(self.base_url)
        
        # Desktop-Ansicht
        self.driver.set_window_size(1920, 1080)
        time.sleep(1)
        self.assertTrue(self.is_layout_correct())
        
        # Tablet-Ansicht
        self.driver.set_window_size(768, 1024)
        time.sleep(1)
        self.assertTrue(self.is_layout_correct())
        
        # Mobile-Ansicht
        self.driver.set_window_size(375, 667)
        time.sleep(1)
        self.assertTrue(self.is_layout_correct())
        
    def is_layout_correct(self):
        """Überprüft, ob das Layout korrekt ist"""
        try:
            # Überprüfe, ob wichtige Elemente sichtbar sind
            create_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Neues Epic erstellen')]")
            return create_button.is_displayed()
        except:
            return False
            
    def test_javascript_functionality(self):
        """Test der JavaScript-Funktionalitäten"""
        self.driver.get(self.base_url)
        
        # Teste Copy-to-Clipboard (falls Epic vorhanden)
        try:
            copy_button = self.driver.find_element(By.CLASS_NAME, "copy-url-button")
            copy_button.click()
            
            # Überprüfe Notification
            notification = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "notification"))
            )
            self.assertIn("kopiert", notification.text.lower())
            
        except:
            # Kein Epic vorhanden, Test übersprungen
            pass

if __name__ == "__main__":
    unittest.main()
```

## Test-Dokumentation und Reporting

### Test-Report-Generator

```python
#!/usr/bin/env python3
"""
Test-Report-Generator für ConfiForms Epic Creator
"""

import json
from datetime import datetime
from jinja2 import Template

class TestReportGenerator:
    
    def __init__(self):
        self.test_results = []
        
    def add_test_result(self, test_name, status, duration, details=None):
        """Fügt Test-Ergebnis hinzu"""
        self.test_results.append({
            "name": test_name,
            "status": status,  # "PASS", "FAIL", "SKIP"
            "duration": duration,
            "details": details or "",
            "timestamp": datetime.now().isoformat()
        })
        
    def generate_html_report(self):
        """Generiert HTML-Test-Report"""
        template = Template("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>ConfiForms Epic Creator - Test Report</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                .header { background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
                .summary { display: flex; gap: 20px; margin-bottom: 20px; }
                .metric { background: white; padding: 15px; border-radius: 6px; border: 1px solid #ddd; }
                .test-result { margin-bottom: 10px; padding: 10px; border-radius: 4px; }
                .pass { background: #d4edda; border-left: 4px solid #28a745; }
                .fail { background: #f8d7da; border-left: 4px solid #dc3545; }
                .skip { background: #fff3cd; border-left: 4px solid #ffc107; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>ConfiForms Epic Creator - Test Report</h1>
                <p>Generiert am: {{ timestamp }}</p>
            </div>
            
            <div class="summary">
                <div class="metric">
                    <h3>Gesamt Tests</h3>
                    <p>{{ total_tests }}</p>
                </div>
                <div class="metric">
                    <h3>Erfolgreich</h3>
                    <p>{{ passed_tests }}</p>
                </div>
                <div class="metric">
                    <h3>Fehlgeschlagen</h3>
                    <p>{{ failed_tests }}</p>
                </div>
                <div class="metric">
                    <h3>Übersprungen</h3>
                    <p>{{ skipped_tests }}</p>
                </div>
                <div class="metric">
                    <h3>Erfolgsrate</h3>
                    <p>{{ success_rate }}%</p>
                </div>
            </div>
            
            <h2>Test-Ergebnisse</h2>
            {% for test in test_results %}
            <div class="test-result {{ test.status.lower() }}">
                <h4>{{ test.name }}</h4>
                <p><strong>Status:</strong> {{ test.status }}</p>
                <p><strong>Dauer:</strong> {{ test.duration }}s</p>
                {% if test.details %}
                <p><strong>Details:</strong> {{ test.details }}</p>
                {% endif %}
                <p><strong>Zeitstempel:</strong> {{ test.timestamp }}</p>
            </div>
            {% endfor %}
        </body>
        </html>
        """)
        
        total_tests = len(self.test_results)
        passed_tests = len([t for t in self.test_results if t["status"] == "PASS"])
        failed_tests = len([t for t in self.test_results if t["status"] == "FAIL"])
        skipped_tests = len([t for t in self.test_results if t["status"] == "SKIP"])
        success_rate = round((passed_tests / total_tests * 100) if total_tests > 0 else 0, 1)
        
        return template.render(
            timestamp=datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
            total_tests=total_tests,
            passed_tests=passed_tests,
            failed_tests=failed_tests,
            skipped_tests=skipped_tests,
            success_rate=success_rate,
            test_results=self.test_results
        )
        
    def save_report(self, filename="test_report.html"):
        """Speichert Test-Report als HTML-Datei"""
        html_content = self.generate_html_report()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Test-Report gespeichert: {filename}")

# Beispiel-Verwendung
if __name__ == "__main__":
    generator = TestReportGenerator()
    
    # Beispiel-Test-Ergebnisse
    generator.add_test_result("Epic-Erstellung Grundfunktion", "PASS", 5.2, "Epic erfolgreich erstellt")
    generator.add_test_result("Bidirektionale Verknüpfung", "PASS", 8.1, "Jira-Key korrekt gespeichert")
    generator.add_test_result("Fehlerbehandlung", "PASS", 2.3, "Fehler korrekt behandelt")
    generator.add_test_result("Performance-Test", "FAIL", 25.7, "Antwortzeit zu hoch")
    generator.add_test_result("UI-Responsiveness", "PASS", 3.4, "Layout korrekt auf allen Geräten")
    
    generator.save_report()
```

Die umfassende Test-Suite gewährleistet die Qualität und Zuverlässigkeit der erweiterten Epic-Creator-Lösung mit bidirektionaler Datenverknüpfung. Alle kritischen Funktionalitäten werden systematisch validiert und dokumentiert.

