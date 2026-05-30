from fastapi import FastAPI
from app.routers.task_router import router as tasks_router
from fastapi.exceptions import RequestValidationError
from app.core.exception_handlers import validation_exception_handler
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.include_router(tasks_router)