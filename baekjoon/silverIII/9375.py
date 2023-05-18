import sys
from collections import Counter
from functools import reduce

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    
    cat = []
    for _ in range(N):
        k, v = sys.stdin.readline().split()
        cat.append(v)

    counter = Counter(cat)
    cnt = 1
    for v in counter.values(): # 각 카테고리의 개수 + 1을 곱한 것에서 1을 뺀 공식을 사용
        cnt *= (v + 1)

    print(cnt-1)