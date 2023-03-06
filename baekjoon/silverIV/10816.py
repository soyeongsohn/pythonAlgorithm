import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))

n_count = Counter(n_list)

for i in m_list:
    if i in n_count.keys():
        print(n_count[i], end=" ")
    else:
        print(0, end=" ")