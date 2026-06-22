from fastapi import APIRouter, HTTPException
from app.db import crud
from app.schemas import CategoryCreate

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/")
def get_categories():
    return crud.get_categories()


@router.get("/{category_id}")
def get_category(category_id: int):

    category = crud.get_category(category_id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


@router.post("/")
def create_category(category: CategoryCreate):
    return crud.create_category(category.title)


@router.put("/{category_id}")
def update_category(category_id: int, category: CategoryCreate):

    result = crud.update_category(
        category_id,
        category.title
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return result


@router.delete("/{category_id}")
def delete_category(category_id: int):

    if not crud.get_category(category_id):
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    crud.delete_category(category_id)

    return {"message": "Category deleted"}
