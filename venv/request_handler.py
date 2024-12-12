from fastapi import FastAPI, HTTPException
import books_service

app = FastAPI()

@app.get("/")
def root():
    return {"menssage": "Hello world!"}

@app.get("/book/{book_id}")
def get_book(book_id: str):
    if len(book_id) != 10 and len(book_id) != 13:
            raise HTTPException(status_code=400, detail="ISBN no valido")
    book_data = books_service.get_book_basic_data(book_id)
    if book_data == None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    book_data["details"] = "http://localhost:8000/book/details/" + book_id
    return book_data

@app.get("/book/details/{book_id}")
def get_book(book_id: str):
    book_details = books_service.get_a_book_details(book_id)
    print(book_details)
    book_data = {"isbn": book_id}
    book_data["details"] = book_details
    return book_data

@app.put("/book/{book_id}")
def update_book(book_id: str, updated_data: dict):
    updated_book = books_service.update_book(book_id, updated_data)
    return updated_book