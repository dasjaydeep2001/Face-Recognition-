from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime,Text
from sqlalchemy.orm import relationship
import datetime
from database import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "face_data"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, unique=True, index=True)
    encoding = Column(Text(length=None))
    created_date =Column(DateTime, default=datetime.datetime.utcnow)

