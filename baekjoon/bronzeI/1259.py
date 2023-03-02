import sys

while True:
    a = sys.stdin.readline().rstrip()

    if a == "0":
        break
    
    print("yes" if a == a[::-1] else "no")
