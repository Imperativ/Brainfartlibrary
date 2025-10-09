# ZED AI PROVIDERS SETUP GUIDE

## Konfiguration der AI-Dienste in Zed

### 1. ANTHROPIC (Claude)
```json
// In settings.json unter "assistant" ergänzen:
"provider": {
  "name": "anthropic",
  "api_key_env_var": "ANTHROPIC_API_KEY",
  "models": [
    {
      "name": "claude-3-5-sonnet-20241022",
      "display_name": "Claude 3.5 Sonnet"
    },
    {
      "name": "claude-3-opus-20240229",
      "display_name": "Claude 3 Opus"
    }
  ]
}
```

### 2. OPENAI
```json
// Alternative Konfiguration:
"provider": {
  "name": "openai",
  "api_key_env_var": "OPENAI_API_KEY",
  "models": [
    {
      "name": "gpt-4-turbo-preview",
      "display_name": "GPT-4 Turbo"
    },
    {
      "name": "gpt-3.5-turbo",
      "display_name": "GPT-3.5 Turbo"
    }
  ]
}
```

### 3. GOOGLE GEMINI
```json
// Google AI Studio Setup:
"provider": {
  "name": "google",
  "api_key_env_var": "GOOGLE_AI_API_KEY",
  "models": [
    {
      "name": "gemini-pro",
      "display_name": "Gemini Pro"
    },
    {
      "name": "gemini-pro-vision",
      "display_name": "Gemini Pro Vision"
    }
  ]
}
```

### 4. MANUS.IM (falls API verfügbar)
```json
// Custom Provider Setup - muss eventuell als externe Integration erfolgen
"provider": {
  "name": "custom",
  "api_url": "https://api.manus.im/v1/chat/completions",
  "api_key_env_var": "MANUS_API_KEY"
}
```

## ENVIRONMENT VARIABLES SETUP

### Windows (cmd):
```cmd
setx ANTHROPIC_API_KEY "your-claude-api-key"
setx OPENAI_API_KEY "your-openai-api-key"
setx GOOGLE_AI_API_KEY "your-gemini-api-key"
setx MANUS_API_KEY "your-manus-api-key"
```

### PowerShell:
```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "your-claude-api-key", "User")
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your-openai-api-key", "User")
[Environment]::SetEnvironmentVariable("GOOGLE_AI_API_KEY", "your-gemini-api-key", "User")
[Environment]::SetEnvironmentVariable("MANUS_API_KEY", "your-manus-api-key", "User")
```

## MULTI-PROVIDER KONFIGURATION

Für die Verwendung mehrerer Provider kannst du diese Konfiguration verwenden:

```json
"assistant": {
  "enabled": true,
  "version": "2",
  "providers": [
    {
      "name": "anthropic",
      "api_key_env_var": "ANTHROPIC_API_KEY",
      "default": true
    },
    {
      "name": "openai",
      "api_key_env_var": "OPENAI_API_KEY"
    },
    {
      "name": "google",
      "api_key_env_var": "GOOGLE_AI_API_KEY"
    }
  ],
  "default_model": {
    "provider": "anthropic",
    "model": "claude-3-5-sonnet-20241022"
  }
}
```

## VERWENDUNG

1. **Provider wechseln**: Über das Assistant Panel kannst du zwischen den konfigurierten Modellen wechseln
2. **Shortcuts**:
   - `Ctrl+Shift+A`: Assistant Panel öffnen/schließen
   - `Ctrl+Enter`: Query an AI senden
3. **Context**: Der Editor sendet automatisch den aktuellen Code-Kontext mit

## TROUBLESHOOTING

- **API Keys**: Stelle sicher, dass alle Environment Variables korrekt gesetzt sind
- **Neustart**: Nach Änderung der Environment Variables Zed neu starten
- **Logs**: Zed Logs findest du unter `%APPDATA%\Zed\logs\`