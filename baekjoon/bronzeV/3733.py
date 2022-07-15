while True:
    try:
        N, S = map(int, input().split())
    except Exception:
        break
    else: # try 구문이 실행되었을 경우 실행
        print(S // (N + 1))