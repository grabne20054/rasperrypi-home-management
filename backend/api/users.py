from fastapi import APIRouter

from api.model import UserSchema, UserDB
from crud import crud


router = APIRouter()

@router.post("/users/", response_model=UserDB, status_code=201)
async def create_user(user: UserSchema):
    user = await crud.create_user(user)
    response_object = {
        "id": user.id,
        "name": user.name,
        "password": user.password
    }
    return response_object


@router.get("/users/", status_code=200)
async def read_users(username: str = None, password: str = None):
    users = await crud.read_users(username, password)
    return users


@router.get("/users/{user_id}", response_model=UserDB, status_code=200)
async def read_user(user_id: int):
    user = await crud.read_user(user_id)
    response_object = {
        "id": user.id,
        "name": user.name,
        "password": user.password
    }
    return response_object


@router.put("/users/{user_id}", response_model=UserDB, status_code=200)
async def update_user(user_id: int, user: UserSchema):
    user = await crud.update_user(user_id, user)
    response_object = {
        "id": user.id,
        "name": user.name,
        "password": user.password
    }
    return response_object


@router.delete("/users/{user_id}", status_code=200)
async def delete_user(user_id: int):
    return await crud.delete_user(user_id)
    
