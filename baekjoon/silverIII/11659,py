import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

nums = list(map(int, sys.stdin.readline().rstrip().split()))
# 누적합 구하기
for i in range(N-1):
    nums[i+1] += nums[i]

nums = [0] + nums # 1번 인덱스가 구간에 포함될 때 빼지 않도록 0 추가

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(nums[j] - nums[i-1])
