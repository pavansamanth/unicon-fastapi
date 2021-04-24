from sqlalchemy import Column, Integer, String, Text, DateTime, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base


class FileUpload(Base):
    __tablename__ = "FileUpload"

    id = Column(Integer, primary_key=True, index=True)
    fileName = Column(VARCHAR,unique=True)
    userId = Column(Integer, ForeignKey("Users.id"))
    uploadedDate = Column(DateTime)
    fileSize = Column(Integer)
    fileType = Column(VARCHAR)
    file_upload = relationship("UserTable",back_populates="fileUpload")