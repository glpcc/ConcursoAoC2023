from matplotlib import pyplot as plt
import numpy as np
from z3 import *

file = open("24/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

hailstones = []
real_lines = []


for l in lines:
    pos,vel = l.split('@')
    pos = np.array([int(i) for i in pos.split(',')])
    vel = np.array([int(i) for i in vel.split(',')])
    hailstones.append((pos,vel)) 

rng = 900
x = Int('x')
y = Int('y')
z = Int('z')
dx = Int('dx')
dy = Int('dy')
dz = Int('dz')
t1 = Int('t1')
t2 = Int('t2')
t3 = Int('t3')

s = Solver()
s.add(x == hailstones[149][0][0] + t1*(hailstones[149][1][0] - dx))
s.add(y == hailstones[149][0][1] + t1*(hailstones[149][1][1] - dy))
s.add(z == hailstones[149][0][2] + t1*(hailstones[149][1][2] - dz))
s.add(x == hailstones[1][0][0] + t2*(hailstones[1][1][0] - dx))
s.add(y == hailstones[1][0][1] + t2*(hailstones[1][1][1] - dy))
s.add(z == hailstones[1][0][2] + t2*(hailstones[1][1][2] - dz))
s.add(x == hailstones[2][0][0] + t3*(hailstones[2][1][0] - dx))
s.add(y == hailstones[2][0][1] + t3*(hailstones[2][1][1] - dy))
s.add(z == hailstones[2][0][2] + t3*(hailstones[2][1][2] - dz))
s.add(t1 >= 0)
s.add(t2 >= 0)
s.add(t3 >= 0)

print(s)
print(s.check())
print(s.model())
print(s.model()[x] + s.model()[y] + s.model()[z])
print(194723518367339 + 181910661443432 + 150675954587450)