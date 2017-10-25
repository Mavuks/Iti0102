"""Diagramm."""


import random
import calendar
import locale
import turtle
t = turtle
t.speed(100)
data_list = [100, 50, 150, 300, 200, 100, 50, 150, 300, 200.9, 200]


def get_month_name(month_no):
    """Convert a month's numeric value into its Estonian name as a string."""
    locale.setlocale(locale.LC_TIME, "et-EE")
    return calendar.month_name[month_no]


def draw_graph(pencil: turtle.Turtle, posx, posy, data_list):
    """
    Draw a bar chart-style graph and a legend describing the data.

    Arguments:
    pencil -- the turtle object used for drawing
    posx, posy -- start coordinates of the drawing
    data_list -- the data shown on the graph as a list of numeric values
    """
    # Your code here
    data_list = [100, 50, 150, 300, 200, 100, 50, 150, 300, 200.9, 200]
    turtle.setup(1500, 800)
    t.penup()
    t.goto(posx, posy)
    t.pendown()
    draw_bars(turtle, data_list)
    draw_legend(turtle, data_list)
    t.done()


def draw_legend(pencil: turtle.Turtle, data_list):
    """
    Draw a legend box for a graph.

    The legend box contains text describing the data.
    Arguments:
    pencil -- the turtle object used for drawing
    data_list -- the data as a list of numeric values
    """
    # Your code here
    t.forward(50)
    t.pendown()
    for i in range(4):
        t.forward(330)
        t.left(90)
    t.penup()
    t.goto(-75, 100)
    for index, item in enumerate(data_list):
        t.write(get_month_name(index + 1) + " " + str(item) + "€")
        t.right(90)
        t.forward(20)
        t.left(90)
    t.write("kokku:   ", True), t.write(sum(data_list), True), t.write("  €")
    t.goto(-75, -160)
    t.write("Saad minna kontserdile!")


def draw_bars(pencil: turtle.Turtle, data_list):
    """
    Draw a bar chart.

    Arguments:
    pencil -- the turtle object used for drawing
    data_list -- the data as a list of numeric values
    """
    # Your code here
    color = ["red", "orange", "yellow", "green", "violet", "blue", "deeppink", "aqua", "brown", "gold"]
    for i in data_list:
        t.begin_fill()
        t.color(random.choice(color))
        t.pencolor("black")
        t.left(90)
        t.forward(i)
        t.right(90)
        t.forward(30)
        t.right(90)
        t.forward(i)
        t.right(90)
        t.forward(30)
        t.end_fill()
        t.backward(30)
        t.setheading(0)


def main():
    """Set up the turtle window and start the drawing process."""
    # Your code here
    draw_graph(turtle, -500, -200, 0)


if __name__ == "__main__":
    main()
