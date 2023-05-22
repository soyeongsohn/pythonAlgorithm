import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**7) # resursion 허용 범위 넓혀주기
# dfs
def dfs(idx):
    global visited

    visited[idx] = 1
    for next in range(1, N + 1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

N, M = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

visited = [0] * (N + 1)

cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)