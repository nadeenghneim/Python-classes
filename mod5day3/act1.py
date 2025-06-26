#classes and subclasses(inheritance)
class vehicles():
    def __init__(self,color,speed,mil):
        self.color=color
        self.speed=speed
        self.mil=mil
class car(vehicles):
    pass
obj1=car('red',200,18)

print("the first vehicle is a car and its color is",obj1.color,"and its maximum speed is",obj1.speed,"and its mileage is",obj1.mil)