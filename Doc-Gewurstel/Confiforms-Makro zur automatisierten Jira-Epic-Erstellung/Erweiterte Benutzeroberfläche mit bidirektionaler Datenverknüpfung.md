# Erweiterte Benutzeroberfläche mit bidirektionaler Datenverknüpfung

## Übersicht der UI-Erweiterungen

Die bidirektionale Datenverknüpfung erfordert eine erweiterte Benutzeroberfläche, die nicht nur die Epic-Erstellung ermöglicht, sondern auch die gespeicherten Jira-Keys anzeigt und eine verbesserte Benutzererfahrung bietet. Die erweiterte UI umfasst dynamische Statusanzeigen, interaktive Jira-Links, erweiterte Tabellenansichten und Real-time-Updates der bidirektionalen Datenverknüpfung.

## Erweiterte ListView-Konfiguration

### Hauptkonfiguration der ListView

Die ListView wird erheblich erweitert, um alle neuen Datenfelder anzuzeigen:

```
Makro: ConfiForms ListView
Parameter:
- Form name: epicCreator
- Filter: id IS NOT EMPTY
- Number of items to show: 20
- Sort by: createdDate
- Sort order: DESC
- Show search: true
- Show pagination: true
- Enable row selection: true
- Show export options: true
```

### Erweiterte ListView-Template

Das ListView-Template wird um umfassende Darstellung der bidirektionalen Daten erweitert:

```html
<div class="epic-entry-container" data-entry-id="[entry.id]" data-jira-key="[entry.jiraKey]">
    <div class="epic-header">
        <div class="epic-title-section">
            <h3 class="epic-name">[entry.epicName]</h3>
            <div class="epic-metadata">
                <span class="creation-date">Erstellt: [entry.createdDate|dateFormat:dd.MM.yyyy HH:mm]</span>
                <span class="creator">von [entry.createdBy]</span>
            </div>
        </div>
        <div class="epic-status-section">
            <span class="status-badge status-[entry.epicStatus|lowercase]">[entry.epicStatus]</span>
        </div>
    </div>
    
    <div class="epic-content">
        <div class="jira-integration-panel">
            <div class="jira-key-display" data-condition="[entry.jiraKey] IS NOT EMPTY">
                <div class="jira-key-container">
                    <label class="jira-key-label">Jira Epic:</label>
                    <div class="jira-key-value">
                        <span class="jira-key-text">[entry.jiraKey]</span>
                        <a href="[entry.jiraUrl]" target="_blank" class="jira-link-button" title="Epic in Jira öffnen">
                            <svg class="jira-icon" viewBox="0 0 24 24" width="16" height="16">
                                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                            </svg>
                            In Jira öffnen
                        </a>
                    </div>
                </div>
                
                <div class="jira-metadata">
                    <div class="jira-url-display">
                        <label>Direktlink:</label>
                        <input type="text" value="[entry.jiraUrl]" readonly class="jira-url-input" onclick="this.select()">
                        <button class="copy-url-button" onclick="copyToClipboard('[entry.jiraUrl]')" title="URL kopieren">
                            <svg viewBox="0 0 24 24" width="14" height="14">
                                <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
            
            <div class="processing-indicator" data-condition="[entry.jiraKey] IS EMPTY AND [entry.epicStatus]:In Bearbeitung">
                <div class="processing-animation">
                    <div class="spinner"></div>
                    <span class="processing-text">Epic wird in Jira erstellt...</span>
                </div>
                <div class="processing-details">
                    <small>Bitte warten Sie, während die bidirektionale Verknüpfung hergestellt wird.</small>
                </div>
            </div>
            
            <div class="error-display" data-condition="[entry.epicStatus]:Fehler">
                <div class="error-message">
                    <svg class="error-icon" viewBox="0 0 24 24" width="16" height="16">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                    </svg>
                    <span>Epic-Erstellung fehlgeschlagen</span>
                </div>
                <div class="error-details">
                    <small>[entry.errorMessage]</small>
                </div>
                <button class="retry-button" onclick="retryEpicCreation('[entry.id]')">
                    Erneut versuchen
                </button>
            </div>
        </div>
        
        <div class="epic-actions">
            <button class="action-button refresh-button" onclick="refreshEpicStatus('[entry.id]')" title="Status aktualisieren">
                <svg viewBox="0 0 24 24" width="14" height="14">
                    <path d="M17.65 6.35C16.2 4.9 14.21 4 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"/>
                </svg>
                Aktualisieren
            </button>
            
            <button class="action-button details-button" onclick="showEpicDetails('[entry.id]')" title="Details anzeigen">
                <svg viewBox="0 0 24 24" width="14" height="14">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                </svg>
                Details
            </button>
        </div>
    </div>
    
    <div class="epic-footer">
        <div class="timing-information">
            <span class="completion-time" data-condition="[entry.completedAt] IS NOT EMPTY">
                Abgeschlossen: [entry.completedAt|dateFormat:dd.MM.yyyy HH:mm]
            </span>
            <span class="processing-time" data-condition="[entry.processingTime] IS NOT EMPTY">
                Verarbeitungszeit: [entry.processingTime]ms
            </span>
        </div>
    </div>
</div>
```

