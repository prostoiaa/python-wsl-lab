from fastapi import FastAPI
from app.db.db import Base, engine

from app.api import books, categories

app = FastAPI()

# создаём таблицы при старте
Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(categories.router)
app.include_router(books.router)