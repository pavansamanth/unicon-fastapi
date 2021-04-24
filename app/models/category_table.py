from sqlalchemy import Column, Integer, String, Text, DateTime, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from sqlalchemy.dialects.postgresql import UUID


class Category(Base):
    __tablename__ = "Category"

    id = Column(Integer, primary_key=True, index=True)
    categoryName = Column(Text,unique=True)
    categoryDescription = Column(Text)
    userID = Column(Integer)
    createdDate = Column(DateTime)
    modifiedDate = Column(DateTime)