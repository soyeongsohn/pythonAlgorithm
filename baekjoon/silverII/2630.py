import sys; input = sys.stdin.readline

def solution(x, y, N):
    color = matrix[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != matrix[i][j]:
                solution(x, y, N // 2)
                solution(x, y + N // 2, N // 2)
                solution(x + N // 2, y, N // 2)
                solution(x + N // 2, y + N // 2, N // 2)
                return None
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0]

solution(0, 0, N)
print(result[0])
print(result[1])