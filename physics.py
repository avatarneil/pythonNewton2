import math
v0 = 100
vx = v0 * math.cos(30)
vy = v0 * math.sin(30)
t = 0
dt = .1
m = .5
c = 1
d = .5
x = 0
y = 0
g = 9.81

while (t < 20):
    vx = vx - ((c*d**2) * vx*dt * math.sqrt(vx**2+vy**2))/m
    vy = vy -(g*dt) - ((c*d**2) * vy*dt * math.sqrt(vx**2+vy**2))/m
    x = x + vx * dt
    y = y + vy * dt
    t=t+dt
    print (x)
    print (y)
    print (t)
