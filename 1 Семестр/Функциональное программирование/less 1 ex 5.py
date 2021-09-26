#less 1 ex5
import turtle

turtle.shape('turtle')
for i in range (1, 11):
    for j in range (1, 5):
        turtle.forward(i * 20)
        turtle.left (90)
    turtle.penup()
    turtle.goto( -0.5 * 20 * i, -0.5 * 20 * i)
    turtle.pendown()

import time
time.sleep(3)
