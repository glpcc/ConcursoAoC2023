import numpy as np

file = open("15/input.txt", "r")

line = file.readline().strip()

strs = list(line.split(','))

def get_hash(s: str):
    hsh = 0
    for chr in s:
        hsh += ord(chr)
        hsh *= 17
        hsh = hsh%256
    return hsh

tot = 0
for s in strs:
    tot += get_hash(s)

print(tot)