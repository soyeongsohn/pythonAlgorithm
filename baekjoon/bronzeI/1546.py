N = int(input())
scores = list(map(int, input().split()))

print(sum([i / max(scores) * 100 for i in scores]) / N)