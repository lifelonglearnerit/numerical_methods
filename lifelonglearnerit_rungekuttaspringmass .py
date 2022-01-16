from vpython import *
#GlowScript 3.2 VPython
from vpython import *


# initial conditions of the system

x0 = float(input('Displacement x (E.g: 50.0): ')) 
v0 = float(input('Velocity v (E.g: 0.0): '))   
k = float(input('Spring constant k: (E.g: 5.0) ')) 
c = float(input('Damping constant c: (E.g: 1.0) ')) 
m = 5.0  # mass 
dt = 0.1  # integration step
t0 = 0.0  # initial time
stop = 1000  

# creation of lists with zeros

x_position = [0.0 for time in range(int(t0),stop)] # dziedzina funkcji
v_velocity = [v for v in x_position]
time = [t for t in v_velocity]

# initialisation 

x_position[0] = x0
v_velocity[0] = v0
time[0] = t0

# elements of animation 
# mass on the spring  

mass=box(pos=vector(x_position[0],0,0), velocity=vector(v_velocity[0],0,0),
         size=vector(10,10,10), color=color.blue)

# spring

spring=helix(pos=vector(-50,0,0), axis=mass.pos, radius=4,
             thickness=0.5, coils=20, color=color.red)


# visualisation fo equilibrium point

x0_arrow = arrow(pos=vector(0,-15,0), axis=vector(0,10,0), shaftwidth=1, 
                 shaftlength=50, color=color.red)
                 
x0_label = label(pos=vector(0,-15,0), text='Point of equilibrium')

# labels of the plot

f1 = gdots(color=color.red, label='Displacement: x(t)')
f2 = gdots(color=color.blue, label='Velocity: v(t)')
f3 = gdots(color=color.green, label='Acceleration: a(t)')

# labels

label(pos=vector(-35, 25, 0), text="Initial displacement: x0 = {:{2}f}\n \
      Initial velocity: v0 = {:f}\nSpring constatnt k = {:f}\n \
      Damping constatnt c = {:f}".format(x0, v0, k, c))
      
label(pos=vector(35, -35, 0), text="Created by: Tomasz Waszczewski")

# function computing acceleration

def f(x: float, v: float) -> float:
    return -(k/m) * x -(c/m) * v

# function computing position and velocity - used method Runge - Kutta 4th

def runge_kutta_4(k: float, m: float,  x_position: list, c: float, \
                  v_velocity: list, time: list, dt: float,) -> list:
                      
    acceleration = []
    for n in range(len(time)+1):
        # makes sure that a least 0.1 second has elapsed (1 sec / frequency)
        rate(10)
        
        # time
        time[n+1] = time[n] + dt
        
        # k1 - step 1
        k1_x = x_position[n]
        k1_v = v_velocity[n]
        k1_a = f(k1_x, k1_v)
        
        # k2 - step 2
        k2_x = x_position[n] + k1_v * (dt / 2)
        k2_v = v_velocity[n] + k1_a * (dt / 2)
        k2_a = f(k2_x, k2_v)
        
        # k3 - step 3
        k3_x = x_position[n] + k2_v * (dt / 2)
        k3_v = v_velocity[n] + k2_a * (dt / 2)
        k3_a = f(k3_x, k3_v)
        
        # k4 - step 4
        k4_x = x_position[n] + k3_v * dt
        k4_v = v_velocity[n] + k3_a  * dt
        k4_a =  f(k4_x, k4_v)

        x_position[n + 1] = x_position[n] + (dt / 6) * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)
        v_velocity[n + 1] = v_velocity[n] + (dt / 6) * (k1_a + 2 * k2_a + 2 * k3_a + k4_a)
        acceleration.append(k4_a)
        
        # visualisation of spring and mass 
        mass.velocity = vector(v_velocity[n], 0, 0)
        mass.pos = vector(x_position[n], 0, 0)
        spring.axis = mass.pos - spring.pos
        
        # plot
        f1.plot(pos=[(time[n], x_position[n])])
        f2.plot(pos=[(time[n], v_velocity[n])])
        f3.plot(pos=[(time[n], acceleration[n])])
        
        # labels 
        label(pos=vector(25, 25, 0), text="Displacement: x(t) = {:f}\n \
              Velocity: v(t) = {:f}\nAcceleration: a(t) = {:f}\n \
              Time: t = {:f}".format(x_position[n],v_velocity[n],acceleration[n],time[n]))

    
    return x_position, v_velocity, time, acceleration

runge_kutta_4(k, m, x_position, c, v_velocity, time, dt)

