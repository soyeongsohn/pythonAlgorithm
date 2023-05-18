import math

def solution(n):
    # n**0.5가 정수일 때
    if int(math.sqrt(n)) == math.sqrt(n):
        return 1
    # (n - i**2)**0.5가 정수일 때
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
            return 2
    # (n - i**2 - j ** 2)**0.5가 정수일 때
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                return 3
    # 남은 경우는 4
    return 4


n = int(input())
print(solution(n))