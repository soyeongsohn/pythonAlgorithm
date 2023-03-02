import sys

N = int(sys.stdin.readline().rstrip())
for i in range(1, N+1):
    sum_ = sum(list(map(int, str(i))))
    if i + sum_ == N:
        print(i)
        break
    
    if i == N: # 생성자 없음
        print(0)
