N, X = map(int, input().split())
A = list(map(int, input().split()))
answer = [str(A[i]) for i in range(N) if A[i] < X]
print(" ".join(answer))