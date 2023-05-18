import sys
input = sys.stdin.readline


def n_case(n):
    dp = {1: 1, 2: 2, 3: 4}

    if n in dp:
        return dp[n]
    else:
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]


T = int(input())

for _ in range(T):
    n = int(input())
    print(n_case(n))