from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    brand: str
    cost: float
    weight: int
    alternative:int
