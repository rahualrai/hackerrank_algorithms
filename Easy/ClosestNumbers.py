def closestNumbers(arr):
    # Write your code here
    arr.sort()
    min_diff = arr[1] - arr[0]
    result = [arr[0], arr[1]]
    
    for i in range(len(arr)-1):
        
        if arr[i+1] - arr[i] == min_diff:
            result.append(arr[i])
            result.append(arr[i+1])
            
        elif arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]
            result = [arr[i], arr[i+1]]
            
    return result