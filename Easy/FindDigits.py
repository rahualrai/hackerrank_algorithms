def findDigits(n):
    # Write your code here
    count = 0
    for i in str(n):
        if int(i) == 0:
            continue
        elif n % int(i) == 0:
            count += 1
    return count

# time complexity: O(n)