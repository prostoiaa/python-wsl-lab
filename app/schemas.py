from pydantic import BaseModel


# ---------------- CATEGORY ----------------

class CategoryCreate(BaseModel):
    title: str


class CategoryUpdate(BaseModel):
    title: str


class CategoryResponse(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True


# ---------------- BOOK ----------------

class BookCreate(BaseModel):
    title: str
    description: str | None = None
    price: int
    url: str | None = None
    category_id: int


class BookUpdate(BaseModel):
    title: str
    description: str | None = None
    price: int
    url: str | None = None
    category_id: int


class BookResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    price: int
    url: str | None = None
    category_id: int

    class Config:
        from_attributes = True