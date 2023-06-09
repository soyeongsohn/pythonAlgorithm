import sys; input = sys.stdin.readline
from itertools import combinations

def distance(mbtis):
    return len(set(mbtis[0]+mbtis[1])) + len(set(mbtis[1]+mbtis[2])) \
        + len(set(mbtis[2]+mbtis[0])) - 12


T = int(input())
for _ in range(T):
    min_dist = sys.maxsize
    N = int(input())
    mbti = input().split()
    cnt = [mbti.count(i) for i in list(set(mbti))]
    if max(cnt) >= 3:
        print(0)
        continue
    
    comb = combinations(mbti, 3)
    
    for i in comb:
        dist = distance(i)
        if dist == 0:
            min_dist = 0
            break
        if dist < min_dist:
            min_dist = dist

    print(min_dist)