import sys; input=sys.stdin.readline

n = int(input())

rects = [list(map(int, input().strip().split())) for _ in range(n)]


dp = [[0] * 2 for _ in range(n)]
dp[0] = rects[0]

for i in range(1, n):
    dp[i][0] = rects[i][0] + max(dp[i-1][0] + abs(rects[i-1][1] - rects[i][1]),
                                dp[i-1][1] + abs(rects[i-1][0] - rects[i][1]))

    dp[i][1] = rects[i][1] + max(dp[i-1][0] + abs(rects[i-1][1] - rects[i][0]),
                                dp[i-1][1] + abs(rects[i-1][0] - rects[i][0]))
print(max(dp[n-1][0], dp[n-1][1]))
