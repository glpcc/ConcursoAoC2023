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
t1 = Int('t1')
t2 = Int('t2')
t3 = Int('t3')

s = Solver()

s.add(179797749771737-179982504986147 == t1*(-83))


print(s)
print(s.check())
print(s.model())
print(s.model()[x] + s.model()[y] + s.model()[z])
print(194723518367339 + 181910661443432 + 150675954587450)