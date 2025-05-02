import uuid

from fastapi import APIRouter, UploadFile, Header, Response, status

from typing import Annotated
import app.services.file_service as file_svc
from app.model.statement_data import StatementData

router = APIRouter(prefix="/statement", tags=["statement"])

@router.post("/upload", status_code=201)
async def upload_statement(file: list[UploadFile],
                           x_user_id: Annotated[uuid.UUID | None, Header()] = None):
    statements: list[StatementData] = []
    for f in file:
        statement_data = file_svc.extract_file_information_then_move(f, str(x_user_id))
        statements.append(statement_data)

    return Response(status_code=status.HTTP_201_CREATED)