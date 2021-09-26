import turtle
turtle.shape('turtle')
turtle.speed(0)
def krug(r):
    for i in range(0, 28):
        turtle.forward(r)
        turtle.left(8)
    for i in range(0, 23):
        turtle.forward(r/4)
        turtle.left(8)
k=4
for i in range(1, 100):
   krug(k)
while True:
    turtle.left(1080)