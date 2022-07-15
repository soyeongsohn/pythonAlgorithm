true = [1, 1, 2, 2, 2, 8]
found = list(map(int, input().split()))

print(" ".join(list(map(lambda x, y: str(x - y), true, found))))