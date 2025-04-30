import uuid

from fastapi import APIRouter, UploadFile, Header

from typing import Annotated

router = APIRouter(prefix="/statement", tags=["statement"])

@router.post("/upload")
async def upload_statement(file: list[UploadFile],
                           x_user_id: Annotated[uuid.UUID | None, Header()] = None):
    print("testing file: ", file)
    for f in file:
        print("testing loop in file: ", f)
    print("testing user_id: ", x_user_id)
    return {"hello": x_user_id}