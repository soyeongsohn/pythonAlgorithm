import sys; input=sys.stdin.readline

# - 이후 다음 -까지 있는 모든 +를 더해서 빼준다

string = input()

lst = string.split("-")
answer = 0

for i in lst[0].split("+"):
    answer += int(i)

for i in lst[1:]:
    for j in i.split("+"):
        answer -= int(j)

print(answer)