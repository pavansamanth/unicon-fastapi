from decouple import config
from datetime import datetime, timedelta
from jose import jwt, JWTError
import subprocess


cmd = "openssl rand -hex 32"
process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
out, err = process.communicate()
value = out.decode().strip()

SECRET_KEY = "'" + value + "'"
ALGORITHM = config("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES")



def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(

        minutes=float(str(ACCESS_TOKEN_EXPIRE_MINUTES))

    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt



def get_email_by_token(token):

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    email: str = payload.get("sub")

    return email