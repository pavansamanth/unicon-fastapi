from ..models import user_table, user_roles
from ..schemas import user_signup
from datetime import datetime
from dateutil import tz
import smtplib
from decouple import config
from sqlalchemy.orm import Session
from pydantic import EmailStr

# mail configurations

MAIL_SERVER = config("MAIL_SERVER")
MAIL_PORT = config("MAIL_PORT")
MAIL_PASSWORD = config("MAIL_PASSWORD")
MAIL_FROM = config("MAIL_FROM")
from_zone = tz.tzutc()
to_zone = tz.tzlocal()


def get_user_by_email(db: Session, email: EmailStr):
    return (
        db.query(user_table.UserTable)
        .filter(user_table.UserTable.email == email)
        .first()
    )


def get_id_by_email(db: Session, email: EmailStr):
    user = (
        db.query(user_table.UserTable)
        .filter(user_table.UserTable.email == email)
        .first()
    )
    return user.id


def add_user_to_userTable(firstName, lastName, email, password, db: Session):
    created_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    created = datetime.strptime(created_date, "%Y-%m-%d %H:%M:%S")
    created = created.replace(tzinfo=from_zone)
    central = created.astimezone(to_zone)
    new_user = user_table.UserTable(
        firstName=firstName,
        lastName=lastName,
        email=email,
        password=password,
        createdDate=central,
        modifiedDate=central,
    )
    db.add(new_user)
    db.commit()


async def send_email(email_reciever, email_token):
    Subject = "Unicon"
    url = f"https://google/email/activate/{email_token}"
    message = "Subject :{}\n\n Hi, \n Welcome to unicon! \n For Email verification or reset password please click on the below link: {}".format(Subject, url)

    try:
        server = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
        server.starttls()
        server.ehlo()
        server.login(MAIL_FROM, MAIL_PASSWORD)
        server.sendmail(MAIL_FROM, email_reciever, message)
        server.close()
        return f"The mail has been sent to :{email_reciever}"

    except:
        return "Cannot send email!"


def add_email_verify_token_db(email_token, token, db: Session):
    created_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    created = datetime.strptime(created_date, "%Y-%m-%d %H:%M:%S")
    created = created.replace(tzinfo=from_zone)
    central = created.astimezone(to_zone)
    email_verification = (
        db.query(user_table.UserTable)
        .filter(user_table.UserTable.email == email_token)
        .first()
    )
    email_verification.emailVerifyToken = token
    email_verification.emailVerifiedOn = central
    db.commit()


def add_role_db(account_type, id, db: Session):
    new_role = user_roles.UserRoles(accountType=account_type, userId=id)
    db.add(new_role)
    db.commit()


def update_user_password(email, hash_pass, reset_token, db):
    modified_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    modified = datetime.strptime(modified_date, "%Y-%m-%d %H:%M:%S")
    modified = modified.replace(tzinfo=from_zone)
    modified_date = modified.astimezone(to_zone)
    pass_update = (
        db.query(user_table.UserTable)
        .filter(user_table.UserTable.email == email)
        .first()
    )
    pass_update.resetPasswordToken = reset_token
    pass_update.password = hash_pass
    pass_update.modifiedDate = modified_date
    db.commit()
    db.refresh(pass_update)
    return pass_update
