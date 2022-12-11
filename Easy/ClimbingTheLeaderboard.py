def climbingLeaderboard(ranked, player):
    ranks = []
    for i in player:
        ranked.append(i)
        ranked = sorted(set(ranked), reverse = True)
        ranks.append(ranked.index(i)+1)
    return ranks

"""this function is wrong"""