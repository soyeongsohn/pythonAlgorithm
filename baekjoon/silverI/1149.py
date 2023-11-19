import sys; input=sys.stdin.readline

n = int(input())
costs = [list(map(int, input().strip().split())) for _ in range(n)]

# R, G, B에 대해 이전 집들의 비용의 합의 최솟값들을 더해준다.
for i in range(1, n):
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])

print(min(costs[-1])) # 그 중 최솟값을 출력