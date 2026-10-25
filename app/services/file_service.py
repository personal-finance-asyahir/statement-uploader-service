from fastapi import UploadFile
from pypdf import PdfReader, mult
from types import SimpleNamespace
from app.model.settings import Settings
from app.model.statement_data import StatementData
from io import BytesIO
from pathlib import Path
from datetime import datetime
from app.utils.statement_extractor_util import *
import shutil
import hashlib

def extract_file_information_then_move(file: UploadFile, user_id: str) -> StatementData:
    contents = file.file.read()
    buffer = BytesIO(contents)
    statement_data = __extract_file_information(buffer)
    path = __move_file_directory(file, user_id)
    statement_data.file_path = path

    return statement_data

def __extract_file_information(buffer: BytesIO) -> StatementData:

    def visitor_body(text, cm, tm, font_dict, font_size):
        text = text.strip()
        if not text:
            return

        txt2user = mult(tm, cm)
        idx = txt2user[4:]

        if metadata.author == 'Maybank2U.com':
            if metadata.title == 'Credit Card Statement':
                maybank_credit_card_statement_extractor(obj, idx, text)
            if metadata.title == 'Saving Account Statement':
                maybank_debit_card_statement_extractor(obj, idx, text)


    pdf_reader = PdfReader(buffer)
    metadata = pdf_reader.metadata
    obj = SimpleNamespace()
    page = pdf_reader.pages[0]
    page.extract_text(visitor_text=visitor_body)

    statement_data = StatementData(name=obj.name,
                                   bank=obj.bank,
                                   title=obj.title,
                                   statement_date=obj.statement_date,
                                   account_number=obj.account_number)

    if hasattr(obj, 'current_balance'):
        statement_data.current_balance = obj.current_balance
    if hasattr(obj, 'previous_balance'):
        statement_data.previous_balance = obj.previous_balance


    return statement_data

def __move_file_directory(file: UploadFile, user_id: str) -> str | None:
    date_time = datetime.today().strftime('%Y-%m-%d')
    settings = Settings()
    upload_dir = Path(settings.upload_dir)
    destination_path = upload_dir / user_id / str(date_time)
    destination_path.mkdir(parents=True, exist_ok=True)

    original_filename = file.filename or ''
    md5_hash = hashlib.md5(original_filename.encode('utf-8')).hexdigest()
    filename = f"{md5_hash}.pdf"

    destination_path = destination_path / filename

    file.file.seek(0)
    with destination_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return str(destination_path)