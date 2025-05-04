import uuid
from dataclasses import asdict

from fastapi import APIRouter, UploadFile, Header, Response, status, BackgroundTasks
from typing import Annotated
import app.services.file_service as file_svc
from app.model.statement_data import StatementData
from app.services.kafka_producer_service import KafkaProducerService
import json

router = APIRouter(prefix="/statement", tags=["statement"])

@router.post("/upload", status_code=201)
async def upload_statement(file: list[UploadFile],
                           background_tasks: BackgroundTasks,
                           x_user_id: Annotated[uuid.UUID | None, Header()] = None):
    statements: list[StatementData] = []
    for f in file:
        statement_data = file_svc.extract_file_information_then_move(f, str(x_user_id))
        statements.append(statement_data)
    background_tasks.add_task(__send_kafka_message, statements, x_user_id)

    return Response(status_code=status.HTTP_201_CREATED)

def __send_kafka_message(statements: list[StatementData], x_user_id: uuid.UUID):
    kafka_producer = KafkaProducerService()
    statements_payload = []
    for statement in statements:
        statements_payload.append(asdict(statement))
    serialized_data = json.dumps(statements_payload).encode("utf-8")
    print('serialized_data:', serialized_data)
    kafka_producer.send_event("file.upload", str(x_user_id), serialized_data)