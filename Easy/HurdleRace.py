def hurdleRace(k, height):
    max_height = max(height)
    jump = max_height - k
    if jump<0:
        return 0
    else:
        return jump