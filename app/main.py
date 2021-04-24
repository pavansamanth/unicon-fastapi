from fastapi import FastAPI
from .models import user_roles, user_table,file_upload,category_table
from .database import engine
from .v1 import user_api,job_api,admin

app = FastAPI()


user_table.Base.metadata.create_all(engine)
user_roles.Base.metadata.create_all(engine)


app.include_router(user_api.router)
app.include_router(admin.router)
app.include_router(job_api.router)


