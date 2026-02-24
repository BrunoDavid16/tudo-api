from database import SessionLocal, engine
from fastapi import FastAPI
from auth import hash_senha, verificar_senha, criar_token
from models import Task, TaskModel, Usuario, UsuarioModel

app = FastAPI()

@app.get("/tasks")
def get_tasks():
    db = SessionLocal()
    tasks = db.query(TaskModel).all()
    db.close()
    return tasks

@app.post("/tasks")
def post_task(task: Task):
    db = SessionLocal()
    db_task = TaskModel(titulo=task.titulo, completa=task.completa, descricao=task.descricao)
    db.add(db_task)
    db.commit()
    db.close()
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()
    task =db.query(TaskModel).filter(TaskModel.id == task_id).first()
    db.delete(task)
    db.commit()
    db.close()

@app.put("/tasks/{task_id}")
def put_task(task_id: int, task: Task):
    db = SessionLocal()
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    db_task.titulo = task.titulo
    db_task.completa = task.completa
    db_task.descricao = task.descricao
    db.commit()
    db.close()
    return db_task

@app.post("/register")
def registrar(usuario: Usuario):
    db = SessionLocal()
    db_usuario = UsuarioModel(email=usuario.email, senha_hash=hash_senha(usuario.senha))
    db.add(db_usuario)
    db.commit()
    db.close()
    return usuario

@app.post("/login")
def login(usuario: Usuario):
    db = SessionLocal()
    db_usuario = db.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).first()
    if not verificar_senha(usuario.senha, db_usuario.senha_hash):
        return {"erro": "Senha incorreta"}
    token = criar_token({"sub": usuario.email})
    return {"access_token": token}