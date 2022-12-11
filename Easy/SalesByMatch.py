def sockMerchant(n, ar):
    # Create a dictionary to store the number of socks of each color
    sock_counts = {}
    
    # Count the number of socks of each color
    for sock in ar:
        if sock in sock_counts:
            sock_counts[sock] += 1
        else:
            sock_counts[sock] = 1
    
    # Initialize the number of pairs of socks
    num_pairs = 0
    
    # Calculate the number of pairs of socks by dividing the number of socks
    # of each color by 2 and rounding down to the nearest integer
    for sock, count in sock_counts.items():
        num_pairs += count // 2
    
    return num_pairs