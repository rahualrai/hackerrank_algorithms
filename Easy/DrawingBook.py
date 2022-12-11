def pageCount(n, p):
    # Calculate the number of pages to turn from the front and from the back of the book
    from_front = p // 2
    from_back = (n // 2) - (p // 2)

    # Return the minimum of these two values
    return min(from_front, from_back)