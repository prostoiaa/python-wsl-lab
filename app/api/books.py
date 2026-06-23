from fastapi import APIRouter, Query, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app.schemas import BookCreate, BookUpdate, BookResponse

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
def get_books(
    category_id: int | None = Query(None),
    db: Session = Depends(get_db)
):
    return crud.get_books(db, category_id)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):

    if not crud.get_category(db, book.category_id):
        raise HTTPException(status_code=404, detail="Category not found")

    return crud.create_book(
        db,
        book.title,
        book.description,
        book.price,
        book.url,
        book.category_id
    )


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book: BookUpdate,
    db: Session = Depends(get_db)
):

    if not crud.get_category(db, book.category_id):
        raise HTTPException(status_code=404, detail="Category not found")

    result = crud.update_book(
        db=db,
        book_id=book_id,
        title=book.title,
        description=book.description,
        price=book.price,
        url=book.url,
        category_id=book.category_id
    )

    if not result:
        raise HTTPException(status_code=404, detail="Book not found")

    return result


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):

    if not crud.get_book(db, book_id):
        raise HTTPException(status_code=404, detail="Book not found")

    crud.delete_book(db, book_id)

    return {"message": "Book deleted"}