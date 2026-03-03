from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas.user import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

# In-memory database (replace with real DB later)
users_db: List[dict] = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]


def get_next_id() -> int:
    """Generate next user ID"""
    return max((user["id"] for user in users_db), default=0) + 1


def find_user(user_id: int) -> dict | None:
    """Find user by ID"""
    for user in users_db:
        if user["id"] == user_id:
            return user
    return None


@router.get("/", response_model=List[UserResponse])
def get_all_users():
    """Get all users"""
    return users_db


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    """Get a single user by ID"""
    user = find_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return user


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate):
    """Create a new user"""
    # Check if email already exists
    for user in users_db:
        if user["email"] == user_data.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    
    new_user = {
        "id": get_next_id(),
        "name": user_data.name,
        "email": user_data.email
    }
    users_db.append(new_user)
    return new_user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate):
    """Update an existing user"""
    user = find_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    
    # Check email uniqueness if being updated
    if user_data.email and user_data.email != user["email"]:
        for u in users_db:
            if u["email"] == user_data.email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered"
                )
    
    # Update only provided fields
    if user_data.name is not None:
        user["name"] = user_data.name
    if user_data.email is not None:
        user["email"] = user_data.email
    
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    """Delete a user"""
    user = find_user(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    
    users_db.remove(user)
    return None