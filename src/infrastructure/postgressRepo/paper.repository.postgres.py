import psycopg2
from typing import List
from datetime import datetime
from app.modules.papers.entities import Paper, Author, Category
from app.modules.papers.repositories import PaperRepository, AuthorRepository, CategoryRepository


class PaperRepositoryPostgres(PaperRepository):
    def __init__(self, conn):
        self.conn = conn

    def get_all(self) -> List[Paper]:
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, title, abstract, authors, categories, publication_date FROM papers")
            rows = cur.fetchall()
            return [Paper(*row) for row in rows]

    def get_by_id(self, paper_id: int) -> Paper:
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, title, abstract, authors, categories, publication_date FROM papers WHERE id = %s", (paper_id,))
            row = cur.fetchone()
            if row:
                return Paper(*row)
            else:
                return None