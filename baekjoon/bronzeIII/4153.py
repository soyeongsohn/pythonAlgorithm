while True:
    lines = sorted(list(map(int, input().split())))
    if lines == [0, 0, 0]:
        break
    answer = "right" if lines[-1] ** 2 == (lines[0] ** 2 + lines[1] ** 2) else "wrong"
    print(answer)