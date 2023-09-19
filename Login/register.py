import mysql.connector
from cryptography.fernet import Fernet

# make connection 

db = mysql.connector.connect(
    host = "localhost", 
    username = "root", 
    password = "",
    database = "my database"
)
cur = db.cursor()
print(db)

# Take values from the user

name = input("Enter name:\n ")
email = input("Enter Your E-mail:\n ")
# first_name = input("Enter First Name:\n ")
# last_name = input("Enter Last Name:\n ")
password = input("Enter Your Password:\n ")

#   password encrypt

key = Fernet.generate_key()
fernet = Fernet(key)
hash_password = fernet.encrypt(password.encode())




try:
    q = 'INSERT INTO register values(%s,%s,%s)' #,%s,%s
    t =(name,email,hash_password) #first_name,last_name
    cur.execute(q,t)
    
    
except Exception as err:
    print("User Name or Email is already taken..........",err)
    

db.commit()