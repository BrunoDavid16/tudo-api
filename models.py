from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    id: Optional[int] = None
    titulo: str
    completa: bool
    descricao: Optional[str] = None

class Base(DeclarativeBase):
    pass

class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String)
    completa = Column(Boolean)
    descricao = Column(String)

class Usuario(BaseModel):
    email: str
    senha: str

class UsuarioModel(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    senha_hash = Column(String)