import sys

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

N = int(sys.stdin.readline().rstrip())

num = map(int, sys.stdin.readline().rstrip().split())

print(len([n for n in num if is_prime(n)]))