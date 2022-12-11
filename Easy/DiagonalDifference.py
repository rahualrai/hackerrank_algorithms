def diagonalDifference(arr):
    # Initialize empty lists to store the main diagonal and anti-diagonal elements
    right = []
    left = []
    
    # Iterate through the array
    for i in range(len(arr)):
        # Add the element of the main diagonal at the current index to the right list
        right.append(arr[i][i])
        # Add the element of the anti-diagonal at the current index to the left list
        left.append(arr[i][-i-1])
        
    # Calculate the difference between the sum of the right and left lists
    diff = sum(left) - sum(right)
    # Return the absolute value of this difference
    return abs(diff)
