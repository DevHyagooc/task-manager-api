import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services import task_service

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_tasks():
    task_service.tasks.clear()
    task_service.next_id = 1

def create_task(
    title: str = "Estudar Python",
    description: str = "Criar testes automatizados",
    priority: str = "high",
    status: str = "pending"
):
    return client.post(
        "/tasks",
        json={
            "title": title,
            "description": description,
            "priority": priority,
            "status": status
        }
    )

def test_should_create_task():
    response = create_task()

    print(response.status_code)
    print(response.json())

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Estudar Python"
    assert data["description"] == "Criar testes automatizados"
    assert data["priority"] == "high"
    assert data["status"] == "pending"

def test_should_get_task_by_id():
    create_task()

    response = client.get("/tasks/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Estudar Python"

def test_should_return_404_not_found():
    response = client.get("/tasks/80")

    assert response.status_code == 404
    assert response.json()["detail"] == "Tarefa não encontrada"

def test_should_update_task():
    create_task()

    response = client.patch(
        "/tasks/1",
        json={
            "status": "done"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Estudar Python"
    assert data["status"] == "done"

def test_should_delete_task():
    create_task()

    response = client.delete("/tasks/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Tarefa deletada com sucesso"

    get_response = client.get("/tasks/1")

    assert get_response.status_code == 404