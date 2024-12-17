# lending_service.py

import sqlite3
from models import Lending

def get_db_connection():
    conn = sqlite3.connect("tf_backend_book.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_lending_list():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM book_lending")
    rows = cur.fetchall()
    conn.close()
    return rows

def create_lending(lending: Lending):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO book_lending (book_id, user_id, start_date, end_date)
            VALUES (?, ?, ?, ?)
        """, (lending.book_id, lending.user_id, lending.start_date, lending.end_date))
        
        conn.commit()
        conn.close()
        return {"message": "lending creado exitosamente."}
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al crear el lending: {str(e)}"}

def get_lending_data(book_id, user_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        res = cur.execute("""
            SELECT * FROM book_lending WHERE book_id = ? AND user_id = ?
        """, (book_id, user_id)).fetchone()
        
        conn.commit()
        conn.close()
        
        if res is None:
            return {"message": f"lending con ID {lending_id} no encontrado."}
        return res
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al obtener los datos del lending: {str(e)}"}

def update_lending(book_id, user_id, lending: Lending):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        res = cur.execute("""
            UPDATE book_lending SET start_date = ?, end_date = ? WHERE book_id = ? AND user_id = ?
        """, (lending.start_date, lending.end_date, book_id, user_id))
        
        if cur.rowcount == 0:
            conn.close()
            return {"message": f"lending con BOOK_ID {book_id} y USER_ID {user_id} no encontrado."}

        conn.commit()
        conn.close()
        return {"message": "lending actualizado exitosamente."}
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al actualizar el lending: {str(e)}"}

def delete_lending(book_id, user_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        res = cur.execute("""
            DELETE FROM book_lending WHERE book_id = ? AND user_id = ?
        """, (book_id, user_id))

        if cur.rowcount == 0:
            conn.close()
            return {"message": f"lending con BOOK_ID {book_id} y USER_ID {user_id} no encontrado."}
        
        conn.commit()
        conn.close()
        return {"message": "lending eliminado exitosamente."}
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al eliminar el lending: {str(e)}"}
