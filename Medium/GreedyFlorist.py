def getMinimumCost(k, c):
    cost = 0
    c = sorted(c, reverse = True)
    for i in range (0, len(c)):
        cost += (i//k + 1)*c[i]
    return cost
# time complexity: O(n log n)