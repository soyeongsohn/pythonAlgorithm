N = int(input())
for i in range(N):
    ox = input()
    score = 0
    inrow = 0
    for i in ox:
        if i == "O":
            score += (1 + inrow)
            inrow += 1
        else:
            inrow = 0
    print(score)
