import sys

def binary_search(heights):
    start = 0
    end = sum(heights)

    while start <= end:
        mid = (start + end) // 2
        take = sum([i - mid for i in heights if i > mid])

        if take >= M:
            start = mid + 1
        else:
            end = mid - 1

    return end # M과 같거나 M보다 큰 수를 선택해야하므로 end 값을 고른다!

N, M = map(int, sys.stdin.readline().rstrip().split())
heights = list(map(int, sys.stdin.readline().rstrip().split()))
print(binary_search(heights))