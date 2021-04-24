from typing import List, Optional

from pydantic import BaseModel, EmailStr, validator
import datetime
from ..services import camelcase
import re
from fastapi import HTTPException, status


class Category(BaseModel):
    categoryName : str
    categoryDescription : str
    userID: int
    class Config:
        orm_mode = True