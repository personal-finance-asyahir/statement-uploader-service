from PyPDF2 import PdfReader
from typing import BinaryIO
from app.model.statement_data import StatementData
from io import BytesIO


CREDIT_CARD_STATEMENT = "Credit Card Statement"
CIMB_BANK = "CIMB"


def extract_file_information(file: BinaryIO) -> StatementData:
    contents = file.read()
    buffer = BytesIO(contents)
    pdf_reader = PdfReader(buffer)
    metadata = pdf_reader.metadata
    title = metadata.title
    author = metadata.author

    if title and author:
        return StatementData(author, title)

    page = pdf_reader.pages[0]
    text = page.extract_text()

    if CREDIT_CARD_STATEMENT.casefold() in text.casefold():
        title = "Credit Card Statement"

    if CIMB_BANK.casefold() in text.casefold():
        author = CIMB_BANK

    return StatementData(author, title)

# def extract_file_title(file: BinaryIO) -> StatementData:
#     pdf_reader = PdfReader(file)
#     metadata = pdf_reader.metadata
#     title = metadata.title
#     author = metadata.author
#     statement_data = StatementData(author, title)
#     # page = pdf_reader.pages[0]
#     # print('test page: ', page)
#     # text = page.extract_text()
#     # print('test text: ', text)
#     return statement_data

def __py_pdf_metadata(file: BytesIO) -> StatementData | None:
    pdf_reader = PdfReader(file)
    metadata = pdf_reader.metadata
    title = metadata.title
    author = metadata.author

    if title and author:
        return StatementData(author, title)

    return None

def __visitor_header(text, cm, tm, fontDic, fontSize):
    y = tm[5]
    print("y", y)

def __py_pdf_text(file: BytesIO) -> str:
    pdf_reader = PdfReader(file)
    page = pdf_reader.pages[0]
    text = page.extract_text()
    print('test text: ', text)
    return "test"

def __pdf_plumber_text() -> StatementData | None:
    return None

def extract_file_metadata(file: BinaryIO):
    contents = file.read()
    buffer = BytesIO(contents)

    # pdf_reader = PdfReader(buffer)
    # metadata = pdf_reader.metadata
    # title = metadata.title
    # author = metadata.author

    # if title and author:
    #     return StatementData(author, title)
    # else:

    statement_data = __py_pdf_metadata(buffer)

    if statement_data is None:
        # statement_data = __pdf_plumber_text()
        __py_pdf_text(buffer)

    return statement_data


    # with pdfplumber.open(buffer) as pdf:
    #
    #     metadata = pdf.metadata
    #     print('test pdf: ', pdf)
    #     pdf.pages[0].extract_words()
    # text = ""
    # with pdfplumber.open(file) as pdf:
    #     for page in pdf.pages:
    #         text += page.extract_text() or ""
    # return text