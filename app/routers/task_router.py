from fastapi import APIRouter, HTTPException, status
from app.schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import createTask, list_tasks, get_task_by_id, update_task, delete_task

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create(task_data: TaskCreate):
    return createTask(task_data)

@router.get("/", response_model=list[TaskResponse])
def list_all(status: str | None = None, priority: str | None = None):
    return list_tasks(status=status, priority=priority)

@router.get("/{task_id}", response_model=TaskResponse)
def get_by_id(task_id: int):
    task = get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    
    return task

@router.patch("/{task_id}", response_model=TaskResponse)
def update(task_id: int, task_data: TaskUpdate):
    task = update_task(task_id, task_data)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    
    return task

@router.delete("/{task_id}")
def delete(task_id: int):
    deleted = delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada"
        )
    
    return {"message": "Tarefa deletada com sucesso"}