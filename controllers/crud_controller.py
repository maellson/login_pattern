
from models.user import User


def getUser(username: str, current_user: dict) -> dict:
    """
    Tenta autenticar o usuário com base no username e na senha fornecidos.

    Retorna um usuario com base no username.:
      - success: True se a autenticação for bem-sucedida, False caso contrário.
      - message: Mensagem explicativa.
      - user: Dados do usuário (se autenticado com sucesso).
    """
    if current_user.get("role") != "superadmin":
        return {"success": False, "message": "Apenas superadmin pode remover usuários."}

    user = User.get_by_username(username)
    if not user:
        return {"success": False, "message": "Usuário não encontrado."}
    return {"success": True, "message": "Usuário encontrado.", "user": user.to_dict()}


def register_user(name: str, username: str, password: str, confirm_password: str, role: str) -> dict:
    """
    Registra um novo usuário.

    Valida se:
      - As senhas informadas batem.
      - O username não está em uso.

    Retorna um dicionário com:
      - success: True se o registro for bem-sucedido, False caso contrário.
      - message: Mensagem explicativa.
      - user: Dados do usuário recém-criado (quando o registro é bem-sucedido).
    """
    if password != confirm_password:
        return {"success": False, "message": "As senhas não conferem."}

    # Verifica se o usuário já existe
    if User.get_by_username(username) is not None:
        return {"success": False, "message": "Usuário já cadastrado."}

    try:
        new_user = User.create(name, username, password, role)
        return {"success": True, "message": "Usuário registrado com sucesso.", "user": new_user.to_dict()}
    except Exception as e:
        return {"success": False, "message": f"Erro ao registrar usuário: {e}"}


def remove_user(username: str, current_user: dict) -> dict:
    """
    Remove um usuário cadastrado, mas apenas se o usuário atual for superadmin.
    current_user é o dicionário com os dados do usuário logado (armazenado em st.session_state["user"]).
    """
    if current_user.get("role") != "superadmin":
        return {"success": False, "message": "Apenas superadmin pode remover usuários."}

    if current_user.get("username") == username:
        return {"success": False, "message": "Você não pode remover a si mesmo."}

    # Verifica se o usuário existe
    user = User.get_by_username(username)
    if not user:
        return {"success": False, "message": "Usuário não encontrado."}

    # 4. Remove o usuário
    User.delete_by_username(username)
    return {"success": True, "message": f"Usuário '{username}' removido com sucesso."}


def get_Users(current_user: dict) -> dict:
    """
    Retorna uma lista de todos os usuários cadastrados.
    """
    if current_user.get("role") != "superadmin":
        return {"success": False, "message": "Apenas superadmin pode ver a lista de usuários."}
    users = User.get_all_users()
    user_list = [{"id": user.id, "name": user.name, "username": user.username, "role": user.role}
                 for user in users]
    return {"success": True, "message": "Lista de usuários retornada com sucesso.", "users": user_list}
