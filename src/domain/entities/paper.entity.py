from ast import List


class Paper:
    def __init__(self, id:int, title:str, abstract:str, authors: List[str], categories: List[str], publication_date:str):
        self.id = id
        self.title = title
        self.abstract = abstract
        self.authors = authors
        self.categories = categories
        self.publication_date = publication_date
        
