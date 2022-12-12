def viralAdvertising(n):
    # Write your code here
    shared = 5
    liked = 0
    cumulative = 0
    for i in range(1,n+1):
        liked = shared//2
        cumulative = cumulative + liked
        shared = liked * 3
    return cumulative
