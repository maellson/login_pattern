import streamlit as st
from controllers.crud_controller import register_user, remove_user, get_Users


def administrar():
    if st.session_state["user"].get("role") == "superadmin":
        # Formulário de Registro
        # st.markdown("---")
        st.header("Registrar-se", divider="violet")  # rainbow)
        st.write("Conteúdo exclusivo para superadmins.")

        # Botão de logout
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.rerun()

        # Formulário de Registro
        with st.form(key="register_form"):
            name = st.text_input("Nome")
            reg_username = st.text_input("Username", key="reg_username")
            reg_password = st.text_input(
                "Senha", type="password", key="reg_password")
            reg_confirm_password = st.text_input(
                "Confirmar Senha", type="password", key="reg_confirm_password")
            role = st.selectbox("Perfil", ["user", "admin", "superadmin"])
            submit_register = st.form_submit_button("Registrar")

        if submit_register:
            resultado = register_user(
                name, reg_username, reg_password, reg_confirm_password, role)
            if resultado["success"]:
                st.success(resultado["message"])
            else:
                st.error(resultado["message"])

         # Formulário de Remoção de Usuário
        st.header("Remover Usuário", divider="violet")
        with st.form(key="remove_form"):
            response = get_Users(st.session_state["user"])
            if response["success"]:
                users = response["users"]
                username_to_remove = st.selectbox(
                    "Selecione o usuário para remover", [user["username"] for user in users])
                submit_remove = st.form_submit_button("Remover Usuário")

                if submit_remove:
                    result = remove_user(username_to_remove,
                                         st.session_state["user"])
                    if result["success"]:
                        st.success(result["message"])
                    else:
                        st.error(result["message"])
            else:
                st.error(response["message"])
    else:
        st.info("Somente superadmin podem cadastrar/remover usuários.")
