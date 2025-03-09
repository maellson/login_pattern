from wordcloud import WordCloud
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def dashboard():
    if not st.session_state.get("logged_in", False):
        st.warning("Você não está logado. Por favor, vá para o menu de login.")
        return

    st.header("Dashboard", divider="violet")

    # Botão de logout
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()

    st.write("Bem-vindo ao Dashboard!")

    # Primeira linha com 3 gráficos
    row1 = st.columns(3)

    with row1[0]:
        st.subheader("Solicitações por Assunto")
        topics = ["Suporte", "Informações",
                  "Vendas", "Reclamações", "Feedback"]
        counts = [120, 95, 70, 30, 50]  # Dados mockados
        fig1, ax1 = plt.subplots()
        ax1.bar(topics, counts, color="skyblue")
        ax1.set_ylabel("Quantidade")
        ax1.set_title("Solicitações por Assunto")
        st.pyplot(fig1)

    with row1[1]:
        st.subheader("Acessos Diários")
        days = np.arange(1, 8)  # Últimos 7 dias
        accesses = [200, 250, 220, 300, 280, 310, 260]  # Dados mockados
        fig2, ax2 = plt.subplots()
        ax2.plot(days, accesses, marker='o', linestyle='-', color="green")
        ax2.set_xlabel("Dia")
        ax2.set_ylabel("Acessos")
        ax2.set_title("Acessos Diários (Última Semana)")
        st.pyplot(fig2)

    with row1[2]:
        st.subheader("Tokens Consumidos")
        tokens = [5000, 5200, 5100, 5300, 5500, 5400, 5600]  # Dados mockados
        fig3, ax3 = plt.subplots()
        ax3.plot(days, tokens, marker='o', linestyle='-', color="red")
        ax3.set_xlabel("Dia")
        ax3.set_ylabel("Tokens")
        ax3.set_title("Tokens Consumidos (Última Semana)")
        st.pyplot(fig3)

    # Segunda linha com 3 gráficos
    row2 = st.columns(2)

    with row2[0]:
        st.subheader("Tempo Médio de Resposta")
        # Tempo médio de resposta (em segundos) nos últimos 7 dias
        response_times = [2.5, 2.7, 2.4, 3.0, 2.8, 2.6, 2.9]
        fig5, ax5 = plt.subplots()
        ax5.plot(days, response_times, marker='o',
                 linestyle='-', color="purple")
        ax5.set_xlabel("Dia")
        ax5.set_ylabel("Tempo (s)")
        ax5.set_title("Tempo Médio de Resposta")
        st.pyplot(fig5)

    with row2[1]:
        st.subheader("Satisfação dos Usuários")
        # Pie chart com dados mockados: Percentual de feedback positivo, neutro e negativo
        labels = ["Positivo", "Neutro", "Negativo"]
        sizes = [70, 20, 10]
        colors = ["lightgreen", "lightgrey", "salmon"]
        fig6, ax6 = plt.subplots()
        ax6.pie(sizes, labels=labels, autopct="%1.1f%%",
                startangle=90, colors=colors)
        ax6.axis("equal")
        ax6.set_title("Satisfação dos Usuários")
        st.pyplot(fig6)

    # Terceira linha com 1 gráfico
    row3 = st.columns(1)
    with row3[0]:
        st.subheader("Nuvem de Assuntos")
        # Texto mockado para gerar a nuvem
        text = (
            "suporte suporte suporte suporte "
            "informações informações informações "
            "vendas vendas "
            "reclamações reclamações "
            "feedback feedback feedback feedback feedback"
        )
        wordcloud = WordCloud(width=400, height=200,
                              background_color="white").generate(text)
        fig4, ax4 = plt.subplots(figsize=(4, 2))
        ax4.imshow(wordcloud, interpolation="bilinear")
        ax4.axis("off")
        st.pyplot(fig4)
