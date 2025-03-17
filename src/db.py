import psycopg2
from psycopg2.extras import RealDictCursor
from src.config import DATABASE_URL

def get_connection():
    """Establish and return a PostgreSQL database connection."""
    try:
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        print("✅ Database connected successfully!")
        return conn
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return None
