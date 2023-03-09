import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()
B.sort(reverse=True)

print(sum([A[i] * B[i] for i in range(N)]))