def func(n):
    dp = {1:1, 2:2}
    if n in dp:
        return dp[n] % 10007
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n] % 10007

n = int(input())
print(func(n))