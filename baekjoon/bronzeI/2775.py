import sys


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    tmp = list(range(1, n+1))

    for i in range(k):
        tmp = [sum(tmp[:j]) for j in range(1, n+1)]

    print(tmp[-1])
