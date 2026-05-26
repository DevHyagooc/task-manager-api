from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="API para gerenciamento de tarefas com FastAPI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Task Manager API está rodando"
    }

@app.get("/health")
def root():
    return {
        "status": "ok"
    }