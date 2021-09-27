# less 1 ex 6

n = int(input())

import turtle
turtle.shape('turtle')

for i in range (1, n + 1):
    turtle.left(360/n)
    turtle.forward(50)
    turtle.stamp()
    if i != n:
        turtle.goto(0, 0)

import time
time.sleep(3)
