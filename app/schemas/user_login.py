from typing import List, Optional
from pydantic import BaseModel, EmailStr



class UserLogin(BaseModel):

    email: EmailStr

    password: str