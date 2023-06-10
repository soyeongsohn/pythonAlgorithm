import sys; input = sys.stdin.readline


def solution(M, N, x, y):
    # 정답은 x에 M을 계속 더해나간 값 == y에 N을 계속 더해나간 값
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M 
    return -1

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(solution(M, N, x, y))