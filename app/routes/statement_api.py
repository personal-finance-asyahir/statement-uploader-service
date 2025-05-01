import uuid

from fastapi import APIRouter, UploadFile, Header

from typing import Annotated
import app.services.file_service as file_svc
from app.model.statement_data import StatementData

router = APIRouter(prefix="/statement", tags=["statement"])

@router.post("/upload")
async def upload_statement(file: list[UploadFile],
                           x_user_id: Annotated[uuid.UUID | None, Header()] = None):
    print("testing file: ", file)
    all_statement = []
    for f in file:
        # print("testing loop in file: ", f)
        # statement_data: StatementData = file_svc.extract_file_title(f.file)
        # all_statement.append(statement_data)
        # print('syahir testing x: ', statement_data)

        test = file_svc.extract_file_information(f.file)
        all_statement.append(test)
        # print('this is test with pdfplumber: ', test)

    print("testing user_id: ", x_user_id)

    return {"hello": all_statement}