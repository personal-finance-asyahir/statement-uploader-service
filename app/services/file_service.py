from PyPDF2 import PdfReader
from typing import BinaryIO
from app.model.statement_data import StatementData
from io import BytesIO
from app.utils.statement_matcher import STATEMENT_MATCHERS

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