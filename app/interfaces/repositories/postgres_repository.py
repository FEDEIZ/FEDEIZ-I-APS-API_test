from typing import List
from psycopg2 import sql
from app.entities.paper import Paper
from app.adapters.database.postgres_database import PostgreSQLDatabase


class PostgresRepository:
    def __init__(self, db: PostgreSQLDatabase):
        self.db = db

    def get_all_papers(self) -> List[Paper]:
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            sql.SQL("SELECT * FROM papers;")
        )
        papers = []
        for row in cursor.fetchall():
            paper = Paper(*row)
            papers.append(paper)
        cursor.close()
        conn.close()
        return papers

    def get_paper_by_id(self, paper_id: str) -> Paper:
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            sql.SQL("SELECT * FROM papers WHERE id = %s;"),
            [paper_id]
        )
        row = cursor.fetchone()
        if row is None:
            return None
        paper = Paper(*row)
        cursor.close()
        conn.close()
        return paper

    def get_papers_by_author(self, author_id: str) -> List[Paper]:
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            sql.SQL("""
                SELECT papers.* FROM papers
                INNER JOIN author_paper ON papers.id = author_paper.paper_id
                WHERE author_paper.author_id = %s;
            """),
            [author_id]
        )
        papers = []
        for row in cursor.fetchall():
            paper = Paper(*row)
            papers.append(paper)
        cursor.close()
        conn.close()
        return papers

    def get_papers_by_category(self, category_id: str) -> List[Paper]:
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute(
            sql.SQL("""
                SELECT papers.* FROM papers
                INNER JOIN category_paper ON papers.id = category_paper.paper_id
                WHERE category_paper.category_id = %s;
            """),
            [category_id]
        )
        papers = []
        for row in cursor.fetchall():
            paper = Paper(*row)
            papers.append(paper)
        cursor.close()
        conn.close()
        return papers
