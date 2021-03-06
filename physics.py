import matplotlib.pyplot as plt
from math import *
v0 = 100
theta = 30*pi/180
c = .25
j = 0
def graphstuff(z):
    vx = v0 * cos(theta)
    vy = v0 * sin(theta)
    t = 0
    dt = .001
    m = .5
    d = .05
    x = 0
    y = 0
    g = 9.81
    xlist = [0]
    ylist = [0]
    while (y >= 0):
        xlist.append(x)
        ylist.append(y)
        x = x + vx * dt
        y = y + vy * dt      
        vx = vx - ((z*d**2) * vx*dt * sqrt(vx**2+vy**2))/m
        vy = vy -(g*dt) - ((z*d**2) * vy*dt * sqrt(vx**2+vy**2))/m
        t=t+dt
    plt.plot(xlist,ylist)
graphstuff(c)
graphstuff(j)
plt.show()