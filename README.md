# login_pattern
sistema de login com padroes de projeto no streamlit


## Descrição
Este projeto implementa um sistema de login utilizando padrões de projeto no Streamlit. Ele serve como um exemplo de como estruturar um sistema de autenticação em aplicações web.

## Funcionalidades basicas
- Autenticação de usuários
- Registro de novos usuários
- Remocao de usarios
- Alteração de usuarios
- Interface amigável com Streamlit

## Tecnologias Utilizadas
- Python
- Streamlit
- SQLite (ou outro banco de dados de sua escolha)

## Como Executar
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/login_pattern.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd login_pattern
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. cadastrar um usuario superadmin
altere o arquivo test/test_model.py para adicionar um usuario superadmin e depois rode o comando:
    ```bash
    python test/test_model.py
    ```

 5. Execute a aplicação:
    ```bash
    streamlit run app.py
    ```

## Estrutura do Projeto
- `app.py`: Arquivo principal que inicia a aplicação Streamlit.
- `controllers/`: Diretório contendo os módulos com os controladores da aplicação, de autenticação e registro de usuários.
- `models/`: Diretório contendo o modelo de criação da tabela de users no banco de dados e o arquivo de classe de users.
- `pages_/`: Diretório contendo os arquivos de páginas da aplicação.
- `requirements.txt`: Arquivo de dependências do projeto.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.