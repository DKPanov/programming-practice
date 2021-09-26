#less 1 ex11

import turtle
turtle.shape('turtle')

def circle(s):
    for i in range(1, 361):
        turtle.forward(s/10)
        turtle.left(1)
    for i in range(1, 361):
        turtle.forward(s/10)
        turtle.right(1)

turtle.speed(0)
turtle.left(90)
for s in range(10, 21, 1):
    circle(s)

import time
time.sleep(3)
