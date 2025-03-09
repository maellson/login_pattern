import streamlit as st


def configurar():
    if st.session_state["user"].get("role") in ("admin", "superadmin"):
        # st.markdown("---")

        st.header('Configurações do Assistente', divider="violet")

        # Botão de logout
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.rerun()

        model_name = st.selectbox(
            'Nome do modelo: ', ['gpt-3.5-turbo-0125', 'gpt-4o']
        )
        retrieval_search_type = st.selectbox(
            'Tipo de busca de recuperação: ', ['mmr', 'similarity']
        )

        prompt = st.text_area(
            'Prompt: ', value=(
                'Olá, tudo bem?'
            ),
            height=350)
    else:
        st.info("Somente administradores podem alterar as configurações de prompts.")
