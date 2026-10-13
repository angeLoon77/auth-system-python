# Sistema de Autenticação

Sistema de cadastro e login feito em Python, com banco de dados SQLite e senhas protegidas por hash (bcrypt). Projeto pessoal de aprendizado, usado para praticar banco de dados, segurança básica de senhas e organização de código em módulos.

## Funcionalidades

- Cadastro de usuários, com validação de usuário e senha antes de salvar
- Login com verificação da senha
- Senhas nunca são guardadas em texto puro: só o hash gerado com bcrypt vai para o banco
- Dados persistidos em SQLite (`login_database.db`)

## Estrutura do projeto

| Arquivo | Função |
| --- | --- |
| `database.py` | Conexão com o SQLite e operações no banco |
| `auth.py` | Regras de cadastro, validação, hash da senha e login |
| `main.py` | Ponto de entrada, uso por terminal |

## Tecnologias

- Python 3
- SQLite (módulo `sqlite3` da biblioteca padrão)
- [bcrypt](https://pypi.org/project/bcrypt/) para hash de senhas

## Como rodar

1. Clone o repositório:

```
git clone https://github.com/angeLoon77/auth-system-python.git
cd auth-system-python
```

2. Crie e ative um ambiente virtual:

```
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows (PowerShell)
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Rode o programa:

```
python main.py
```

## Por que bcrypt?

Guardar a senha em texto puro expõe todos os usuários se o banco vazar. O bcrypt gera um hash com *salt* aleatório e é propositalmente lento, o que dificulta ataques de força bruta. No login, a senha digitada é comparada com o hash salvo, sem nunca precisar recuperar a senha original.

## Próximos passos

- Interface gráfica ou web para a tela de login (ideia: backend em Python reaproveitando `database.py` e `auth.py`)
- Testes automatizados para as regras de cadastro e login
