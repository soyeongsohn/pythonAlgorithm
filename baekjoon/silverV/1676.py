import math

N = int(input())
fact = math.factorial(N)

cnt = 0
while True:
    if fact % (10 ** (cnt + 1)) == 0:
        cnt += 1
    else:
        break

print(cnt)
