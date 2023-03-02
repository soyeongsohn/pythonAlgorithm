N = int(input())

n, cnt = 1, 1

while N > n:
    n += 6 * cnt
    cnt += 1

print(cnt)