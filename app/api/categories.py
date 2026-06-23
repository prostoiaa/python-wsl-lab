from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app.schemas import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(
    category_id: int,
    db: Session = Depends(get_db)
):

    category = crud.get_category(db, category_id)

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    return category


@router.post("/", response_model=CategoryResponse)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    return crud.create_category(
        db,
        category.title
    )


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db)
):

    result = crud.update_category(
        db,
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
def delete_category(
    category_id: int,
    db: Session = Depends(get_db)
):

    if not crud.get_category(db, category_id):
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    crud.delete_category(db, category_id)

    return {"message": "Category deleted"}