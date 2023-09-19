class Customer:
    def __init__(self, name, age, membership_type):
        self.name = name
        self.age = age 
        self.membership_type = membership_type
        print("Customer Created")
        
cus1 = Customer("Varshil", 20, "Gold")   
# cus2 = Customer("Dhrupal", 21, "Sliver")
# cus3 = Customer("Smit", 22, "Bronze")

print(cus1.name, cus1.age, cus1.membership_type)