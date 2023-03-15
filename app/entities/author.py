from typing import List

from api.app.entities.paper import Paper

class Author:
    def __init__(self, id: str, name: str, papers: List[Paper]):
        self.id = id
        self.name = name
        self.papers = papers
