import sys

# fib(n+1)은 fib(n)과 fib(n-1)을 호출한다 -> 그들의 0, 1 호출 수의 합이다

def cnt_fib(n):
    dp = {0:[1, 0], 1:[0, 1]}

    if n < 2:
        return dp[n]
    else:
        for i in range(2, n+1):
            if i in dp:
                return dp[i]
            dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]
        return dp[n]

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    x, y = cnt_fib(n)

    print(x, y)