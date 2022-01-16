from vpython import *
from time import *
import matplotlib.pyplot as plt
# ball parameters
ball_radius = .5
# box parameters
wall_thickness = .1
box_width = 10
box_depth = 10
box_height = 10
distance = 4.5

# position parameters
left_wall = box(pos=vector(-box_width / 2 - distance, 0, 0), size=vector(wall_thickness, box_depth, box_height), color=color.white)
right_wall = box(pos=vector(box_width / 2 + distance, 0, 0), size=vector(wall_thickness, box_depth, box_height), color=color.blue)
celing = box(pos=vector(0, box_height / 2 + distance, 0), size=vector(box_width, wall_thickness, box_depth), color=color.cyan)
back_wall = box(pos=vector(0, 0, -box_depth / 2 - distance), size=vector(box_width, box_height, wall_thickness), color=color.green)
front_wall = box(pos=vector(0,0, box_depth / 2 + distance), size=vector(box_width,box_height,wall_thickness), color=color.green)
floor = box(pos=vector(0,-box_height / 2 - distance, 0), size=vector(box_width, wall_thickness, box_depth), color=color.red)
ball_1 = sphere(radius=ball_radius, color=color.magenta)
ball_2 = sphere(radius=ball_radius, color=color.orange)
ball_3 = sphere(radius=ball_radius, color=color.yellow)
delta_x = .1
delta_y = .1
delta_z = .1
x_pos = 2
y_pos = 4
z_pos = 6
visual = []
#while True:
for i in range(1000):
    rate(100)
    x_pos = x_pos + delta_x
    visual.append(x_pos)
    y_pos = y_pos + delta_y
    z_pos = y_pos + delta_z
    if x_pos > 8.9 or x_pos < -8.9:
        delta_x = delta_x * -1
    ball_1.pos = vector(x_pos, 0, 0)
    if y_pos > 8.9 or y_pos < -8.9:
        delta_y = delta_y * -1
    ball_2.pos = vector(0, y_pos, 0)
    if z_pos > 8.9 or z_pos < -8.9:
        delta_z = delta_z * -1
    ball_3.pos = vector(0, 0, z_pos)
plt.plot(visual)
plt.show()