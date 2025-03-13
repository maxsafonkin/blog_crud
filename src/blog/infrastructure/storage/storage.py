from datetime import datetime

import psycopg2

from blog import entities
from . import models
from .config import StorageConfig


class Storage:
    def __init__(self, storage_config: StorageConfig):
        self._conn = psycopg2.connect(
            host=storage_config.host,
            port=storage_config.port,
            user=storage_config.username,
            password=storage_config.password,
            dbname=storage_config.db_name,
        )

    def create_post(self, title: str, content: str) -> int:
        date = datetime.now()

        query = "INSERT INTO posts(title, content, created_at) VALUES (%s, %s, %s) RETURNING id;"
        vars = (title, content, date)

        with self._conn.cursor() as cur:
            self._execute(cur, query, vars)
            self._conn.commit()
            return cur.fetchone()[0]

    def delete_post(self, id: int) -> None:
        query = "DELETE FROM posts WHERE id = %s;"
        vars = (id,)

        with self._conn.cursor() as cur:
            self._execute(cur, query, vars)

    def update_post_title(self, id: int, title: str) -> None:
        query = "UPDATE posts SET title = %s WHERE id = %s;"
        vars = (title, id)

        with self._conn.cursor() as cur:
            self._execute(cur, query, vars)

    def update_post_content(self, id: int, content: str) -> None:
        query = "UPDATE posts SET content = %s WHERE id = %s;"
        vars = (content, id)

        with self._conn.cursor() as cur:
            self._execute(cur, query, vars)

    def get_post_ids(self) -> list[int]:
        query = "SELECT id FROM posts"

        with self._conn.cursor() as cur:
            self._execute(cur, query)
            ids = [row[0] for row in cur.fetchall()]

        return ids

    def get_post(self, id: int) -> entities.Post:
        query = "SELECT * FROM posts WHERE id = %s;"
        vars = (id,)

        with self._conn.cursor() as cur:
            self._execute(cur, query, vars)
            raw_data = cur.fetchone()
            post = models.Post(*raw_data)

        return post.to_entity()

    def _execute(self, cursor, query: str, vars: tuple | None = None) -> None:
        cursor.execute(query, vars)
        self._conn.commit()
