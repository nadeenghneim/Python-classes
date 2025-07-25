from abc import ABC,abstractmethod

class BMW(ABC):
    def __init__(self,popularity,type):
        self.popularity=popularity
        self.type=type
    def information(self):
        print("A BMW is very well liked with",self.popularity)
        print("A BMW is a",self.type)

class Ferrari(ABC):
    def __init__(self,popularity,type):
        self.popularity=popularity 
        self.type= type 
    def information(self):
        print("A Ferrari is very well liked with",self.popularity)
        print("A Ferrari is a",self.type)
b=BMW("enthusiasts","luxury car")
f=Ferrari("speed chasers","sports car")
for i in (b,f):
    i.information()
