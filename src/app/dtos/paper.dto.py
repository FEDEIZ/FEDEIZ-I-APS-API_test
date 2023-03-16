from api.src.domain.entities.paper.entity import Paper


class PaperDto:
    def __init__(self, id:int, title:str, abstract:str, authors: List[str], categories: List[str], publication_date: str):
        self.id = id
        self.title = title
        self.abstract = abstract
        self.authors = authors
        self.categories = categories
        self.publication_date = publication_date
        
    @classmethod
    def from_entity(cls, paper:Paper):
        return cls(
            id = paper.id,
            title=paper.title,
            abstract=paper.abstract,
            categories=paper.categories,
            publication_date = paper.publication_date
        )
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "abstract": self.abstract,
            "authors": self.authors,
            "categories": self.categories,
            "publication_date": self.publication_date.strftime("%Y-%m-%d"),
        }