def serviceLane(n, cases):
    # Write your code here
    results = [] 
    for i in range(len(cases)):
        start = cases[i][0]
        end = cases[i][1]
        results.append(min(width[start:end+1]))
    return results