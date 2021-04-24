from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from pydantic import EmailStr
from ..models import user_table, user_roles, file_upload, category_table
from datetime import datetime
from dateutil import tz


from_zone = tz.tzutc()
to_zone = tz.tzlocal()


def add_file_to_db(
    file_name, file_size, file_type, current_user: user_table.UserTable, db: Session
):
    created_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    created = datetime.strptime(created_date, "%Y-%m-%d %H:%M:%S")
    created = created.replace(tzinfo=from_zone)
    central = created.astimezone(to_zone)
    new_file_upload = file_upload.FileUpload(
        fileName=file_name, uploadedDate=central, fileSize=file_size, fileType=file_type
    )
    new_file_upload.file_upload = current_user
    db.add(new_file_upload)
    db.commit()
    db.refresh(new_file_upload)
    return new_file_upload


def add_to_categorytable(category, db: Session):
    created_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    created = datetime.strptime(created_date, "%Y-%m-%d %H:%M:%S")
    created = created.replace(tzinfo=from_zone)
    central = created.astimezone(to_zone)
    new_category = category_table.Category(
        categoryName=category.categoryName,
        categoryDescription=category.categoryDescription,
        userID=category.userID,
        createdDate=central,
        modifiedDate=central,
    )
    db.add(new_category)
    db.commit()


def get_categories_from_db(db: Session):
    get_all = db.query(category_table.Category.categoryName).all()
    return get_all