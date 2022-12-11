def migratoryBirds(arr):
    # Initialize a dictionary to count the number of occurrences of each type of bird
    bird_counts = {}
    for bird in arr:
        bird_counts[bird] = bird_counts.get(bird, 0) + 1

    # Initialize variables to track the most frequently sighted bird and its count
    most_frequent_bird = None
    most_frequent_count = 0
    # Iterate over the keys and values in the dictionary
    for bird, count in bird_counts.items():
        # Update the most frequently sighted bird and its count if necessary
        if count > most_frequent_count:
            most_frequent_bird = bird
            most_frequent_count = count
        # If two birds have the same number of sightings, keep the one with the lowest type id
        elif count == most_frequent_count and bird < most_frequent_bird:
            most_frequent_bird = bird

    # Return the type id of the most frequently sighted bird
    return most_frequent_bird