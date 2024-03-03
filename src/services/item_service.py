from typing import Any

from fastapi import HTTPException
from starlette import status

from db import db
from src.repositories import db_handler


class ItemService:
    def __init__(self):
        self.db_handler = db_handler.DBHandler(db, "ITEMS")

    def get_all_items_by(self, key: str, value: Any):
        items = self.db_handler.find({key: value})
        if items:
            return items
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"items with {key} {value} not found")
