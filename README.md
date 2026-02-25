# Todo API

## Descrição
API REST criada por Bruno David para gerenciar tarefas. Possui autenticação com JWT, banco de dados SQLite e as operações completas de CRUD. Cada tarefa tem id, titulo, status de conclusão e descrição opcional.

## API ao vivo
Acesse a documentação em: https://tudo-api-uwzz.onrender.com/docs

## Tecnologias usadas
- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Bcrypt (passlib)

## Como instalar e rodar localmente

1. Clone o repositório:
```bash
git clone https://github.com/BrunoDavid16/tudo-api.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a API:
```bash
python -m uvicorn main:app --reload
```

4. Acesse a documentação em:
```
http://127.0.0.1:8000/docs
```

## Rotas

### Tarefas
- **GET** `/tasks` — lista todas as tarefas
- **POST** `/tasks` — cria uma nova tarefa
- **PUT** `/tasks/{task_id}` — edita uma tarefa pelo id
- **DELETE** `/tasks/{task_id}` — deleta uma tarefa pelo id

### Autenticação
- **POST** `/register` — cria um novo usuário
- **POST** `/login` — autentica o usuário e retorna o token JWT