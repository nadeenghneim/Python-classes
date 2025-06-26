class sentence():
    def __init__(self):
        self.str=""
    def get(self):
        self.str=input("enter any sentence:")
    def print(self):
        print("the sentence in caps is ",self.str.upper())
x=sentence()
x.get()
x.print()