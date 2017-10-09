import calendar
import locale
import turtle
t = turtle
t.speed(100)
data_list = [100, 50, 150, 300, 200, 100, 50, 150, 300, 200.9, 200, 100]

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
    data_list = [100, 50, 150, 300, 200, 100, 50, 150, 300, 200.9, 200, 100]
    turtle.setup(1500, 800)
    t.penup()
    t.goto(posx, posy)
    t.pendown()
    draw_bars(turtle,data_list)
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
    t.goto(-110, 100)
    t.write(get_month_name(1), True),t.write(":    ", True),  t.write(data_list[0], True), t.write(" €")
    t.goto(-110,80)
    t.write(get_month_name(2), True), t.write(":    ", True), t.write(data_list[1], True), t.write(" €")
    t.goto(-110, 60)
    t.write(get_month_name(3), True), t.write(":    ", True), t.write(data_list[2], True), t.write(" €")
    t.goto(-110, 40)
    t.write(get_month_name(4), True), t.write(":    ", True), t.write(data_list[3], True), t.write(" €")
    t.goto(-110, 20)
    t.write(get_month_name(5), True), t.write(":    ", True), t.write(data_list[4], True), t.write(" €")
    t.goto(-110, 0)
    t.write(get_month_name(6), True), t.write(":    ", True), t.write(data_list[5], True), t.write(" €")
    t.goto(-110, -20)
    t.write(get_month_name(7), True), t.write(":    ", True), t.write(data_list[6], True), t.write(" €")
    t.goto(-110, -40)
    t.write(get_month_name(8), True), t.write(":    ", True), t.write(data_list[7], True), t.write(" €")
    t.goto(-110, -60)
    t.write(get_month_name(9), True), t.write(":    ", True), t.write(data_list[8], True), t.write(" €")
    t.goto(-110, -80)
    t.write(get_month_name(10), True), t.write(":    ", True), t.write(data_list[9], True), t.write(" €")
    t.goto(-110, -100)
    t.write(get_month_name(11), True), t.write(":    ", True), t.write(data_list[10], True), t.write(" €")
    t.goto(-110, -120)
    t.write(get_month_name(12), True), t.write(":    ", True), t.write(data_list[11], True), t.write(" €")
    t.goto(-110, -140)
    t.write("kokku:   ", True), t.write(sum(data_list), True), t.write("  €")
    t.goto(-110, -160)
    t.write("Saad minna kontserdile!")


def draw_bars(pencil: turtle.Turtle, data_list):
    """
    Draw a bar chart.

    Arguments:
    pencil -- the turtle object used for drawing
    data_list -- the data as a list of numeric values
    """
    # Your code here
    t.color("red")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[0])
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(data_list[0])
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.right(180)
    t.forward(60)
    t.color("orange")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[1])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(data_list[1])
    t.left(90)
    t.forward(60)
    t.end_fill()
    t.color("yellow")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[2])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(data_list[2])
    t.left(90)
    t.forward(60)
    t.end_fill()
    t.color("green")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[3])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(data_list[3])
    t.left(90)
    t.forward(60)
    t.end_fill()
    t.color("violet")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[4])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(data_list[4])
    t.left(90)
    t.forward(60)
    t.end_fill()
    t.color("blue")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[5])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(data_list[5])
    t.left(90)
    t.forward(60)
    t.end_fill()
    t.color("purple")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[6])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(data_list[6])
    t.left(90)
    t.forward(60)
    t.end_fill()
    t.color("Tan")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[7])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(data_list[7])
    t.left(90)
    t.forward(60)
    t.end_fill()
    t.color("brown")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[8])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(data_list[8])
    t.left(90)
    t.forward(60)
    t.end_fill()
    t.color("deeppink")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[9])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(data_list[9])
    t.left(90)
    t.forward(60)
    t.end_fill()
    t.color("aqua")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[10])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(data_list[10])
    t.left(90)
    t.forward(60)
    t.end_fill()
    t.color("gold")
    t.begin_fill()
    t.left(90)
    t.forward(data_list[11])
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(data_list[11])
    t.left(90)
    t.end_fill()
    t.color("black")
    t.penup()





def main():
    """Set up the turtle window and start the drawing process."""
    # Your code here
    draw_graph(turtle, -500, -200,0)

if __name__ == "__main__":
    main()
    
