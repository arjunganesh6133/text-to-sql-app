import sqlite3

DB_PATH = "sample_data.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create sample tables
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            salary REAL,
            hire_date TEXT
        );

        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            budget REAL,
            location TEXT
        );

        INSERT OR IGNORE INTO employees VALUES
        (1, 'Alice', 'Engineering', 95000, '2021-03-15'),
        (2, 'Bob', 'Marketing', 72000, '2020-07-01'),
        (3, 'Charlie', 'Engineering', 105000, '2019-11-20'),
        (4, 'Diana', 'HR', 68000, '2022-01-10'),
        (5, 'Eve', 'Marketing', 78000, '2021-09-05');

        INSERT OR IGNORE INTO departments VALUES
        (1, 'Engineering', 500000, 'New York'),
        (2, 'Marketing', 300000, 'Chicago'),
        (3, 'HR', 150000, 'Austin');
    """)
    conn.commit()
    conn.close()

def run_query(sql: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        return columns, rows, None
    except Exception as e:
        return None, None, str(e)
    finally:
        conn.close()

def get_schema() -> str:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    schema = ""
    for (table,) in tables:
        cursor.execute(f"PRAGMA table_info({table})")
        cols = cursor.fetchall()
        col_defs = ", ".join([f"{c[1]} {c[2]}" for c in cols])
        schema += f"Table: {table} ({col_defs})\n"
    conn.close()
    return schema