# book_service.py

import sqlite3
from models import Book

def get_db_connection():
    conn = sqlite3.connect("tf_backend_book.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_books_list():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def create_book(book: Book):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO books (id, name, publisher, year, edition, authors)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (book.id, book.name, book.publisher, book.year, book.edition, book.authors))
        
        conn.commit()
        conn.close()
        return {"message": "Libro creado exitosamente."}
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al crear el libro: {str(e)}"}

def get_book_data(book_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        res = cur.execute("""
            SELECT * FROM books WHERE id = ?
        """, (book_id)).fetchone()
        
        conn.commit()
        conn.close()
        
        if res is None:
            return {"message": f"Libro con ID {book_id} no encontrado."}
        return res
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al obtener los datos del libro: {str(e)}"}

def update_book(book_id, book: Book):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        res = cur.execute("""
            UPDATE books SET name = ?, publisher = ?, year = ?, edition = ?, authors = ? WHERE id = ?
        """, (book.name, book.publisher, book.year, book.edition, book.authors, book_id))
        
        if cur.rowcount == 0:
            conn.close()
            return {"message": f"Libro con ID {book_id} no encontrado."}

        conn.commit()
        conn.close()
        return {"message": "Libro actualizado exitosamente."}
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al actualizar el libro: {str(e)}"}

def delete_book(book_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        res = cur.execute("""
            DELETE FROM books WHERE id = ?
        """, (book_id))

        if cur.rowcount == 0:
            conn.close()
            return {"message": f"Libro con ID {book_id} no encontrado."}
        
        conn.commit()
        conn.close()
        return {"message": "Libro eliminado exitosamente."}
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al eliminar el libro: {str(e)}"}
