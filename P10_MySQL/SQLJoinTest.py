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
        try:
            print("creating tables! if doesn't exist")
            cursor.execute("CREATE TABLE py_users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav_product_id VARCHAR(255))")
            cursor.execute("CREATE TABLE py_products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price DECIMAL(10, 2))")
        except Error as e:
            print(f"Error while creating tables: {e}")

        sql = "INSERT INTO py_users (name, fav_product_id) VALUES (%s, %s)"
        val = ("John", "2")
        cursor.execute(sql, val)
        sql = "INSERT INTO py_users (name, fav_product_id) VALUES (%s, %s)"
        val = ("Peter", "2")
        cursor.execute(sql, val)
        sql = "INSERT INTO py_users (name, fav_product_id) VALUES (%s, %s)"
        val = ("Amy", "3")
        cursor.execute(sql, val)
        sql = ("INSERT INTO py_users (name, fav_product_id) VALUES (%s, %s)")
        val = ("Hannah", "1")
        cursor.execute(sql, val)
        sql = ("INSERT INTO py_users (name, fav_product_id) VALUES (%s, %s)")
        val = ("Michael", "4")
        cursor.execute(sql, val)


        sql = "INSERT INTO py_products (name, price) VALUES (%s, %s)"
        val = ("Chocolate Heaven'", 19.99)
        cursor.execute(sql, val)
        sql = "INSERT INTO py_products (name, price) VALUES (%s, %s)"
        val = ("Tasty Lemons", 29.99)
        cursor.execute(sql, val)
        sql = "INSERT INTO py_products (name, price) VALUES (%s, %s)"
        val = ("Vanilla Dreams", 29.99)
        cursor.execute(sql, val)

        connection.commit()

        # SQL Join

        sql = "SELECT py_users.name AS user, py_products.name AS favorite FROM py_users INNER JOIN py_products ON py_users.fav_product_id = py_products.id"

        cursor.execute(sql)

        result = cursor.fetchall()

        for x in result:
            print(x)
            print(x[0], " likes ", x[1])



except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # 5. Always close the cursor and connection when done
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")

print("connection successful")