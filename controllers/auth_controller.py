
from models.user import User


def login_user(username: str, password: str) -> dict:
    """
    Tenta autenticar o usuário com base no username e na senha fornecidos.

    Retorna um dicionário com:
      - success: True se a autenticação for bem-sucedida, False caso contrário.
      - message: Mensagem explicativa.
      - user: Dados do usuário (se autenticado com sucesso).
    """
    user = User.get_by_username(username)
    if user:
        if user.check_password(password):
            return {"success": True, "message": "Login realizado com sucesso.", "user": user.to_dict()}
        else:
            return {"success": False, "message": "Senha incorreta."}
    else:
        return {"success": False, "message": "Usuário não encontrado."}
