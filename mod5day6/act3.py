#fruits quiz
import random 

class Fruits:
    fruit_colors={"Orange":"orange","Mango":"orange","Banana":"yellow","Pineapple":"yellow"}
    def __init__(self):
        pass
    def select(self):
        random_fruit=random.choice(list(self.fruit_colors))
        answer=input(f"enter the color of a/an {random_fruit}:")
        correct_color=self.fruit_colors[random_fruit]
        if answer.lower()==correct_color:
            print("your answer is correct")
        else:
            print("your nswer is incorrect")
            print("the correct answer is",correct_color)

f=Fruits()
f.select()