''' models.py
Defines the database tables via SQLAlchemy ORM models.'''

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base 

#Book model representing a "books" table
class Book(Base):
    #Name of the table
    __tablename__ = "books"  

    #Primary key field
    id = Column(Integer, primary_key=True, index=True)  
    #Title of the book, up to 255 chars
    title = Column(String(255), nullable=False)         
    #Author name, up to 255 chars
    author = Column(String(255), nullable=False)        
    #Publication date of the book, stored as DATE in MySQL
    publication_date = Column(Date, nullable=True)      
    #ISBN of the book, unique if desired
    isbn = Column(String(13), unique=True, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationship: each book belongs to one user
    user = relationship("User", back_populates="books")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    #Relationship: one user can have many books
    books = relationship("Book", back_populates="user")

