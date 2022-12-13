def organizingContainers(container):
    n = len(container)
    types_sums = [0]*n
    container_sums = [0]*n
    
    for i in range(n):
        container_sums[i] = sum(container[i]) # sum of the balls in each container
        for j in range(n):
            types_sums[j] += container[i][j] # sum of each type of ball
    
            
    # if the sums of each type of ball and the sums of each container are the same, then it is possible to sort the balls into the containers
    if sorted(types_sums)==sorted(container_sums):
        return "Possible"
    # otherwise, it is not
    else:
        return "Impossible"

# time complexity: O(n^2)