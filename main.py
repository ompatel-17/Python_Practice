#                                              array
'''arr = ['amit','kiran','raj','op']
# print("element of array:",arr)

arr[0]
# print(arr[0])

for i in range(0,len(arr)):
    # print(arr[i])
'''

#                                               list

# a=[10,20,30,40,10.5,'op']
# b=[9,8,7,6,5,4,33.55,'boss']
'''print(a[2])
   # print(a[-2])
#                            accessing list by loop
for i in a:
    # print(i)
'''

'''n=len(a)
for i in range(n):
    # print(i,a[i])
'''
#                              add element in the list
'''
a[2]="patel"
# print(a)
'''
#                             add element in the list (last position) append

'''
a.append("55555")
# print(a)
'''
#                            add with insert
'''
a.insert(4,888)
# print(a)
'''
#                            delete last element pop
'''
a.pop()
# print(a)
'''
'''
a.pop(3)
# print(a)
'''
#                             using remove method it's take value which is removed
'''
a.remove(10)
# print(a)
'''
#                               clear method
'''
a.clear()
# print(a)
'''
#                               del method
'''
del a[3]
# print(a)

del a[0:4]
# print(a)
'''
#                               combine list
'''num = a + b
# print(num)
'''
#                                tuple

# a=(1,3,5,7,'op',9.1)
# b=(2,4,6,8,'boss',7.4)
#                              combine tuple

'''c=a + b
# print(c)
'''
#                             delete tuple by devide tuple   del
'''
tup1 = a[0:3]
# print(tup1)
'''
#                             delete perticular item/value (7)
'''s1 = a[0:3]
s2 = a[4:]
tup = s1 + s2
# print(tup)
'''
#                          take tuple elements from the user  [using list]

'''
a = []
n = int(input("enter number of elements:"))

for i in range(n):
    a.append(int(input("enter element:")))

# print(type(a))

a=tuple(a)

# print(type(a))
# print("tuples:")

for element in a:
    # print(element)
'''
#                                     while loop
#                                     finite
'''x=0
while x<=20:
    # print(x)
    x=x+2
'''
#                                      infinite
'''
while True:
    # print(17)
'''
#                                      dictionary

'''
mobile = {
    "brand": "Iphone",
    "model": "20-pro-ultra-max",
    "year": "2028"
}
# print(mobile)
'''

#                                           function

'''
def my_function():
    b=a*a
    # print(b)

my_function()
'''

#                                    today date
# from datetime import datetime
# #a=['12-02-2002','19-09-1999','19-10-2020','24/11/2024','26022005']
# dt=datetime.today()
# print(dt)

# # a= dt.strftime("%d-%m-%Y")
# # print(dt)

# tm=dt.strftime("%I-%M-%S")
# print(tm)

######################################################################################

#                                          sort integer

'''
a = [22,44,33,45,21,0, 7 ,10]

a.sort()
# print("sorted data is:")
for b in a:
    # print(b)
'''
# sort string

# name = ['raj','lalu','amiraj','vaibhav','bhavesh']
# for element in name:
#     print(element)

# name.sort()
# print("sorted names are:")

# for b in name:
#     print(b)

##############


# from datetime import datetime

# a = ['24-11-2024', '12-02-2002', '19-09-1999', '26-02-2005', '19-10-2020']

# a.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))

# print("Sorted dates are:")

# for element in a:
#     print(element)


#                                        Pattern Programs


# row_no=int(input("Enter the no of row: "))

# --------------------------------------------------------------------------------------
# for row in range(1, row_no+1):
#     for column in range(1,row+1):
#         print("*", end=" ")
#     print()

# --------------------------------------------------------------------------------------
# for row in range(row_no, 0, -1):
#     for column in range(1, row+1):
#         print("*",end=" ")
#     print()

# --------------------------------------------------------------------------------------
# for row in range(1, row_no+1):
#     for column in range(1, row+1):
#         print("*",end=" ")
#     print()

# for row in range(row_no-1, 0, -1):
#     for column in range(1, row+1):
#         print("*",end=" ")
#     print()

# --------------------------------------------------------------------------------------

# for row in range(1, row_no+1):
#     for column in range(1, row+1):
#         print(row,end=" ")
#     print()

# --------------------------------------------------------------------------------------

# for row in range(1, row_no+1):
#     for column in range(1, row+1):
#         print(column, end=" ")
#     print()

# --------------------------------------------------------------------------------------

# for row in range(1, row_no+1):
#     for column in range(1,row+1):
#         print(column, end=" ")
#     print()

# for row in range(row_no-1, 0, -1):
#     for column in range(1, row+1):
#         print(column, end=" ")
#     print()

# --------------------------------------------------------------------------------------

#                                       lambda

# add = lambda a, b : a+b
# print(add(10,5))

# add = lambda x,y,z: x*y*z
# print(add(12,2,10))

# --------------------------------------------------------------------------------------
#                                       oop

