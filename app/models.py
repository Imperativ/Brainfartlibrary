from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict
from pydantic import BaseModel

class PromptStatus(str, Enum):
    ACTIVE = "active"
    DRAFT = "draft"

class PromptColor(str, Enum):
    NONE = "none"
    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    TEAL = "teal"
    BLUE = "blue"
    INDIGO = "indigo"
    PURPLE = "purple"
    PINK = "pink"
    BROWN = "brown"
    GRAY = "gray"
    BLACK = "black"

class PromptVersion(BaseModel):
    version: int
    content: str
    updated_at: datetime
    title: Optional[str] = None

class Prompt(BaseModel):
    id: str
    title: str
    content: str
    tags: List[str] = []
    color: PromptColor = PromptColor.NONE
    status: PromptStatus = PromptStatus.ACTIVE
    created_at: datetime
    updated_at: datetime
    version: int = 1
    history: List[PromptVersion] = []

class PromptCreate(BaseModel):
    title: str
    content: str
    tags: List[str] = []
    color: PromptColor = PromptColor.NONE
    status: PromptStatus = PromptStatus.ACTIVE

class PromptUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None
    color: Optional[PromptColor] = None
    status: Optional[PromptStatus] = None

class DatabaseMetadata(BaseModel):
    version: str
    created_at: datetime
    last_modified: datetime
    total_prompts: int
    total_drafts: int

class TagManagement(BaseModel):
    available_tags: List[str] = []

class Database(BaseModel):
    prompts: Dict[str, Prompt] = {}
    metadata: DatabaseMetadata
    tag_management: TagManagement = TagManagement()
