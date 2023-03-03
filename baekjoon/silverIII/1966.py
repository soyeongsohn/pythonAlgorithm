import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, k = map(int, sys.stdin.readline().rstrip().split())
    rank = deque(list(map(int, sys.stdin.readline().rstrip().split())))

    cnt = 0
    while rank:
        max_rank = max(rank)
        a = rank.popleft()
        k -= 1
        if a == max_rank:
            cnt += 1
            if k < 0:
                print(cnt)
                break
        else:
            rank.append(a)
            if k < 0:
                k = len(rank) - 1