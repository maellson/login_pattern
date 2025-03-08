import bcrypt
from models.database import get_connection


class User:
    def __init__(self, name: str, username: str, password: str, role: str = "user", id: int = None):
        """
        Inicializa o objeto User.
        O atributo 'password' deve conter a senha já em formato hash.
        'role' pode ser "user", "admin" ou "superadmin".
        """
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        """Serializa o objeto User para dicionário."""
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    @staticmethod
    def hash_password(password: str) -> str:
        """Gera e retorna o hash da senha usando bcrypt."""
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        return hashed

    @classmethod
    def create(cls, name: str, username: str, password: str, role: str = "user") -> 'User':
        """
        Cria um novo usuário, inserindo-o no banco de dados.
        Por padrão, o role é "user". Para criar um superadmin, passe role="superadmin".
        """
        hashed_password = cls.hash_password(password)
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO users (name, username, password, role) VALUES (?, ?, ?, ?)',
                (name, username, hashed_password, role)
            )
            conn.commit()
            user_id = cursor.lastrowid
        return cls(name, username, hashed_password, role, id=user_id)

    @classmethod
    def get_by_username(cls, username: str) -> 'User':
        """
        Busca e retorna um usuário com base no username.
        Retorna None se o usuário não for encontrado.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT id, name, username, password, role FROM users WHERE username = ?',
                (username,)
            )
            row = cursor.fetchone()
            if row:
                return cls(row['name'], row['username'], row['password'], row['role'], id=row['id'])
            return None

    def check_password(self, password: str) -> bool:
        """Verifica se a senha informada confere com o hash armazenado."""
        return bcrypt.checkpw(password.encode(), self.password.encode())

    @classmethod
    def delete_by_username(self, username: str):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE username = ?', (username,))
            conn.commit()

    @classmethod
    def get_all_users(cls) -> list:
        """
        Retorna uma lista de todos os usuários cadastrados, exceto superadmins.
        """
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'SELECT id, name, username, role FROM users WHERE role != "superadmin"'
            )
            rows = cursor.fetchall()
            users = [cls(row['name'], row['username'],
                         row['role'], id=row['id']) for row in rows]
        return users

    @classmethod
    def update_user(cls, username: str, name: str, role: str, password: str = None):
        with get_connection() as conn:
            cursor = conn.cursor()
            if password:
                hashed_password = cls.hash_password(password)
                cursor.execute(
                    'UPDATE users SET name = ?, role = ?, password = ? WHERE username = ?',
                    (name, role, hashed_password, username)
                )
            else:
                cursor.execute(
                    'UPDATE users SET name = ?, role = ? WHERE username = ?',
                    (name, role, username)
                )
            conn.commit()
        return cls.get_by_username(username)
