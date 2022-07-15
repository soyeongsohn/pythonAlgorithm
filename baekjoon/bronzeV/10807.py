from collections import Counter

N = int(input())
nums = list(map(int, input().split()))
v = int(input())
print(Counter(nums)[v])