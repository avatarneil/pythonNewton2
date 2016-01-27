from math import *
v0 = 100
theta = 30*pi/180
vx = v0 * cos(theta)
vy = v0 * sin(theta)
t = 0
dt = .001
m = .5
c = 1
d = .05
x = 0
y = 0
g = 9.81

while (y >= 0):
    print (t,x,y,vy)
    x = x + vx * dt
    y = y + vy * dt      
    vx = vx - ((c*d**2) * vx*dt * sqrt(vx**2+vy**2))/m
    vy = vy -(g*dt) - ((c*d**2) * vy*dt * sqrt(vx**2+vy**2))/m
    t=t+dt
 
