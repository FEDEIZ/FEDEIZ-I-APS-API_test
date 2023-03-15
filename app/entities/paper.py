from typing import List

from api.app.entities.author import Author
from api.app.entities.category import Category


class Paper:
    def __init__(self, id: str, title: str, abstract: str, authors: List[Author], categories: List[Category], publication_date: str):
        self.id = id
        self.title = title
        self.abstract = abstract
        self.authors = authors
        self.categories = categories
        self.publication_date = publication_date
