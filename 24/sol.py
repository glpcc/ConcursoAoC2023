
file = open("24/input.txt", "r")

lines = [i.strip() for i in file.readlines()]

segments = []
for l in lines:
    pos,vel = l.split('@')
    x,y,z = [int(i) for i in pos.split(',')]
    dx,dy,dz = [int(i) for i in vel.split(',')]
    segments.append((x,y,x+dx,y+dy))

num_intersections = 0
test_area_l = 200000000000000
test_area_h = 400000000000000
for i, seg1 in enumerate(segments):
    for j, seg2 in enumerate(segments[i+1:]):
        x1,y1,x2,y2 = seg1
        x3,y3,x4,y4 = seg2
        den = ((x1-x2)*(y3-y4)) - ((y1-y2)*(x3-x4))
        numt = ((x1-x3)*(y3-y4)) - ((y1-y3)*(x3-x4))
        numu = ((x1-x3)*(y1-y2)) - ((y1-y3)*(x1-x2))
        if den == 0: continue
        u = numu/den
        t = numt/den
        if u < 0 or t < 0: continue
        new_x = x1 + t*(x2-x1)
        new_y = y1 + t*(y2-y1)
        if test_area_l <= new_x <= test_area_h and test_area_l <= new_y <= test_area_h:
            num_intersections += 1

print(num_intersections)
