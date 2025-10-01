from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    author_id = Column(ForeignKey('users.id'), nullable=False)

    author = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title}, description={self.description[:20]})"
    