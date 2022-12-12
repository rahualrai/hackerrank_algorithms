def saveThePrisoner(n, m, s):
    prisoner_num = (s+m-1) % n
    if prisoner_num == 0:
        return n
    else:
        return prisoner_num