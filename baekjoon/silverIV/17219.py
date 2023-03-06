import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

pws = {}

for _ in range(N):
    site, pw = sys.stdin.readline().rstrip().split()
    pws[site] = pw

for _ in range(M):
    site = sys.stdin.readline().rstrip()
    print(pws[site])

