from fastapi import FastAPI

from app.routes import statement

app = FastAPI()

app.include_router(statement.router)