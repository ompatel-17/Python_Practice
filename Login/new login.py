import mysql.connector
import bcrypt
from datetime import datetime

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my database"
)

cursor = db.cursor()

email = input("Enter Your Email: ")
password = input("Enter Password: ")

# def login_user(email, password):
    # Query the database to retrieve user's hashed password
   
cursor.execute("SELECT email, password FROM register WHERE email = %s", (email,))
user = cursor.fetchone()
    

if user:
    stored_password = user[1].encode('utf-8')  # Convert to bytes
    if bcrypt.checkpw(password.encode('utf-8'), stored_password):
        print("Login successful")
        # Store login details in another table
        hashed_password = stored_password
        login_time = datetime.now()
        cursor.execute("INSERT INTO login_status (email, hashed_password, login_time) VALUES (%s, %s, %s)", (email, hashed_password, login_time))
        db.commit()
    else:
        print("Invalid password")
else:
    print("User not found")

    
    
# login_user(email, password)


# cursor.execute("SELECT name From register WHERE name = %s", (name,))
# user_name = cursor.fetchone()

# if (user_name == name ) :
#     print(f"{name} login at {datetime.now()}")


# Close the database connection
db.close()
