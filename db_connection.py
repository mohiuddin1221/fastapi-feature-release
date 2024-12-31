import psycopg2

try:
    # Make sure to replace the password with the correct one
    conn = psycopg2.connect(
        host="",  # Azure PostgreSQL host
        database="",  # Database name, typically 'postgres' for default
        user="",  # Your database username
        password=""  # Replace with your actual password
    )
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
