from sqlalchemy import Column, Integer, String, Text, DateTime, VARCHAR
from sqlalchemy.orm import relationship
from ..database import Base


class EmailVerify(Base):
    __tablename__ = "EmailVerification"

    id = Column(Integer, primary_key=True, index=True)
    
