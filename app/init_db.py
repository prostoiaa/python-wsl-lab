from app.db.db import Base, engine
from app.db import crud


def init_db():
    # создаём таблицы
    Base.metadata.create_all(bind=engine)

    # создаём категории
    cat1 = crud.create_category("Фантастика")
    cat2 = crud.create_category("Образование")

    # создаём книги
    crud.create_book(
        "Дюна",
        "Книга про пустынную планету",
        500,
        "",
        cat1.id
    )

    crud.create_book(
        "Гарри Поттер",
        "Школа магии",
        400,
        "",
        cat1.id
    )

    crud.create_book(
        "Python для начинающих",
        "Учебник по Python",
        600,
        "",
        cat2.id
    )


if __name__ == "__main__":
    init_db()
    print("База данных заполнена")