from sqlalchemy import Column, Integer, String, Text, DateTime, VARCHAR
from sqlalchemy.orm import relationship
from ..database import Base

class UserTable(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String(50))
    lastName = Column(String(50))
    email = Column(Text, unique=True)
    emailVerifyToken = Column(Text, unique=True)
    emailVerifiedOn = Column(DateTime)
    resetPasswordToken = Column(Text, unique=True)
    password = Column(VARCHAR)
    createdDate = Column(DateTime)
    modifiedDate = Column(DateTime)
    user = relationship("UserRoles", backref="Users")
    fileUpload = relationship("FileUpload",back_populates="file_upload")

