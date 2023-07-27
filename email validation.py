email = input("Enter your email: ") #g@g.in    patelom22@gmail.com  6033@saffrony.ac.in(basic condition)

o,p,k = 0,0,0

if len(email) >= 6: #1
    
    if (email[0].isalpha()) or (email[0].isdigit()): #2
        
        if ("@" in email) and (email.count("@") == 1): #3
            
            if (email[-3] == ".") or (email[-4] == ".") or (email[-6] == "."):#4
                
                for i in email: #5
                    
                    if i==i.isspace():
                        k=1
                    
                    elif i.isalpha():
                        if i==i.upper():
                            o=1 
                    
                    elif i.isdigit():
                        continue
                    
                    elif i=="_" or i=="@" or i==".":
                        continue
                    
                    else:
                        p=1
                        
                if o==1 or k==1 or p==1:
                    print("wrong email 5")
                
                else:
                    print("Your email is right.....")
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")    
    else:
        print("wrong email 2")   
else:
    print("wrong email 1")