import random
import turtle
t = turtle.Turtle()
t.speed(0)

def pen(color):
    t.color(color)

pen('red')

def move():
    t.pu()
    x = random.randint(-165,165)
    y = random.randint(-165,165)
    t.goto(x,y)
    t.pd()

def sky(colour):
     wn = turtle.Screen()
     wn.bgcolor(colour)

sky('#10102a')

def firework(size):
    for num in range(20):
         t.fd(size)
         t.rt(180-(360/20))

# Begin Config #
C_BRIGHT_MIN = 0x10
C_BRIGHT_MAX = 0xef
F_SIZE_MIN = 15
F_SIZE_MAX = 200
FIREWORK_PER_CLEAR = 2
# End Config #

while True:
    # this generates a random color sequence using RGB
    color_r = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
    color_g = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
    color_b = hex(random.randint(C_BRIGHT_MIN, C_BRIGHT_MAX))[2:]
    pen('#'+color_r+color_g+color_b)
    for i in range(FIREWORK_PER_CLEAR):
        firework(random.randint(F_SIZE_MIN, F_SIZE_MAX))
        move()