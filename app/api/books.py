from fastapi import APIRouter, Query
from app.db import crud
from app.schemas import BookCreate

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
def get_books(category_id: int | None = Query(None)):
    books = crud.get_books()

    if category_id:
        books = [b for b in books if b.category_id == category_id]

    return books


@router.post("/")
def create_book(book: BookCreate):
    return crud.create_book(
        book.title,
        book.description,
        book.price,
        book.url,
        book.category_id
    )