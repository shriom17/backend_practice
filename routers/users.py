from fastapi import APIRouter
router = APIRouter()

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]
@router.get("/users")
def get_users():
    return users

@router.post("/users")
def create_users(user: dict):
    user["id"] = len(users) + 1
    users.append(user)
    return {"message": "User created successfully", "user": user}

@router.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"message": "User not found"}