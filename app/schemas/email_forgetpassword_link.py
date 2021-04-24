from typing import List, Optional
from pydantic import BaseModel, EmailStr


class email_forgetpassword(BaseModel):
    Email: EmailStr
