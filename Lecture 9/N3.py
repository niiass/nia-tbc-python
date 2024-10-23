import random
import math
import turtle
import time

x = turtle.Turtle()
y = turtle.Turtle()
t = turtle.Turtle()

# Function to draw a point at (x, y)
def draw_point(x, y, color, size):
    t.speed(0)
    t.penup()  # Lift the pen to avoid drawing a line
    t.goto(x, y)  # Move to the point (x, y)
    t.dot(size, color)  # Draw the point with the specified size and color

# Hide turtle and display the window
t.hideturtle()

def drawX():
    x.speed(0)
    x.setpos(-250, 0)
    x.forward(500)

def drawY():
    y.speed(0)
    y.setpos(0, -250)
    y.setheading(90)
    y.forward(500)

drawX()
drawY()


n = int(input("Enter an integer: "))

if n <= 1:
    print("Input must be more than 1!")
    exit(1)

counter = 0
for i in range(n):
    color = "green"
    a = random.uniform(0, 1)
    b = random.uniform(0, 1)
    print("Value of a is - ", a, "; Value of b is - ", b)
    if (math.sqrt(a ** 2 + b ** 2) <= 1):
        counter += 1
        color = "red"
    x = a * 200
    y = b * 200
    draw_point(x, y, color, 10)

print(4*counter/n)

time.sleep(20)