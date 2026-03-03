from fastapi import FastAPI
from routers import users

app = FastAPI(
    title="User API",
    description="A simple User CRUD API with validation and error handling",
    version="1.0.0"
)

app.include_router(users.router)


@app.get("/", tags=["root"])
def root():
    return {"message": "Welcome to the User API"}
