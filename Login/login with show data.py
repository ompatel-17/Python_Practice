import mysql.connector
import bcrypt
from datetime import datetime
import json

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my database"
)

# cursor = db.cursor(dictionary=True)
cursor = db.cursor()

user_id = input("Enter Your ID: ")
email = input("Enter Your Email: ")
password = input("Enter Password: ")



# def login_user(email, password):
    
    # Query the database to retrieve user's hashed password

cursor.execute("SELECT id FROM `register` WHERE id = %s", (user_id,))
check_id = cursor.fetchall()

cursor.execute("SELECT email, password FROM register WHERE email = %s", (email,))
user = cursor.fetchone()




if(user and check_id):
    
    stored_password = user[1].encode('utf-8')  # Convert to bytes
    
    if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                    
        print("Login successful")
        hashed_password = stored_password
        login_time = datetime.now()
        cursor.execute("INSERT INTO login_status (email, hashed_password, login_time, user_id) VALUES (%s, %s, %s, %s)", 
                    (email, hashed_password, login_time, user_id))
        
        cursor.execute("SELECT register.name, login_status.login_time FROM register INNER JOIN login_status ON register.id = login_status.user_id")
        rows = cursor.fetchall()

        def datetime_handler(x):
            if isinstance(x, datetime):
                return x.isoformat()
            raise TypeError("Unknown type")

        json_data = json.dumps(rows, default= datetime_handler, indent=4)
        print(json_data)
        
        db.commit()
                
    else:
        print("Invalid password")
            
else:
    print("User not found")

    
# login_user(email, password)



db.close()
