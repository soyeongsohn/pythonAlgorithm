import sys

N = int(sys.stdin.readline().rstrip())

scores = []
for _ in range(N):
    name, *subjects = sys.stdin.readline().rstrip().split()
    subjects = list(map(int, subjects))
    scores.append([name, *subjects])

scores = sorted(scores, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for score in scores:
    print(score[0])