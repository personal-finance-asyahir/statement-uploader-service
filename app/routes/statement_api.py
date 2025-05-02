import uuid

from fastapi import APIRouter, UploadFile, Header

from typing import Annotated
import app.services.file_service as file_svc
from app.model.statement_data import StatementData

router = APIRouter(prefix="/statement", tags=["statement"])

@router.post("/upload")
async def upload_statement(file: list[UploadFile],
                           x_user_id: Annotated[uuid.UUID | None, Header()] = None):
    statements: list[StatementData] = []
    for f in file:
        statement_data = file_svc.extract_file_information(f.file)
        statements.append(statement_data)
        statement_data.file_path = file_svc.move_file_directory(f, str(x_user_id))

    return {"hello": statements}