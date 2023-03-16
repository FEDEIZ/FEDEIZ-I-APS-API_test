class CategoryUseCases:
    def __init__(self, category_repo: CategoryRepository, paper_repo: PaperRepository):
        self.category_repo = category_repo
        self.paper_repo = paper_repo

    def get_all_categories(self) -> List[Category]:
        return self.category_repo.get_all()

    def get_category_by_id(self, category_id: int) -> Category:
        category = self.category_repo.get_by_id(category_id)
        category.papers = self.paper_repo.get_by_category(category_id)
        return category