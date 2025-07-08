#printing a sentence with reverse order using classes 
class Reverse():
    def __init__(self,s=''):
        self.s=s
        
    def execute(self):
        s=input("enter any string:")
        reversed_s=s[::-1]
        print("your reversed string is:",reversed_s)
r=Reverse()
r.execute()