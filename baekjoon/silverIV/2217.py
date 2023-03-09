import sys

N = int(sys.stdin.readline())

lst = [int(sys.stdin.readline()) for _ in range(N)]
lst.sort(reverse=True)

best = []

for i in range(N):
    best.append(lst[i] * (i + 1))

print(max(best))