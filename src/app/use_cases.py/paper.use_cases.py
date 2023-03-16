from api.src.domain.repositories.paper.repository import PaperRepository


class PaperUseCases:
    def __init__(self, paper_repository: PaperRepository):
        self.paper_repository = paper_repository
        
    def get_all_papers(self) -> List[PaperDto]:
        papers = self.paper_repository.get_all_papers()
        paper_dtos = [PaperDto.from_entity(paper) for paper in papers]
        return paper_dtos
    
    def get_paper_by_id(self,paper_id:int) ->PaperDto:
        paper = self.paper_repository.get_paper_by_id(paper_id)
        paper_dto = PaperDto.from_entity(paper)
        return paper_dto