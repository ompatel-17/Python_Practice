import mysql.connector
import json
from datetime import datetime

db = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "",
    database= "my database"
)


cursor = db.cursor(dictionary=True)


query = '''SELECT register.name, login_status.login_time 
        FROM register 
        INNER JOIN login_status ON register.id = login_status.user_id'''


cursor.execute(query)

rows = cursor.fetchall()

# for row in rows:
#     print(row)  
    
def datetime_handler(x):
    if isinstance(x, datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

json_data = json.dumps(rows, default= datetime_handler, indent=4)
print(json_data)

    
# class MyObject:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name


# objects = {}
# for row in rows:
#     obj = MyObject[row['id'], row['name']]
#     objects.append(obj)


# for obj in objects:
#     print(obj.id, obj.name)

db.close()
