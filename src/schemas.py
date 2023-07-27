from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field
from fastapi import File
from src.database.models import Role


class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=16)


class UserModel(UserBase):
    role: str = Field()


class UserDb(BaseModel):
    id: int
    username: str = "Jack"
    email: str = "jacck@jack.com"
    created_at: datetime

    # avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    username: UserDb
    detail: str = "User successfully created"


class UserBan(BaseModel):
    user_id: int
    banned: bool = True


class UserChangeRole(BaseModel):
    user_id: int
    role: Role


class UserDBBanned(UserDb):
    banned: bool


class UserDBRole(UserDb):
    role: Role


####################################TAG###############################
class TagModel(BaseModel):
    name_tag: str = Field(max_length=25)


class TagResponse(TagModel):
    id: int
    name_tag: str

    class Config:
        orm_mode = True


#################################TOKEN###############################
class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


#################################COMMENT####################################
class CommentDeleteResponse(BaseModel):
    id: int = 1
    comment: str = 'My comment'

    class Config:
        orm_mode = True


#
class CommentResponse(BaseModel):
    id: int = 1
    comment: str
    username: UserDb
    image_id: int = 1

    class Config:
        orm_mode = True


class CommentModel(BaseModel):
    comment: str = Field(min_length=1, max_length=255)
    image_id: int = Field(1, gt=0)
    user_id: int = Field(1, gt=0)


######################################IMAGE#############################
class ImageAddModel(BaseModel):
    description: str = Field(max_length=500)
    tags: Optional[List[str]]


class ImageAddTagModel(BaseModel):
    tags: Optional[List[str]]


class ImageUpdateModel(BaseModel):
    description: str = Field(max_length=500)


class ImageDb(BaseModel):
    id: int
    url: str
    title: str
    description: str
    tags: List[TagResponse]
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
        exclude = {'updated_at', 'user', 'title'}


class ImageGetResponse(BaseModel):
    image: ImageDb
    comments: List[CommentResponse]

class ImageChangeSizeModel(BaseModel):
    title: str
    height: int 
    width: int
    description: str
    tags: Optional[List[str]]


class ImageChangeColorModel(BaseModel):
    title: str
    object: str 
    color: str
    description: str
    tags: Optional[List[str]]

class ImageTransformModel(BaseModel):
    title: str
    description: str
    tags: Optional[List[str]]

class ImageSignModel(BaseModel):
    title: str
    text: str
    description: str
    tags: Optional[List[str]]



class ImageGetAllResponse(BaseModel):
    images: List[ImageGetResponse]


class ImageAddResponse(BaseModel):
    image: ImageDb
    detail: str = "Image has been added"

    class Config:
        orm_mode = True


class ImageAddTagResponse(BaseModel):
    id: int
    tags: List[TagResponse]
    detail: str = "Image tag has been updated"

    class Config:
        orm_mode = True


class ImageUpdateDescrResponse(BaseModel):
    id: int
    description: str
    detail: str = "Image has been updated"

    class Config:
        orm_mode = True


class ImageDeleteResponse(BaseModel):
    image: ImageDb
    detail: str = "Image has been deleted"
