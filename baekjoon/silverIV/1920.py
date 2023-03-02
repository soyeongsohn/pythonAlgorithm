import sys

def binary_search(k, n_lst, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if k == n_lst[m]:
        return 1
    elif k < n_lst[m]:
        return binary_search(k, n_lst, start, m - 1)
    else:
        return binary_search(k, n_lst, m + 1, end)



N = int(sys.stdin.readline().rstrip())
n_lst = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())
m_lst = list(map(int, sys.stdin.readline().rstrip().split()))


for k in m_lst:
    start = 0
    end = len(n_lst) - 1
    print(binary_search(k, n_lst, start, end))

