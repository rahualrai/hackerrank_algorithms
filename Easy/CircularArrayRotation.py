def circularArrayRotation(a, k, queries):
    result = []
    for query in queries:
        result.append(a[(query - k) % len(a)])
    return result