import random
randnumber = random.randint(1, 100)
# print(randnumber)

userguess = None
guesses = 0

while (userguess != randnumber):
    userguess = int(input("Enter your guess:"))
    guesses += 1
    
    if (userguess == randnumber):
        print("You guess it right !!!")
    else:
        if (userguess > randnumber):
            print("You guess it wrong... Enter a smaller number")
        else:
            print("You guess it Wrong... Enter a larger number")
            
print(f"You guessed the number in {guesses} guesses")

with open("highscore.txt","r") as f:
    highscore = int(f.read())        

if(guesses < highscore):
    print("You have just broken the High Score.....")
    
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))
