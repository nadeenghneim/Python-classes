from abc import ABC,abstractmethod
class players(ABC):
    def display(self):
        pass

class arakji(players):
    def display(self):
        print("I am AL Riyadi's point gaurd and I am injurred")
class zeinoun(players):
    def display(self):
        print("i wear the number 7 for the Al riyadi team.")
class maker(players):
    def display(self):
        print("i am the big for al riyadi's team and excell at blocking shots.")
class mansour(players):
    def display(self):
        print("i am the point guard currently")

a=arakji()
a.display()
z=zeinoun()
z.display()
m=maker()
m.display()
m2=mansour()
m2.display()