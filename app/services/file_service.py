from PyPDF2 import PdfReader
from typing import BinaryIO

from fastapi import UploadFile

from app.model.statement_data import StatementData
from io import BytesIO
from app.utils.statement_matcher import STATEMENT_MATCHERS
from pathlib import Path
from datetime import datetime
import shutil

DESTINATION_PATH = Path("/Users/syahirghariff/Developer/personal-finance-project/bank_statement")


def extract_file_information(file: BinaryIO) -> StatementData:
    contents = file.read()
    buffer = BytesIO(contents)
    pdf_reader = PdfReader(buffer)
    metadata = pdf_reader.metadata

    if metadata and metadata.title and metadata.author:
        return StatementData(metadata.author, metadata.title)

    page = pdf_reader.pages[0]
    text = page.extract_text()

    for matcher in STATEMENT_MATCHERS:
        result = matcher.match(text)
        if result:
            return result

    return StatementData(author=None, title=None)


def move_file_directory(file: UploadFile, user_id: str) -> str | None:
    date_time = datetime.today().strftime('%Y-%m-%d')
    destination_path = DESTINATION_PATH / user_id / str(date_time)
    destination_path.mkdir(parents=True, exist_ok=True)

    destination_path = destination_path / file.filename

    file.file.seek(0)
    with destination_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(destination_path)