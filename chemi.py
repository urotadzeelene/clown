def draw_lines(t):
    t.speed(0)

    colors = ["red", "blue", "green", "yellow"]
    lines = 12

    t.pensize(6)

    for i in range(lines):
        t.penup()
        t.goto(0, 0)
        t.setheading(360 / lines * i)
        t.pendown()
        
        t.color(colors[i % len(colors)])
        t.forward(200)
