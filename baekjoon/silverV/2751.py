import sys

N = int(sys.stdin.readline().rstrip())

lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline().rstrip()))

lst.sort()

for i in lst:
    print(i)