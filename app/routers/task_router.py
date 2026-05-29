from fastapi import APIRouter, HTTPException, status, Query
from app.schemas.task_schema import TaskCreate, TaskResponse, TaskListResponse, TaskUpdate, TaskPriority, TaskStatus
from app.services.task_service import create_task, list_tasks, get_task_by_id, update_task, delete_task

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create(task_data: TaskCreate):
    return create_task(task_data)

@router.get("/", response_model=TaskListResponse)
def list_all(
    status: TaskStatus | None = None, 
    priority: TaskPriority | None = None,
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100)
):
    return list_tasks(
        status=status, 
        priority=priority,
        page=page,
        limit=limit
    )

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