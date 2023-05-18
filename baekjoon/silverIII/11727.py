def func(n):
    dp = {1:1}

    if n == 1:
        return dp[n]
    for i in range(2, n+1):
        if i % 2 == 0:
            dp[i] = dp[i-1] * 2 + 1
        else:
            dp[i] = dp[i-1] * 2 - 1

    return dp[n] % 10007


n = int(input())
print(func(n))