# Todo API

## Descrição
API criada por Bruno David com intuito de gerenciar tarefas, verificando se estão completas ou não. Possui rotas GET, POST e DELETE. Cada tarefa tem id, titulo, status de conclusão e descrição opcional.

## Tecnologias usadas
- Python
- FastAPI
- Pydantic

## Como instalar e rodar

1. Clone o repositório:
```bash
git clone https://github.com/BrunoDavid16/tudo-api.git
```

2. Instale as dependências:
```bash
pip install fastapi uvicorn
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
- **GET** `/tasks` — lista todas as tarefas
- **POST** `/tasks` — cria uma nova tarefa
- **DELETE** `/tasks/{task_id}` — deleta uma tarefa pelo id