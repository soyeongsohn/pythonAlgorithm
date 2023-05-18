import sys

def binary_search(lst, n):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2
        if n == lst[mid]:
            return 1
        elif n < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return 0




T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    n_list = list(map(int, sys.stdin.readline().rstrip().split()))
    n_list.sort()
    M = int(sys.stdin.readline())
    m_list = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in m_list:
        print(binary_search(n_list, i))
