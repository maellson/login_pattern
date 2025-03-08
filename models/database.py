import sqlite3

DATABASE_FILE = 'login.db'  # Nome do arquivo do banco SQLite


def get_connection():
    """Cria e retorna uma conexão com o banco SQLite."""
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row  # Permite acessar as colunas por nome
    return conn


def create_users_table():
    """Cria a tabela 'users' se ela não existir."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'user' CHECK(role IN ('admin', 'superadmin', 'user'))
                       
            )
        ''')
        conn.commit()
