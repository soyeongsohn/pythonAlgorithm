import sys

# 크기제한을 두고 푼 방법
# fib = [0] * 46

# def fibonacci(n):
#     if n <= 1:
#         fib[n] = n
#         return fib[n]
#     elif fib[n] > 1:
#         return fib[n]

#     fib[n] = fibonacci(n-2) + fibonacci(n-1)
#     return fib[n]


# 크기 제한을 두지 않고 푼 방법
fib = {0: 0, 1: 1}

def fibonacci(n):
    if n not in fib:
        fib[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib[n]

n = int(sys.stdin.readline().rstrip())
print(fibonacci(n))