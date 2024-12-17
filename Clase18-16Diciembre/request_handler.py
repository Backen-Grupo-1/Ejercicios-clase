# request_handler.py

from fastapi import FastAPI, Body
import books_service
import reviews_service
import lending_service
from models import Book, Review, Lending

app = FastAPI()

# BOOKS
@app.get("/books")
def get_books():
    return books_service.get_books_list()

@app.post("/book")
def create_book(book: Book):
    return books_service.create_book(book)

@app.get("/book/{book_id}")
def get_book(book_id: str):
    return books_service.get_book_data(book_id)

@app.put("/book/{book_id}")
def update_book(book_id: str, updated_data: Book):
    return books_service.update_book(book_id, updated_data)

@app.delete("/book/{book_id}")
def delete_book(book_id: str):
    return books_service.delete_book(book_id)

    
# REVIEWS
@app.get("/reviews")
def get_reviews():
    return reviews_service.get_reviews_list()

@app.post("/review")
def create_review(review: Review):
    return reviews_service.create_review(review)

@app.get("/review/{review_id}")
def get_review(review_id: str):
    return reviews_service.get_review_data(review_id)

@app.put("/review/{review_id}")
def update_review(review_id: str, updated_data: Review):
    return reviews_service.update_review(review_id, updated_data)

@app.delete("/review/{review_id}")
def delete_review(review_id: str):
    return reviews_service.delete_review(review_id)


# LENDING
@app.get("/lendings")
def get_lendings():
    return lending_service.get_lending_list()

@app.post("/lending")
def create_lending(lending: Lending):
    return lending_service.create_lending(lending)

@app.get("/lending/{book_id}/{user_id}")
def get_lending(book_id: str, user_id: str):
    return lending_service.get_lending_data(book_id, user_id)

@app.put("/lending/{book_id}/{user_id}")
def update_lending(book_id: str, user_id: str, updated_data: Lending):
    return lending_service.update_lending(book_id, user_id, updated_data)

@app.delete("/lending/{book_id}/{user_id}")
def delete_lending(book_id: str, user_id: str):
    return lending_service.delete_lending(book_id, user_id)
