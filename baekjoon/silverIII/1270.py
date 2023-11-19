import sys; input=sys.stdin.readline
from collections import Counter


n = int(input())
multi = False
for _ in range(n):
    ti, *sol = map(int, input().strip().split())
    counts = Counter(sol)
    max_ = max(counts.values())
    maxlist = [k for k in counts.keys() if counts[k] == max_]

    if len(maxlist) == 1 and max_ > ti / 2:
        print(maxlist[0])
    else:
        print("SYJKGW")
    