import turtle
import colorsys


t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(150)

n=35
h=0

for i in range(450):
 c=colorsys.hsv_to_rgb(h, 0.9, 0.9)
 h+=2/n
 t.color(c)
 t.left(145)

 

 

 for j in range(5):
     t.forward(320)
     t.left(150)
     t.circle(5)