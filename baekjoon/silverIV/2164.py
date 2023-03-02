from collections import deque

N = int(input())

d = deque(list(range(1, N+1)))

while len(d) > 1:
    d.popleft()
    d.append(d.popleft())

print(d[0])