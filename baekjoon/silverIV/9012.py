import sys

def check(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack == []: # ")"로 시작하는 경우
                return False
            
            stack.pop()
    if stack:
        return False

    return True


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        ps = sys.stdin.readline().rstrip()
        print("YES" if check(ps) else "NO")