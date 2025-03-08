import streamlit as st


def require_login(message: str = "Você não está logado. Por favor, faça login para acessar esta página."):
    if not st.session_state.get("logged_in", False):
        st.warning(message)
        st.stop()
