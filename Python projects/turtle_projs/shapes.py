import random
import turtle as tt 
from turtle import colormode
a = 4
def pickThreeColors():
    rd = random.Random()
    tp = []
    for i in range(3):
        tp.append(rd.randint(0,255))
    tp = tuple(tp)
    return tp


kohli = tt.Turtle()
my_screen = tt.Screen()
kohli.shape("turtle")
sides = 3
angle = 30
color_list = ["orange,blue, green, yellow, red, pink, maroon,black"]
colormode(cmode=255)
for i in range(8):
    
    kohli.pencolor(pickThreeColors())
    for i in range(sides):
        kohli.forward(100)
        kohli.right(90+angle)
    angle -= 30
    if angle + 90 ==0:
        kohli.right(90)
    sides += 1

my_screen.exitonclick()