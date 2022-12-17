def chocolateFeast(n, c, m):
    # Write your code here
    wrappers = n//c
    chocolates = wrappers
    while wrappers >= m:
        new_wrappers = wrappers // m
        chocolates += new_wrappers
        wrappers = wrappers % m + new_wrappers
    return chocolates