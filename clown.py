from turtle import *
import random
screen = Screen()
speed(200)
bgcolor("black")
#head-----------------------------------------
def stencil(X,Y,r):
    penup()
    goto(X,Y)
    pendown()
    color('papayawhip')
    begin_fill()
    circle(r)
path = [(-45,-115), (42-115), (0,-130), (-50,50), (110, -30 ), (-110,-30),(40,100)]
for x, y in path:
    stencil(x,y, random.randint(60, 70))
    end_fill()
    penup()

color("white")
#hair ---------------------------------------
def stencil(X,Y,r=60):
    penup()
    goto(X,Y)
    pendown()
    color('red')
    begin_fill()
    circle(r)
path = [(125,25), (-125,25 ), (-60, 50), (25,125), (110, -30), (-110,-30),(40,100)]
for x, y in path:
    stencil(x,y, random.randint(60, 70))
    end_fill()
    penup()
    
def stencil(X,Y,r=40):
    penup()
    goto(x,y)
    pendown()
    color('orangered')
    begin_fill()
    circle(r)
path = [(125,25), (-125,26), (-60, 50), (25,125), (110, -30), (-90,-30),(10,100)]
for x, y in path:
    stencil(x,y, random.randint(40,60))
    end_fill()
#---------------------------------------------------


# # --- hair ---
# t.penup()
# t.goto(125,25)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(60)
# t.end_fill()

# t.penup()
# t.goto(-125,25)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(60)
# t.end_fill()

# t.penup()
# t.goto(-60,50)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(40)
# t.end_fill()

# t.penup()
# t.goto(25,125)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(60)
# t.end_fill()

# t.penup()
# t.goto(110,-30)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(59)
# t.end_fill()

# t.penup()
# t.goto(-110,-30)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(59)
# t.end_fill()

# # --- Head ---
# t.penup()
# t.goto(0, -100)
# t.pendown()
# t.color("papayawhip")
# t.begin_fill()
# t.circle(100)  
# t.end_fill()
# t.penup()
# #cheeks
# t.goto(-42,-115)
# t.pendown()
# t.color("papayawhip")
# t.begin_fill()
# t.circle(70)
# t.end_fill()
# t.penup()

# t.goto(42,-115)
# t.pendown()
# t.color("papayawhip")
# t.begin_fill()
# t.circle(73)
# t.end_fill()
# t.penup()
# #chin
# t.goto(0,-130)
# t.pendown()
# t.color("papayawhip")
# t.begin_fill()
# t.circle(60)
# t.end_fill()
# t.penup()


# # --- Eyes ---
# for x in [-50, 50]:
#     t.penup()
#     t.goto(x, 14)
#     t.pendown()
#     t.color("white")
#     t.begin_fill()
#     t.circle(19)
#     t.end_fill()
    
  
#     t.penup()
#     t.goto(x, 18)
#     t.pendown()
#     t.color("mediumblue")
#     t.begin_fill()
#     t.circle(15)
#     t.end_fill()
    
#     t.penup()
#     t.goto(x, 22)
#     t.pendown()
#     t.color("black")
#     t.begin_fill()
#     t.circle(11)
#     t.end_fill()
    
#     t.penup()
#     t.goto(x, 36)
#     t.pendown()
#     t.color("white")
#     t.begin_fill()
#     t.circle(3)
#     t.end_fill()

 
# # --- Nose ---
# t.penup()
# t.goto(0,-40)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(29)
# t.end_fill()

# t.penup()
# t.goto(0,-20)
# t.pendown()
# t.color("orangered")
# t.begin_fill()
# t.circle(17)
# t.end_fill()
# # --- Mouth ---
# t.penup()
# t.goto(-75, -40)
# t.setheading(-60)
# t.pendown()
# t.color("black")
# t.width(5)
# t.circle(85, 120)

# t.penup()
# t.goto(-92, -32)
# t.setheading(-60)
# t.pendown()
# t.color("black")
# t.width(4)
# t.circle(17.6, 170)

# t.penup()
# t.goto(73, -16)
# t.setheading(-120)
# t.pendown()
# t.color("black")
# t.width(4)
# t.circle(17.6, 180)


#   # smile

# # --- Hair ---
# t.penup()
# t.goto(0,100)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# t.penup()
# t.goto(45,90)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# t.penup()
# t.goto(100,90)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(60)
# t.end_fill()

# t.penup()
# t.goto(149,45)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(49)
# t.end_fill()

# t.penup()
# t.goto(-75,50)
# t.pendown()
# t.color("red")
# t.begin_fill()
# t.circle(40)
# t.end_fill()

# # --- highlight ---
# t.penup()
# t.goto(10,100)
# t.pendown()
# t.color("orangered")
# t.begin_fill()
# t.circle(30)
# t.end_fill()

# t.penup()
# t.goto(-125,0)
# t.pendown()
# t.color("orangered")
# t.begin_fill()
# t.circle(23)
# t.end_fill()

# t.penup()
# t.goto(-139,67)
# t.pendown()
# t.color("orangered")
# t.begin_fill()
# t.circle(30)
# t.end_fill()

# t.penup()
# t.goto(130,80)
# t.pendown()
# t.color("orangered")
# t.begin_fill()
# t.circle(25)
# t.end_fill()

# t.penup()
# t.goto(-90,115)
# t.pendown()
# t.color("orangered")
# t.begin_fill()
# t.circle(25)
# t.end_fill()

# t.penup()
# t.goto(60,120)
# t.pendown()
# t.color("orangered")
# t.begin_fill()
# t.circle(10)
# t.end_fill()


# t.penup()
# t.goto(25,175)
# t.pendown()
# t.color("orangered")
# t.begin_fill()
# t.circle(25)
# t.end_fill()


# t.penup()
# t.goto(150,15)
# t.pendown()
# t.color("orangered")
# t.begin_fill()
# t.circle(25)
# t.end_fill()


# t.penup()
# t.goto(-100,50)
# t.pendown()
# t.color("orangered")
# t.begin_fill()
# t.circle(20)
# t.end_fill()

done()