# class Phone:
#     def set_color(self,color):
#         self.color=color

#     def set_cost(self,cost):
#         self.cost=cost

#     def show_color(self):
#         return self.color

#     def show_cost(self):
#         return self.cost

#     def make_call(self):
#         print("make a call")

#     def play_game(self):
#         print("playing a game")

# p1 = Phone()

# p1.set_color("black")
# p1.set_cost(50000)

# p1.show_color()
# p1.show_cost()
# p1.make_call()
# p1.play_game()


#                                             constructor

# class Employee:
#     def __init__(self, name, age, salary, gender):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.gender=gender

#     def show_employee_detail(self):
#         print("Employee name is",self.name)
#         print("Employee age is",self.age)
#         print("Employee salary is",self.salary)
#         print("Employee gender is",self.gender)

# e1 = Employee("ram",44,50000,"Male")
# e1.show_employee_detail()

# --------------------------------------------------------------------------------------
#                                      inheritance

# class Vehicle:
#     def __init__(self,mileage,cost):
#         self.mileage=mileage
#         self.cost=cost

#     def show_vehicle_detail(self):
#         print("mileage is:",self.mileage)
#         print("cost is:",self.cost)
#         print("I am a vehicle")

# v1 = Vehicle(80,79000)
# v1.show_vehicle_detail()

# class Car(Vehicle):
#     def show_car_detail(self):
#         print("I am a car")

# c1 = Car(60,50000)
# c1.show_vehicle_detail()

# --------------------------------------------------------------------------------------
#                        constructor override

# class Vehicle:
#     def __init__(self,mileage,cost):
#         self.mileage=mileage
#         self.cost=cost

#     def show_vehicle_detail(self):
#         print("mileage is:",self.mileage)
#         print("cost is:",self.cost)
#         print("I am a vehicle")

# v1 = Vehicle(80,79000)
# v1.show_vehicle_detail()

# class Car(Vehicle):
#     def __init__(self,mileage,cost,tyres,hp):
#         super().__init__(mileage,cost)
#         self.tyres=tyres
#         self.hp=hp

#     def show_car_detail(self):
#         print("Number of tyres is:",self.tyres)
#         print("Horse power is:",self.hp)

# c1 = Car(50,80000,4,5000)
# c1.show_vehicle_detail()
# c1.show_car_detail()

# --------------------------------------------------------------------------------------
#                                              open file
# f=open("op1.txt","x")
# f.write("helloooo")
# f.close()

# --------------------------------------------------------------------------------------

#                                         database


# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "localhost",
#     username = "root",
#     password = "",
#     database = "my database"
# )
# mycursor = mydb.cursor()
# print(mydb)

# mycursor.execute("SELECT enrollment_no FROM `student details` ")
# myresult = mycursor.fetchall()

# for row in myresult:
#     print(row)


# --------------------------------------------------------------------------------------

# import mysql.connector

# db = mysql.connector.connect(
#     host = "localhost",
#     username = "root",
#     password = "",
#     database = "my database"
# )
# cur = db.cursor()
# print(db)

# u = input("Enter Username:\n ")
# fn = input("Enter First Name:\n ")
# ln = input("Enter Last Name:\n ")
# e = input("Enter Your E-mail:\n ")
# p = input("Enter Your Password:\n ")

# q = 'INSERT INTO register values(%s,%s,%s,%s,%s)'
# t =(u,fn,ln,e,p)

# try:
#     cur.execute(q,t)
# except:
#     print("This user name is already taken...........")

# try:
#     cur.execute(q,t)
# except:
#     print("This Email is already taken...........")


# db.commit()


# ----------------------------------------------------------------------------------------------
#                                 Functions

# def greet(name = "Try again"):
#     print("Good Day," + name)
#     return

# greet(" op")
# greet()

# ---------------------------------------------------------------------------------------------
#                                  factorial by recursion

# a = int(input("Enter the number: "))

# def factorial(a):
#     product = 1
#     for i in range(a):
#         product = product * (i + 1)
#     return product

# print(factorial(a))

# ---------------------------------------------------------------------------------------------------
#                               larger number

# def maximum(num1,num2,num3):
#     if num1 > num2:
#         if num1 > num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2 > num3:
#             return num2
#         else:
#             return num3

# m = maximum(25,11,65)
# print("Large number is: " + str(m))

# ------------------------------------------------------------------------------------------------
#                           Game: Snake,Water,Gun
# import random

# def gamwin(comp,you):
#     if comp == you:
#         return None
#     elif comp == 's':
#         if you =='w':
#             return False
#         elif you == 'g':
#             return True
#     elif comp == 'w':
#         if you == 'g':
#             return False
#         elif you == 's':
#             return True
#     elif comp == 'g':
#         if you == 's':
#             return False
#         elif you == 'w':
#             return True

# print("Computer Turn: Snake(s),Water(w),Gun(g)?")
# randno = random.randint(1,3)

