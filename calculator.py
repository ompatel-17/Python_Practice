# a = float(input("Enter First Number: "))
# b = float(input("Enter Second Number: "))
# operator = input("Select Operation: ") 

#                                method 1



# add = lambda a,b: a+b
# sub = lambda a,b: a-b
# mul = lambda a,b: a*b
# div = lambda a,b: a/b
# mod = lambda a,b: a%b



# def calc(a,b,operator):
    
#     if (operator == '+'):
#         return add(a,b)
#     elif (operator == '-'):
#         return sub(a,b)
#     elif(operator== '*'):
#         return mul(a,b)
#     elif(operator== '/'):
#         return div(a,b)
#     else:
#         print("Invalid operator.......")


# a = calc(a, b, operator)
# print(a)


#                                           method  2



# calc_dic ={
#     '+' : lambda a,b: a+b,
#     '-' : lambda a,b: a-b,
#     '*' : lambda a,b: a*b,
#     '/' : lambda a,b: a/b,
#     '%' : lambda a,b: a%b
   
# }


# def calc(a,b,operator):
    
#     if (operator == '+'):
#         return calc_dic[operator] (a,b)
#     elif (operator == '-'):
#         return calc_dic[operator] (a,b)
#     elif(operator== '*'):
#         return calc_dic[operator] (a,b)
#     elif(operator== '/'):
#         return calc_dic[operator] (a,b)
#     else:
#         print("Invalid operator.......")


# a = calc(a, b, operator)
# print(a)



#                                       method 3




        
class Calculator:
        def add(self):
            print(num1 + num2)

        def sub(self):
            print(num1 - num2)

        def mul(self):
            print(num1 * num2)

        def div(self):
            print(num1 / num2)


num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

obj = Calculator()

# choice = 1
# while choice != 0:
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
choice = int(input("Enter your choice:"))

if choice == 1:
    print(obj.add())
elif choice == 2:
    print(obj.sub())
elif choice == 3:
    print(obj.mul())
elif choice == 4:
    print(obj.div())
else:
    print("Invalid choice")
    