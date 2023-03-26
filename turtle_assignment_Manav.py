import turtle

turtle.speed(3)
turtle.bgcolor("white")


def rectangle_will_fit_draw(shape, color, x, y, length, height=0):
    if shape == "r":
        if x + length <= 400 and y + height <= 400:
            turtle.up()
            turtle.goto(x, y)
            turtle.fillcolor(color)
            turtle.begin_fill()
            turtle.down()
            for i in range(1, 3):
                turtle.forward(length)
                turtle.right(90)
                turtle.forward(height)
                turtle.right(90)
            turtle.end_fill()
            turtle.up()
            turtle.goto(0, 400)
            return color
        else:
            return  

    elif shape == "c":
        if height <= 400:
            turtle.up()
            turtle.goto(x, y)
            turtle.left(180)
            turtle.fillcolor(color)
            turtle.begin_fill()
            turtle.forward(height)
            turtle.down()
            turtle.circle(height)
            turtle.end_fill()
            turtle.up()
            turtle.goto(0, 400)
            turtle.left(180)
        else:
            return 0

    elif shape == "t":
        turtle.up()
        turtle.fillcolor(color)
        turtle.goto(x, y)
        turtle.begin_fill()
        turtle.down()
        if height <= 400:
            i = 0
            while i < 3:
                turtle.forward(height)
                turtle.left(120)
                i = i + 1
        else:
            return 0
        turtle.end_fill()


rectangle_will_fit_draw("r", "black", 100, 125, 200, 125)
rectangle_will_fit_draw("c", "yellow", -5, 0, 250, 75)
rectangle_will_fit_draw("t", "green", -105, 150, 150, 105)

turtle.done()




