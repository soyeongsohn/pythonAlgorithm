for i in range(100):
    try:
        string = input()
        if string == "":
            break
        else:
            print(string)
    except Exception:
        break