from turtle import Turtle, Screen

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

while xs < xe:
    computed = y(xs)
    print(xs, computed)
    if abs(computed) < s.canvheight * iyscale:
        print("Drawn", True)
        t.goto(xs, computed)
        t.pendown()
        t.dot(2)
    xs+=resolution

input()