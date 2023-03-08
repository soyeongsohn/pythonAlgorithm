import sys

dict_ = {1:0}

def func(n):
    if n in dict_:
        return dict_[n]

    if n % 6 == 0:
        dict_[n] = min(func(n // 3) + 1, func(n // 2) + 1)
    elif n % 3 == 0:
        dict_[n] = min(func(n // 3) + 1, func(n - 1) + 1)
    elif n % 2 == 0:
        dict_[n] = min(func(n // 2) + 1, func(n - 1) + 1)
    else:
        dict_[n] = func(n - 1) + 1

    return dict_[n]


n = int(sys.stdin.readline())
print(func(n))