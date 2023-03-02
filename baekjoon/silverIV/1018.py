import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

board = []
result = []

for _ in range(N):
    board.append(sys.stdin.readline().rstrip())

for i in range(N - 7):
    for j in range(M - 7):
        m1 = 0 # 1행 1열 시작이 B
        m2 = 0 # 1행 1열 시작이 W

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != "B":
                        m1 += 1
                    elif board[x][y] != "W":
                        m2 += 1
                else:
                    if board[x][y] != "W":
                        m1 += 1
                    elif board[x][y] != "B":
                        m2 += 1
        result.extend((m1, m2))

print(min(result))


