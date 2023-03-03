import sys

M = int(sys.stdin.readline().rstrip())
S = set()

for _ in range(M):
    op = sys.stdin.readline().rstrip()
    if op == "all":
        S = set(range(1, 21))
    elif op == "empty":
        S = set()
    else:
        op, x = op.split()
        x = int(x)
        if op == "add":
            S = S | set([x])
        elif op == "remove":
            S = S - set([x])
        elif op == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif op == "toggle":
            if x in S:
                S = S - set([x])
            else:
                S = S | set([x])
