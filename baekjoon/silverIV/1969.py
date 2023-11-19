import sys; input=sys.stdin.readline

def hamming_dist(s1, s2):
    count = 0
    for i, j in zip(s1, s2):
        if i != j:
            count += 1

    return count

n, m = map(int, input().strip().split())

dnas = []
for _ in range(n):
    dnas.append(input())

answer = ""

for i in range(m):
    count_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for j in range(n):
        count_dict[dnas[j][i]] += 1
    answer += max(count_dict, key=count_dict.get)

hamm = 0
for i in range(n):
    hamm += hamming_dist(answer, dnas[i])

print(answer)
print(hamm)