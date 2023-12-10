from fastapi import APIRouter, status, Response, Path
from typing import Union, List
from models.users import User
from models.common import DefaultResponse
from utilite import get_user_by_id

router = APIRouter(
    prefix="/api",
    tags=["user"]
)

all_users = [
    User(id=1, name="Михаил", phone="+12345678", passport="00132345678"),
    User(id=2, name="Виталий", phone="+7912323456", passport="2434567891"),
    User(id=3, name="Антон", phone="+78005553535", passport="42224736385")
]

responses = {
    status.HTTP_404_NOT_FOUND: {"model": DefaultResponse, "description": "Not found"}
}


@router.get("/users/", response_model=Union[List[User], None], status_code=status.HTTP_200_OK)
def read_users():
    return all_users


@router.get("/users/{id}", response_model=Union[User, DefaultResponse],
            responses={**responses, status.HTTP_200_OK: {"model": User}})
def get_user(id: int, response: Response):
    user: User = get_user_by_id(id, all_users)
    if user == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="User not found")

    return user


@router.post("/users", response_model=DefaultResponse, status_code=status.HTTP_200_OK)
def create_user(user: User):
    all_users.append(user)

    return DefaultResponse(success=True, message="User successfully created")


@router.put("/users", response_model=Union[User, DefaultResponse],
            responses={**responses, status.HTTP_200_OK: {"model": User}})
def update_user(user: User, response: Response):
    exists_user: User = get_user_by_id(user.id, all_users)
    if exists_user == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="User not found")

    exists_user.name = user.name
    exists_user.phone = user.phone
    exists_user.passport = user.passport

    return exists_user


@router.delete("/users/{id}", response_model=DefaultResponse,
               responses={**responses, status.HTTP_200_OK: {"model": DefaultResponse}})
def remove_user(id: int, response: Response):
    user: User = get_user_by_id(id, all_users)
    if user == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="User not found")

    all_users.remove(user)

    return DefaultResponse(success=True, message="User successfully removed")