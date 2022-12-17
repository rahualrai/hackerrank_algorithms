"""def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    games = 0
    while s >= p:
        games += 1
        s -= p
        if p > m:
            p -= d
        else:
            p = m
    return games"""

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    total = 0
    while s >= p:
        total += 1
        s -= p
        p = max(p-d, m)
    return total