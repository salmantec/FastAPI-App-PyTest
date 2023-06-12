from fastapi import APIRouter

from src.app.api.models import NoteSchema, NoteDB
from src.app.api import crud

router = APIRouter()

@router.post("/", response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await crud.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description
    }

    return response_object