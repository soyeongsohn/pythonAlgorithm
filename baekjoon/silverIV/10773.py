import sys

K = int(sys.stdin.readline().rstrip())

lst = []

for _ in range(K):
    n = int(sys.stdin.readline().rstrip())
    if n != 0:
        lst.append(n)
    else:
        lst.pop()

print(sum(lst))