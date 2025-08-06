import sqlite3
import json
from pathlib import Path

# Define the path to the SQLite database file
DB_FILE = Path("data/todo_app.db")
# Ensure the directory exists
DB_FILE.parent.mkdir(exist_ok=True)

# Function to initialize the database and create the tasks table if it doesn't exist
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            subtasks TEXT,
            completed INTEGER DEFAULT 0,
            translated_task TEXT,
            language TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to add a new task to the database
def add_task_to_db(task, subtasks):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (task, subtasks, completed) VALUES (?, ?, ?)",
        (task, json.dumps(subtasks), 0)
    )
    conn.commit()
    conn.close()

# Function to fetch all tasks from the database
def get_all_tasks():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Function to mark a task as completed
def mark_task_complete(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Function to update the translated task in the database
def update_translation(task_id, translated_task, language):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET translated_task = ?, language = ? WHERE id = ?",
        (translated_task, language, task_id)
    )
    conn.commit()
    conn.close()
