import sys; input = sys.stdin.readline

s = list(map(int, list(input().strip())))
flag = False
for i in list(range(2, len(s) + 1, 2))[::-1]:
    for j in range(len(s)-i+1):
        s_split = s[j:j+i]

        if sum(s_split[:i//2]) == sum(s_split[i//2:]):
            print(len(s_split))
            flag = True
            break
    
    if flag:
        break

if not flag:
    print(0)