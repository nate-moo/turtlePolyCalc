from turtle import Turtle, Screen
from time import time

t = Turtle()
s = Screen()

### Window Props
s.setup(500, 500) # Window Size
s.xscale = 15     # x axis scale
s.yscale = 0.2    # y axis scale
iyscale = 6
xs = -10          # X axis start
xe = 10           # X axis end
resolution = 0.25
t.speed(0)        # Speed of pen

print(s.canvheight)
print(s.canvwidth)

t.goto(xe, 0)
t.goto(xs, 0)
t.goto(0, 0)
t.goto(0, xs*10)
t.goto(0, xe*10)
t.goto(0, 0)

t.penup()
y = lambda x: 2*x**3 + (5*x)**2 + x
t.goto(xs, 0)
computed = list()
st = time()
while xs < xe:
    computed.append([xs, y(xs)])
    print(xs, computed)
    xs+=resolution

e = time()

std = time()
for a, i in computed:
    if abs(i) < s.canvheight * iyscale:
        print("Drawn", True)
        t.goto(a, i)
        t.pendown()
        t.dot(2)
    else:
        print("Drawn", False)
ed = time()
print("Calculation took", f"{round(e-st, 4)}s")
print("drawing took:", f"{round(ed - std, 4)}s")
input()