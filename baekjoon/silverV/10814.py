import sys

N = int(sys.stdin.readline().rstrip())

pinfo = []

for _ in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    pinfo.append((age, name))


pinfo = sorted(pinfo, key=lambda x: int(x[0]))

for i in pinfo:
    print(i[0], i[1])