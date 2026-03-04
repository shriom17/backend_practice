from fastapi import FastAPI
from routers import users, todo
from database.database import engine, Base
from models import user  # Import models to register them
from models import todo_model  # Import todo model

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User API",
    description="A simple User CRUD API with validation and error handling",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(todo.router)


@app.get("/", tags=["root"])
def root():
    return {"message": "Welcome to the User API"}
