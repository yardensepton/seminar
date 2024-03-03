from typing import Any

from src.services.item_service import ItemService


class ItemController:

    def __init__(self):
        self.itemService = ItemService()

    def get_all_items_by(self,key:str, value:Any):
        return self.itemService.get_all_items_by(key,value)

