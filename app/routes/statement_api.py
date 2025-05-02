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
        statement_data.user_id = x_user_id
        statements.append(statement_data)

    return {"hello": statements}