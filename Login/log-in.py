import mysql.connector
import datetime
import socket
from cryptography.fernet import Fernet

hostname = socket.gethostname() #for ip
myip = socket.gethostbyname(hostname) # for ip
x = datetime.datetime.now()

# make connection

db = mysql.connector.connect(
    host = "localhost", 
    username = "root", 
    password = "",
    database = "my database"
)

# make object of db

cur = db.cursor(buffered=True)
print(db)


# take values from the user

user = input("Enter Username:\n ")
password = input("Enter Your Password:\n ")

# put query

check_user = f"SELECT user_name FROM `register` WHERE user_name='{user}'"
check_password = f"SELECT password FROM `register` WHERE password='{password}'"

# execute queries

cur.execute(check_user)
username_result= cur.fetchall()

cur.execute(check_password)
password_result = cur.fetchall()

# store in a variable

passwor = password_result
usernam = username_result

# print those variables

print(usernam)
print(passwor)

# check length

print(len(usernam))
print(len(passwor))

# AND logic of 0,1

if(len(usernam) > 0 and len(passwor) > 0):
     print("log in successful")
     a = 'INSERT INTO login_status values(%s,%s,%s)'
     b = (user,x,myip)
     cur.execute(a,b)
     print("ip is:" + myip)
     
else:
     print("Login failed, wrong username or password")
     


db.commit()

# store = f"SELECT user_name,password FROM `register` WHERE user_name='{user}'"
# cur.execute(store)

# result=cur.fetchall()

# if(len(result) > 0):
#      pen=result[0][1]
#      print(type(pen))
#      key = Fernet.generate_key()
#      print(key)
#      #ernet = Fernet(key)

#      #decMessage = fernet.decrypt(pen).decode()
#      # print(decMessage)
#      # print("ok")
# else:
#      print("incorrect")
     
# print(result)