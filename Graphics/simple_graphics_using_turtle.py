# Turtle graphics toolkit provides a simple and enjoyable way to draw pictures in a window 
# and gives you an opportunity to run several methods with an object.

# To find the sum of interior angles of a polygon, multiply the number of triangles in the polygon by 180 degree.
# The formula for calculating the sum of interior angles is ( n − 2 ) × 180, where is the number of sides. 
# All the interior angles in a regular polygon are equal.

from turtle import *

# Turtle's state

# Heading - in degrees anti-clockwise - positive
# Color
# Width
# Down - Is turtle's pen down or up

# Turtle methods

# t = Turtle() - Creates a new turtle object and opens it's window.
# t.home() - Moves t to the center of the window and points east.
# t.up()
# t.penup()
# t.down()
# t.pendown()
# t.setheading(degrees)
# t.left(degrees)
# t.right (degrees)
# t.goto(x, y)
# t.forward(distance)
# t.pencolor(r, g, b) 
# t.pencolor(string)
# t.fillcolor (r, g, b)
# t.fillcolor(string)
# t.begin_fill()
# t.end_fill()
# t.clear()
# t.width(pixels)
# t.hideturtle()
# t.showturtle()
# t.position()
# t.heading()
# t.isdown()
# t.speed(val)

t = Turtle() 

t.pencolor('green')

# Drawing a hexagon
def hexagon(t, a):
    for _ in range(6):
        t.forward(a)
        t.right(60)

hexagon(t, 50)

t.clear()
t.home()

# Drawing a square
def square(t, a):
    for _ in range(4):
        t.forward(a)
        t.right(90)

square(t, 50)

t.clear()

# t.speed(1)

# Radial hexagon
for i in range(6):
    hexagon(t, 50)
    t.left(360 / 6)

t.clear()

t.begin_fill()
t.penup()
t.goto(30, 30)
t.setheading(0)
t.pendown()
t.shape("square")
t.fillcolor('red')
t.end_fill()

mainloop()