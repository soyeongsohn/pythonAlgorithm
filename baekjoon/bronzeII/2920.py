melody = list(map(int, input().split()))
if melody == list(range(1, 9)):
    print("ascending")
elif melody == list(range(8, 0, -1)):
    print("descending")
else:
    print("mixed")
