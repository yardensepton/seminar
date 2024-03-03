from abc import ABC, abstractmethod
from typing import Any, List


class DBHandlerBase(ABC):

    @abstractmethod
    def find(self, keys_and_values: dict[str, str]) -> List[Any]:
        pass
