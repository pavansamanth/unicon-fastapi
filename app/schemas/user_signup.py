from typing import List, Optional
from pydantic import BaseModel, EmailStr, validator
import datetime
from ..services import camelcase
import re
from fastapi import HTTPException, status


class UserSignup(BaseModel):

    first_name: str

    last_name: str

    Email: EmailStr

    password: str

    account_type: str


    class Config:

        alias_generator = camelcase.to_camel

        allow_population_by_field_name = True

        orm_mode = True


    @validator("first_name", "last_name")

    def name_valid(cls, v):

        if all(x.isalpha() or x.isspace() for x in v):

            return v

        else:

            raise HTTPException(

                status_code=418,

                detail="Sorry, No special characters or numbers. You can use spaces along with letters",

            )


    @validator("Email")

    def user_email_valid(cls, v):

        regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"

        if re.search(regex, v):

            return v

        else:

            raise HTTPException(status_code=420, detail="Invalid email address!")


    @validator("password")

    def user_password_valid(cls, v):

        if len(v) < 8:

            raise HTTPException(

                status_code=400, detail="Make sure your password is at lest 8 letters"

            )

        elif re.search("[0-9]", v) is None:

            raise HTTPException(

                status_code=400, detail="Make sure your password has a number in it"

            )

        elif re.search("[A-Z]", v) is None:

            raise HTTPException(

                status_code=400,

                detail="Make sure your password has a capital letter in it",

            )

        elif re.search("[#@$&*_!]", v) is None:

            raise HTTPException(

                status_code=400, detail="Make sure you have a special character in it"

            )

        else:

            return v
