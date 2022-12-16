def permutationEquation(p):
    # Write your code here
    result = []
    for i in range(1,len(p)+1):
        x = p.index(i)
        result.append(p.index(x+1)+1)
    return result

    