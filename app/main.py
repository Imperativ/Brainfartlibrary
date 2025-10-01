from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Optional
from pydantic import BaseModel
import uvicorn
import os
import sys

# Relativen Import-Pfad korrigieren
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from app.database import PromptDatabase
from app.models import Prompt, PromptCreate, PromptUpdate, PromptStatus, PromptColor

# Request Models für Tag-Management
class TagCreate(BaseModel):
    tag: str

class TagDelete(BaseModel):
    tag: str

# FastAPI App initialisieren
app = FastAPI(
    title="Brainfart Library",
    description="Lokale Prompt-Bibliothek für LLM-Prompts",
    version="1.0.0"
)

# Absolute Pfade für Static Files und Templates
project_root = parent_dir
static_path = os.path.join(project_root, "static")
templates_path = os.path.join(project_root, "templates")

app.mount("/static", StaticFiles(directory=static_path), name="static")
templates = Jinja2Templates(directory=templates_path)

# Datenbank initialisieren mit absolutem Pfad
data_path = os.path.join(project_root, "data", "prompts.json")
db = PromptDatabase(data_path)

# Web-Interface Route
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Hauptseite der Web-Anwendung"""
    return templates.TemplateResponse("index.html", {"request": request})

# API Routen - Prompts
@app.get("/api/prompts", response_model=List[Prompt])
async def get_prompts(status: Optional[PromptStatus] = None, color: Optional[PromptColor] = None):
    """Alle Prompts abrufen, optional gefiltert nach Status und/oder Farbe"""
    return db.get_all_prompts(status=status, color=color)

@app.get("/api/prompts/{prompt_id}", response_model=Prompt)
async def get_prompt(prompt_id: str):
    """Einzelnen Prompt abrufen"""
    prompt = db.get_prompt(prompt_id)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt nicht gefunden")
    return prompt

@app.post("/api/prompts", response_model=Prompt)
async def create_prompt(prompt_data: PromptCreate):
    """Neuen Prompt erstellen"""
    return db.create_prompt(prompt_data)

@app.put("/api/prompts/{prompt_id}", response_model=Prompt)
async def update_prompt(prompt_id: str, update_data: PromptUpdate):
    """Prompt aktualisieren"""
    prompt = db.update_prompt(prompt_id, update_data)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt nicht gefunden")
    return prompt

@app.delete("/api/prompts/{prompt_id}")
async def delete_prompt(prompt_id: str):
    """Prompt löschen"""
    success = db.delete_prompt(prompt_id)
    if not success:
        raise HTTPException(status_code=404, detail="Prompt nicht gefunden")
    return {"message": "Prompt erfolgreich gelöscht"}

@app.get("/api/search", response_model=List[Prompt])
async def search_prompts(q: str, tags: Optional[str] = None):
    """Prompts durchsuchen"""
    tag_list = tags.split(",") if tags else None
    return db.search_prompts(q, tag_list)

# API Routen - Tag-Management
@app.get("/api/tags", response_model=List[str])
async def get_all_tags():
    """Alle verfügbaren Tags abrufen"""
    return db.get_all_tags()

@app.get("/api/tags/available", response_model=List[str])
async def get_available_tags():
    """Liste der verwalteten Tags abrufen"""
    return db.get_available_tags()

@app.post("/api/tags", response_model=dict)
async def add_tag(tag_data: TagCreate):
    """Neuen Tag zur Verwaltungsliste hinzufügen"""
    success = db.add_tag(tag_data.tag)
    if not success:
        raise HTTPException(status_code=400, detail="Tag existiert bereits")
    return {"message": "Tag erfolgreich hinzugefügt", "tag": tag_data.tag}

@app.delete("/api/tags/{tag}")
async def delete_tag(tag: str):
    """Tag aus Verwaltungsliste und allen Prompts entfernen"""
    count = db.delete_tag(tag)
    return {
        "message": "Tag erfolgreich gelöscht",
        "tag": tag,
        "removed_from_prompts": count
    }

# API Routen - Statistiken
@app.get("/api/stats")
async def get_stats():
    """Statistiken abrufen"""
    database = db.load_database()
    return {
        "total_prompts": database.metadata.total_prompts,
        "total_drafts": database.metadata.total_drafts,
        "last_modified": database.metadata.last_modified,
        "version": database.metadata.version
    }

@app.get("/api/colors", response_model=List[dict])
async def get_available_colors():
    """Alle verfügbaren Farben abrufen"""
    return [
        {"value": color.value, "name": color.value.capitalize()}
        for color in PromptColor
    ]

# Server starten
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
