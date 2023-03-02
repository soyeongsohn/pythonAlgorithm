import math
import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

g = math.gcd(a, b)
print(g)
print(g * (a // g) * (b // g))