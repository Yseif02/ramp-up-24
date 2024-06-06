from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    year: int


app = FastAPI()

books = {} 

@app.post("/books/")
def create_book(book: Book):
    book.id = len(books) + 1
    books[book.id] = book
    return book, book.id

@app.get("/books/")
def get_all_books():
    return books

@app.get("/books/{id}")
def get_book_by_id(id: int):
    for book in books:
        if book.id == id:
            return {"Title" : book.title, "book" : book}
    return {"message": "Book not found"}

@app.put("/books/{id}")
def update_book(id: int, updated_book: Book):
    if books[id] is None:
        return {"message": "Book not found"}
    else:
        books[id] = updated_book
        return {"message": "Book updated successfully"}
    return {"message": "Book not found"}

@app.delete("/books/{id}")
def delete_book(id: int):
    for book in books:
        if book.id == id:
            books.remove(book)
            return {"message": "Book deleted successfully", "book id": id}
    return {"message": "Book not found"}