from application.use_cases.category_use_cases import CategoryUseCases

class CategoryController:
    def __init__(self, category_use_cases):
        self.category_use_cases = category_use_cases

    def get_all_categories(self):
        categories = self.category_use_cases.get_all_categories()
        # Here we would convert the list of Category objects to a list of dictionaries for the API response
        return categories

    def get_category_by_id(self, category_id):
        category = self.category_use_cases.get_category_by_id(category_id)
        # Here we would convert the Category object to a dictionary for the API response
        return category

    def get_papers_by_category_id(self, category_id):
        papers = self.category_use_cases.get_papers_by_category_id(category_id)
        # Here we would convert the list of Paper objects to a list of dictionaries for the API response
        return papers
