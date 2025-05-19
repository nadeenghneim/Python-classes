#number guessing game 
import random 
num=str(random.randint(1,10))
x=True
print("welcome to the number guessing game! You will be guessing a number between 1 and 10.")
while x:
    guess=input("enter your guess:")
    if guess==num:
        print("perfect, you won the game! you guessed number", guess)
        break
    elif guess<num:
        print("your guess is too low, try a higher number")
    elif guess>num:
        print("your guess is too high, try a lower number")
    else:
        print("oops wrong guess. try again!")