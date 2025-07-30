import sqlite3
from typing import Dict, List, Optional, Any

class SQLiteMCPServer:
    def __init__(self, db_path: str = ":memory:"):
        """Initialize the SQLite MCP server with an in-memory database"""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self):
        """Create the demo data table if it doesn't exist"""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS demo_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                value REAL
            )
        """)
        self.conn.commit()
    
    def add_data(self, name: str, description: str, value: float) -> Dict:
        """Add data to the SQLite database"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO demo_data (name, description, value) VALUES (?, ?, ?)",
            (name, description, value)
        )
        self.conn.commit()
        return {"status": "success", "id": cursor.lastrowid}
    
    def fetch_data(self, limit: int = 10) -> List[Dict]:
        """Fetch data from the SQLite database"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM demo_data LIMIT ?", (limit,))
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def close(self):
        """Close the database connection"""
        self.conn.close()