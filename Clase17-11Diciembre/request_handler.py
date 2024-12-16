# request_handler.py

from fastapi import FastAPI
import books_service

app = FastAPI()

@app.get("/book/{book_id}")
def get_book(book_id: str):
    if len(book_id) not in [10, 13]:
        raise HTTPException(status_code=400, detail="ISBN no válido.")
    
    book_data = books_service.get_book_basic_data(book_id)
    if not book_data:
        raise HTTPException(status_code=404, detail="Book no encontrado.")
    
    book_data["more_data"] = "http://localhost:8000/book/details/" + book_id
    return book_data

@app.get("/book/details/{book_id}")
def get_book_details(book_id: str):
    if len(book_id) not in [10, 13]:
        raise HTTPException(status_code=400, detail="ISBN no válido.")
    
    book_details = books_service.get_a_book_details(book_id)
    if not book_details:
        raise HTTPException(status_code=404, detail="Book no encontrado.")
    
    return book_details

@app.put("/book/{book_id}")
def update_book(book_id: str, updated_data: dict):
    if len(book_id) not in [10, 13]:
        raise HTTPException(status_code=400, detail="ISBN no válido.")
    
    updated_book = books_service.update_book(book_id, updated_data)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book no encontrado.")
    
    return updated_book

@app.delete("/book/{book_id}")
def delete_book(book_id: str):
    if len(book_id) not in [10, 13]:
        raise HTTPException(status_code=400, detail="ISBN no válido.")
    
    result = books_service.delete_book(book_id)
    if not result:
        raise HTTPException(status_code=404, detail="Book no encontrado.")
    
    return result
