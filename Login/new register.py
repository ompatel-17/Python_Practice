import mysql.connector
import bcrypt

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my database"
)

cursor = db.cursor()

name = input("Enter Youe Name: ")
email = input("Enter Youe Email: ")
password = input("Enter Youe Password: ")


def register_user(name, email, password) :
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    cursor.execute("INSERT INTO register (name, email, password) VALUES (%s, %s, %s)", (name, email, hashed_password))
    db.commit()
    
    print("Registered Successfully...")

register_user(name, email, password)

db.close()
