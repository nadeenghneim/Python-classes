import math

def circ(radius):
    circumference=2 *math.pi *radius
    return circumference
radius=int(input("enter the radius of your circle:"))

print("the circumference of the circle is", circ(radius))
