from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.todo_model import Todo
from schemas.todo_schema import ToDoCreate

router = APIRouter(prefix="/todos", tags=["todos"])
@router.get("/")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos
@router.post("/")
def create_todo(todo: ToDoCreate, db: Session = Depends(get_db)):
    new_todo = Todo(title=todo.title, description=todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo