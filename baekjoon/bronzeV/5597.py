submitted = [int(input()) for _ in range(28)]
not_submitted = [ _ for _ in range(1, 31) if _ not in submitted] #1부터 순서대로 순회하므로 정렬할 필요는 없음

print(not_submitted[0], not_submitted[1])
