import sys

N = int(sys.stdin.readline().rstrip())

lst = []
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))

answer = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if (lst[j][0] > lst[i][0]) and (lst[j][1] > lst[i][1]):
            cnt += 1
        
    answer.append(cnt+1)

for i in answer:
    print(i, end=" ")