## Erweiterte CSS-Styles

### Hauptstyles für die erweiterte UI

```css
/* Container und Layout */
.epic-entry-container {
    background: #ffffff;
    border: 1px solid #e1e5e9;
    border-radius: 8px;
    margin-bottom: 16px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    position: relative;
}

.epic-entry-container:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    border-color: #0052cc;
}

/* Header-Bereich */
.epic-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid #f4f5f7;
}

.epic-title-section {
    flex: 1;
}

.epic-name {
    margin: 0 0 8px 0;
    font-size: 18px;
    font-weight: 600;
    color: #172b4d;
    line-height: 1.3;
}

.epic-metadata {
    display: flex;
    gap: 16px;
    font-size: 13px;
    color: #6b778c;
}

.epic-status-section {
    flex-shrink: 0;
}

/* Status-Badges */
.status-badge {
    display: inline-flex;
    align-items: center;
    padding: 4px 12px;
    border-radius: 16px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.status-erstellt {
    background-color: #e3fcef;
    color: #006644;
    border: 1px solid #79e2a0;
}

.status-in-bearbeitung {
    background-color: #fff4e6;
    color: #974f0c;
    border: 1px solid #ffab00;
}

.status-abgeschlossen {
    background-color: #e3fcef;
    color: #006644;
    border: 1px solid #36b37e;
}

.status-fehler {
    background-color: #ffebe6;
    color: #bf2600;
    border: 1px solid #ff5630;
}

/* Jira-Integration Panel */
.jira-integration-panel {
    background: #f8f9fa;
    border: 1px solid #e1e5e9;
    border-radius: 6px;
    padding: 16px;
    margin-bottom: 16px;
}

.jira-key-container {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
}

.jira-key-label {
    font-weight: 600;
    color: #172b4d;
    min-width: 80px;
}

.jira-key-value {
    display: flex;
    align-items: center;
    gap: 8px;
    flex: 1;
}

.jira-key-text {
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 14px;
    font-weight: 600;
    color: #0052cc;
    background: #ffffff;
    padding: 6px 10px;
    border: 1px solid #dfe1e6;
    border-radius: 4px;
}

.jira-link-button {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 8px 12px;
    background: #0052cc;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    font-size: 13px;
    font-weight: 500;
    transition: background-color 0.2s ease;
}

.jira-link-button:hover {
    background: #0065ff;
    text-decoration: none;
    color: white;
}

.jira-icon {
    fill: currentColor;
}

/* URL-Display */
.jira-url-display {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 8px;
}

.jira-url-display label {
    font-size: 12px;
    color: #6b778c;
    min-width: 60px;
}

.jira-url-input {
    flex: 1;
    padding: 4px 8px;
    border: 1px solid #dfe1e6;
    border-radius: 3px;
    font-size: 12px;
    background: #fafbfc;
    color: #6b778c;
}

.copy-url-button {
    padding: 4px 6px;
    border: 1px solid #dfe1e6;
    border-radius: 3px;
    background: white;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.copy-url-button:hover {
    background: #f4f5f7;
}

/* Processing Indicator */
.processing-indicator {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    text-align: center;
}

.processing-animation {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 8px;
}

.spinner {
    width: 20px;
    height: 20px;
    border: 2px solid #f3f3f3;
    border-top: 2px solid #0052cc;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.processing-text {
    font-weight: 500;
    color: #172b4d;
}

.processing-details {
    color: #6b778c;
    font-size: 12px;
}

/* Error Display */
.error-display {
    text-align: center;
    padding: 16px;
}

.error-message {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-bottom: 8px;
    color: #bf2600;
    font-weight: 500;
}

.error-icon {
    fill: currentColor;
}

.error-details {
    color: #6b778c;
    font-size: 12px;
    margin-bottom: 12px;
}

.retry-button {
    padding: 8px 16px;
    background: #ff5630;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.retry-button:hover {
    background: #de350b;
}

/* Action Buttons */
.epic-actions {
    display: flex;
    gap: 8px;
    justify-content: flex-end;
}

.action-button {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 6px 10px;
    border: 1px solid #dfe1e6;
    border-radius: 4px;
    background: white;
    color: #172b4d;
    font-size: 12px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.action-button:hover {
    background: #f4f5f7;
    border-color: #b3bac5;
}

.action-button svg {
    fill: currentColor;
}

/* Footer */
.epic-footer {
    margin-top: 16px;
    padding-top: 12px;
    border-top: 1px solid #f4f5f7;
}

.timing-information {
    display: flex;
    gap: 16px;
    font-size: 11px;
    color: #6b778c;
}

/* Responsive Design */
@media (max-width: 768px) {
    .epic-header {
        flex-direction: column;
        gap: 12px;
    }
    
    .epic-metadata {
        flex-direction: column;
        gap: 4px;
    }
    
    .jira-key-container {
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
    }
    
    .jira-url-display {
        flex-direction: column;
        align-items: flex-start;
        gap: 4px;
    }
    
    .epic-actions {
        justify-content: center;
    }
}

/* Dark Mode Support */
@media (prefers-color-scheme: dark) {
    .epic-entry-container {
        background: #1e1e1e;
        border-color: #333;
        color: #e1e1e1;
    }
    
    .epic-name {
        color: #ffffff;
    }
    
    .jira-integration-panel {
        background: #2a2a2a;
        border-color: #444;
    }
    
    .jira-key-text {
        background: #333;
        border-color: #555;
        color: #4a9eff;
    }
    
    .jira-url-input {
        background: #333;
        border-color: #555;
        color: #e1e1e1;
    }
}
```

