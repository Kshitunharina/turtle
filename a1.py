import turtle

# Create screen
screen = turtle.Screen()
screen.setup(width=600, height=600)   # Screen size
screen.bgcolor("lightblue")           # Background colour
screen.title("Drawing a Square")      # Title

# Create turtle
pen = turtle.Turtle()
pen.color("black")                    # Pen colour
pen.pensize(3)                        # Pen thickness

# Draw a square
for i in range(4):
    pen.forward(100)
    pen.right(90)

# Keep the window open
turtle.done()
