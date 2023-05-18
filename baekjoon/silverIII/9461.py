import sys
input = sys.stdin.readline

def length(n):
    dp = {1: 1, 2: 1, 3: 1}

    if n in dp:
        return dp[n]
    else:
        for i in range(4, n+1):
            dp[i] = dp[i-3] + dp[i-2]

        return dp[n] 


T = int(input())

for _ in range(T):
    n = int(input())
    print(length(n))