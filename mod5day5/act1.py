from abc import ABC,abstractmethod

class parent(ABC):
    def show(self,x):
        print("we have passed the value",x)
    
    @abstractmethod
    def display(self):
        print("we are inside the parent class and methods")
class child(parent):
    def display(self):
        print("we are inside the child class and methods")

obj1=child()
obj1.show(10)
obj1.display()

