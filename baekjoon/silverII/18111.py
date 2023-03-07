import sys
from collections import Counter

N, M, B = map(int, sys.stdin.readline().split())
ground = []
for _ in range(N): 
    ground += map(int, sys.stdin.readline().split()) # 2차원 배열이 아닌 1차원으로 받아온다

height, time = 0, sys.maxsize

min_h = min(ground)
max_h = max(ground)
_sum = sum(ground)
ground = Counter(ground) # 각 층 별 수를 센다

for i in range(min_h, max_h + 1):
    if _sum + B >= i * N * M:
        cur_time = 0
        for g in ground:
            if g > i:
                cur_time += (g - i) * ground[g] * 2
            elif g < i:
                cur_time += (i - g) * ground[g]
        if cur_time <= time:
            time = cur_time
            height = i

print(time, height)