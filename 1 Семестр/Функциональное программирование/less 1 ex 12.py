#less 1 ex12

import turtle
turtle.shape('turtle')

def spring():
    for i in range(1, 181):
        turtle.forward(1)
        turtle.right(1)
    for i in range(1, 181):
        turtle.forward(0.2)
        turtle.right(1)

turtle.speed(0)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.left(90)
for i in range(0, 5):
    spring()
for i in range(1, 181):
    turtle.forward(1)
    turtle.right(1)

import time
time.sleep(3)