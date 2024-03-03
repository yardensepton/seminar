from typing import List, Union

from fastapi import APIRouter, Query

from src.controllers.item_controller import ItemController
from src.entity.item import Item

router = APIRouter(
    prefix="/items",
    tags=["ITEMS"]
)

items_controller = ItemController()


@router.get("", response_model=Union[List[Item], Item])
async def get_items(
        name: str = Query(None, description="Name of the item"),
        alternative: int = Query(None, description="Alternative parameter"),
        item_id: int = Query(None, description="Item ID parameter")
):
    if name:
        return items_controller.get_all_items_by(key="name", value=name)
    elif alternative is not None:
        return items_controller.get_all_items_by(key="alternative", value=alternative)
    elif item_id is not None:
        return items_controller.get_all_items_by(key="id", value=item_id)
    else:
        return items_controller.get_all_items_by(key="all", value=None)
