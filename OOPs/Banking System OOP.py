# Parent Class----------------------------------------------

class User():
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details (self) :
        print("Personal Details")
        print("")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)
        
varshil = User("Varshil", 20, "Male")
dhrupal = User("Dhrupal", 21, "Male")
smit = User("Smit", 22, "Male")
rutvi = User("Rutvi", 19, "Female")
# varshil.show_details()

# Chaild Class-------------Inheritance-----------------------

class Bank(User) :
    def __init__(self, name, age, gender):
        super(). __init__(name, age, gender)
        self.balance = 0
        
# print(varshil.name, varshil.age, varshil.gender)

    def deposit (self, amount):
        self.amount = amount
        self.balance = (self.balance + self.amount)
        print("Your Account Balance has been Updtaed : ₹", self.balance)

# varshil = Bank("Varshil", 20, "Male")
# dhrupal = Bank("Dhrupal", 21, "Male")
# smit = Bank("Smit", 22, "Male")
# rutvi = Bank("Rutvi", 19, "Female")
# print(varshil.deposit(500))
        
    def withdraw(self, amount) :
        self.amount = amount
        
        if self.amount > self.balance : 
            print("Insufficient Funds | Balance Available : ₹", self.balance)
        else :
            self.balance = self.balance - self.amount
            print("Account Balance Updated | Available Amount is: ₹", self.balance)
            
# varshil = Bank("Varshil", 20, "Male")
# varshil.deposit(500) 
# print(varshil.withdraw(200))         

    def view_balance(self):
        self.show_details()
        print("Account Balance is: ₹", self.balance)
        
# varshil = Bank("Varshil", 20, "Male")
# varshil.deposit(500) 
# print(varshil.withdraw(200))
# print(varshil.view_balance())