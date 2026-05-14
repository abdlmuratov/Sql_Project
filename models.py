from typing import List, Optional
from sqlalchemy import String, Text, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from datetime import datetime

post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)

class Author(Base):
    __tablename__ = "authors"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    
    posts: Mapped[List["Post"]] = relationship(back_populates="author")

class Category(Base):
    __tablename__ = "categories"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    
    posts: Mapped[List["Post"]] = relationship(back_populates="category")

class Tag(Base):
    __tablename__ = "tags"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    
    posts: Mapped[List["Post"]] = relationship(secondary=post_tags, back_populates="tags")

class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    category_id: Mapped[Optional[int]] = mapped_column(ForeignKey("categories.id"))
    
    author: Mapped["Author"] = relationship(back_populates="posts")
    category: Mapped["Category"] = relationship(back_populates="posts")
    tags: Mapped[List["Tag"]] = relationship(secondary=post_tags, back_populates="posts")