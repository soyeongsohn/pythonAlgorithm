alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

string = input()

for a in alpha:
    string = string.replace(a, ".")
print(len(string))