def birthday(s, d, m):
    # Initialize the number of ways the bar can be divided to 0
    count = 0

    # Iterate over the elements of the array
    for i in range(len(s)):
        # Calculate the sum of the current sub-array of length m
        sub_array_sum = sum(s[i:i+m])
        # If the sum is equal to d, increment the count
        if sub_array_sum == d:
            count += 1

    # Return the number of ways the bar can be divided
    return count
