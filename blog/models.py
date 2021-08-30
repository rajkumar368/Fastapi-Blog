
from blog.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id =  Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    blog = relationship('blog', back_populates='creator')


class blog(Base):
    __tablename__ = 'blog'

    id =  Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    description = Column(String)
    creator_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship('User', back_populates='blog')