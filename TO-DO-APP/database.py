import sqlite3
from datetime import datetime, timedelta

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db', check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority INTEGER DEFAULT 1,
            category TEXT DEFAULT 'General',
            due_date TEXT,
            completed BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_task(self, title, description="", priority=1, category="General", due_date=None):
        query = """
        INSERT INTO tasks (title, description, priority, category, due_date)
        VALUES (?, ?, ?, ?, ?)
        """
        self.conn.execute(query, (title, description, priority, category, due_date))
        self.conn.commit()

    def get_all_tasks(self):
        query = "SELECT * FROM tasks ORDER BY priority DESC, created_at DESC"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def get_tasks_by_category(self, category):
        query = "SELECT * FROM tasks WHERE category = ? ORDER BY priority DESC"
        cursor = self.conn.execute(query, (category,))
        return cursor.fetchall()

    def get_tasks_by_priority(self, priority):
        query = "SELECT * FROM tasks WHERE priority = ? ORDER BY created_at DESC"
        cursor = self.conn.execute(query, (priority,))
        return cursor.fetchall()

    def get_pending_tasks(self):
        query = "SELECT * FROM tasks WHERE completed = FALSE ORDER BY priority DESC, due_date ASC"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def get_completed_tasks(self):
        query = "SELECT * FROM tasks WHERE completed = TRUE ORDER BY created_at DESC"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def mark_completed(self, task_id):
        query = "UPDATE tasks SET completed = TRUE WHERE id = ?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def mark_pending(self, task_id):
        query = "UPDATE tasks SET completed = FALSE WHERE id = ?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def delete_task(self, task_id):
        query = "DELETE FROM tasks WHERE id = ?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def update_task(self, task_id, title=None, description=None, priority=None, category=None, due_date=None):
        updates = []
        params = []
        
        if title:
            updates.append("title = ?")
            params.append(title)
        if description:
            updates.append("description = ?")
            params.append(description)
        if priority:
            updates.append("priority = ?")
            params.append(priority)
        if category:
            updates.append("category = ?")
            params.append(category)
        if due_date:
            updates.append("due_date = ?")
            params.append(due_date)
        
        if updates:
            query = f"UPDATE tasks SET {', '.join(updates)} WHERE id = ?"
            params.append(task_id)
            self.conn.execute(query, params)
            self.conn.commit()

    def search_tasks(self, keyword):
        query = """
        SELECT * FROM tasks 
        WHERE title LIKE ? OR description LIKE ? 
        ORDER BY priority DESC
        """
        cursor = self.conn.execute(query, (f'%{keyword}%', f'%{keyword}%'))
        return cursor.fetchall()

    def get_categories(self):
        query = "SELECT DISTINCT category FROM tasks"
        cursor = self.conn.execute(query)
        return [row[0] for row in cursor.fetchall()]

    def get_today_tasks(self):
        today = datetime.now().strftime('%Y-%m-%d')
        query = "SELECT * FROM tasks WHERE due_date = ? ORDER BY priority DESC"
        cursor = self.conn.execute(query, (today,))
        return cursor.fetchall()

    def close(self):
        self.conn.close()