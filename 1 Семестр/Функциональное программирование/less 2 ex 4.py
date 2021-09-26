#less 2 ex4

import turtle
turtle.shape('turtle')

#рисуем землю
turtle.width(3)
turtle.color('brown')
turtle.goto(310, 0)
turtle.goto(-310, 0)
turtle.forward(10)
turtle.width(1)
turtle.color('black')

#g = 9,8 м/с^2
x = - 300    #начальные координаты черепашки
y = 0
t = 0
dt = 0.1     #малый интервал времени, в течение которого будем считать vx и vy постоянными
vx = 10
v0y = 49
for i in range(0, 1001):
    vy = v0y - 9.8 * t
    x += vx * dt
    y += vy * dt
    if y < 0:
        y = 0
        v0y = - vy + vy/10  #считаем, что часть энергии при ударе переходит в тепло, поэтому модуль скорости
        vx = vx - vx/10     #                                                                    уменьшается
        t = 0
    turtle.goto(x,y)
    t += dt
