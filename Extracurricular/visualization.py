'''
თავიდან ცოტა ნელა შვება, სიჩქარე დაბალზე მაქვს დაყენებული
იმიტომ რომ მერე ძალიან ჩქარდება
'''

import turtle
import time

cube = 27

line = turtle.Turtle()
t = turtle.Turtle()

def drawLine():
    line.speed(0)
    line.setpos(-250, 0)
    line.forward(500)

def draw_point(x, y, color, size):
    t.speed(3)
    t.penup()
    t.goto(x, y)
    t.dot(size, color)

t.hideturtle()

drawLine()

'''
High point is red color
Low point is green color
Answer point is blue color
'''
epsilon = 0.00000000000001
low = 0
high = cube
answer = (low + high) / 2

iterations = 0
while abs(answer ** 3 - cube) >= epsilon:
    draw_point(high*100 - 250, 0, "red", 5)
    draw_point(low*100 - 250, 0, "green", 5)
    draw_point(answer*100 - 250, 0, "blue", 5)
    if answer ** 3 > cube:
        high = answer
    else:
        low = answer
    answer = (low + high) / 2
    iterations += 1

print("Number of iterations = ", iterations)
print("Answer = ", answer)

time.sleep(5)

