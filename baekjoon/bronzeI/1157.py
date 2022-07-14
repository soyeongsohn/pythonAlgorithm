from collections import Counter

word = input().upper()

freq = []
for k, v in Counter(word).items():
    if v == max(Counter(word).values()):
        freq.append(k)

print("?" if len(freq) > 1 else freq[0])