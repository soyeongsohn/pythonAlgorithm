import sys

# 크기 제한을 두고 푼 방법
# def fibonacci(n):
#     fib = [0] * 46
#     fib[1] = 1
#     if n > 1:
#         for i in range(2, n+1):
#             fib[i] = fib[i-2] + fib[i-1]
    
#     return fib[n]

# 크기 제한을 두지 않고 푼 방법
def fibonacci(n):
    fib = {0: 0, 1: 1}
    if n in fib:
        return fib[n]
    for i in range(2, n+1):
        fib[i] = fib[i-2] + fib[i-1]
    return fib[n]

n = int(sys.stdin.readline().rstrip())
print(fibonacci(n))