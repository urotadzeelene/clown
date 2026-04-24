from turtle import *
import random
from chemi import draw_lines

print("1. for green, 2. for yellow")

bgcolor_number = input("color of back")
match (bgcolor_number):
    case '1':
          b_color = (0,1,0) # green
    
    case '2':
        b_color = (0,1,1) #yellow 
       
    case _:
        b_color = (1,1,1)

    

screen = Screen()
speed(200)
bgcolor(b_color)

print("1. for red, 2. for blue")

hcolor_number = int(input("color of hair"))
match (hcolor_number):
    case 1:
        h_color = (1,0,0) # red
        hh_color = (1.0, 0.647, 0) #orange
    case 2:
        h_color = (0,0,1) #blue
        hh_color = (0.68, 0.85, 0.90) ## light blue
    case _:
        h_color = (1,1,1)
        hh_color = (0.5,0.5,0.5)



draw_lines()


# draw_lines()
# penup()
# goto(0,0)


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

highlight =[(140,2), (-150,25), (-60,50), (25,80), (30,80), (20,60), (50,50), (140,-30),(-140,-30), (35,80)]
for X, Y in highlight:
    stencil(X,Y, random.randint(40,60), hh_color)
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
# smile = [(-75,40,-60,5,(85,120)), (-92,-32, -60, 4,(17.6, 170)), (73,-16,-120, 4, (17.6,180))]
# for X,Y,seth, W, circle, in smile:
#     stencil(X,Y,seth, W, circle,'black')
#     penup()

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
col= []

TEACHER I GIVE UP. IT IS NOT WORKING NO MATTER WHAT I DO!!!!




  
    
    # for steps in range(90):
    #     for c in ('red',):
    #         color(c)
    #         width(5)
    #         distance += 2
    #         forward(steps)
    #         right(100)


    # penup()
    # goto(X,Y)
    # pendown()
    # color('red')
    # begin_fill()
    # circle(random.randint(60,70))


#hair---------------------------------------

# path = [(125,25), (-125,25), (-60, 50), (25,125), (110, -30), (-110,-30),(40,100)]

    

    #  penup()
    # goto(X,Y)
    # pendown()
    # color('papayawhip')
    # begin_fill()
    # circle(r)

    # stencil(x,y, random.randint)
    # end_fill()
    # penup()

#hair ---------------------------------------
# def stencil(X,Y,r=60):
#     penup()
#     goto(X,Y)
#     pendown()
#     color('red')
#     begin_fill()
#     circle(r)
# path = [(125,25), (-125,25), (-60, 50), (25,125), (110, -30), (-110,-30),(40,100)]
# for X, Y in path:
#     stencil(X,Y, random.randint(60, 70))
#     end_fill()
#     penup()
    
# def stencil(X,Y,r=40):
#     penup()
#     goto(X,Y)
#     pendown()
#     color('orangered')
#     begin_fill()
#     circle(r)
# path = [(125,25), (-125,26), (-60, 50), (25,125), (110, -30), (-90,-30),(10,100)]
# for X, Y in path:
#     stencil(X,Y, random.randint(40,60))
#     end_fill()


done()
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

