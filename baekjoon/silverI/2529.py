import sys; input=sys.stdin.readline


def check(num1, num2, op):
    if op == "<" and num1 > num2:
        return False
    elif op == ">" and num1 < num2:
        return False
    else:
        return True

def backtrack(cnt, num):
    if cnt == k+1:
        answer.append(num)
        return None
    
    for i in range(10):
        if visited[i]:
            continue
        if cnt == 0 or check(num[cnt-1], str(i), sign[cnt-1]):
            visited[i] = True
            backtrack(cnt+1, num+str(i))
            visited[i] = False
    

k = int(input())
sign = input().strip().split()

visited = [False] * 10
cnt = 0
answer = []
backtrack(cnt, "")
answer.sort()
print(answer[-1])
print(answer[0])