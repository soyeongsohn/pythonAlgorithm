T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    floor = 0
    num = 0
    floor = H * 100 if N % H == 0 else (N % H) * 100
    num = N // H if N % H == 0 else 1 + N // H

    print(floor + num)