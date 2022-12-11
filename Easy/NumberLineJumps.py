def kangaroo(x1, v1, x2, v2):
    # If the two kangaroos are already moving away from each other or moving at the same speed, they will never meet
    if((x2 > x1 and v2 > v1) or (x1 > x2 and v1 > v2)) or (v1 == v2):
        return 'NO'
    # If the difference in positions is a multiple of the difference in velocities, they will meet at some point
    elif((x1-x2) % (v2-v1) == 0):
        return 'YES'
    # Otherwise, they will never meet
    else:
        return 'NO'
