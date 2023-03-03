N = int(input())

cnt = 0

for _ in range(N):
    word = input()
    tmp = {k: 0 for k in list(set(word))}
    front = word[0]
    for w in word:
        if front != w and tmp[w] > 0:
            cnt -= 1
            break
        else:
            tmp[w] += 1
        front = w
    cnt += 1

print(cnt)