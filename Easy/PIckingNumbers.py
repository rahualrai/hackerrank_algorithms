def pickingNumbers(a):
    a = sorted(a)
    compare = a[0]
    counts = []
    count = 0
    i = 0
    
    for i in a:
        if i - compare <= 1:
            count += 1
        elif i - compare > 1:
            count = 1
            compare = i
        counts.append(count)
    return max(counts)