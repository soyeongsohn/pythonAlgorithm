import sys

M = int(sys.stdin.readline().rstrip())
S = 0

for _ in range(M):
    op = sys.stdin.readline().rstrip()
    if op == "all":
        S = (1 << 20) - 1
    elif op == "empty":
        S = 0
    else:
        op, x = op.split()
        x = int(x) - 1
        if op == "add":
            S |= (1 << x)
        elif op == "remove":
            S &= ~(1 << x)
        elif op == "check":
            if S & (1 << x) == 0:
                print(0)
            else:
                print(1)
        elif op == "toggle":
            S ^= (1 << x)
