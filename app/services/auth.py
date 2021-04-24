from jose import jwt, JWTError
from fastapi import HTTPException, Security, Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .token import SECRET_KEY
from decouple import config
from ..database import get_db
from sqlalchemy.orm import Session
from ..crud import user_crud
from ..schemas import token_data

ALGORITHM = config("ALGORITHM")


# class for token authentication.

class AuthHandler:

    security = HTTPBearer()

    # decoding access token and getting the user email for that token

    def decode_token(self, token, db: Session = Depends(get_db)):

        try:

            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

            email: str = payload.get("sub")

            if email is None:

                raise HTTPException(

                    status_code=status.HTTP_401_UNAUTHORIZED,

                    detail="Invalid Credentials",

                )

            token_data_ex = token_data.TokenData(email=email)


        except JWTError:

            raise HTTPException(

                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"

            )

        user = user_crud.get_user_by_email(db, email=token_data_ex.email)

        if user is None:

            raise HTTPException(

                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"

            )

        return user


    # function for token authorization

    def auth_wrapper(

        self,

        auth: HTTPAuthorizationCredentials = Security(security),

        db: Session = Depends(get_db),

    ):

        return self.decode_token(auth.credentials, db)