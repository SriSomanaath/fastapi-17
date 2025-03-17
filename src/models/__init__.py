from db import get_connection

def create_table():
    """Create books table if it doesn't exist."""
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS books (
                        id SERIAL PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        published_year INT
                    )
                """)
                conn.commit()
                print("✅ Table 'books' created successfully!")
        except Exception as e:
            print(f"❌ Error creating table: {e}")
        finally:
            conn.close()

# Run this function when the module is imported
create_table()
