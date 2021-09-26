import turtle
turtle.shape('turtle')
turtle.speed(5)
def krug(r):
    turtle.pendown()
    for i in range(0, 45):
        turtle.forward(r)
        turtle.left(8)
    turtle.penup()
krug(10)
turtle.left(90)
turtle.forward(100)
turtle.pendown()
turtle.begin_fill()
turtle.color(2)
turtle.begin_fill()
turtle.left(90)
turtle.forward(28)
krug(1)
turtle.backward(70)
krug(1)
while True:
    turtle.left(1080)