from PyPDF2 import PdfReader

from fastapi import UploadFile

from app.model.settings import Settings
from app.model.statement_data import StatementData
from io import BytesIO
from app.utils.statement_matcher import STATEMENT_MATCHERS
from pathlib import Path
from datetime import datetime
import shutil


def extract_file_information_then_move(file: UploadFile, user_id: str) -> StatementData:
    contents = file.file.read()
    buffer = BytesIO(contents)
    author, title = __extract_file_information(buffer)
    path = __move_file_directory(file, user_id)

    return StatementData(author, title, path)

def __extract_file_information(buffer: BytesIO) -> tuple[str | None, str | None]:
    pdf_reader = PdfReader(buffer)
    metadata = pdf_reader.metadata

    if metadata and metadata.title and metadata.author:
        return metadata.author, metadata.title

    page = pdf_reader.pages[0]
    text = page.extract_text()

    for matcher in STATEMENT_MATCHERS:
        result = matcher.match(text)
        if result:
            return result

    return None, None


def __move_file_directory(file: UploadFile, user_id: str) -> str | None:
    date_time = datetime.today().strftime('%Y-%m-%d')
    settings = Settings()
    upload_dir = Path(settings.upload_dir)
    destination_path = upload_dir / user_id / str(date_time)
    destination_path.mkdir(parents=True, exist_ok=True)

    destination_path = destination_path / file.filename

    file.file.seek(0)
    with destination_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(destination_path)