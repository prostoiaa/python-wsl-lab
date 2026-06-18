from fastapi import APIRouter
from app.db import crud
from app.schemas import CategoryCreate

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/")
def get_categories():
    return crud.get_categories()


@router.post("/")
def create_category(category: CategoryCreate):
    return crud.create_category(category.title)