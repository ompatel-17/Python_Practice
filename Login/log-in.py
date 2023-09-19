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

email = input("Enter email:\n ")
password = input("Enter Your Password:\n ")

# put query

check_email = f"SELECT email FROM `register` WHERE email='{email}'"
check_password = f"SELECT password FROM `register` WHERE password='{password}'"

# execute queries

cur.execute(check_email)
email_result= cur.fetchall()

cur.execute(check_password)
password_result = cur.fetchall()


key = Fernet.generate_key()
fernet = Fernet(key)
unhash_password = fernet.decrypt(password_result).decode()


print(unhash_password)
# store in a variable

passwor = unhash_password
usernam = email_result

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
     b = (email,x,myip)
     cur.execute(a,b)
     print("ip is:" + myip)
     
else:
     print("Login failed, wrong email or password")
     


db.commit()



# key = Fernet.generate_key()
# fernet = Fernet(key)
# hash_password = fernet.decrypt(password).decode()



# hash_password = fernet.crypt(password.encode())
# decMessage = fernet.decrypt(encMessage).decode()
 
# print("decrypted string: ", decMessage)


# store = f"SELECT user_name,password FROM `register` WHERE user_name='{user}'"
# cur.execute(store)

# result=cur.fetchall()

# if(len(result) > 0):
#      pen=result[0][1]
#      print(type(pen))
#      key = Fernet.generate_key()
#      print(key)
#      fernet = Fernet(key)

#      #decMessage = fernet.decrypt(pen).decode()
#      # print(decMessage)
#      # print("ok")
# else:
#      print("incorrect")
     
# print(result)