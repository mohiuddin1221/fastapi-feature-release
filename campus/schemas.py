from pydantic import BaseModel, EmailStr, HttpUrl # type: ignore
from typing import Optional

class CampusAmbassadorCreate(BaseModel):
    name: str
    phone_number: str
    email_address: EmailStr
    university: str
    cv: Optional[bytes] = None
    want_to_be: str 
    in_any_club: str
    facebook: Optional[HttpUrl] = None
    instagram: Optional[HttpUrl] = None
    linkdin: Optional[HttpUrl] = None
