from abc import ABC, abstractmethod
from typing import List
from .entity import Author

class AuthorRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Author]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Author:
        pass

    @abstractmethod
    def create(self, name: str, papers: List[Paper]) -> Author:
        pass

    @abstractmethod
    def update(self, author: Author) -> Author:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
