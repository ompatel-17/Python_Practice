import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my database"
)

cursor = db.cursor()

user_id = input("Enter the ID to search: ")

query = "SELECT * FROM register WHERE id = %s"
cursor.execute(query, (user_id,))

row = cursor.fetchone()


if row:
    print("ID found!")
    print("ID:", row[0])  
    print("Name:", row[1]) 
    
else:
    print("ID not found.")


db.close()
