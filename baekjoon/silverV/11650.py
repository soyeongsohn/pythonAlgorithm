import sys

N = int(sys.stdin.readline().rstrip())

lst = []
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

lst.sort(key=lambda x: (x[0], x[1]))

for i in lst:
    print(i[0], i[1])