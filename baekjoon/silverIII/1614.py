import sys; input = sys.stdin.readline

hurt = int(input())
maxcnt = int(input())

cnt = 0

if hurt == 1:
    result = 8 * maxcnt

elif hurt == 5:
    result = 8 * maxcnt + 4

else:
    if maxcnt % 2 == 0:
        result = 4 * maxcnt + (hurt - 1)
    else:
        result = 4 * maxcnt + (5 - hurt)

print(result)