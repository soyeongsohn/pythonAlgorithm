n, k = map(int, input().split())

lst = list(range(1, n+1))

print("<", end="")
while lst:
    for i in range(0, k-1):
        lst.append(lst[0])
        lst.pop(0)
    print(lst.pop(0), end="")
    if lst:
        print(",", end=" ")
print(">")