class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("the area of your circle is:",3.14159*(self.radius**2))
    
    def perimeter(self):
        print("the  perimeter of your circle is ",2*3.14159*self.radius)
radius=int(input("enter the radius of your circle:"))
c=Circle(radius)
c.area()
c.perimeter()
