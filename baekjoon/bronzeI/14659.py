import sys

# 이중 for문으로 구현하면 시간초과
# 아이디어: 현재 제일 큰 값과 다음 큰 값 사이의 값들은 어차피 카운트 해도 작으므로 무시
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
answer = []

h = lst[0]

for i in range(1, len(lst)):
    if lst[i] < h:
        cnt += 1
    else:
        h = lst[i]
        answer.append(cnt)
        cnt = 0

answer.append(cnt)
print(max(answer))