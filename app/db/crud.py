from .db import SessionLocal
from .models import Category, Book


# ---------------- CATEGORY ----------------

def create_category(title: str):
    db = SessionLocal()
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    db.close()
    return category


def get_categories():
    db = SessionLocal()
    data = db.query(Category).all()
    db.close()
    return data


def get_category(category_id: int):
    db = SessionLocal()
    category = db.query(Category).filter(Category.id == category_id).first()
    db.close()
    return category


def update_category(category_id: int, title: str):
    db = SessionLocal()
    category = db.query(Category).filter(Category.id == category_id).first()

    if category:
        category.title = title
        db.commit()
        db.refresh(category)

    db.close()
    return category


def delete_category(category_id: int):
    db = SessionLocal()
    category = db.query(Category).filter(Category.id == category_id).first()

    if category:
        db.delete(category)
        db.commit()

    db.close()


# ---------------- BOOK ----------------

def create_book(title, description, price, url, category_id):
    db = SessionLocal()

    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )

    db.add(book)
    db.commit()
    db.refresh(book)
    db.close()

    return book


def get_books():
    db = SessionLocal()
    data = db.query(Book).all()
    db.close()
    return data


def get_book(book_id: int):
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == book_id).first()
    db.close()
    return book


def update_book(
    book_id: int,
    title=None,
    description=None,
    price=None,
    url=None,
    category_id=None
):
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == book_id).first()

    if book:
        if title is not None:
            book.title = title
        if description is not None:
            book.description = description
        if price is not None:
            book.price = price
        if url is not None:
            book.url = url
        if category_id is not None:
            book.category_id = category_id

        db.commit()
        db.refresh(book)

    db.close()
    return book


def delete_book(book_id: int):
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == book_id).first()

    if book:
        db.delete(book)
        db.commit()

    db.close()
