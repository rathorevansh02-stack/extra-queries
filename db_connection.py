import psycopg2

def get_connection():
    """Establishes a connection tunnel to the PostgreSQL service."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="0210",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Connection Failure: {e}")
        return None