def stones(n, a, b):
    # Write your code here
    result = []
    for i in range(n):
        result.append(a*i + b*(n-i-1))
    return sorted(list(set(result)))