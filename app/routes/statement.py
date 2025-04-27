import uuid

from fastapi import APIRouter

from app.model import UploadRequest

router = APIRouter(prefix="/statement", tags=["statement"])

@router.put("/upload")
async def upload_statement(request: UploadRequest):
    print("user_id: ", request.user_id)
    return {"hello": "world"}