from app.adapters.database import Database
from app.adapters.repository import Repository
from app.adapters.arxiv_api import ArxivApi
from app.use_cases import (
    ListPapersUseCase,
    GetPaperUseCase,
    ListAuthorsUseCase,
    GetAuthorUseCase,
    ListCategoriesUseCase,
    GetCategoryUseCase,
)
from app.adapters.api import app


def main():
    # Instantiate components
    database = Database()
    repository = Repository(database)
    arxiv_api = ArxivApi()

    # Instantiate use cases
    list_papers_use_case = ListPapersUseCase(repository, arxiv_api)
    get_paper_use_case = GetPaperUseCase(repository, arxiv_api)
    list_authors_use_case = ListAuthorsUseCase(repository)
    get_author_use_case = GetAuthorUseCase(repository)
    list_categories_use_case = ListCategoriesUseCase(repository)
    get_category_use_case = GetCategoryUseCase(repository)

    # Register endpoints
    app.register_list_papers_endpoint(list_papers_use_case)
    app.register_get_paper_endpoint(get_paper_use_case)
    app.register_list_authors_endpoint(list_authors_use_case)
    app.register_get_author_endpoint(get_author_use_case)
    app.register_list_categories_endpoint(list_categories_use_case)
    app.register_get_category_endpoint(get_category_use_case)

    # Start the web server
    app.run()


if __name__ == "__main__":
    main()
