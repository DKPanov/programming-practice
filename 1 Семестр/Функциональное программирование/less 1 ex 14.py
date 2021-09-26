#less 1 ex14

import turtle
turtle.shape('turtle')

def point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def star(n):
    turtle.right(180)
    for i in range(0,n):
        turtle.forward(300)
        turtle.left(180 - 180/n)
    import time
    time.sleep(3)

star(5)
turtle.right(180)
point(320, 0)
star(11)
