import datetime
import uuid
from fastapi import UploadFile
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import UUID as UUIDType
from sqlalchemy import UUID


class TagSchema(BaseModel):
    name: str
    class Config:
        from_attributes = True


class PostDetailsschema(BaseModel):
    title: str = Field(..., description="Title of the post detail")
    text_area: str = Field(..., description="Content of the post detail")
    class Config:
        from_attributes = True
        

class UpdateReleaseModelschema(BaseModel):
    title: Optional[str]  = None
    tags: Optional[List[TagSchema]]  = None
    release_date: datetime
    release_version: Optional[str]  = None
    post_image_url: Optional[str] = None
    info: Optional[str]  = None
    post_details: Optional[List[PostDetailsschema]]  = None


    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            UUID: str 
        }



# schemas.py

class ReleaseResponsechema(BaseModel):
    id: int
    uuid: Optional[str] = None 
    title: str
    tags: Optional[List[TagSchema]] = None
    release_date: datetime
    release_version: Optional[str] = None
    post_image_url: Optional[str] = None
    info: Optional[str] = None
    post_details: Optional[List[PostDetailsschema]] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders={UUID: str}




class PostPreviewSchema(BaseModel):
    id: str  
    uuid: Optional[str] = None
    title: str
    tags: Optional[List[TagSchema]] = None
    post_image_url: Optional[str] = None
    info: Optional[str] = None
    release_date: datetime
    release_version: Optional[str] = None
    post_details: Optional[List[PostDetailsschema]] = None

    class Config:
        orm_mode = True