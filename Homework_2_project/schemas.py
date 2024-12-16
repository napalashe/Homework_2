''' schemas.py
 Defines Pydantic models for request and response validation. These ensure that data sent to and from the API is validated and documented.'''

from pydantic import BaseModel
from typing import Optional
from datetime import date

#Base model for Book that will be reused or extended
class BookBase(BaseModel):
    #using title, author, publication and isbn
    title: str
    author: str
    publication_date: Optional[date] = None
    isbn: Optional[str] = None

#Model for creating a new book; all fields required except optional ones
class BookCreate(BookBase):
    pass

#Model for updating a book
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publication_date: Optional[date] = None
    isbn: Optional[str] = None

#Model for returning a book to the client
class BookOut(BookBase):
    id: int

    class Config:
        orm_mode = True
        #orm_mode = True allows Pydantic to read data from ORM objects directly.
