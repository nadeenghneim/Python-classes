
class Numbers:
    def __init__(self,uinput,conversion):
        self.uinput=uinput
        self.conversion=conversion
    def ask(self):
        num=int(input("enter the number you want to convert to a roman numeral"))
        if num%1000==0:
            print("M")
        elif num%500==0:
            print("D")
        