import json

import pytest
from src.app.api import crud


def test_create_note(test_app, monkeypatch):
    test_request_payload = {"title": "Something", "description": "Something else"}
    test_response_payload = {"id": 1, "title": "Something", "description": "Something else"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    response = test_app.post("/notes/", content=json.dumps(test_request_payload), )

    assert response.status_code == 201
    assert response.json() == test_response_payload


def test_create_note_invalid_json(test_app):
    response = test_app.post("/notes", content=json.dumps({"title": "something"}))
    assert response.status_code == 422
