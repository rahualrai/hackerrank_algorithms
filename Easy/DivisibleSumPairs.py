def divisibleSumPairs(n, k, ar):
    # Initialize the count of pairs to 0
    count = 0

    # Iterate over the elements of the array
    for i in range(len(ar)):
        # Iterate over the elements after the current element
        for j in range(i+1, len(ar)):
            # If the sum of the current element and the next element is divisible by k, increment the count
            if (ar[i]+ar[j])%k == 0:
                count += 1

    # Return the count of pairs
    return count