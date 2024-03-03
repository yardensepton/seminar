from pymongo.cursor import Cursor
from src.repositories.db_handler_base import DBHandlerBase
import json
from typing import Any, List

class DBJson(DBHandlerBase):
    def __init__(self, json_file_path: str = "items.json", items_data: List[dict[str, Any]] = None):
        self.json_file_path = json_file_path
        self.items_data = items_data or self.load_items()

    def load_items(self):
        with open(self.json_file_path, "r") as file:
            return json.load(file)

    def find(self, keys_and_values: dict[str, any]) -> List[Any]:
        filtered_items = []
        for item in self.items_data:
            # Check if the item matches the query parameters
            if all(item.get(key) == value for key, value in keys_and_values.items()):
                filtered_items.append(item)

        return filtered_items