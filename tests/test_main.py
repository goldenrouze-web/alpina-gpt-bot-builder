from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from app.main import app, get_client

client = TestClient(app)


@pytest.fixture(autouse=True)
def fake_openai():
    """Подменяем OpenAI-клиент заглушкой для всех тестов модуля."""
    fake_completion = MagicMock()
    fake_completion.choices = [
        MagicMock(message=MagicMock(content="Привет из мока!"))
    ]

    fake_client = MagicMock()
    fake_client.chat.completions.create.return_value = fake_completion

    app.dependency_overrides[get_client] = lambda: fake_client
    yield fake_client
    app.dependency_overrides.clear()


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_chat_validation():
    r = client.post("/chat", json={})
    assert r.status_code == 422


def test_chat_success(fake_openai):
    r = client.post("/chat", json={"message": "Привет"})
    assert r.status_code == 200
    assert r.json() == {"response": "Привет из мока!"}
    fake_openai.chat.completions.create.assert_called_once()
