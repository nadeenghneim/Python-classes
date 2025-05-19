#rock paper scissors game
import random
while True:
    options=["rock","paper","scissors"]
    choices=input("choose either rock, paper or scissors:")
    randomchoice=random.choice(options)
    print("your choice is ",choices)
    print("the computer's choice is",randomchoice)

    if choices==randomchoice:
        print("it is a tie game..")
    elif choices=="rock" and randomchoice=="paper":
        print("paper beats rock, the computer wins..")
    elif choices=="paper" and randomchoice=="rock":
        print("well done! paper beats rock, you win!!")
    elif choices=="scissors" and randomchoice=="paper":
        print("you win, scissors beat paper")
    elif choices=="paper" and randomchoice=="scissors":
        print("you lose, scissors beat paper")
    elif choices=="rock" and randomchoice=="scissors":
        print("you win! rock beats scissors..")
    elif choices=="scissors" and randomchoice=="rock":
        print("you lose! rock beats scissors..")
    else:
        print("wrong input")
    again=input("do you want to play again(yes or no):")
    if again!="yes":
        break