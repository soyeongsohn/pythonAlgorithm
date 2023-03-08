import sys

N = int(sys.stdin.readline())
scores = [0] + [int(sys.stdin.readline()) for _ in range(N)]
dp = [0] * (N + 1)

if N == 1:
    print(scores[1])

elif N == 2:
    print(scores[1] + scores[2]) 
    # max(scores[1] + scores[2], scores[2])가 맞으나
    # 점수가 자연수이므로 scores[1] + scores[2]가 더 큰 게 자명하다

else:

    dp[1] = scores[1]
    dp[2] = scores[1] + scores[2]

    for i in range(3, N+1):
        # i번째 계단을 "어떻게 올라왔는지"에 대한 경우의 수
        dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])

    print(dp[-1])