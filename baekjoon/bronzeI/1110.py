N = int(input())
new = N
cnt = 0
while True:
    a, b = new // 10, new % 10
    c = (a + b) % 10
    new = b * 10 + c
    cnt += 1
    if N == new:
        break

print(cnt)