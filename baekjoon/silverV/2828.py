import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
J = int(sys.stdin.readline())

basket = list(range(1, M+1))
cnt = 0

for _ in range(J):
    apple = int(sys.stdin.readline())

    while True:
        if apple in basket:
            break
        elif apple not in basket and basket[0] > apple:
            basket = list(map(lambda x: x-1, basket))
            cnt += 1
        else:
            basket = list(map(lambda x:x+1, basket))
            cnt += 1

print(cnt)