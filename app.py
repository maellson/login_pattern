import streamlit as st
from streamlit_option_menu import option_menu
from pages_.chatbot import chatbot
from pages_.dashboard import dashboard
from pages_.login import login
from pages_.administracao import administrar
from pages_.configuracao import configurar
from utils.utils import require_login

# Configuração da página
st.set_page_config(page_title="Login Center", layout="wide")

# Inicializar estado de sessão para controle de autenticação
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Menu lateral de navegação
with st.sidebar:
    menu_option = option_menu(
        menu_title="Menu",
        options=["Home", "Dashboard", "Login",
                 "Área Administrativa", "Configuração", "Sair"],
        icons=["house", "bar-chart", "key",
               "gear", "tools", "box-arrow-right"],
        default_index=0,
    )

# Roteamento de páginas
if menu_option == "Home":
    # require_login("Você precisa estar logado para acessar o Dashboard.")
    st.title("Chatbot")
    # Home já exibe o Chatbot, sem verificação de login
    chatbot()

elif menu_option == "Dashboard":
    # Verifica se o usuário está logado usando função do utils require_login
    require_login("Você precisa estar logado para acessar o Dashboard.")
    dashboard()

elif menu_option == "Login":
    # Exibe a página de Login
    login()

elif menu_option == "Área Administrativa":
    # Verifica se o usuário está logado para acessar área restrita
    require_login(
        "Você precisa estar logado para acessar a área administrativa.")
    st.title("Área Administrativa")
    st.write("Conteúdo exclusivo para a área administrativa.")
    administrar()


elif menu_option == "Configuração":
    require_login("Você precisa estar logado para acessar a configuracao.")
    st.title("Configuracao de Pagina")
    # Verifica se o usuário está logado usando função do utils require_login
    # require_login("Você precisa estar logado para acessar o Dashboard.")
    configurar()


elif menu_option == "Sair":
    st.session_state["logged_in"] = False
    st.success("Você saiu da sessão!")
