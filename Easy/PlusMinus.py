def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    total = len(arr)
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print(round(pos/total, 6))
    print(round(neg/total, 6))
    print(round(zero/total, 6))