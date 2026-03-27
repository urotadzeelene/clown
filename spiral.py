from turtle import *
pendown
speed(200)
bgcolor("black")
penup()
goto(0,0)
pendown()
color("white")


pendown
for steps in range(150):
    for c in ('blue', 'red', 'green', 'pink','white'):
        color(c)
        forward(steps)
        right(30)
