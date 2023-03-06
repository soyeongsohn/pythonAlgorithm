import sys
import math


N, K = map(int, sys.stdin.readline().rstrip().split())

value = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

cnt = 0
exp = int(math.log(value[-1], 10))
for i in value[::-1]:
    cnt += K // i
    K %= i

print(cnt)