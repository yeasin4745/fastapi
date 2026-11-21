from fastapi import APIRouter, HTTPException, status, Response

from app.schemas.item import (
    ItemCreate,
    ItemUpdate,
    ItemResponse
)

from app.services import item_service


router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


# CREATE
@router.post(
    "/",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED
)
def create_item(item: ItemCreate):

    return item_service.create_item(item)


# READ ALL
@router.get(
    "/",
    response_model=list[ItemResponse]
)
def get_all_items():

    return item_service.get_all_items()


# READ ONE
@router.get(
    "/{item_id}",
    response_model=ItemResponse
)
def get_item(item_id: int):

    item = item_service.get_item(item_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return item


# UPDATE
@router.put(
    "/{item_id}",
    response_model=ItemResponse
)
def update_item(item_id: int, item: ItemUpdate):

    updated_item = item_service.update_item(
        item_id,
        item
    )

    if updated_item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return updated_item


# DELETE
@router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_item(item_id: int):

    deleted = item_service.delete_item(item_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return Response(status_code=204)
