from models import Task
from fastapi import FastAPI

app = FastAPI()


tasks = []

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def post_task(task: Task):
    tasks.append(task)
    return tasks

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task_id == task.id:
            tasks.remove(task)
    return tasks