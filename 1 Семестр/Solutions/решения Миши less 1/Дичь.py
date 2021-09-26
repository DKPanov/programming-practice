import turtle
turtle.shape('turtle')
turtle.speed(0)
turtle.penup()
turtle.forward(50)
turtle.left(90)
turtle.pendown()
shag=0
for i in range(0, 100000):
    shag=shag+0.01
    turtle.forward(shag)
    turtle.left(2)
while True:
    turtle.left(1)