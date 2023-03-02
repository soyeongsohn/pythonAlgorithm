x, y, w, h = map(int, input().split())
min_dist = min([_ for _ in [x, y, w-x, h-y] if _ >= 0])
print(min_dist)