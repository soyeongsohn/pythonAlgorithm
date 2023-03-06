import sys

n = int(sys.stdin.readline().rstrip())

operation = [] # +/-를 담을 리스트
stack = [] # 값을 담을 리스트 (오름차순)
curr = 1 # 비교할 숫자
flag = True # 수열 가능 여부

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    while curr <= num: # num까지 stack에 넣는다
        stack.append(curr)
        operation.append("+")
        curr += 1
    if stack[-1] == num: # stack의 마지막이 num과 같아지면 pop
        stack.pop()
        operation.append("-")
    else:
        flag = False
        print("NO")
        break

if flag:
    for op in operation:
        print(op)