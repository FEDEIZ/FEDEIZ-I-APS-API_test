from ast import List

from api.src.domain.paper.entity import Paper




class Author:
    def __init__(self, id: int, name: str, papers: List[Paper]):
        self.id = id
        self.name = name
