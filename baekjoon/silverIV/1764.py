import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

unseen = set([sys.stdin.readline().rstrip() for _ in range(N)])
unheard = set([sys.stdin.readline().rstrip() for _ in range(M)])

both = unseen & unheard
both = sorted(list(both))

print(len(both))
for i in both:
    print(i)