N, M = map(int, input().split())

A, B = [], []

A = [list(map(int, input().split())) for _ in range(N)]


for _ in range(N):
    b = list(map(int, input().split())) # 한 줄 씩 받아서
    for i in range(M):
        print(A[_][i] + b[i], end=" ") # A의 원소와 더해서 바로 출력
    print()
