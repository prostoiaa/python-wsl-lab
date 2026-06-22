# Python WSL Lab

## Описание

REST API для работы с книгами и категориями с использованием FastAPI, PostgreSQL и SQLAlchemy.

## Установка

```bash
git clone https://github.com/prostoiaa/python-wsl-lab.git
cd python-wsl-lab
```

Создание виртуального окружения:

```bash
python -m venv venv
source venv/bin/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Создать файл `.env`:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345
```

## Запуск проекта

```bash
uvicorn app.main:app --reload
```

Swagger-документация:

```text
http://127.0.0.1:8000/docs
```

## Структура проекта

* app/main.py
* app/schemas.py
* app/api/books.py
* app/api/categories.py
* app/db/db.py
* app/db/models.py
* app/db/crud.py
