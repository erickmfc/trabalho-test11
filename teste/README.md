# Plataforma de Cursos Online

Este é um projeto de uma plataforma de cursos online desenvolvida com Django, onde professores podem criar e gerenciar cursos, e alunos podem se inscrever e assistir às aulas.

## Configuração do Ambiente

Siga estas instruções para configurar e executar o projeto em seu computador:

1. Descompacte a pasta do projeto em um local de sua preferência

2. Abra um terminal/CMD na pasta do projeto

3. Crie um ambiente virtual:
   ```
   python -m venv .venv
   ```

4. Ative o ambiente virtual:
   - Windows:
     ```
     .venv\Scripts\activate
     ```
   - Linux/Mac:
     ```
     source .venv/bin/activate
     ```

5. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

6. Execute as migrações do banco de dados:
   ```
   python manage.py migrate
   ```

7. Inicie o servidor de desenvolvimento:
   ```
   python manage.py runserver
   ```

8. Acesse a plataforma em seu navegador:
   ```
   http://127.0.0.1:8000/
   ```

## Estrutura do Projeto

O projeto está organizado em dois principais apps:

- **usuarios**: Gerencia autenticação, cadastro e perfis de usuários (Alunos e Instrutores)
- **cursos**: Administra o cadastro e visualização de cursos e aulas

## Funcionalidades Principais

- Cadastro de usuários (Alunos e Instrutores)
- Login e autenticação
- Criação e gerenciamento de cursos (para Instrutores)
- Listagem e inscrição em cursos (para Alunos)
- Painel personalizado para cada tipo de usuário

## Tecnologias Utilizadas

- Python 3.11+
- Django 5.0.1
- SQLite (banco de dados)
- HTML/CSS para templates

## Observações

- O banco de dados SQLite (db.sqlite3) já está incluído com alguns dados de exemplo para facilitar os testes
- As senhas dos usuários de exemplo são armazenadas de forma segura usando o sistema de hash do Django
- O projeto segue as boas práticas de desenvolvimento Django e inclui validações de segurança básicas