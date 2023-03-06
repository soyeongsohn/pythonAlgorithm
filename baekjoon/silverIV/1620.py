import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

pokemon = {}

for i in range(N):
    p = sys.stdin.readline().rstrip()
    pokemon[p] = i + 1
    pokemon[i+1] = p

for _ in range(M):
    q = sys.stdin.readline().rstrip()
    if q.isdigit():
        print(pokemon[int(q)])
    else:
        print(pokemon[q])
