import mysql.connector
#pip install mysql-connector-python
from mysql.connector import Error

try:
    print("connecting to MySQL database  trying...")
    # 1. Establish the connection to the database
    connection = mysql.connector.connect(
        host='localhost',          # Your MySQL server host (e.g., '127.0.0.1')
        database='testdb',  # Name of the database you want to use
        user='root',               # Your MySQL username
        password='Root@123$' ,  # Your MySQL password
        use_pure=True     # Bypasses problematic C-extension bugs on Windows
    )

    if connection.is_connected():
        print("Successfully connected to the database!")

        # 2. Create a cursor object to execute queries
        cursor = connection.cursor()

        # 3. Execute a SQL query
        cursor.execute("SELECT VERSION();")

        # 4. Fetch the result
        db_version = cursor.fetchone()
        print(f"MySQL Database Version: {db_version[0]}")

        cursor.execute("SHOW TABLES")

        for x in cursor:
            print(x)

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # 5. Always close the cursor and connection when done
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")

print("connection successful")