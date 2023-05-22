import sys; input = sys.stdin.readline

N, r, c = map(int, input().split())

result = 0

while N > 1:
    size = (2 ** N) // 2

    if r < size and c >= size: # 2사분면
        result += size ** 2
        c -= size
    elif r >= size and c < size: # 3사분면
        result += size ** 2 * 2
        r -= size
    elif r >= size and c >= size: # 4사분면
        result += size ** 2 * 3
        r -= size
        c -= size
    
    N -= 1

if r == 0 and c == 1:
    result += 1
elif r == 1 and c == 0:
    result += 2
elif r == 1 and c == 1:
    result += 3

print(result)