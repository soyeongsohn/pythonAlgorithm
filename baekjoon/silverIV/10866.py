import sys
from collections import deque

def is_empty(d):
    return 1 if len(d) == 0 else 0

N = int(sys.stdin.readline().rstrip())
d = deque()

for _ in range(N):
    comm = sys.stdin.readline().rstrip()

    if comm == "empty":
        print(is_empty(d))
    elif comm == "size":
        print(len(d))
    elif comm == "front":
        print(-1 if is_empty(d) else d[0])
    elif comm == "back":
        print(-1 if is_empty(d) else d[-1])
    elif comm == "pop_front":
        print(-1 if is_empty(d) else d.popleft())
    elif comm == "pop_back":
        print(-1 if is_empty(d) else d.pop())
    else:
        push, num = comm.split()
        if push == "push_front":
            d.appendleft(num)
        else:
            d.append(num)