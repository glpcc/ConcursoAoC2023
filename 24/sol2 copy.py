from matplotlib import pyplot as plt
import numpy as np
from skspatial.objects import Line
import intervaltree

file = open("24/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

hailstones = []
real_lines = []


for l in lines:
    pos,vel = l.split('@')
    pos = np.array([int(i) for i in pos.split(',')])
    vel = np.array([int(i) for i in vel.split(',')])
    hailstones.append((pos,vel)) 

rng = 300
posible_dx = intervaltree.IntervalTree()
posible_dx.add(intervaltree.Interval(-rng,rng))

posible_dy = intervaltree.IntervalTree()
posible_dy.add(intervaltree.Interval(-rng,rng))

posible_dz = intervaltree.IntervalTree()
posible_dz.add(intervaltree.Interval(-rng,rng))


for i,(pos1, vel1) in enumerate(hailstones):
    for pos2,vel2 in hailstones[i+1:]:
        if pos1[0] > pos2[0] and vel1[0] > vel2[0]:
            m = min(vel1[0],vel2[0])
            mx = max(vel1[0],vel2[0])
            if mx >= 159 and m <= 159:
                print(pos1,pos2,vel1,vel2)
                print('x',vel1[0],vel2[0])
            posible_dx.chop(m,mx)
        if pos1[1] > pos2[1] and vel1[1] > vel2[1]:
            m = min(vel1[1],vel2[1])
            mx = max(vel1[1],vel2[1])
            posible_dy.chop(m,mx)
        if pos1[2] > pos2[2] and vel1[2] > vel2[2]:
            m = min(vel1[2],vel2[2])
            mx = max(vel1[2],vel2[2])
            posible_dz.chop(m,mx)

posible_dx.merge_overlaps()
posible_dy.merge_overlaps()
posible_dz.merge_overlaps()
totx = 0
for intr in posible_dx:
    totx += intr.end - intr.begin
    print('x',intr)
toty = 0
for intr in posible_dy:
    print('y',intr)
    toty += intr.end - intr.begin
totz = 0
for intr in posible_dz:
    totz += intr.end - intr.begin
    print('z',intr)
print(totx*toty*totz)
# generator of posible points
def posible_velocities():
    i = 0
    for intr in posible_dx:
        for dx in range(intr.begin,intr.end+1):
            for int2 in posible_dy:
                for dy in range(int2.begin,int2.end+1):
                    for int3 in posible_dz:
                        for dz in range(int3.begin,int3.end+1):
                            yield (dx,dy,dz)
                            i += 1
                            if i % 100000 == 0:
                                print(i)

def calculate_number_ns(point,line: Line):
    # Point must be in line
    rest = point - line.point
    steps_vec = np.zeros(3)
    steps_vec: np.ndarray = np.divide(rest,line.direction,where=line.direction!=0)
    if any(steps_vec[i] == 0 and point[i] != line.point[i]  for i in range(len(steps_vec))):
        return -1
    else:
        steps_vec = steps_vec[steps_vec != 0]
    if all(x.is_integer() for x in steps_vec):
        steps_vec = steps_vec.astype(int)
        if np.all(steps_vec >= 0) and np.all(steps_vec == steps_vec[0]):
            return steps_vec[0]
        else:
            return -1
    else:
        return -1
    
def check_intersection(pos1,vel1,point):
    line = Line(pos1,vel1)
    return calculate_number_ns(point,line) >= 0

for dx,dy,dz in posible_velocities():
    reference_vel = np.array([dx,dy,dz])
    if (dx,dy,dz) == (148, 159 ,249):
        print(reference_vel)
        print(hailstones[0][1])
    new_vel1 = hailstones[0][1] - reference_vel
    new_vel2 = hailstones[1][1] - reference_vel
    line1 = Line(hailstones[0][0],new_vel1)
    line2 = Line(hailstones[1][0],new_vel2)
    if (dx,dy,dz) == (148, 159 ,249):
            print(line1,line2)
    # print(dx,dy,dz)
    try:
        inter = line1.intersect_line(line2)
        if (dx,dy,dz) == (148, 159 ,249):
            print(inter)
        inter = inter.round().astype('int64')
        if (dx,dy,dz) == (148, 159 ,249):
            print(inter)
        nmbr_ns = calculate_number_ns(inter,line1)
        if (dx,dy,dz) == (148, 159 ,249):
            print(nmbr_ns)
        if nmbr_ns < 0:
            continue
        nmbr_ns = calculate_number_ns(inter,line2)
        if nmbr_ns < 0:
            continue
    except ValueError as e:
        continue
    # except TypeError as e:
    #     continue
    # Check if the rest of the lines intersect
    posible = True
    for i in range(2,len(hailstones)):
        pos,vel = hailstones[i]
        new_vel = vel - reference_vel
        if not check_intersection(pos,new_vel,inter):
            posible = False
            break
    if posible:
        print(inter)
        print(reference_vel)
        break

