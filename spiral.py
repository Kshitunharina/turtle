import turtle

# Create screen
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("Rainbow Spiral Web")
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Rainbow colours
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw spiral web
distance = 5
for i in range(100):
    pen.color(colors[i % 7])
    pen.forward(distance)
    pen.right(30)
    distance += 3

# Finish
turtle.done()
