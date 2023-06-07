import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**7) # resursion 허용 범위 넓혀주기
# dfs
def dfs(y, x):
    # 상하좌우 이동을 위함
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if (0 <= new_x < M) and (0 <= new_y < N): # 밭 내에 있으면
            if matrix[new_y][new_x] == 1:
                matrix[new_y][new_x] = -1 # 본 걸로 표시
                dfs(new_y, new_x)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    # 행렬 초기화
    matrix = [[0] * M for _ in range(N)]

    cnt = 0

    # 배추 위치 집어넣기
    for _ in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1
    
    for i in range(M):
        for j in range(N):
            if matrix[j][i] == 1:
                dfs(j, i)
                cnt += 1
    
    print(cnt)