import sys
import math

A, B, V = map(int, sys.stdin.readline().rstrip().split())

day = (V - B) / (A - B)
print(math.ceil(day))
