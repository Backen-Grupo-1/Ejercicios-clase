# review_service.py

import sqlite3
from models import Review

def get_db_connection():
    conn = sqlite3.connect("tf_backend_book.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_reviews_list():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM book_reviews")
    rows = cur.fetchall()
    conn.close()
    return rows

def create_review(review: Review):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO book_reviews (review_id, book_id, review, validated)
            VALUES (?, ?, ?, ?)
        """, (review.review_id, review.book_id, review.review, review.validated))
        
        conn.commit()
        conn.close()
        return {"message": "Review creado exitosamente."}
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al crear el Review: {str(e)}"}

def get_review_data(review_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        res = cur.execute("""
            SELECT * FROM book_reviews WHERE review_id = ?
        """, (review_id)).fetchone()
        
        conn.commit()
        conn.close()
        
        if res is None:
            return {"message": f"Review con ID {review_id} no encontrado."}
        return res
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al obtener los datos del Review: {str(e)}"}

def update_review(review_id, review: Review):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        res = cur.execute("""
            UPDATE book_reviews SET book_id = ?, review = ?, validated = ? WHERE review_id = ?
        """, (review.book_id, review.review, review.validated, review_id))
        
        if cur.rowcount == 0:
            conn.close()
            return {"message": f"Review con ID {review_id} no encontrado."}

        conn.commit()
        conn.close()
        return {"message": "Review actualizado exitosamente."}
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al actualizar el Review: {str(e)}"}

def delete_review(review_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        res = cur.execute("""
            DELETE FROM book_reviews WHERE review_id = ?
        """, (review_id))

        if cur.rowcount == 0:
            conn.close()
            return {"message": f"Review con ID {review_id} no encontrado."}
        
        conn.commit()
        conn.close()
        return {"message": "Review eliminado exitosamente."}
    except sqlite3.Error as e:
        conn.close()
        return {"error": f"Ocurrió un error al eliminar el Review: {str(e)}"}
