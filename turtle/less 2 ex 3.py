#less 2 ex3

import turtle
turtle.shape('turtle')

#изображение цифры cо смещением на х
def f(s, x):
    turtle.width(3)
    turtle.color('blue')
    for j in range(len(s)):
        if j != 0:
            turtle.goto(s[j][0] + x, s[j][1])
        else:
            turtle.penup()
            turtle.goto(s[0][0] + x, s[0][1])
            turtle.pendown()


#координаты точек цифр
s0 = [[25, 50], [0, 50], [0, 0], [25, 0], [25, 50]]
s1 = [[0, 25], [25, 50], [25, 0]]
s2 = [[0, 50], [25, 50], [25,25], [0, 0], [25, 0]]
s3 = [[0, 50], [25, 50], [0, 25], [25,25], [0, 0]]
s4 = [[0, 50], [0, 25], [25,25], [25, 50], [25, 0]]
s5 = [[25, 50], [0, 50], [0, 25], [25, 25], [25, 0], [0, 0]]
s6 = [[25, 50], [0, 25], [0, 0], [25, 0], [25, 25], [0, 25]]
s7 = [[0, 50], [25, 50], [0, 25], [0, 0]]
s8 = [[25,25], [25, 50], [0, 50], [0, 25], [25, 25], [25, 0], [0, 0], [0, 25]]
s9 = [[25, 25], [0, 25], [0, 50], [25, 50], [25, 25], [0, 0]]
numbers = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]

inp = open('input.txt', 'r')
str_post = inp.read()
post = []
for j in str_post:
    post.append(j)

#рисуем почтовый индекс
x = -150
for elem in post:
    #рисуем цифру и смещаемся после этого по иксу
    for i in range(0, 10):
        if int(elem) == i:
            f(numbers[i], x)
    x += 50

import time
time.sleep(3)