## Erweiterte JavaScript-Funktionalitäten

### Core JavaScript für bidirektionale UI

```javascript
// Epic Creator Enhanced UI - Bidirektionale Datenverknüpfung
(function() {
    'use strict';
    
    // Konfiguration
    const CONFIG = {
        formName: 'epicCreator',
        refreshInterval: 3000,
        maxRetries: 5,
        jiraBaseUrl: 'https://your-jira-instance.com',
        apiEndpoint: '/rest/api/3/issue'
    };
    
    // Utility-Funktionen
    const Utils = {
        // Kopiert Text in die Zwischenablage
        copyToClipboard: function(text) {
            if (navigator.clipboard) {
                navigator.clipboard.writeText(text).then(() => {
                    this.showNotification('URL in Zwischenablage kopiert', 'success');
                }).catch(() => {
                    this.fallbackCopyToClipboard(text);
                });
            } else {
                this.fallbackCopyToClipboard(text);
            }
        },
        
        // Fallback für ältere Browser
        fallbackCopyToClipboard: function(text) {
            const textArea = document.createElement('textarea');
            textArea.value = text;
            textArea.style.position = 'fixed';
            textArea.style.left = '-999999px';
            textArea.style.top = '-999999px';
            document.body.appendChild(textArea);
            textArea.focus();
            textArea.select();
            
            try {
                document.execCommand('copy');
                this.showNotification('URL in Zwischenablage kopiert', 'success');
            } catch (err) {
                this.showNotification('Kopieren fehlgeschlagen', 'error');
            }
            
            document.body.removeChild(textArea);
        },
        
        // Zeigt Benachrichtigungen an
        showNotification: function(message, type = 'info') {
            const notification = document.createElement('div');
            notification.className = `notification notification-${type}`;
            notification.textContent = message;
            notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 12px 20px;
                border-radius: 6px;
                color: white;
                font-weight: 500;
                z-index: 10000;
                animation: slideIn 0.3s ease;
            `;
            
            switch (type) {
                case 'success':
                    notification.style.background = '#36b37e';
                    break;
                case 'error':
                    notification.style.background = '#ff5630';
                    break;
                default:
                    notification.style.background = '#0052cc';
            }
            
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.style.animation = 'slideOut 0.3s ease';
                setTimeout(() => {
                    if (notification.parentNode) {
                        notification.parentNode.removeChild(notification);
                    }
                }, 300);
            }, 3000);
        },
        
        // Formatiert Zeitstempel
        formatTimestamp: function(timestamp) {
            const date = new Date(timestamp);
            return date.toLocaleString('de-DE', {
                day: '2-digit',
                month: '2-digit',
                year: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
            });
        }
    };
    
    // Epic-Management-Funktionen
    const EpicManager = {
        // Aktualisiert den Status eines Epics
        refreshEpicStatus: function(entryId) {
            const container = document.querySelector(`[data-entry-id="${entryId}"]`);
            if (!container) return;
            
            // Zeigt Loading-Indikator
            this.showLoadingState(container);
            
            // Simuliert API-Aufruf (in echter Implementierung würde hier ein AJAX-Call stehen)
            setTimeout(() => {
                this.hideLoadingState(container);
                Utils.showNotification('Epic-Status aktualisiert', 'success');
                
                // Aktualisiert die Seite, um neue Daten zu laden
                location.reload();
            }, 1500);
        },
        
        // Zeigt Epic-Details in einem Modal
        showEpicDetails: function(entryId) {
            const container = document.querySelector(`[data-entry-id="${entryId}"]`);
            if (!container) return;
            
            const epicName = container.querySelector('.epic-name').textContent;
            const jiraKey = container.dataset.jiraKey;
            const status = container.querySelector('.status-badge').textContent;
            
            const modal = this.createModal('Epic-Details', `
                <div class="epic-details-content">
                    <div class="detail-row">
                        <label>Epic Name:</label>
                        <span>${epicName}</span>
                    </div>
                    <div class="detail-row">
                        <label>Jira Key:</label>
                        <span>${jiraKey || 'Noch nicht verfügbar'}</span>
                    </div>
                    <div class="detail-row">
                        <label>Status:</label>
                        <span>${status}</span>
                    </div>
                    <div class="detail-row">
                        <label>Entry ID:</label>
                        <span>${entryId}</span>
                    </div>
                </div>
            `);
            
            document.body.appendChild(modal);
        },
        
        // Wiederholt die Epic-Erstellung
        retryEpicCreation: function(entryId) {
            if (confirm('Möchten Sie die Epic-Erstellung wirklich wiederholen?')) {
                Utils.showNotification('Epic-Erstellung wird wiederholt...', 'info');
                
                // Hier würde in der echten Implementierung ein IFTTT-Trigger ausgelöst
                setTimeout(() => {
                    location.reload();
                }, 2000);
            }
        },
        
        // Zeigt Loading-State
        showLoadingState: function(container) {
            const overlay = document.createElement('div');
            overlay.className = 'loading-overlay';
            overlay.innerHTML = `
                <div class="loading-content">
                    <div class="spinner"></div>
                    <span>Wird aktualisiert...</span>
                </div>
            `;
            overlay.style.cssText = `
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(255, 255, 255, 0.9);
                display: flex;
                align-items: center;
                justify-content: center;
                border-radius: 8px;
                z-index: 100;
            `;
            
            container.style.position = 'relative';
            container.appendChild(overlay);
        },
        
        // Versteckt Loading-State
        hideLoadingState: function(container) {
            const overlay = container.querySelector('.loading-overlay');
            if (overlay) {
                overlay.remove();
            }
        },
        
        // Erstellt ein Modal
        createModal: function(title, content) {
            const modal = document.createElement('div');
            modal.className = 'epic-modal';
            modal.innerHTML = `
                <div class="modal-backdrop" onclick="this.parentNode.remove()"></div>
                <div class="modal-content">
                    <div class="modal-header">
                        <h3>${title}</h3>
                        <button class="modal-close" onclick="this.closest('.epic-modal').remove()">×</button>
                    </div>
                    <div class="modal-body">
                        ${content}
                    </div>
                </div>
            `;
            modal.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                z-index: 10000;
                display: flex;
                align-items: center;
                justify-content: center;
            `;
            
            return modal;
        }
    };
    
    // Auto-Refresh für bidirektionale Updates
    const AutoRefresh = {
        intervalId: null,
        retryCount: 0,
        
        start: function() {
            this.intervalId = setInterval(() => {
                this.checkForUpdates();
            }, CONFIG.refreshInterval);
        },
        
        stop: function() {
            if (this.intervalId) {
                clearInterval(this.intervalId);
                this.intervalId = null;
            }
        },
        
        checkForUpdates: function() {
            const incompleteEntries = document.querySelectorAll('[data-jira-key=""], [data-jira-key="null"]');
            
            if (incompleteEntries.length > 0 && this.retryCount < CONFIG.maxRetries) {
                this.retryCount++;
                console.log(`Checking for updates... Attempt ${this.retryCount}`);
                
                setTimeout(() => {
                    location.reload();
                }, 1000);
            } else if (incompleteEntries.length === 0) {
                this.retryCount = 0;
            }
        }
    };
    
    // Event-Listener
    document.addEventListener('DOMContentLoaded', function() {
        // Globale Funktionen verfügbar machen
        window.copyToClipboard = Utils.copyToClipboard.bind(Utils);
        window.refreshEpicStatus = EpicManager.refreshEpicStatus.bind(EpicManager);
        window.showEpicDetails = EpicManager.showEpicDetails.bind(EpicManager);
        window.retryEpicCreation = EpicManager.retryEpicCreation.bind(EpicManager);
        
        // Auto-Refresh starten
        AutoRefresh.start();
        
        // CSS-Animationen hinzufügen
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideIn {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            
            @keyframes slideOut {
                from { transform: translateX(0); opacity: 1; }
                to { transform: translateX(100%); opacity: 0; }
            }
            
            .modal-backdrop {
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: rgba(0, 0, 0, 0.5);
            }
            
            .modal-content {
                background: white;
                border-radius: 8px;
                max-width: 500px;
                width: 90%;
                max-height: 80vh;
                overflow-y: auto;
                position: relative;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            }
            
            .modal-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px;
                border-bottom: 1px solid #e1e5e9;
            }
            
            .modal-header h3 {
                margin: 0;
                color: #172b4d;
            }
            
            .modal-close {
                background: none;
                border: none;
                font-size: 24px;
                cursor: pointer;
                color: #6b778c;
                padding: 0;
                width: 30px;
                height: 30px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .modal-body {
                padding: 20px;
            }
            
            .epic-details-content .detail-row {
                display: flex;
                justify-content: space-between;
                padding: 8px 0;
                border-bottom: 1px solid #f4f5f7;
            }
            
            .epic-details-content .detail-row:last-child {
                border-bottom: none;
            }
            
            .epic-details-content label {
                font-weight: 600;
                color: #172b4d;
            }
            
            .loading-content {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 12px;
                color: #172b4d;
                font-weight: 500;
            }
        `;
        document.head.appendChild(style);
    });
    
    // Cleanup beim Verlassen der Seite
    window.addEventListener('beforeunload', function() {
        AutoRefresh.stop();
    });
})();
```

## Erweiterte ConfiForms Table-Integration

### Table-Konfiguration für bidirektionale Daten

```
Makro: ConfiForms Table
Parameter:
- Form name: epicCreator
- Filter: id IS NOT EMPTY
- Sort by: createdDate
- Sort order: DESC
- Show search: true
- Show pagination: true
- Items per page: 15
- Enable row selection: true
- Show export options: true
- Enable column sorting: true
```

### Table-Header-Konfiguration

```html
<thead>
    <tr>
        <th data-sort="epicName">Epic Name</th>
        <th data-sort="jiraKey">Jira Key</th>
        <th data-sort="epicStatus">Status</th>
        <th data-sort="createdDate">Erstellt</th>
        <th data-sort="completedAt">Abgeschlossen</th>
        <th>Aktionen</th>
    </tr>
