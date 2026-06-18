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