import sys; input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
sorted_x = sorted(list(set(x)))
dict_x = {sorted_x[i]: i for i in range(len(sorted_x))}

for i in x:
    print(dict_x[i], end=" ")