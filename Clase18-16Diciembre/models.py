# models.py
from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[int] = None
    name: str
    publisher: str
    year: int
    edition: int
    authors: str

class Review(BaseModel):
    review_id: Optional[int] = None
    book_id: int
    review: str
    validated: int

class Lending(BaseModel):
    book_id: Optional[int] = None
    user_id: Optional[int] = None
    start_date: str
    end_date: str