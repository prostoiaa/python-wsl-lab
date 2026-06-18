from app.db import crud


def main():
    print("\n📚 КАТЕГОРИИ:")
    for c in crud.get_categories():
        print(f"{c.id} - {c.title}")

    print("\n📖 КНИГИ:")
    for b in crud.get_books():
        print(f"{b.id} - {b.title} | {b.price} | cat={b.category_id}")


if __name__ == "__main__":
    main()