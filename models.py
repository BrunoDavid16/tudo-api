from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    id: int
    titulo: str
    completa: bool
    descricao: Optional[str] = None

