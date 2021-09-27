#less 1 ex13

import turtle
turtle.shape('turtle')

def point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def round(s):
    turtle.begin_fill()
    for i in range(1, 361):
        turtle.forward(s)
        turtle.right(1)
    turtle.end_fill()

def circle():
    for i in range(1, 181):
        turtle.forward(1)
        turtle.right(1)

def eye(a, b):
    point(a, b)
    p = s_ / 10
    turtle.color('blue')
    round(p)

#face
turtle.speed(0)
point(-120, 0)
turtle.left(90)
s_ = 2
turtle.color('yellow')
round(s_)

#eyes
eye(-55, 55)
eye(25, 55)

#nose
turtle.right(180)
point(-3, 30)
turtle.width(5)
turtle.color('brown')
turtle.begin_fill()
turtle.forward(40)
turtle.end_fill()

#mound
point(55, -10)
circle()

import time
time.sleep(3)