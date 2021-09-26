#less 2 ex 1
import random
import turtle
turtle.shape('turtle')

turtle.speed(0)
for i in range(1, 301):
    turtle.right(random.randint(0, 361))
    turtle.forward(random.randint(1, 11))
