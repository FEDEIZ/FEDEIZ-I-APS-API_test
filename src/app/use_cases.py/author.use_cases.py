class AuthorUseCases:
    def __init__(self, author_repo: AuthorRepository, paper_repo: PaperRepository):
        self.author_repo = author_repo
        self.paper_repo = paper_repo

    def get_all_authors(self) -> List[Author]:
        return self.author_repo.get_all()

    def get_author_by_id(self, author_id: int) -> Author:
        author = self.author_repo.get_by_id(author_id)
        author.papers = self.paper_repo.get_by_author(author_id)
        return author