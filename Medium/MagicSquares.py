def formingMagicSquare(s):
    # Pre-defined list of magic squares
    magic_squares = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]], [[6, 1, 8], [7, 5, 3], [2, 9, 4]], [[4, 9, 2], [3, 5, 7], [8, 1, 6]], [[2, 9, 4], [7, 5, 3], [6, 1, 8]], [[8, 3, 4], [1, 5, 9], [6, 7, 2]], [[4, 3, 8], [9, 5, 1], [2, 7, 6]], [[6, 7, 2], [1, 5, 9], [8, 3, 4]], [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

    # Create an empty list to store the differences between the input square and each magic square
    differences = []
    
    # Iterate over the magic squares
    for i in magic_squares:
        # Initialize the difference for this magic square
        difference = 0
        # Iterate over the rows and columns of the square
        for a in range(3):
            for b in range(3):
                # Calculate the difference between the values at each position and add it to the total difference
                difference += abs(s[a][b] - i[a][b])
        # Add the total difference for this magic square to the list of differences
        differences.append(difference)
    
    # Return the minimum difference from the list of differences
    return min(differences)
