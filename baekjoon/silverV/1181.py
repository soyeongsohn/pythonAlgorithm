import sys

N = int(input())

words = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    words.append(word)

words = list(set(words))
words = sorted(words, key=lambda x: (len(x), x))

for i in words:
    print(i)