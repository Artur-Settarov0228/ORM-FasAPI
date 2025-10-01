from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    username = Column(String, unique=True, nullable=False)
    gender = Column(String, nullable=False)
    phone = Column(String)

    relationship('Post', back_populates='author', cascade='all, delete-orphan')
    # comments = relationship('Comment', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, username={self.username}, phone={self.phone})"
    
