#two values x and y coordinates with super method to print as a coordinate 
class coordinates:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):

        return f"({self.x},{self.y})"

coord=coordinates(10,20)
print(coord)
