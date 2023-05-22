from collections import deque
import sys
input = sys.stdin.readline


# dfs
def dfs(idx):
    global visited

    visited[idx] = 1
    print(idx, end=" ")
    for next in range(1, N + 1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

# bfs
def bfs():
    global q, visited
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for next in range(1, N + 1):
            if not visited[next] and graph[cur][next]:
                visited[next] = 1
                q.append(next)



N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

# graph 생성
for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

visited = [0] * (N + 1) # bfs용
dfs(V)
print()

visited = [0] * (N + 1) # dfs용
q = deque()
q.append(V)
visited[V] = 1
bfs()