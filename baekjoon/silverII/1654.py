import sys

K, N = map(int, sys.stdin.readline().rstrip().split())

lans = []
for _ in range(K):
    lans.append(int(sys.stdin.readline().rstrip()))

start = 0
end = max(lans)

while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        break
    n = sum([i // mid for i in lans])

    if n < N:
        end = mid - 1
    else:
        start = mid + 1
    

print(end)