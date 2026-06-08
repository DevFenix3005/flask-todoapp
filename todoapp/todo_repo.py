import sqlite3

from datetime import datetime
from zoneinfo import ZoneInfo


def create_todo(db: sqlite3.Connection, title: str, description: str, user_id: int):
    current_time = datetime.now().astimezone(ZoneInfo("America/Mexico_City"))

    db.execute(
        """
    INSERT INTO todos(title, description, created_at, user_id)
    VALUES (?,?,?,?)
    """,
        [title, description, current_time, user_id],
    )
    db.commit()


def read_todo(db: sqlite3.Connection, user_id: int):
    return db.execute("SELECT * FROM todos WHERE user_id = ?", (user_id,)).fetchall()


def read_todo_by_id(db: sqlite3.Connection, todo_id: int, user_id: int):
    return db.execute(
        "SELECT * FROM todos WHERE todo_id = ? AND user_id = ?", (todo_id, user_id)
    ).fetchone()


def update_todo_by_id(db: sqlite3.Connection, todo_id: int, user_id: int, state: bool):
    db.execute(
        """
               UPDATE todos
                set completed = ?
                WHERE todo_id = ?
                AND user_id = ?
               """,
        (
            state,
            todo_id,
            user_id,
        ),
    ).fetchone()
    db.commit()
