import sys

def check(string):
    stack = []

    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == '[':
            stack.append(s)
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
                break
    if stack:
        return False
    else:
        return True

if __name__ == "__main__":

    while True:
        string = sys.stdin.readline().rstrip()
        if string == ".":
            break

        print("yes" if check(string) else "no")
