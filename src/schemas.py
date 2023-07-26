from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr
from fastapi import File

from src.database.models import Role

class UserModel(BaseModel):
    username: str = Field(min_length=3, max_length=16)
    email: EmailStr
    password: str = Field(min_length=6, max_length=16)
    role: str = Field()


class UserDb(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    role: Role

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TagModel(BaseModel):
    name_tag: str = Field(max_length=25)


class TagResponse(TagModel):
    id: int
    class Config:
        orm_mode = True

class ImageBase(BaseModel):
    username: str
    id: int
    title: str
    url: str
    created_at: datetime

class ImageModel(ImageBase):
    tags: List[int]

class ImageResponse(ImageBase):
    user: UserDb
    id: int
    tags: List[TagResponse]

class CommentsBase(BaseModel):
    comment: str

class CommentsResponce(CommentsBase):
    username: str
    edit_date: str

class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
