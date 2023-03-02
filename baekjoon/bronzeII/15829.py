import sys

L = int(input())
string = sys.stdin.readline().rstrip()

hash = 0
for i in range(L):
    hash += (ord(string[i]) - 96) * 31 ** i

hash %= 1234567891

print(hash)