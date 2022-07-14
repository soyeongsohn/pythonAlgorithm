while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except Exception: # while문 탈출 (ex. A, B 중 문자가 들어 있는 경우)
        break