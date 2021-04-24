from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from ..database import Base



class UserRoles(Base):
    __tablename__ = "UserRoles"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("Users.id"))
    accountType = Column(String)
    roles = relationship("UserTable", back_populates="user")
