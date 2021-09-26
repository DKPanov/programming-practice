#less 1 ex10

import turtle
turtle.shape('turtle')

def circle():
    for i in range(1, 361):
        turtle.forward(1)
        turtle.left(1)
    for i in range(1, 361):
        turtle.forward(1)
        turtle.right(1)

turtle.speed(0)
for i in range(0, 3):
    circle()
    turtle.left(60)

import time
time.sleep(3)
