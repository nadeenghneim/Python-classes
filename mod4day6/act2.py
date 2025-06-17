import random 
print("Welcome to the number guessing game!! What would you like me to call you?")
username=str(input("enter your name:"))



def guess(start,end):
    secret=random.randint(1,100)
    if secret%2==0:
        print("hint:the number is even")
    else:
        print("hint:the number is odd.")


    attempts=0
    while True:
        user_guess=int(input("choose a number between 1 and a 100: "))
        attempts+=1
        if secret>user_guess:
            print("your number is too low, try again")
        elif secret<user_guess:
            print("your number is too high, try again")
        else:
            print("you have guessed correctly. the number is ", secret,"you have guessed in",attempts,"attempts")
            break
guess(1,100)