import sys; input = sys.stdin.readline

def bfs():
    global q, linked
    while q:
        cur = q.pop(0)
        linked.append(cur)
        for next in range(1, N + 1):
            if not visited[next] and graph[cur][next]:
                visited[next] = 1
                q.append(next)

N = int(input())
M = int(input())

graph = [[0] * (N + 1) for _ in range(N + 1)]

# graph 생성
for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

visited = [0] * (N + 1)
visited[1] = 1
linked = []
q = [1]
bfs()

print(len(linked) - 1)
