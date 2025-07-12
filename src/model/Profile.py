from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import random

Base = declarative_base()

class ProfileEntity(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, unique=True, nullable=False, default=lambda: str(random.randint(100000, 999999)))
    name = Column(String, nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ProfileEntity(user_id={self.user_id}, name='{self.name}', createdAt={self.createdAt})>"