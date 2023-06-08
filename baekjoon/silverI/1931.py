import sys; input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# # 종료 시간, 시작시간 순으로 고려하여 정렬
meetings.sort(key=lambda x: (x[1], x[0]))
max_time = max(meetings, key=lambda x: x[1])[1]

n = 0
end = 0

for s, e in meetings:
    if s < end:
        continue
    n += 1
    end = e

print(n)