# if randno == 1:
#     comp = 's'
# elif randno == 2:
#     comp = 'w'
# elif randno == 3:
#     comp = 'g'

# you = input("Ypur Turn: Snake(s),Water(w),Gun(g)?")
# a = gamwin(comp, you)

# print(f"Computer chose {comp}")
# print(f"You chose {you}")

# if a == None:
#     print("Game is Tie!!!")
# elif a:
#     print("You Win This Game.....")
# else:
#     print("You Lose!!!!!!!!!")

# --------------------------------------------------------------------------------------------------
#                                   File  Operations

#               Use open function to read the content of a file

# f = open('sample.txt', 'r')
# data = f.read()
# print(data)
# f.close()

# ----------------------- readline() -----------------------------------

# f = open('sample.txt', 'r')
# #read first line
# data = f.readline()
# print(data)
# #read second line               and so on......
# data = f.readline()
# print(data)

# f.close()

#                            Write() function

#           create a new file and insert data in to with 'w' mode
# f = open('another.txt', 'w')
# f.write("I am a Devil of my world!!!!!")
# f.close()

#                     append the data with 'a' mode

# f = open('another.txt', 'a')
# f.write("I am appending....")
# f.close()

# ----------------------------with function-------------------------------------------------------
# this function is the best way to open file, it autometically close the file,you do not write f.close()

# with open('another.txt', 'r') as f:
#     a = f.read()
# with open('another.txt', 'w') as f:
#     a = f.write("I am the Boss")
# print(a)

# ----------------

# def game():
#     return 1792

# score = game()
# with open('hiscore.txt') as f:
#     hiscorestr = f.read()
# if hiscorestr == '':
#     with open('hiscore.txt','w') as f:
#         f.write(str(score))

# elif int(hiscorestr) < score:
#     with open('hiscore.txt','w') as f:
#         f.write(str(score))

# ------------------------replace any word in file and rewrite with specific eord------------------------------------------------------------

# with open('sample.txt') as f:
#     content = f.read()
# content = content.replace("adimanav","12345")

# with open('sample.txt','w') as f:
#     f.write(content)

# --------------------------oop practis------------------------------------------------------------

# class Programmer:
    
#     company = "Google"

#     def __init__(self, name, product):
#         self.name = name
#         self.product = product

#     def getinfo(self):
#         print(f"The name of {self.company} Programmer is {self.name} and product is {self.product}")

# Varshil = Programmer("Varshil", "JAVA")
# Om = Programmer("Om", "Python")
# Dhrupal = Programmer("Dhrupal", "Java Script")
# Aksh = Programmer("Aksh", "Node JS")

# Varshil.getinfo()
# Om.getinfo()
# Dhrupal.getinfo()
# Aksh.getinfo()

#---------------------------------------------------------------------------------------------

# class Calculator:
#     # b = input("Enter the number: ")
#     def __init__(self,number):
#         self.number = number 
    
#     def square(self):
#         print(f"The square of {self.number} is {self.number **2}")
    
#     def squareroot(self):
#         print(f"The squareroot of {self.number} is {self.number **0.5}")
    
#     def cube(self):
#         print(f"The cube of {self.number} is {self.number **3}")
        
# a = Calculator(4)
# a.square()
# a.squareroot()
# a.cube()

#------------------------------------------------------------------------------------------------

# class Employee:
#     company = "Google"
#     ecode = 170

# class Freelancer:
#     company = "Fiverr"
#     level = 0
    
#     def upgradelevel(self):
#         self.level = self.level + 1

# class Programmer(Employee, Freelancer):
#     name = "op"

# p = Programmer()
# print(p.company)
# p.upgradelevel()
# print(p.level)

#-------------------------------------------------------------------------------------------------
#                                   practis
#               Vector Representation By Inheritance

# class C2dvec:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j
    
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"
        
# class C3dvec(C2dvec):
#     def __init__(self, i, j ,k):
#         super().__init__(i, j)
#         self.kcap = k   

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
# v2d = C2dvec(1, 7)
# v3d = C3dvec(2, 4, 6)

# print(v2d)
# print(v3d)

#-----------------------------------------------------------------------------------------------
#      (a+bi)(c+di) = (ac-bd) + (ac+bc)i


# class Complex:
#     def __init__(self, r, i):
#         self.real = r
#         self.imaginary = i
        
#     def __add__(self, c):
#         return complex(self.real + c.real, self.imaginary + c.imaginary)
    
#     def __mul__(self, c):
#         mulreal = self.real*c.real - self.imaginary*c.imaginary
#         mulimg = self.real*c.imaginary + self.imaginary*c.real 
#         return complex(mulreal, mulimg)
    
# # def __str__(self):
# #     return f"{self.real} + {self.imaginary}i"

# c1 = Complex(1, 4)
# c2 = Complex(8, 5)
# print(c1 + c2)
# print(c1 * c2)

#----------------------------------------------------------------------------------------------

