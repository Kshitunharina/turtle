import turtle

# Create the screen
screen = turtle.Screen()
screen.setup(width=700, height=600)     # Screen size
screen.title("Turtle Star Drawing")     # Screen title
screen.bgcolor("black")                 # Background colour (you can change it)

# Create turtle
star = turtle.Turtle()
star.color("yellow")                    # Star colour
star.pensize(3)
star.speed(5)

# Draw a star
for i in range(5):
    star.forward(150)
    star.right(144)

# Finish
turtle.done()
