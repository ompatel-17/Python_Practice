import mysql.connector
import bcrypt
from datetime import datetime
import json

try:
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="my database"
    )

    cursor = db.cursor()

    user_id = input("Enter Your ID: ")
    email = input("Enter Your Email: ")
    password = input("Enter Password: ")

    cursor.execute("SELECT id FROM `register` WHERE id = %s", (user_id,))
    check_id = cursor.fetchall()

    cursor.execute("SELECT email, password FROM register WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user and check_id:
        stored_password = user[1].encode('utf-8')  # Convert to bytes

        if bcrypt.checkpw(password.encode('utf-8'), stored_password):
            print("Login successful")
            hashed_password = stored_password
            login_time = datetime.now()
            cursor.execute("INSERT INTO login_status (email, hashed_password, login_time, user_id) VALUES (%s, %s, %s, %s)", 
                        (email, hashed_password, login_time, user_id))
            db.commit()
        else:
            print("Invalid password")
    else:
        print("User not found")

except mysql.connector.Error as err:
    print("Error:", err)
finally:
    if 'db' in locals() and db.is_connected():
     db.close()
