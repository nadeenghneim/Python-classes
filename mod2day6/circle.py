import turtle
turtle.Screen().bgcolor("aqua")
turtle.Screen().setup(750,1000)
circle=turtle.Turtle()
while True:
    for i in range(100):
        circle.circle(i)
        circle.right(15)
turtle.done()