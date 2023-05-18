import sys
import math

A, B, V = map(int, sys.stdin.readline().rstrip().split())

day = (V - B) / (A - B) # V = A * day - B * (day - 1)
print(math.ceil(day))
