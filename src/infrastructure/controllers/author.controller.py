from application.use_cases.author_use_cases import AuthorUseCases

class AuthorController:
    def __init__(self, author_use_cases):
        self.author_use_cases = author_use_cases

    def get_all_authors(self):
        authors = self.author_use_cases.get_all_authors()
        # Here we would convert the list of Author objects to a list of dictionaries for the API response
        return authors

    def get_author_by_id(self, author_id):
        author = self.author_use_cases.get_author_by_id(author_id)
        # Here we would convert the Author object to a dictionary for the API response
        return author

    def get_papers_by_author_id(self, author_id):
        papers = self.author_use_cases.get_papers_by_author_id(author_id)
        # Here we would convert the list of Paper objects to a list of dictionaries for the API response
        return papers
