from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)

    description: str | None = None

    price: float = Field(gt=0)

    in_stock: bool = True


class ItemUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)

    description: str | None = None

    price: float = Field(gt=0)

    in_stock: bool


class ItemResponse(BaseModel):
    id: int

    name: str

    description: str | None

    price: float

    in_stock: bool
