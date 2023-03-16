from ast import Dict, List
from application.use_cases.paper_use_cases import PaperUseCases

class PaperController:
    def __init__(self, paper_use_cases):
        self.paper_use_cases = paper_use_cases

    def get_all_papers(self) -> List[Dict]:
        papers = self.paper_use_cases.get_all_papers()
        return [paper.to_dict() for paper in papers]

    def get_paper_by_id(self, paper_id):
        paper = self.paper_use_cases.get_paper_by_id(paper_id)
        return paper.to_dict()
