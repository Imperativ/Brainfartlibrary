# 🚀 ZED EDITOR - VOLLSTÄNDIGE INSTALLATION & SETUP

## 📁 **Dateien kopieren**

### 1. Settings installieren:
```cmd
copy "D:\claude-workspace\zed-settings.json" "%APPDATA%\Zed\settings.json"
```

### 2. Backup der aktuellen Settings (optional):
```cmd
copy "%APPDATA%\Zed\settings.json" "%APPDATA%\Zed\settings.json.backup"
```

## 🤖 **Verfügbare AI-Modelle**

### **ANTHROPIC (Standard)**
- ✅ **Claude 3.5 Sonnet** - Neuestes & bestes Modell (Standard)
- ✅ **Claude 3 Opus** - Für komplexe Reasoning-Tasks
- ✅ **Claude 3 Haiku** - Schnell für einfache Aufgaben

### **OPENAI**
- ✅ **GPT-4o** - Neuestes OpenAI Modell
- ✅ **GPT-4 Turbo** - Für längere Kontexte
- ✅ **GPT-3.5 Turbo** - Schnell & effizient

### **GOOGLE GEMINI**
- ✅ **Gemini 1.5 Pro** - 2M Token Context!
- ✅ **Gemini Pro** - Standard Google AI
- ✅ **Gemini Pro Vision** - Mit Bildverständnis

### **MANUS.IM**
- ⚠️ **Custom Integration** - Eventuell über Extension

## 🎯 **Verwendung in Zed**

### **AI Assistant aktivieren:**
1. **Panel öffnen:** `Ctrl+Shift+A`
2. **Model wechseln:** Dropdown im Assistant Panel
3. **Query senden:** `Ctrl+Enter`

### **Shortcuts:**
- `Ctrl+Shift+A` - Assistant Panel toggle
- `Ctrl+Enter` - Query an AI senden
- `Ctrl+Shift+C` - Code Context hinzufügen
- `F1` - Command Palette

## 🔧 **Features für SQL/JavaScript/Bash**

### **SQL Development:**
- Auto-completion für Tabellen & Spalten
- Syntax-Highlighting für alle SQL-Dialekte
- Query-Formatting beim Speichern
- Inline-Dokumentation

### **JavaScript/TypeScript:**
- Prettier Auto-Formatting
- ESLint Integration
- Import-Organisation
- Inlay Hints für Types

### **Bash Scripting:**
- Shellcheck Integration
- Auto-completion für Commands
- Syntax-Validation
- Function-Dokumentation

## 🎨 **Theme & UI**

- **Theme:** Andromeda (elegantes Dark Theme)
- **Font:** JetBrains Mono für Code
- **UI Font:** Segoe UI
- **Panel Layout:** Links = Project, Rechts = AI Assistant

## ✅ **Installation Check**

Nach der Installation solltest du:

1. **Zed neustarten**
2. **Assistant Panel öffnen** (`Ctrl+Shift+A`)
3. **Model-Dropdown prüfen** - alle Provider sollten verfügbar sein
4. **Test-Query senden:** "Erkläre mir diese SQL-Query: SELECT * FROM users;"

## 🔍 **Troubleshooting**

### **AI-Models werden nicht angezeigt:**
- Zed komplett neu starten
- Settings-Datei auf JSON-Syntax prüfen
- API-Keys validieren

### **Formatting funktioniert nicht:**
- Language Servers installiert? (automatisch bei erstem Öffnen)
- Prettier/ESLint global installiert?

### **Performance Issues:**
- Inlay Hints deaktivieren falls zu langsam
- Weniger Context an AI senden

## 📊 **Model-Empfehlungen je Use-Case**

| **Task** | **Empfohlenes Model** | **Grund** |
|----------|----------------------|-----------|
| **SQL Queries optimieren** | Claude 3.5 Sonnet | Beste Code-Analyse |
| **JavaScript Debugging** | GPT-4o | Gute Debug-Skills |
| **Bash Scripts** | Claude 3 Haiku | Schnell für einfache Scripts |
| **Große Datenanalyse** | Gemini 1.5 Pro | 2M Token Context |
| **Lernen & Erklärungen** | Claude 3.5 Sonnet | Beste didaktische Fähigkeiten |

## 🔐 **Sicherheit**

- API-Keys sind lokal in der settings.json gespeichert
- Keine Übertragung an Dritte außer den AI-Providern
- Regelmäßig API-Key Rotation empfohlen