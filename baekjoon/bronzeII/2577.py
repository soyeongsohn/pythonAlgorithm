from math import prod
from collections import Counter


abc = [int(input()) for _ in range(3)]

cnt = Counter(str(prod(abc)))
for i in range(10):
    if str(i) in cnt.keys():
        print(cnt[str(i)])
    else:
        print(0)