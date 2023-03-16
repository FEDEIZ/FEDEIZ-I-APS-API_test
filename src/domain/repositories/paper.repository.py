from abc import ABC, abstractmethod


class PaperRepository(ABC):
    @abstractmethod
    def get_all_papers(self) -> List[Paper]:
        pass
    
    @abstractmethod
    def get_paper_by_id(self,paper_id: int) -> Paper:
        pass