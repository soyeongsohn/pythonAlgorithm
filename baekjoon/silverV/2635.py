import sys; input = sys.stdin.readline

n = int(input())
ans = []

for i in range(1, n + 1):
    lst = [n, i]
    while True:
        if lst[-1] < 0:
            break

        lst.append(lst[-2] - lst[-1])

    if len(lst) > len(ans):
        maxnum = len(lst) - 1
        ans = lst[:]

print(maxnum)
print(*ans[:-1], sep=" ")