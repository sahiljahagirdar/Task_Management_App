from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.orm import session
from src.users.dtos import UserSchema,ResponseModel,LoginSchema
from src.utils.db import get_db
from src.users import controller
from typing import List


user_router = APIRouter(prefix='/user')

@user_router.post("/register",response_model=ResponseModel,status_code=status.HTTP_201_CREATED)
def register(body:UserSchema,db=Depends(get_db)):
    return controller.register_user(body,db)

@user_router.get('/all_users',response_model=List[ResponseModel],status_code=status.HTTP_200_OK)
def all_users(db=Depends(get_db)):
    return controller.get_all_users(db)

@user_router.post('/login',status_code=status.HTTP_200_OK)
def login(body:LoginSchema,db:session=Depends(get_db)):
    return controller.login_user(body,db)


@user_router.get('/is_auth',response_model=ResponseModel,status_code=status.HTTP_200_OK)
def is_auth(request:Request,db=Depends(get_db)):
    return controller.is_authenticated(request,db)