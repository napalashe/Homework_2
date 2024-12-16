# Book Management System

A simple FastAPI application to manage books stored in a MySQL database. It provides endpoints to register users, log in, and perform CRUD operations on books. Users must be logged in to create, update, or delete books.

## Features

- **User Registration**: Create an account by providing a unique username and password.
- **User Login**: Log in with your credentials to start creating or managing books.
- **Create Book**: Add a new book with a title, author, publication date, and ISBN.
- **Read Books**: Retrieve all books or fetch details of a specific book by its ID.
- **Update Book**: Update the title, author, publication date, or ISBN of an existing book.
- **Delete Book**: Remove a book from the database.

## Endpoints

- `POST /register`: Register a new user.
- `POST /login`: Log in as a user.
- `POST /books`: Create a new book (requires login).
- `GET /books`: List all books.
- `GET /books/{book_id}`: Get details of a specific book.
- `PUT /books/{book_id}`: Update a book (requires login).
- `DELETE /books/{book_id}`: Delete a book (requires login).

## Requirements

- Python 3.10+
- MySQL database
- Virtual environment (recommended)

## Setup

1. Clone this repository.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
