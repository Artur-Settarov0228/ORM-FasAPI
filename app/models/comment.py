from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    post_id = Column(ForeignKey('posts.id'), nullable=False)

    # user = relationship('User', back_populates='comments')
    # post = relationship('Post', back_populates='comments')

    def __repr__(self):
        return f"Post(id={self.id})"
    