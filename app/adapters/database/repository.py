from abc import ABC, abstractmethod
from typing import List

from app.entities.paper import Paper
from app.entities.author import Author
from app.entities.category import Category


class Repository(ABC):
    @abstractmethod
    def list_papers(self) -> List[Paper]:
        pass

    @abstractmethod
    def get_paper(self, id: str) -> Paper:
        pass

    @abstractmethod
    def list_authors(self) -> List[Author]:
        pass

    @abstractmethod
    def get_author(self, id: str) -> Author:
        pass

    @abstractmethod
    def list_categories(self) -> List[Category]:
        pass

    @abstractmethod
    def get_category(self, id: str) -> Category:
        pass
