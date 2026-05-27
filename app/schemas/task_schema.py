from typing import Optional, Literal
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Literal["low", "medium", "high"] = "medium"
    status: Literal["pending", "in_progress", "done"] = "pending"

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[Literal["low", "medium", "high"]] = None
    status: Optional[Literal["pending", "in_progress", "done"]] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    status: str