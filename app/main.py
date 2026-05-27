from fastapi import FastAPI
from app.routers.task_router import router as tasks_router

app = FastAPI(
    title="Task Manager API",
    description="API para gerenciamento de tarefas com FastAPI",
    version="1.0.0"
)

app.include_router(tasks_router)