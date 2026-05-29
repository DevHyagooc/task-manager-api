import math
from app.schemas.task_schema import TaskCreate, TaskUpdate

tasks = []
next_id = 1

def create_task(task_data: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task_data.title,
        "description": task_data.description,
        "priority": task_data.priority,
        "status": task_data.status,
    }

    tasks.append(new_task)
    next_id += 1

    return new_task

def list_tasks(
        status: str | None = None, 
        priority: str | None = None,
        page: int = 1,
        limit: int = 10,
):
    filtered_tasks = tasks

    if status:
        filtered_tasks = [
            task for task in filtered_tasks
            if task["status"] == status
        ]
    
    if priority:
        filtered_tasks = [
            task for task in filtered_tasks
            if task["priority"] == priority
        ]

    total = len(filtered_tasks)
    total_pages = math.ceil(total / limit) if total > 0 else 0

    start = (page - 1) * limit
    end = start + limit

    paginated_tasks = filtered_tasks[start:end]

    return {
        "data": paginated_tasks,
        "meta": {
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": total_pages
        }
    }

def get_task_by_id(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
        
    return None

def update_task(task_id: int, task_data: TaskUpdate):
    task = get_task_by_id(task_id)

    if task is None:
        return None
    
    update_data = task_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        task[field] = value
    
    return task

def delete_task(task_id: int):
    task = get_task_by_id(task_id)

    if task is None:
        return False
    
    tasks.remove(task)
    return True