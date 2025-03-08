import streamlit as st
from controllers.auth_controller import login_user


def login():
    # Verifica se o usuário já está logado
    if st.session_state.get("logged_in", False):
        # st.info("Você já está logado!")
        st.success("Você já está logado!")
        return

    st.title("Login")

    # Formulário de Login
    with st.form(key="login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_login = st.form_submit_button("Entrar")

    if submit_login:
        resultado = login_user(username, password)
        if resultado["success"]:
            st.session_state["logged_in"] = True
            st.session_state["user"] = resultado["user"]
            st.success(resultado["message"])
            st.rerun()  # Atualiza a página para refletir o login
        else:
            st.error(resultado["message"])
