from turtle import *
import random
from chemi import draw_lines
import time

print("1. for green, 2. for yellow")

bgcolor_number = input("color of back")
match (bgcolor_number):
    case '1':
          b_color = (0.6, 0.98, 0.737) # green
    
    case '2':
        b_color = (0.988, 0.969, 0.655) #yellow 
       
    case _:
        b_color = (1,1,1)

    

screen = Screen()
speed(0)
bgcolor(b_color)

print("1. for red, 2. for blue")

hcolor_number = int(input("color of hair"))
match (hcolor_number):
    case 1:
        h_color = (1,0,0) # red
        hh_color = (1.0, 0.34, 0.071) #orange
    case 2:
        h_color = (0,0,1) #blue
        hh_color = (0.263, 0.639, 0.988) ## light blue
    case _:
        h_color = (1,1,1)
        hh_color = (0.718,0.796,0.871)







#head-----------------------------------------
def stencil(X,Y,r, c):
    penup()
    goto(X,Y)
    pendown()
    color(c)
    begin_fill()
    circle(r)

face = [(0,-100, 100), (-42, -115, 70), (42, -115, 70), (0, -130, 60)]     
for X, Y, r in face:
    stencil(X,Y, r, 'papayawhip')
    end_fill()
    penup()


hair =[(140,25), (-150,25), (-60,50), (25,80), (30,80), (20,60), (50,50), (140,-30), (-140,-30), (35,80)]
for X, Y in hair:
    stencil(X,Y, random.randint(58,74), h_color)
    end_fill()
    penup()

highlight =[(140,2), (-150,30), (-60,55), (25,81), (30,85), (20,65), (50,55), (140,-30),(-140,-30), (35,85)]
for X, Y in highlight:
    stencil(X,Y, random.randint(40,50), hh_color)
    end_fill()
    penup()

eyes = [(-50,10, 19, 'white'),(48,10,19,'white'),(-50,10,15,'blue'),(48,10,15,'blue'), (-50,19,11,'black'), (48,19,11,'black'), (-50,36,3,'white'), (48,36,3,'white')]
for X, Y, r, c in eyes:
    stencil(X,Y, r, c)
    end_fill()
    penup()
nose = [(0,-40,29,'red'), (0,-20,17,'orange')]
for X, Y, r, c in nose:
    stencil(X,Y,r,c)
    end_fill()
    penup()


arcs = [
    (-75, -40, -60, 85, 120, 5),
    (-92, -32, -60, 17.6, 170, 4),
    (73, -16, -120, 17.6, 180, 4)
]

for x, y, h, r, e, w in arcs:
    penup()
    goto(x, y)
    seth(h)         
    pendown()
    color("black")
    width(w)
    circle(r, e)
    penup()



time.sleep(2)
sun = Turtle()
draw_lines(sun)
done()
