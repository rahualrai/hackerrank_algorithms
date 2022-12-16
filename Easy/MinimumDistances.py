def minimumDistances(a):
    # Write your code here
    min_dist = float('inf')
    
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                min_dist = min(min_dist, j-i)
    
    if min_dist == float('inf'):
        return -1
    
    return min_dist