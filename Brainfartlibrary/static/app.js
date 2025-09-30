// Brainfart Library - Enhanced Frontend Application

class PromptLibrary {
  constructor() {
    this.currentPrompts = [];
    this.currentFilter = "all";
    this.currentColorFilter = null;
    this.selectedTags = [];
    this.availableTagsList = [];
    this.availableColors = [];
    this.selectedPromptTags = [];
    this.selectedPromptColor = "none";
    this.isEditing = false;
    this.editingPromptId = null;
    this.init();
  }

  init() {
    this.bindEvents();
    this.loadInitialData();
  }

  bindEvents() {
    // Navigation Events
    document
      .getElementById("newPromptBtn")
      .addEventListener("click", () => this.showNewPromptForm());
    document.getElementById("refreshBtn").addEventListener("click", () => this.loadInitialData());
    document.getElementById("cancelEditBtn").addEventListener("click", () => this.showListView());

    // Form Events
    document.getElementById("promptForm").addEventListener("submit", (e) => this.handleSubmit(e));
    document.getElementById("deletePromptBtn").addEventListener("click", () => this.deletePrompt());

    // Search Events
    document
      .getElementById("searchInput")
      .addEventListener("input", (e) => this.handleSearch(e.target.value));
    document.getElementById("searchBtn").addEventListener("click", () => this.handleSearch());

    // Filter Events
    document.querySelectorAll("[data-filter]").forEach((btn) => {
      btn.addEventListener("click", (e) => this.handleFilter(e.target.dataset.filter, e.target));
    });

    // Tag Management Events
    document
      .getElementById("manageTagsBtn")
      .addEventListener("click", () => this.showTagManagement());
    document
      .getElementById("closeTagManagementBtn")
      .addEventListener("click", () => this.showListView());
    document.getElementById("addTagBtn").addEventListener("click", () => this.addNewTag());
    document.getElementById("newTagInput").addEventListener("keypress", (e) => {
      if (e.key === "Enter") this.addNewTag();
    });

    // Color Filter Clear
    document
      .getElementById("clearColorFilter")
      .addEventListener("click", () => this.clearColorFilter());

    // Enter key for Search
    document.getElementById("searchInput").addEventListener("keypress", (e) => {
      if (e.key === "Enter") this.handleSearch();
    });
  }

  async loadInitialData() {
    await Promise.all([
      this.loadPrompts(),
      this.loadAvailableTags(),
      this.loadColors(),
      this.loadStats(),
    ]);
    this.renderColorFilters();
  }

