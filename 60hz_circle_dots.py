from vpython import *
import random
#from timer import Timer
import time
# x_min = float(input('x min: '))
# x_max = float(input('x max: '))
# f1 = gcurve(color=color.cyan)
# for x in arange(x_min, x_max, 0.01):
#     f1.plot(x, sin(x))
# circle plot
# cr = shapes.circle(radius=2)
# extrusion(path=[vec(0,0,0), vec(0,0,-0.1)],
#           shape=cr)

n = int(input('give a number: '))
graph(width=600, height=600,
      title='<b>Numerical Methods</b>',
      xtitle='<i>Axis X</i>', ytitle='<i>Axis Y</i>',
      foreground=color.black, background=color.white,
      xmin=-1, xmax=1, ymin=-1, ymax=1)
angle = 0
circle_x = 0
circle_y = 0
step = 0.01
dots = gdots(color=color.blue)
circle = gcurve(color=color.red)

while angle <= 7:
    circle.plot(circle_x + 1*cos(angle), circle_y + 1*sin(angle))
    angle += step
while n > 0:
    rate(60)
    dots.plot(random.uniform(-1, 1), random.uniform(-1, 1))
    n -= 1




