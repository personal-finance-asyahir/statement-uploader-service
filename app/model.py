from pydantic import BaseModel


class UploadRequest(BaseModel):
    user_id: str