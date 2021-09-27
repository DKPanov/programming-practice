#less 1 ex9
import math
import turtle
turtle.shape('turtle')

def nugolnik(n, R):
    n = int(n)
    s = math.sqrt(2 * R * R * (1 - math.cos(math.radians(360/n))))
    povorot = 180 - 180 * (n - 2)/n
    polugla = 180 * (n - 2)/(2 * n)
    turtle.left(povorot + polugla)
    for i in range(0, n):
        turtle.forward(s)
        turtle.left(povorot)
    turtle.right(povorot + polugla)

n_ = 3
R_ = 20
while n_ < 14:
    nugolnik(n_,R_)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    n_ += 1
    R_ += 20

import time
time.sleep(3)