</thead>
```

### Table-Body-Template

```html
<tbody>
    <tr data-entry-id="[entry.id]" class="table-row status-[entry.epicStatus|lowercase]">
        <td class="epic-name-cell">
            <div class="epic-name-container">
                <span class="epic-name-text">[entry.epicName]</span>
                <small class="epic-creator">von [entry.createdBy]</small>
            </div>
        </td>
        <td class="jira-key-cell">
            <div class="jira-key-container" data-condition="[entry.jiraKey] IS NOT EMPTY">
                <span class="jira-key-badge">[entry.jiraKey]</span>
                <a href="[entry.jiraUrl]" target="_blank" class="jira-link-icon" title="In Jira öffnen">
                    <svg viewBox="0 0 24 24" width="14" height="14">
                        <path d="M19 19H5V5h7V3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"/>
                    </svg>
                </a>
            </div>
            <div class="processing-indicator-small" data-condition="[entry.jiraKey] IS EMPTY">
                <div class="spinner-small"></div>
                <span>Wird erstellt...</span>
            </div>
        </td>
        <td class="status-cell">
            <span class="status-badge-small status-[entry.epicStatus|lowercase]">[entry.epicStatus]</span>
        </td>
        <td class="date-cell">
            [entry.createdDate|dateFormat:dd.MM.yyyy HH:mm]
        </td>
        <td class="date-cell">
            <span data-condition="[entry.completedAt] IS NOT EMPTY">
                [entry.completedAt|dateFormat:dd.MM.yyyy HH:mm]
            </span>
            <span data-condition="[entry.completedAt] IS EMPTY" class="not-completed">
                -
            </span>
        </td>
        <td class="actions-cell">
            <div class="table-actions">
                <button class="table-action-btn" onclick="refreshEpicStatus('[entry.id]')" title="Aktualisieren">
                    <svg viewBox="0 0 24 24" width="12" height="12">
                        <path d="M17.65 6.35C16.2 4.9 14.21 4 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"/>
                    </svg>
                </button>
                <button class="table-action-btn" onclick="showEpicDetails('[entry.id]')" title="Details">
                    <svg viewBox="0 0 24 24" width="12" height="12">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                    </svg>
                </button>
            </div>
        </td>
    </tr>
</tbody>
```

Die erweiterte Benutzeroberfläche bietet eine umfassende, benutzerfreundliche Darstellung der bidirektionalen Datenverknüpfung mit modernen UI-Elementen, Real-time-Updates und erweiterten Interaktionsmöglichkeiten.

