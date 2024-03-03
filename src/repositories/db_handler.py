from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.database import Database
from typing import Any, List
from src.repositories.db_handler_base import DBHandlerBase


class DBHandler(DBHandlerBase):

    def __init__(self, db: Database, collection_name):
        self.collection: Collection = db[collection_name]

    def find(self, keys_and_values: dict[str, any]) -> List[Any]:
        cursor: Cursor = self.collection.find(keys_and_values)
        return list(cursor)
