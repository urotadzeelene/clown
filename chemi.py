import random


def draw_lines(t):
    t.speed(0)
    t.hideturtle()

    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta"]

    for _ in range(60):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        r = random.randint(80, 120)
        t.penup()
        t.goto(x, y - r)
        t.pendown()
        t.color(random.choice(colors))
        t.begin_fill()
        t.circle(r)
        t.end_fill()

    t.penup()
    t.goto(0, 0)
    t.color("black")
    t.write("thank you for playin!", align="center", font=("Arial", 24, "bold"))
