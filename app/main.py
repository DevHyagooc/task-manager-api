from fastapi import FastAPI
from app.routers.task_router import router as tasks_router
from fastapi.exceptions import RequestValidationError
from app.core.exception_handlers import validation_exception_handler

app = FastAPI(
    title="Task Manager API",
    description="API para gerenciamento de tarefas com FastAPI",
    version="1.0.0"
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.include_router(tasks_router)