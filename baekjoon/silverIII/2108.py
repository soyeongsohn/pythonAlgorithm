import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())

nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))

# 산술평균
print(int(round(sum(nums) / N, 0)))

nums.sort()
# 중앙값
print(nums[N // 2])

c = Counter(nums)
mc = c.most_common()
# 최빈값
if len(mc) > 1 and mc[0][1] == mc[1][1]: # 최빈값이 두 개 이상인 경우
    print(mc[1][0])
else:
    print(mc[0][0])

# 범위
print(max(nums) - min(nums))