#models.py is used to creat tables inside the database
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.expression import null
from .database import Base

# class Post(Base):
#     __tablename__ = "posts"
#     id = Column(Integer, primary_key = True, nullable = False)
#     title = Column(String, nullable = False)
#     content = Column(String, nullable = False)
#     published = Column(Boolean, server_default = 'TRUE', nullable = False)
#     created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
#     owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)


# class Users(Base):
#     __tablename__ = "users"
#     id = Column(Integer, nullable = False, primary_key = True)
#     email = Column(String, nullable = False, unique = True)
#     password = Column(String, nullable = False)
#     created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))

# class Votes(Base):
#     __tablename__ = "Votes"
#     post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key = True)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key = True)

    