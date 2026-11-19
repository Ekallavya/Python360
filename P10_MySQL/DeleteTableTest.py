import mysql.connector
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
        cursor = connection.cursor()

        sql = "DELETE FROM py_customers WHERE address = 'Highway 23'"

        cursor.execute(sql)

        connection.commit()

        print(cursor.rowcount, "record(s) deleted")




except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # 5. Always close the cursor and connection when done
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")

print("connection successful")