  async apiCall(endpoint, options = {}) {
    try {
      const response = await fetch(`/api${endpoint}`, {
        headers: {
          "Content-Type": "application/json",
          ...options.headers,
        },
        ...options,
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error("API Error:", error);
      this.showError(`Fehler bei API-Aufruf: ${error.message}`);
      throw error;
    }
  }

  async loadPrompts(status = null, color = null) {
    try {
      let endpoint = "/prompts";
      const params = new URLSearchParams();

      if (status) params.append("status", status);
      if (color) params.append("color", color);

      if (params.toString()) endpoint += `?${params.toString()}`;

      this.currentPrompts = await this.apiCall(endpoint);
      this.renderPrompts();
    } catch (error) {
      this.showError("Prompts konnten nicht geladen werden");
    }
  }

  async loadAvailableTags() {
    try {
      this.availableTagsList = await this.apiCall("/tags/available");
    } catch (error) {
      console.error("Tags loading failed:", error);
      this.availableTagsList = [];
    }
  }

  async loadColors() {
    try {
      this.availableColors = await this.apiCall("/colors");
    } catch (error) {
      console.error("Colors loading failed:", error);
    }
  }

  async loadStats() {
    try {
      const stats = await this.apiCall("/stats");
      this.renderStats(stats);
    } catch (error) {
      console.error("Stats loading failed:", error);
    }
  }

  renderPrompts() {
    const container = document.getElementById("promptCards");

    if (this.currentPrompts.length === 0) {
      container.innerHTML = `
                <div class="col-12 text-center py-5">
                    <i class="bi bi-lightbulb" style="font-size: 3rem; color: #dee2e6;"></i>
                    <p class="text-muted mt-3">Keine Prompts gefunden</p>
                    <button class="btn btn-primary" onclick="promptLib.showNewPromptForm()">
                        <i class="bi bi-plus"></i> Ersten Prompt erstellen
                    </button>
                </div>
            `;
      return;
    }

    container.innerHTML = this.currentPrompts
      .map((prompt) => this.renderPromptCard(prompt))
      .join("");
  }

  renderPromptCard(prompt) {
    const createdDate = new Date(prompt.created_at).toLocaleDateString("de-DE");
    const updatedDate = new Date(prompt.updated_at).toLocaleDateString("de-DE");
    const hasHistory = prompt.history && prompt.history.length > 0;
    const colorClass = `color-${prompt.color || "none"}`;

    return `
            <div class="col-md-6 col-lg-4 mb-3">
                <div class="card prompt-card ${colorClass}" onclick="promptLib.editPrompt('${prompt.id}')">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-start mb-2">
                            <h6 class="card-title mb-0">${this.escapeHtml(prompt.title)}</h6>
                            <span class="badge status-badge status-${prompt.status}">
                                ${prompt.status === "active" ? "Aktiv" : "Entwurf"}
                            </span>
                        </div>
                        <p class="card-text text-muted small mb-2">
                            ${this.escapeHtml(prompt.content.substring(0, 100))}${prompt.content.length > 100 ? "..." : ""}
                        </p>
                        ${
                          prompt.tags.length > 0
                            ? `
                            <div class="prompt-tags mb-2">
                                ${prompt.tags
                                  .map(
                                    (tag) =>
                                      `<span class="badge tag-badge">${this.escapeHtml(tag)}</span>`,
                                  )
                                  .join("")}
                            </div>
                        `
                            : ""
                        }
                        <div class="prompt-meta d-flex justify-content-between">
                            <small>
                                <i class="bi bi-calendar"></i> ${createdDate}
                                ${hasHistory ? `<i class="bi bi-clock-history ms-2" title="Version ${prompt.version}"></i>` : ""}
                            </small>
                            ${
                              updatedDate !== createdDate
                                ? `<small class="text-success">Geändert: ${updatedDate}</small>`
                                : ""
                            }
                        </div>
                    </div>
                </div>
            </div>
        `;
  }

  renderColorFilters() {
    const container = document.getElementById("colorFilterList");

    if (!this.availableColors || this.availableColors.length === 0) {
      container.innerHTML = '<small class="text-muted">Laden...</small>';
      return;
    }

    // Nur Farben anzeigen, außer "none"
    const visibleColors = this.availableColors.filter((c) => c.value !== "none");

    container.innerHTML = visibleColors
      .map(
        (color) => `
            <div class="color-filter-btn ${this.currentColorFilter === color.value ? "active" : ""}"
                 style="background-color: ${this.getColorHex(color.value)};"
                 onclick="promptLib.filterByColor('${color.value}')"
                 title="${color.name}">
            </div>
        `,
      )
      .join("");
  }

  renderStats(stats) {
    document.getElementById("totalPrompts").textContent = stats.total_prompts;
    document.getElementById("totalDrafts").textContent = stats.total_drafts;
    const lastModified = new Date(stats.last_modified).toLocaleString("de-DE");
    document.getElementById("lastModified").textContent = lastModified;
  }

  async handleSubmit(e) {
    e.preventDefault();

    const formData = {
      title: document.getElementById("promptTitle").value.trim(),
      content: document.getElementById("promptContent").value.trim(),
      tags: this.selectedPromptTags,
      color: this.selectedPromptColor,
      status: document.getElementById("promptStatus").value,
    };

    if (!formData.title || !formData.content) {
      this.showError("Titel und Inhalt sind erforderlich");
      return;
    }

    try {
      if (this.editingPromptId) {
        await this.apiCall(`/prompts/${this.editingPromptId}`, {
          method: "PUT",
          body: JSON.stringify(formData),
        });
        this.showSuccess("Prompt erfolgreich aktualisiert");
      } else {
        await this.apiCall("/prompts", {
          method: "POST",
          body: JSON.stringify(formData),
        });
        this.showSuccess("Prompt erfolgreich erstellt");
      }

      this.showListView();
      await this.loadInitialData();
    } catch (error) {
      this.showError("Prompt konnte nicht gespeichert werden");
    }
  }

  async deletePrompt() {
    if (!this.editingPromptId) return;

    if (!confirm("Sind Sie sicher, dass Sie diesen Prompt löschen möchten?")) {
      return;
    }

    try {
      await this.apiCall(`/prompts/${this.editingPromptId}`, {
        method: "DELETE",
      });

      this.showSuccess("Prompt erfolgreich gelöscht");
      this.showListView();
      await this.loadInitialData();
    } catch (error) {
      this.showError("Prompt konnte nicht gelöscht werden");
    }
  }

  async editPrompt(promptId) {
    try {
      const prompt = await this.apiCall(`/prompts/${promptId}`);
      this.showEditForm(prompt);
    } catch (error) {
      this.showError("Prompt konnte nicht geladen werden");
    }
  }

  showNewPromptForm() {
    this.showEditForm(null);
  }

  showEditForm(prompt = null) {
    this.isEditing = true;
    this.editingPromptId = prompt?.id || null;

    // Form füllen
    document.getElementById("promptId").value = prompt?.id || "";
    document.getElementById("promptTitle").value = prompt?.title || "";
    document.getElementById("promptContent").value = prompt?.content || "";
    document.getElementById("promptStatus").value = prompt?.status || "active";

    // Tags setzen
    this.selectedPromptTags = prompt?.tags || [];
    this.renderTagSelector();

    // Farbe setzen
    this.selectedPromptColor = prompt?.color || "none";
    this.renderColorPalette();

    // Delete button anzeigen/verstecken
    const deleteBtn = document.getElementById("deletePromptBtn");
    if (prompt) {
      deleteBtn.classList.remove("d-none");
    } else {
      deleteBtn.classList.add("d-none");
    }

    // Views umschalten
    document.getElementById("promptListView").classList.add("d-none");
    document.getElementById("promptEditView").classList.remove("d-none");
    document.getElementById("tagManagementView").classList.add("d-none");

    // Focus auf Titel
    document.getElementById("promptTitle").focus();
  }

  renderColorPalette() {
    const container = document.getElementById("colorPalette");

    if (!this.availableColors || this.availableColors.length === 0) {
      container.innerHTML = '<small class="text-muted">Laden...</small>';
      return;
    }

    container.innerHTML = this.availableColors
      .map(
        (color) => `
            <div class="color-option ${this.selectedPromptColor === color.value ? "selected" : ""}"
                 style="background-color: ${this.getColorHex(color.value)};"
                 onclick="promptLib.selectColor('${color.value}')"
                 title="${color.name}">
            </div>
        `,
      )
      .join("");
  }

  selectColor(color) {
    this.selectedPromptColor = color;
    this.renderColorPalette();
  }

  renderTagSelector() {
    const selectedContainer = document.getElementById("selectedTags");
    const availableContainer = document.getElementById("availableTags");

    // Ausgewählte Tags
    if (this.selectedPromptTags.length === 0) {
      selectedContainer.innerHTML = '<small class="text-muted">Keine Tags ausgewählt</small>';
    } else {
      selectedContainer.innerHTML = this.selectedPromptTags
        .map(
          (tag) => `
                <span class="badge tag-badge selected" onclick="promptLib.removeTagFromPrompt('${this.escapeHtml(tag)}')">
                    ${this.escapeHtml(tag)} <i class="bi bi-x"></i>
                </span>
            `,
        )
        .join("");
    }

    // Verfügbare Tags (die noch nicht ausgewählt sind)
    const availableTags = this.availableTagsList.filter(
      (tag) => !this.selectedPromptTags.includes(tag),
    );

    if (availableTags.length === 0) {
      availableContainer.innerHTML =
        '<small class="text-muted">Alle Tags bereits ausgewählt</small>';
    } else {
      availableContainer.innerHTML = availableTags
        .map(
          (tag) => `
                <span class="badge tag-badge" onclick="promptLib.addTagToPrompt('${this.escapeHtml(tag)}')">
                    ${this.escapeHtml(tag)} <i class="bi bi-plus"></i>
                </span>
            `,
        )
        .join("");
    }
  }

  addTagToPrompt(tag) {
    if (!this.selectedPromptTags.includes(tag)) {
      this.selectedPromptTags.push(tag);
      this.renderTagSelector();
    }
  }

  removeTagFromPrompt(tag) {
    this.selectedPromptTags = this.selectedPromptTags.filter((t) => t !== tag);
    this.renderTagSelector();
  }

  showListView() {
    this.isEditing = false;
    this.editingPromptId = null;
    this.selectedPromptTags = [];
    this.selectedPromptColor = "none";

    document.getElementById("promptEditView").classList.add("d-none");
    document.getElementById("tagManagementView").classList.add("d-none");
    document.getElementById("promptListView").classList.remove("d-none");

    // Form zurücksetzen
    document.getElementById("promptForm").reset();
  }

  async handleSearch(query = null) {
    const searchQuery = query || document.getElementById("searchInput").value.trim();

    if (!searchQuery) {
      await this.loadPrompts(
        this.currentFilter === "all" ? null : this.currentFilter,
        this.currentColorFilter,
      );
      return;
    }

    try {
      const tagQuery = this.selectedTags.length > 0 ? this.selectedTags.join(",") : null;
      const endpoint = `/search?q=${encodeURIComponent(searchQuery)}${tagQuery ? `&tags=${encodeURIComponent(tagQuery)}` : ""}`;

      this.currentPrompts = await this.apiCall(endpoint);

      // Zusätzlicher Farbfilter auf Suchergebnisse anwenden
      if (this.currentColorFilter) {
        this.currentPrompts = this.currentPrompts.filter(
          (p) => p.color === this.currentColorFilter,
        );
      }

      this.renderPrompts();
    } catch (error) {
      this.showError("Suche fehlgeschlagen");
    }
  }

  async handleFilter(filter, button) {
    this.currentFilter = filter;

    // Button states
    document.querySelectorAll("[data-filter]").forEach((btn) => btn.classList.remove("active"));
    button.classList.add("active");

    // Load filtered prompts
    const status = filter === "all" ? null : filter;
    await this.loadPrompts(status, this.currentColorFilter);
  }

  async filterByColor(color) {
    if (this.currentColorFilter === color) {
      // Toggle off
      this.currentColorFilter = null;
      document.getElementById("clearColorFilter").style.display = "none";
    } else {
      this.currentColorFilter = color;
      document.getElementById("clearColorFilter").style.display = "inline";
    }

    this.renderColorFilters();

    const status = this.currentFilter === "all" ? null : this.currentFilter;
    await this.loadPrompts(status, this.currentColorFilter);
  }

  async clearColorFilter() {
    this.currentColorFilter = null;
    document.getElementById("clearColorFilter").style.display = "none";
    this.renderColorFilters();

    const status = this.currentFilter === "all" ? null : this.currentFilter;
    await this.loadPrompts(status, null);
  }

  // Tag Management Functions
  showTagManagement() {
    document.getElementById("promptListView").classList.add("d-none");
    document.getElementById("promptEditView").classList.add("d-none");
    document.getElementById("tagManagementView").classList.remove("d-none");

    this.renderManagedTags();
  }

  renderManagedTags() {
    const container = document.getElementById("managedTagsList");

    if (this.availableTagsList.length === 0) {
      container.innerHTML = '<small class="text-muted">Keine Tags vorhanden</small>';
      return;
    }

    container.innerHTML = this.availableTagsList
      .map(
        (tag) => `
            <div class="managed-tag-item position-relative d-inline-block">
                <span class="badge tag-badge">${this.escapeHtml(tag)}</span>
                <button class="delete-tag-btn" onclick="promptLib.deleteTag('${this.escapeHtml(tag)}')">
                    ×
                </button>
            </div>
        `,
      )
      .join("");
  }

  async addNewTag() {
    const input = document.getElementById("newTagInput");
    const tag = input.value.trim();

    if (!tag) {
      this.showError("Bitte einen Tag-Namen eingeben");
      return;
    }

    if (this.availableTagsList.includes(tag)) {
      this.showError("Dieser Tag existiert bereits");
      return;
    }

    try {
      await this.apiCall("/tags", {
        method: "POST",
        body: JSON.stringify({ tag }),
      });

      this.showSuccess(`Tag "${tag}" erfolgreich hinzugefügt`);
      input.value = "";

      await this.loadAvailableTags();
      this.renderManagedTags();
    } catch (error) {
      this.showError("Tag konnte nicht hinzugefügt werden");
    }
  }

  async deleteTag(tag) {
    if (!confirm(`Tag "${tag}" wirklich löschen?\n\nDieser wird von allen Prompts entfernt.`)) {
      return;
    }

    try {
      const result = await this.apiCall(`/tags/${encodeURIComponent(tag)}`, {
        method: "DELETE",
      });

      this.showSuccess(
        `Tag "${tag}" wurde gelöscht (${result.removed_from_prompts} Prompt(s) aktualisiert)`,
      );

      await this.loadAvailableTags();
      this.renderManagedTags();
      await this.loadPrompts(); // Refresh prompts to reflect changes
    } catch (error) {
      this.showError("Tag konnte nicht gelöscht werden");
    }
  }

  // Utility Functions
  getColorHex(colorName) {
    const colorMap = {
      none: "#f8f9fa",
      red: "#dc3545",
      orange: "#fd7e14",
      yellow: "#ffc107",
      green: "#198754",
      teal: "#20c997",
      blue: "#0d6efd",
      indigo: "#6610f2",
      purple: "#6f42c1",
      pink: "#d63384",
      brown: "#795548",
      gray: "#6c757d",
      black: "#212529",
    };
    return colorMap[colorName] || "#f8f9fa";
  }

  escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
  }

  showError(message) {
    alert(`❌ Fehler: ${message}`);
  }

  showSuccess(message) {
    alert(`✅ ${message}`);
  }
}

// App initialisieren wenn DOM geladen ist
document.addEventListener("DOMContentLoaded", () => {
  window.promptLib = new PromptLibrary();
});
