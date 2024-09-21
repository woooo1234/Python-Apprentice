"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error


# TODO)
#   1. Create a turtle.

def drawSquare():
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)
def drawTriangle():
    turtle.circle(50,360,3)
def drawCricle():
    turtle.circle(50)

user_input = input("What shape do you want to draw: ")

if user_input == "Triangle":
    drawTriangle()
elif user_input == "Circle":
    drawCricle()
elif user_input == "Square":
    drawSquare()

#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
#   3. Ask the user for the for a shape to draw.
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
pass
