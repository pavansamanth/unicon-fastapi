from typing import List, Optional
from pydantic import BaseModel, EmailStr


class TokenData(BaseModel):

    email: Optional[EmailStr] = None