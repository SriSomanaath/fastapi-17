from fastapi import APIRouter, HTTPException
from src.db import get_connection

router = APIRouter()

# ✅ Create a Book
@router.post("/books/")
def create_book(title: str, author: str, published_year: int):
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO books (title, author, published_year) VALUES (%s, %s, %s) RETURNING *",
                (title, author, published_year),
            )
            new_book = cur.fetchone()
            conn.commit()
            return {"message": "Book added successfully!", "book": new_book}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# ✅ Read All Books
@router.get("/books/")
def get_books():
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM books")
            books = cur.fetchall()
            return books
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# ✅ Read a Book by ID
@router.get("/books/{book_id}")
def get_book(book_id: int):
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
            book = cur.fetchone()
            if not book:
                raise HTTPException(status_code=404, detail="Book not found")
            return book
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# ✅ Update a Book
@router.put("/books/{book_id}")
def update_book(book_id: int, title: str, author: str, published_year: int):
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")

    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE books SET title=%s, author=%s, published_year=%s WHERE id=%s RETURNING *",
                (title, author, published_year, book_id),
            )
            updated_book = cur.fetchone()
            if not updated_book:
                raise HTTPException(status_code=404, detail="Book not found")
            conn.commit()
            return {"message": "Book updated successfully!", "book": updated_book}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# ✅ Delete a Book
@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")

    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM books WHERE id = %s RETURNING *", (book_id,))
            deleted_book = cur.fetchone()
            if not deleted_book:
                raise HTTPException(status_code=404, detail="Book not found")
            conn.commit()
            return {"message": "Book deleted successfully!", "book": deleted_book}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()
