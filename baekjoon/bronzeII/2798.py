import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

combs = list(combinations(nums, 3))
sums = [sum(i) for i in combs if sum(i) <= M]
print(max(sums))