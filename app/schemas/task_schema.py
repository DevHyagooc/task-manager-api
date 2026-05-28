from typing import Optional, Literal
from pydantic import BaseModel

TaskPriority = Literal["low", "medium", "high"]
TaskStatus = Literal["pending", "in_progress", "done"]
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: TaskPriority = "medium"
    status: TaskStatus = "pending"

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[TaskPriority] = None
    status: Optional[TaskStatus] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: str
    status: str