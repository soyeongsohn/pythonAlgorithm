import sys; input=sys.stdin.readline

key = input().strip()
code = input().strip()

lines = len(code) // len(key)

sorted_key = sorted(key)

decode = []
for i in range(len(key)):
    decode.append(sorted_key[i] + code[lines*i:lines*(i+1)])

plain = []

for i in range(len(key)):
    for j in range(len(decode)):
        if key[i] == decode[j][0]:
            plain.append(decode.pop(j)[1:]) # key 알파벳 삭제
            break

for i in range(lines):
    for j in plain:
        print(j[i], end="")