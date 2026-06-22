from .models import Category, Book


# ---------------- CATEGORY ----------------

def create_category(db, title: str):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_categories(db):
    return db.query(Category).all()


def get_category(db, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def update_category(db, category_id: int, title: str):
    category = get_category(db, category_id)

    if category:
        category.title = title
        db.commit()
        db.refresh(category)

    return category


def delete_category(db, category_id: int):
    category = get_category(db, category_id)

    if category:
        db.delete(category)
        db.commit()


# ---------------- BOOK ----------------

def create_book(db, title, description, price, url, category_id):
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
    return book


def get_books(db, category_id=None):
    query = db.query(Book)

    if category_id:
        query = query.filter(Book.category_id == category_id)

    return query.all()


def get_book(db, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(db, book_id: int, **kwargs):
    book = get_book(db, book_id)

    if not book:
        return None

    for key, value in kwargs.items():
        if value is not None:
            setattr(book, key, value)

    db.commit()
    db.refresh(book)
    return book


def delete_book(db, book_id: int):
    book = get_book(db, book_id)

    if book:
        db.delete(book)
        db.commit()