import sys; input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = list(map(int, list(input().strip())))
    l = len(n)
    idx = 0

    for i in range(l-1, 0, -1):
        if n[i] > n[i-1]: # 오른쪽이 큰 수를 가지는 값의 인덱스 찾기
            idx = i-1
            break
    
    # 그 수를 기준으로 나누기
    left = n[:idx]
    right = n[idx:]

    if not left or not right:
        print("BIGGEST")

    else:
        right.sort() # 오른쪽 숫자들을 정렬
        for i in range(len(right)):
            if right[i] > n[idx]: # 위에서 찾은 인덱스 값보다 큰 경우
                left.append(right.pop(i)) # right에서 pop해주고 left에 추가
                left.extend(right) # 남은 정렬된 값들을 이어주기
                break

        print("".join(map(str, left)))