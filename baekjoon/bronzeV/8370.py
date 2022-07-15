info = list(map(int, input().split()))
seats = 0
for _ in range(len(info) // 2):
    seats += info[2 * _] * info[2 * _ + 1]

print(seats)