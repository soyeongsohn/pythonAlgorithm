import sys; input = sys.stdin.readline

def solution(x, y, N):
    global result
    color = matrix[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != matrix[i][j]:
                solution(x, y, N // 3)
                solution(x, y + N // 3, N // 3)
                solution(x, y + (N // 3) * 2, N // 3)
                solution(x + N // 3, y, N // 3)
                solution(x + N // 3, y + N // 3, N // 3)
                solution(x + N // 3, y + (N // 3) * 2, N // 3)
                solution(x + (N // 3) * 2, y, N // 3)
                solution(x + (N // 3) * 2, y + N // 3, N // 3)
                solution(x + (N // 3) * 2, y + (N // 3) * 2, N // 3)
                return None
            
    if color == -1:
        result[0] += 1
    elif color == 0:
        result[1] += 1
    else:
        result[2] += 1

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0, 0]

solution(0, 0, N)
for i in result:
    print(i)