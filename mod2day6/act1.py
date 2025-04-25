import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(500,400)
x=turtle.Turtle()
x.color("green")
side= 6
sideln=30
angle=360.0/side
for i in range(side):
    x.forward(sideln)
    x.right(angle)
turtle.done()