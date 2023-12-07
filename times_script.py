import os
import time

days_solved = 6
temp_file = open('temp.txt','w')
temp_file.close()
for i in range(1,days_solved+1):
    start = time.time()
    os.system(f'python ./{i}/sol.py > temp.txt')
    time_part1 = time.time() - start
    start = time.time()
    os.system(f'python ./{i}/sol2.py > temp.txt')
    time_part2 = time.time() - start
    print(f'Day {i} Time for Part1: {time_part1*1000:.2f}ms, Part2: {time_part2*1000:.2f}ms')

temp_file.close()
os.remove('temp.txt')