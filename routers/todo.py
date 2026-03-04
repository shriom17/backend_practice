from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.todo_model import Todo
from schemas.todo_schema import ToDoCreate

router = APIRouter(prefix="/todos", tags=["todos"])
@router.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos