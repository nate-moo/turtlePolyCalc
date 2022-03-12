from turtle import Turtle, Screen
from time import time

t = Turtle()
s = Screen()
computed = list()

### Window Props ###
s.setup(500, 500) # Window Size
s.xscale = 10    # x axis scale
s.yscale = 1    # y axis scale
iyscale = 6
xs = -20          # X axis start
xe = 20           # X axis end
resolution = .1
t.speed(0)        # Speed of pen
y = lambda x: x**3 - x**2 - 14*x + 32
### ------ ###

def _compute(xs):
    st = time()
    while xs < xe:
        computed.append([xs, y(xs)])
        # print([xs, y(xs)])
        xs += resolution
    e = time()
    return e, st

def _draw():
    std = time()
    for a, i in computed:
        if abs(i) < s.canvheight:
            # print("Drawn", True)
            t.goto(a, i)
            t.pendown()
            t.dot(2)
        # else:
            # print("Drawn", False)
    ed = time()
    return ed, std

def setup():
    t.screen = s
    t.goto(xe, 0)
    t.write(f"{xe}")
    t.goto(xs, 0)
    t.write(f"{xs}")
    t.goto(0, 0)
    t.goto(0, xs*10)
    t.write(f"{xs*10}")
    t.goto(0, xe*10)
    t.write(f"{xe*10}")
    t.goto(0, 0)
    t.penup()
    t.goto(xs, 0)

    return _compute(xs), _draw()

(e, st), (ed, std) = setup()

print("Calculation took", f"{round(e-st, 4)}s")
print("drawing took:", f"{round(ed - std, 4)}s")
# print(t.screen.window_height())
print()
input()