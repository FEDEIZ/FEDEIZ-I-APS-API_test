
from api.src.infrastructure.controllers.paper.fastApi import FastApiPaperController
from api.src.infrastructure.controllers.paper.controller import PaperController
from api.src.app.use_cases.py.paper.use_cases import PaperUseCases
from api.src.infrastructure.postgressRepo.paper.repository.postgres import PaperRepositoryPostgres
from api.src.infrastructure.database.postgres.db import PostgresDatabase


def main():
    db = PostgresDatabase() # instantiate the database class here
    db.connect() # connect to the database

    paper_repository = PaperRepositoryPostgres(db) # instantiate the repository with the database instance

    paper_use_cases = PaperUseCases(paper_repository)
    

    # instantiate the controllers
    paper_controller = PaperController(paper_use_cases)
    fastapi_paper_controller = FastApiPaperController(paper_controller)

    # api framework used
    app = FastAPI() # instantiate the FastAPI app here

    #routes for api
    
    @app.get("/papers")
    async def get_all_papers():
        return await fastapi_paper_controller.get_all_papers()

    @app.get("/papers/{paper_id}")
    async def get_paper_by_id(paper_id: int):
        return await fastapi_paper_controller.get_paper_by_id(paper_id)

    

    db.disconnect() # disconnect from the database

if __name__ == '__main__':
    main()
