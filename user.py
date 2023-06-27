# main.py
from fastapi import APIRouter
from typing import List
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from models import Gender, Role, User, UpdateUser
from uuid import UUID

app = FastAPI()

db: List[User] = [
 User(
 id=uuid4(),
 first_name="John",
 last_name="Doe",
 gender=Gender.male,
 roles=[Role.user],
 ),

 User(
 id=uuid4(),
 first_name="Jane",
 last_name="Didier",
 gender=Gender.female,
 roles=[Role.user],
 ),

 User(
 id=uuid4(),
 first_name="James",
 last_name="Gabriel",
 gender=Gender.male,
 roles=[Role.user],
 ),

 User(
 id=uuid4(),
 first_name="Eunit",
 last_name="Eunice",
 gender=Gender.male,
 roles=[Role.admin, Role.user],
 ),

  User(
 id=uuid4(),
 first_name="Eunit",
 last_name="rené",
 gender=Gender.male,
 roles=[Role.admin, Role.user],
 ),

  User(
 id=uuid4(),
 first_name="Eunit",
 last_name="bernard",
 gender=Gender.male,
 roles=[Role.admin, Role.user],
 ),
]


@app.get("/users/", tags=["Utilisateurs"])
async def get_users():
 return db


@app.post("/users/")
async def create_user(user: User):
 db.append(user)
 return {"id": user.id}


@app.put("/users/{id}")
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user.id
    raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")


@app.delete("/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Delete user failed, id {id} not found.")




