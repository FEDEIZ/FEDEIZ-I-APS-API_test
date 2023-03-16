from abc import ABC, abstractmethod
from typing import List
from .entity import Category

class CategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Category]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Category:
        pass

    @abstractmethod
    def create(self, name: str, papers: List[Paper]) -> Category:
        pass

    @abstractmethod
    def update(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
