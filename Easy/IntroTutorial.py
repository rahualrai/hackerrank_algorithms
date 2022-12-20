def introTutorial(V, arr):
    # Write your code here
    left = 0 
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == V:
            return mid 
        elif arr[mid] > V:
            right = mid - 1
        else:
            left = mid + 1
    
    return left
