from models import Task, TaskModel
from database import SessionLocal, engine
from fastapi import FastAPI


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