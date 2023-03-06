import sys

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().rstrip().split()))
P.sort()

for i in range(1, N):
    P[i] += P[i-1]

print(sum(P))