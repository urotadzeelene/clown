from turtle import *

setup(800, 600)
setworldcoordinates(-1000, -1000, 1000, 1000)
def draw_spiral():
    speed(0)
distance = 4

pendown()
    
for steps in range(90):
        for c in ('red','orange', 'yellow', 'green','blue','purple'):
            color(c)
            width(2)
            forward(distance)
            right(30)
            distance += 1  # ⬅️ increase this a lot

print(window_width(), window_height())

done()