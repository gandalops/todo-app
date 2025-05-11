# bkend/services/task_service.py

import sqlite3

DB_NAME = "todo.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL
            )
        ''')
        conn.commit()

def add_task(description):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
        conn.commit()
        task_id = cursor.lastrowid
        return {"id": task_id, "description": description}

def get_all_tasks():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, description FROM tasks")
        rows = cursor.fetchall()
        return [{"id": row[0], "description": row[1]} for row in rows]

def delete_task_by_id(task_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        return cursor.rowcount > 0

def update_task(task_id, new_description):
    with sqlite3.connect("todo.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (new_description, task_id))
        conn.commit()
        return cursor.rowcount > 0

