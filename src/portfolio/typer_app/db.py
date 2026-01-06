import sqlite3
from pathlib import Path

db_path = Path("table.sql")

def get_conn() -> sqlite3.Connection:
    """Establish connection."""
    return sqlite3.connect(db_path)

    
def init_table() -> None:
    """The first command is to initialize sql table."""
    sql_command = """
    CREATE TABLE IF NOT EXISTS typer_table (
        UserID INT Primary Key,
        Name TEXT NOT NULL,
        Password TEXT NOT NULL
    );
    """
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute(sql_command)
    conn.commit()
    conn.close()