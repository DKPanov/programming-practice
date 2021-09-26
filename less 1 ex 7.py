#less 1 ex7
import turtle

turtle.shape('turtle')

for j in range (1, 11):
    k = 0
    for i in range (1, 181):
        turtle.forward(j/10 + k * 0.1/180)
        turtle.left(1)
        k += 1

import time
time.sleep(3)
