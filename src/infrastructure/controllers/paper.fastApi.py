class FastApiPaperController:
    def __init__(self,paper_controller: PaperController):
        self.paper_controller = paper_controller
        
    async def get_all_papers(self):
        papers = self.paper_controller.get_all_papers();
        return JSONResponse(content=papers) 
    
    async def get_paper_by_id(self, paper_id):
        paper = self.paper_controller.get_paper(paper_id)
        return JSONResponse(content=paper)