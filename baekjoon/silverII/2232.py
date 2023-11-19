import sys; input=sys.stdin.readline

# 양 옆의 수가 자신보다 작거나 같다 -> 터트린다
# 시작, 끝 지뢰도 확인하기 위해 앞뒤에 0 추가

n = int(input())

nums = [0]
for _ in range(n):
    nums.append(int(input()))

nums.append(0)

explode = []

for i in range(1, n+1):
    if (nums[i-1] <= nums[i]) and (nums[i+1] <= nums[i]):
        explode.append(i)

print(*explode, sep="\n")