''' models.py
Defines the database tables via SQLAlchemy ORM models.'''

from sqlalchemy import Column, Integer, String, Date
from database import Base  # Import the Base from database.py

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
