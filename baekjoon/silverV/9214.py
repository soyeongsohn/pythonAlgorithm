import sys; input = sys.stdin.readline

cnt = 0

while True:
    n = input().strip()
    if int(n) == 0:
        break
    while True:
        if len(n) % 2 == 1:
            break

        tmp = ''
        for i in range(0, len(n), 2):
            tmp += n[i+1] * int(n[i])

        if n == tmp:
            break
        n = tmp
    cnt += 1

    print(f"Test {cnt}: {n}")
