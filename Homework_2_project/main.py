'''main.py
 Defines the CRUD endpoints for the Book resource.'''

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from typing import List

#Create all tables if they don't exist
Base.metadata.create_all(bind=engine)

#Instantiate the FastAPI app
app = FastAPI(
    title="Book Management System",
    description="A simple CRUD API to manage books in a MySQL database",
    version="1.0.0"
)

# Dependency to get a DB session on each request
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        #Yield the session to the endpoint
        yield db
    finally:
        #Close the session after the request
        db.close()

'''Create a new book inside the database'''
@app.post("/books", response_model=schemas.BookOut, summary="Create a new book")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    # book: schemas.BookCreate -> The request body is validated against BookCreate schema
    # db: Session = Depends(get_db) -> Dependency injection providing a DB session

    #Create a new Book model instance
    db_book = models.Book(
        title=book.title,
        author=book.author,
        publication_date=book.publication_date,
        isbn=book.isbn
    )

    # Add the new book to the session
    db.add(db_book)
    # Commit the transaction to persist in DB
    db.commit()
    # Refresh to load the generated ID
    db.refresh(db_book)

    return db_book


'''Read all books from the list of books'''
@app.get("/books", response_model=List[schemas.BookOut], summary="Get a list of all books")
def list_books(db: Session = Depends(get_db)):
    # uery all Book records
    books = db.query(models.Book).all()
    #Return all books
    return books


'''Read a book by a specific ID '''
@app.get("/books/{book_id}", response_model=schemas.BookOut, summary="Get details of a specific book")
def get_book(book_id: int, db: Session = Depends(get_db)):
    #Query for the book by its ID
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    #If not found, raise a 404 error
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
        #Return Book
    return book


'''Update a book by its ID'''
@app.put("/books/{book_id}", response_model=schemas.BookOut, summary="Update a book's information")
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    #Get the book from the DB
    book_db = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book_db:
        raise HTTPException(status_code=404, detail="Book not found")

    #Update fields if provided
    if book_update.title is not None:
        book_db.title = book_update.title
    if book_update.author is not None:
        book_db.author = book_update.author
    if book_update.publication_date is not None:
        book_db.publication_date = book_update.publication_date
    if book_update.isbn is not None:
        book_db.isbn = book_update.isbn

    # Commit changes
    db.commit()
    db.refresh(book_db)
    #Return book that was updated
    return book_db


'''Delete a book by it's ID'''
@app.delete("/books/{book_id}", summary="Delete a book by ID")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    #Find the book
    book_db = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book_db:
        raise HTTPException(status_code=404, detail="Book not found")

    #Delete the book from DB
    db.delete(book_db)
    db.commit()
    #Return Json message
    return {"message": "Book deleted successfully"}

