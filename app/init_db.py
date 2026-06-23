from app.db.db import Base, engine, SessionLocal
from app.db import crud


def init_db():
    # создаём таблицы
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # создаём категории
        cat1 = crud.create_category(db, "Фантастика")
        cat2 = crud.create_category(db, "Образование")

        # создаём книги
        crud.create_book(
            db,
            "Дюна",
            "Книга про пустынную планету",
            500,
            "",
            cat1.id
        )

        crud.create_book(
            db,
            "Гарри Поттер",
            "Школа магии",
            400,
            "",
            cat1.id
        )

        crud.create_book(
            db,
            "Python для начинающих",
            "Учебник по Python",
            600,
            "",
            cat2.id
        )

    finally:
        db.close()


if __name__ == "__main__":
    init_db()
    print("База данных заполнена")