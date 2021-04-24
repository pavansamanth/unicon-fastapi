from typing import List, Optional
from pydantic import BaseModel, validator
import re
from ..services import camelcase
from fastapi import HTTPException, status



class ForgotPassword(BaseModel):
    reset_password_token: str
    new_password: str
    confirm_password: str
    class Config:
        alias_generator = camelcase.to_camel
        allow_population_by_field_name = True
        orm_mode = True


    @validator("new_password")

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


    @validator("confirm_password")

    def passwords_match(cls, v, values, **kwargs):

        if "new_password" in values and v != values["new_password"]:

            raise HTTPException(

                status_code=status.HTTP_401_UNAUTHORIZED,

                detail="Passwords does not match",

            )

        return v