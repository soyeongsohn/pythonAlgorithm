import sys

for i in range(3):
    n = int(sys.stdin.readline())
    s = 0
    for _ in range(n):
        a = int(sys.stdin.readline())
        s += a
    print("0" if s == 0 else ("+" if s > 0 else "-"))