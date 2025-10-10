import json
import os
import uuid
from datetime import datetime
from typing import List, Optional, Dict, Any

try:
    from .models import Database, Prompt, PromptCreate, PromptUpdate, PromptStatus, PromptColor, DatabaseMetadata, PromptVersion, TagManagement
except ImportError:
    from app.models import Database, Prompt, PromptCreate, PromptUpdate, PromptStatus, PromptColor, DatabaseMetadata, PromptVersion, TagManagement

class PromptDatabase:
    def __init__(self, db_path: str = "data/prompts.json"):
        self.db_path = db_path
        self.ensure_database_exists()

    def ensure_database_exists(self):
        """Erstellt die Datenbank-Datei, falls sie nicht existiert"""
        if not os.path.exists(self.db_path):
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            initial_data = {
                "prompts": {},
                "metadata": {
                    "version": "1.0.0",
                    "created_at": datetime.now().isoformat(),
                    "last_modified": datetime.now().isoformat(),
                    "total_prompts": 0,
                    "total_drafts": 0
                },
                "tag_management": {
                    "available_tags": []
                }
            }
            self.save_database(initial_data)

    def load_database(self) -> Database:
        """Lädt die Datenbank aus der JSON-Datei"""
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Backward compatibility: Füge tag_management hinzu falls nicht vorhanden
                if "tag_management" not in data:
                    data["tag_management"] = {"available_tags": []}
                return Database(**data)
        except Exception as e:
            print(f"Fehler beim Laden der Datenbank: {e}")
            return self.create_empty_database()

    def save_database(self, data: Dict[str, Any]):
        """Speichert die Datenbank in die JSON-Datei"""
        try:
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        except Exception as e:
            print(f"Fehler beim Speichern der Datenbank: {e}")

    def create_empty_database(self) -> Database:
        """Erstellt eine leere Datenbank"""
        metadata = DatabaseMetadata(
            version="1.0.0",
            created_at=datetime.now(),
            last_modified=datetime.now(),
            total_prompts=0,
            total_drafts=0
        )
        tag_management = TagManagement(available_tags=[])
        return Database(prompts={}, metadata=metadata, tag_management=tag_management)

    def create_prompt(self, prompt_data: PromptCreate) -> Prompt:
        """Erstellt einen neuen Prompt"""
        db = self.load_database()
        prompt_id = str(uuid.uuid4())
        now = datetime.now()

        prompt = Prompt(
            id=prompt_id,
            title=prompt_data.title,
            content=prompt_data.content,
            tags=prompt_data.tags,
            color=prompt_data.color,
            status=prompt_data.status,
            created_at=now,
            updated_at=now,
            version=1,
            history=[]
        )

        db.prompts[prompt_id] = prompt
        db.metadata.last_modified = now

        if prompt_data.status == PromptStatus.ACTIVE:
            db.metadata.total_prompts += 1
        else:
            db.metadata.total_drafts += 1

        # Auto-add neue Tags zur Verwaltungsliste
        for tag in prompt_data.tags:
            if tag not in db.tag_management.available_tags:
                db.tag_management.available_tags.append(tag)
        db.tag_management.available_tags.sort()

        self.save_database(db.dict())
        return prompt

    def get_prompt(self, prompt_id: str) -> Optional[Prompt]:
        """Ruft einen Prompt ab"""
        db = self.load_database()
        return db.prompts.get(prompt_id)

    def get_all_prompts(self, status: Optional[PromptStatus] = None, color: Optional[PromptColor] = None) -> List[Prompt]:
        """Ruft alle Prompts ab, optional gefiltert nach Status und/oder Farbe"""
        db = self.load_database()
        prompts = list(db.prompts.values())

        if status:
            prompts = [p for p in prompts if p.status == status]

        if color:
            prompts = [p for p in prompts if p.color == color]

        return sorted(prompts, key=lambda x: x.updated_at, reverse=True)

    def update_prompt(self, prompt_id: str, update_data: PromptUpdate) -> Optional[Prompt]:
        """Aktualisiert einen Prompt und speichert die alte Version"""
        db = self.load_database()

        if prompt_id not in db.prompts:
            return None

        prompt = db.prompts[prompt_id]

        # Alte Version zur Historie hinzufügen
        if update_data.content and update_data.content != prompt.content:
            old_version = PromptVersion(
                version=prompt.version,
                content=prompt.content,
                updated_at=prompt.updated_at,
                title=prompt.title
            )
            prompt.history.append(old_version)
            prompt.version += 1

        # Prompt aktualisieren
        now = datetime.now()

        if update_data.title is not None:
            prompt.title = update_data.title

        if update_data.content is not None:
            prompt.content = update_data.content

        if update_data.tags is not None:
            prompt.tags = update_data.tags
            # Auto-add neue Tags zur Verwaltungsliste
            for tag in update_data.tags:
                if tag not in db.tag_management.available_tags:
                    db.tag_management.available_tags.append(tag)
            db.tag_management.available_tags.sort()

        if update_data.color is not None:
            prompt.color = update_data.color

        if update_data.status is not None:
            old_status = prompt.status
            prompt.status = update_data.status

            # Metadaten-Zähler anpassen
            if old_status != update_data.status:
                if old_status == PromptStatus.ACTIVE:
                    db.metadata.total_prompts -= 1
                else:
                    db.metadata.total_drafts -= 1

                if update_data.status == PromptStatus.ACTIVE:
                    db.metadata.total_prompts += 1
                else:
                    db.metadata.total_drafts += 1

        prompt.updated_at = now
        db.metadata.last_modified = now

        self.save_database(db.dict())
        return prompt

    def delete_prompt(self, prompt_id: str) -> bool:
        """Löscht einen Prompt"""
        db = self.load_database()

        if prompt_id not in db.prompts:
            return False

        prompt = db.prompts[prompt_id]

        if prompt.status == PromptStatus.ACTIVE:
            db.metadata.total_prompts -= 1
        else:
            db.metadata.total_drafts -= 1

        del db.prompts[prompt_id]
        db.metadata.last_modified = datetime.now()

        self.save_database(db.dict())
        return True

    def search_prompts(self, query: str, tags: Optional[List[str]] = None) -> List[Prompt]:
        """Sucht Prompts nach Titel und Tags"""
        db = self.load_database()
        results = []
        query_lower = query.lower()

        for prompt in db.prompts.values():
            # Titel-Suche
            title_match = query_lower in prompt.title.lower()

            # Tag-Suche
            tag_match = any(query_lower in tag.lower() for tag in prompt.tags)

            # Spezifische Tag-Filter
            if tags:
                has_required_tags = all(tag in prompt.tags for tag in tags)
            else:
                has_required_tags = True

            if (title_match or tag_match) and has_required_tags:
                results.append(prompt)

        return sorted(results, key=lambda x: x.updated_at, reverse=True)

    def get_all_tags(self) -> List[str]:
        """Ruft alle aktuell verwendeten Tags ab"""
        db = self.load_database()
        all_tags = set()
        for prompt in db.prompts.values():
            all_tags.update(prompt.tags)
        return sorted(list(all_tags))

    # Tag-Management Methoden
    def get_available_tags(self) -> List[str]:
        """Ruft die verwaltete Liste verfügbarer Tags ab"""
        db = self.load_database()
        return sorted(db.tag_management.available_tags)

    def add_tag(self, tag: str) -> bool:
        """Fügt einen neuen Tag zur Verwaltungsliste hinzu"""
        db = self.load_database()

        tag = tag.strip()
        if not tag or tag in db.tag_management.available_tags:
            return False

        db.tag_management.available_tags.append(tag)
        db.tag_management.available_tags.sort()
        db.metadata.last_modified = datetime.now()

        self.save_database(db.dict())
        return True

    def delete_tag(self, tag: str) -> int:
        """Löscht einen Tag aus der Verwaltungsliste und entfernt ihn von allen Prompts"""
        db = self.load_database()

        # Aus Verwaltungsliste entfernen
        if tag in db.tag_management.available_tags:
            db.tag_management.available_tags.remove(tag)

        # Von allen Prompts entfernen
        removed_count = 0
        for prompt in db.prompts.values():
            if tag in prompt.tags:
                prompt.tags.remove(tag)
                removed_count += 1

        db.metadata.last_modified = datetime.now()
        self.save_database(db.dict())

        return removed_count
