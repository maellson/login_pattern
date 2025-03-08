import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

## --- import --- ##
from models.database import create_users_table
from models.user import User


###


def main():
    # Cria a tabela de usuários (se não existir)
    create_users_table()
    print("Tabela de usuários criada (se ainda não existia).")

    # Cria um usuário para teste
    user = User.create("maelson", "lima", "qwe123", 'superadmin')
    print("Usuário criado:", user.to_dict())

    # Busca o usuário pelo username
    found = User.get_by_username("lima")
    if found:
        print("Usuário encontrado:", found.to_dict())
        # Verifica se a senha confere
        if found.check_password("senha123"):
            print("Senha verificada com sucesso.")
        else:
            print("Senha incorreta.")
    else:
        print("Usuário não encontrado.")


if __name__ == "__main__":
    main()
